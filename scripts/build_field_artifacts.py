"""
ACA — Build Field Artifacts

Generic field artifact builder.

Usage:

    python scripts/build_field_artifacts.py foundational
    python scripts/build_field_artifacts.py factual
    python scripts/build_field_artifacts.py rhetorical

Outputs:

    artifacts/<field_type>/
    ├── basis_vectors.npy
    ├── singular_values.npy
    └── field_metadata.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from atlas.embeddings.openai_embedder import OpenAIEmbedder
from atlas.geometry.svd_basis import build_svd_basis
from atlas.serialization.save_field import save_json, save_numpy


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_field_artifacts(field_type: str) -> None:
    field_path = Path(f"datasets/fields/{field_type}_field.json")
    output_dir = Path(f"artifacts/{field_type}")

    if not field_path.exists():
        raise FileNotFoundError(f"Missing field file: {field_path}")

    output_dir.mkdir(parents=True, exist_ok=True)

    field_data = load_json(field_path)

    embedder = OpenAIEmbedder()

    print(f"Embedding {field_type} field anchors...")
    anchors = field_data["anchors"]
    anchor_embeddings = embedder.embed_texts(anchors)
    context_matrix = np.vstack(anchor_embeddings)

    print("Building SVD basis...")
    svd_basis = build_svd_basis(
        context_matrix=context_matrix,
        energy_threshold=0.95,
        normalize=True,
    )

    print("Saving artifacts...")

    save_numpy(
        output_dir / "basis_vectors.npy",
        svd_basis.basis,
    )

    save_numpy(
        output_dir / "singular_values.npy",
        svd_basis.singular_values,
    )

    save_json(
        output_dir / "field_metadata.json",
        {
            "field_name": field_data["name"],
            "field_type": field_data["field_type"],
            "version": field_data["version"],
            "description": field_data.get("description", ""),
            "n_anchors": len(anchors),
            "embedding_dim": int(context_matrix.shape[1]),
            "svd_rank": int(svd_basis.rank),
            "explained_energy": float(svd_basis.explained_energy),
            "recommended_model": field_data["embedding_policy"]["recommended_model"],
            "normalize_embeddings": field_data["embedding_policy"]["normalize_embeddings"],
            "invariants": field_data.get("invariants", []),
            "runtime_recommendations": field_data.get("runtime_recommendations", {}),
        },
    )

    print("\nDone.")
    print(f"Artifacts saved to: {output_dir}")
    print(f"SVD rank: {svd_basis.rank}")
    print(f"Explained energy: {svd_basis.explained_energy:.4f}")
    print(f"Embedding dim: {context_matrix.shape[1]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "field_type",
        choices=["foundational", "factual", "rhetorical"],
        help="Field type to build.",
    )

    args = parser.parse_args()

    build_field_artifacts(args.field_type)


if __name__ == "__main__":
    main()