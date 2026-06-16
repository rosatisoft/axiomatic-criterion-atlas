from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path
from typing import Any

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI


DEFAULT_SOURCE_PATH = Path("source_definitions/security_access_boundary_sources.json")
DEFAULT_MAX_RANK = 23
DEFAULT_ENERGY_TARGET = 0.95


def normalize_rows(matrix: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return matrix / norms


def normalize_vector(vector: np.ndarray) -> np.ndarray:
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return vector / norm


def embed_texts(texts: list[str], model: str) -> np.ndarray:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing. Add it to your .env file.")

    client = OpenAI(api_key=api_key)

    response = client.embeddings.create(
        model=model,
        input=texts,
        encoding_format="float",
    )

    vectors = [item.embedding for item in response.data]
    return np.array(vectors, dtype=np.float32)


def choose_rank(
    singular_values: np.ndarray,
    max_rank: int,
    energy_target: float,
) -> tuple[int, float]:
    if len(singular_values) == 0:
        return 0, 0.0

    energy = singular_values**2
    total = float(np.sum(energy))

    if total == 0:
        return min(len(singular_values), max_rank), 0.0

    cumulative = np.cumsum(energy) / total

    rank = int(np.searchsorted(cumulative, energy_target) + 1)
    rank = max(1, min(rank, max_rank, len(singular_values)))

    explained = float(cumulative[rank - 1])
    return rank, explained


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def ensure_source_shape(source: dict[str, Any]) -> None:
    if source.get("artifact_family") != "security_access_boundary":
        raise ValueError("Source artifact_family must be 'security_access_boundary'.")

    if source.get("runtime_layer") != "access_gate":
        raise ValueError("Source runtime_layer must be 'access_gate'.")

    if "artifacts" not in source or not isinstance(source["artifacts"], dict):
        raise ValueError("Source must contain an 'artifacts' object.")

    for name, spec in source["artifacts"].items():
        for key in ["axis", "artifact_path", "description", "invariants", "anchors"]:
            if key not in spec:
                raise ValueError(f"Artifact {name!r} missing required key: {key}")

        if spec["axis"] != "access_boundary":
            raise ValueError(f"Artifact {name!r} must have axis='access_boundary'.")

        if not isinstance(spec["anchors"], list) or not spec["anchors"]:
            raise ValueError(f"Artifact {name!r} must define a non-empty anchors list.")


def build_artifact(
    name: str,
    spec: dict[str, Any],
    source: dict[str, Any],
    *,
    max_rank: int,
    energy_target: float,
    force: bool,
) -> dict[str, Any]:
    model = source["embedding_model"]
    embedding_dim = int(source["embedding_dim"])
    normalize_embeddings = bool(source.get("normalize_embeddings", True))

    anchors = spec["anchors"]
    artifact_path = Path(spec["artifact_path"])

    print("\n" + "-" * 100)
    print(f"Building access-boundary artifact: {name}")
    print(f"Path:    {artifact_path}")
    print(f"Anchors: {len(anchors)}")
    print(f"Model:   {model}")
    print(f"Dim:     {embedding_dim}")

    if artifact_path.exists() and not force:
        raise FileExistsError(
            f"Artifact path already exists: {artifact_path}. "
            "Pass --force to overwrite."
        )

    artifact_path.mkdir(parents=True, exist_ok=True)

    embeddings = embed_texts(anchors, model=model)

    if embeddings.shape[1] != embedding_dim:
        raise ValueError(
            f"Embedding dim mismatch for {name}: "
            f"expected {embedding_dim}, got {embeddings.shape[1]}"
        )

    if normalize_embeddings:
        embeddings = normalize_rows(embeddings)

    centroid = normalize_vector(np.mean(embeddings, axis=0))

    # SVD over anchor embedding matrix.
    # Vt contains right singular vectors in embedding space.
    _, singular_values, vt = np.linalg.svd(embeddings, full_matrices=False)

    rank, explained_energy = choose_rank(
        singular_values,
        max_rank=max_rank,
        energy_target=energy_target,
    )

    basis_vectors = vt[:rank].T.astype(np.float32)

    np.save(artifact_path / "anchor_embeddings.npy", embeddings.astype(np.float32))
    np.save(artifact_path / "centroid.npy", centroid.astype(np.float32))
    np.save(artifact_path / "basis_vectors.npy", basis_vectors.astype(np.float32))
    np.save(artifact_path / "singular_values.npy", singular_values.astype(np.float32))

    metadata = {
        "field_name": spec.get("description", name),
        "field_type": name,
        "axis": spec["axis"],
        "artifact_family": source["artifact_family"],
        "runtime_layer": source["runtime_layer"],
        "version": source["version"],
        "description": spec.get("description", ""),
        "expected_decision": spec.get("expected_decision"),
        "n_anchors": len(anchors),
        "embedding_dim": embedding_dim,
        "svd_rank": rank,
        "explained_energy": explained_energy,
        "recommended_model": model,
        "normalize_embeddings": normalize_embeddings,
        "invariants": spec.get("invariants", []),
        "languages": source.get("languages", []),
        "anchors": anchors,
        "runtime_recommendations": {
            "gate_layer": "access_boundary",
            "do_not_create_origin_for_boundary_cases": True,
            "do_not_mutate_state_for_boundary_cases": True,
            "boundary_decisions": source.get("decision_guidance", {}),
            "ambiguity_margin": 0.05,
        },
        "artifact_files": {
            "anchor_embeddings": "anchor_embeddings.npy",
            "centroid": "centroid.npy",
            "basis_vectors": "basis_vectors.npy",
            "singular_values": "singular_values.npy",
            "metadata": "field_metadata.json",
        },
        "source": {
            "source_file": str(DEFAULT_SOURCE_PATH),
            "source_artifact_name": name,
        },
    }

    save_json(artifact_path / "field_metadata.json", metadata)

    print(f"Rank:             {rank}")
    print(f"Explained energy: {explained_energy:.6f}")

    return {
        "name": name,
        "axis": spec["axis"],
        "artifact_path": str(artifact_path),
        "expected_decision": spec.get("expected_decision"),
        "n_anchors": len(anchors),
        "embedding_dim": embedding_dim,
        "svd_rank": rank,
        "explained_energy": explained_energy,
        "recommended_model": model,
        "metadata": str(artifact_path / "field_metadata.json"),
    }


def build_manifest(
    source: dict[str, Any],
    built_artifacts: list[dict[str, Any]],
    source_path: Path,
) -> dict[str, Any]:
    return {
        "version": source["version"],
        "artifact_family": source["artifact_family"],
        "runtime_layer": source["runtime_layer"],
        "description": source.get("description", ""),
        "embedding_model": source["embedding_model"],
        "embedding_dim": source["embedding_dim"],
        "normalize_embeddings": source.get("normalize_embeddings", True),
        "source_file": str(source_path),
        "source_copy": "artifacts/source_definitions/security_access_boundary_sources.json",
        "languages": source.get("languages", []),
        "decision_guidance": source.get("decision_guidance", {}),
        "artifacts": built_artifacts,
        "probe_design": source.get("probe_design", {}),
        "runtime_note": (
            "These artifacts are intended for the access gate before origin creation "
            "and before F-C-P trajectory evaluation."
        ),
    }


def copy_source_to_artifacts(source_path: Path) -> Path:
    target = Path("artifacts/source_definitions/security_access_boundary_sources.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, target)
    return target


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build ACA security access boundary artifacts."
    )
    parser.add_argument(
        "--source",
        default=str(DEFAULT_SOURCE_PATH),
        help="Path to security_access_boundary_sources.json.",
    )
    parser.add_argument(
        "--max-rank",
        type=int,
        default=DEFAULT_MAX_RANK,
        help="Maximum SVD rank per artifact.",
    )
    parser.add_argument(
        "--energy-target",
        type=float,
        default=DEFAULT_ENERGY_TARGET,
        help="SVD explained energy target.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing artifact directories.",
    )

    args = parser.parse_args()

    source_path = Path(args.source)

    if not source_path.exists():
        raise FileNotFoundError(f"Source file not found: {source_path}")

    source = load_json(source_path)
    ensure_source_shape(source)

    print("=" * 100)
    print("ACA Security Access Boundary Artifact Builder")
    print("=" * 100)
    print(f"Source:        {source_path}")
    print(f"Version:       {source.get('version')}")
    print(f"Model:         {source.get('embedding_model')}")
    print(f"Dim:           {source.get('embedding_dim')}")
    print(f"Artifact fam.: {source.get('artifact_family')}")
    print(f"Runtime layer: {source.get('runtime_layer')}")
    print(f"Max rank:      {args.max_rank}")
    print(f"Energy target: {args.energy_target}")
    print(f"Force:         {args.force}")

    built_artifacts: list[dict[str, Any]] = []

    for name, spec in source["artifacts"].items():
        built = build_artifact(
            name,
            spec,
            source,
            max_rank=args.max_rank,
            energy_target=args.energy_target,
            force=args.force,
        )
        built_artifacts.append(built)

    source_copy = copy_source_to_artifacts(source_path)

    manifest = build_manifest(
        source,
        built_artifacts,
        source_path,
    )

    manifest_path = Path("artifacts/security_access_boundary/manifest.json")
    save_json(manifest_path, manifest)

    print("\n" + "=" * 100)
    print("Done. Security access boundary artifacts generated successfully.")
    print("=" * 100)
    print(f"Source copy: {source_copy}")
    print(f"Manifest:    {manifest_path}")
    print(f"Artifacts:   artifacts/security_access_boundary")


if __name__ == "__main__":
    main()
