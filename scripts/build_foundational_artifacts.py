"""
ACA — Build Foundational Artifacts

Creates real ACA artifacts from:

- datasets/fields/foundational_field.json
- atlas/invariants/criterion_poles.py

Outputs:

- artifacts/foundational/basis_vectors.npy
- artifacts/foundational/singular_values.npy
- artifacts/foundational/invariant_directions.npy
- artifacts/foundational/invariant_metadata.json
- artifacts/foundational/field_metadata.json

Compatibility outputs:

- artifacts/foundational/criterion_vectors.npy
- artifacts/foundational/criterion_vector_metadata.json
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from atlas.embeddings.openai_embedder import OpenAIEmbedder
from atlas.geometry.svd_basis import build_svd_basis
from atlas.invariants.criterion_poles import FOUNDATIONAL_POLES
from atlas.invariants.build_registry import (
    build_invariant_registry_from_poles,
    invariant_direction_matrix,
    invariant_names,
)
from atlas.serialization.save_field import save_json, save_numpy


FIELD_PATH = Path("datasets/fields/foundational_field.json")
OUTPUT_DIR = Path("artifacts/foundational")


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    field_data = load_json(FIELD_PATH)

    embedder = OpenAIEmbedder()

    print("Embedding foundational field anchors...")
    anchors = field_data["anchors"]
    anchor_embeddings = embedder.embed_texts(anchors)
    context_matrix = np.vstack(anchor_embeddings)

    print("Building SVD basis...")
    svd_basis = build_svd_basis(
        context_matrix=context_matrix,
        energy_threshold=0.95,
        normalize=True,
    )

    print("Building invariant registry...")
    registry = build_invariant_registry_from_poles(
        poles=FOUNDATIONAL_POLES,
        embedder=embedder,
    )

    invariant_matrix = invariant_direction_matrix(registry)
    names = invariant_names(registry)

    print("Saving artifacts...")

    save_numpy(
        OUTPUT_DIR / "basis_vectors.npy",
        svd_basis.basis,
    )

    save_numpy(
        OUTPUT_DIR / "singular_values.npy",
        svd_basis.singular_values,
    )

    save_numpy(
        OUTPUT_DIR / "invariant_directions.npy",
        invariant_matrix,
    )

    save_json(
        OUTPUT_DIR / "invariant_metadata.json",
        {
            "invariant_names": names,
            "n_invariants": len(names),
            "embedding_dim": int(invariant_matrix.shape[1]),
            "source": "atlas.invariants.criterion_poles.FOUNDATIONAL_POLES",
        },
    )

    # Compatibility with previous benchmark loader.
    save_numpy(
        OUTPUT_DIR / "criterion_vectors.npy",
        invariant_matrix,
    )

    save_json(
        OUTPUT_DIR / "criterion_vector_metadata.json",
        {
            "invariant_names": names,
            "n_vectors": len(names),
            "embedding_dim": int(invariant_matrix.shape[1]),
            "source": "compatibility_alias_of_invariant_directions",
        },
    )

    save_json(
        OUTPUT_DIR / "field_metadata.json",
        {
            "field_name": field_data["name"],
            "field_type": field_data["field_type"],
            "version": field_data["version"],
            "n_anchors": len(anchors),
            "embedding_dim": int(context_matrix.shape[1]),
            "svd_rank": int(svd_basis.rank),
            "explained_energy": float(svd_basis.explained_energy),
            "recommended_model": field_data["embedding_policy"]["recommended_model"],
            "normalize_embeddings": field_data["embedding_policy"]["normalize_embeddings"],
            "invariants": names,
        },
    )

    print("\nDone.")
    print(f"Artifacts saved to: {OUTPUT_DIR}")
    print(f"SVD rank: {svd_basis.rank}")
    print(f"Explained energy: {svd_basis.explained_energy:.4f}")
    print(f"Embedding dim: {context_matrix.shape[1]}")
    print(f"Invariants: {names}")


if __name__ == "__main__":
    main()