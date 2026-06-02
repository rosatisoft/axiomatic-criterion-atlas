from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
from openai import OpenAI


SOURCE_PATH = Path("artifacts/source_definitions/triaxial_artifact_sources.json")
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
    client = OpenAI()
    response = client.embeddings.create(
        model=model,
        input=texts,
    )
    vectors = [item.embedding for item in response.data]
    return np.array(vectors, dtype=np.float32)


def choose_rank(singular_values: np.ndarray, max_rank: int, energy_target: float) -> tuple[int, float]:
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


def build_artifact(name: str, spec: dict[str, Any], global_config: dict[str, Any]) -> None:
    model = global_config["embedding_model"]
    embedding_dim = int(global_config["embedding_dim"])
    normalize_embeddings = bool(global_config.get("normalize_embeddings", True))

    anchors = spec["anchors"]
    artifact_path = Path(spec["artifact_path"])

    print(f"\nBuilding artifact: {name}")
    print(f"Path: {artifact_path}")
    print(f"Anchors: {len(anchors)}")

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
        max_rank=DEFAULT_MAX_RANK,
        energy_target=DEFAULT_ENERGY_TARGET,
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
        "version": global_config["version"],
        "description": spec.get("description", ""),
        "n_anchors": len(anchors),
        "embedding_dim": embedding_dim,
        "svd_rank": rank,
        "explained_energy": explained_energy,
        "recommended_model": model,
        "normalize_embeddings": normalize_embeddings,
        "invariants": spec.get("invariants", []),
        "anchors": anchors,
        "runtime_recommendations": {
            "theta_origin": 0.45,
            "theta_orientation": 0.15,
            "theta_decay": -0.05,
            "ambiguity_margin": 0.05
        },
        "artifact_files": {
            "anchor_embeddings": "anchor_embeddings.npy",
            "centroid": "centroid.npy",
            "basis_vectors": "basis_vectors.npy",
            "singular_values": "singular_values.npy",
            "metadata": "field_metadata.json"
        }
    }

    with open(artifact_path / "field_metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    print(f"Rank: {rank}")
    print(f"Explained energy: {explained_energy:.6f}")


def main() -> None:
    if not SOURCE_PATH.exists():
        raise FileNotFoundError(f"Source file not found: {SOURCE_PATH}")

    with open(SOURCE_PATH, "r", encoding="utf-8") as f:
        source = json.load(f)

    global_config = {
        "version": source["version"],
        "embedding_model": source["embedding_model"],
        "embedding_dim": source["embedding_dim"],
        "normalize_embeddings": source.get("normalize_embeddings", True),
    }

    artifacts = source["artifacts"]

    for name, spec in artifacts.items():
        build_artifact(name, spec, global_config)

    print("\nDone. Triaxial artifacts generated successfully.")


if __name__ == "__main__":
    main()