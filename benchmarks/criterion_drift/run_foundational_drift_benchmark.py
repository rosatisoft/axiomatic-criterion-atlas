"""
ACA — Axiomatic Criterion Atlas

Multi-Field Foundational Drift Benchmark
----------------------------------------

Evaluates trajectories against:

- foundational field
- factual field
- rhetorical field

This allows ACA to observe field transitions during criterion drift.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

import numpy as np

from atlas.embeddings.openai_embedder import OpenAIEmbedder
from atlas.orientation.criterion_vectors import CriterionVector
from atlas.runtime.thresholds import balanced_thresholds
from atlas.trajectories.semantic_trajectory import build_semantic_trajectory
from atlas.trajectories.trajectory_analysis import (
    analyze_trajectory,
    trajectory_summary,
)


USE_REAL_EMBEDDINGS = True

DATASET_DIR = Path("datasets/trajectories")
ARTIFACTS_DIR = Path("artifacts")

FIELDS = [
    "foundational",
    "factual",
    "rhetorical",
]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_trajectory_files() -> List[Path]:
    paths: List[Path] = []

    for category in [
        "stable",
        "drifting",
        "inverted",
        "ambiguous",
        "controversial",
    ]:
        category_dir = DATASET_DIR / category

        if category_dir.exists():
            paths.extend(sorted(category_dir.glob("*.json")))

    return paths


def load_field_bases() -> Dict[str, np.ndarray]:
    field_bases: Dict[str, np.ndarray] = {}

    for field_name in FIELDS:
        basis_path = ARTIFACTS_DIR / field_name / "basis_vectors.npy"

        if not basis_path.exists():
            raise FileNotFoundError(
                f"Missing basis artifact: {basis_path}"
            )

        field_bases[field_name] = np.load(basis_path)

    return field_bases


def load_criterion_vectors() -> List[CriterionVector]:
    vectors_path = ARTIFACTS_DIR / "foundational" / "criterion_vectors.npy"
    metadata_path = ARTIFACTS_DIR / "foundational" / "criterion_vector_metadata.json"

    if not vectors_path.exists():
        raise FileNotFoundError(f"Missing criterion vectors: {vectors_path}")

    if not metadata_path.exists():
        raise FileNotFoundError(f"Missing criterion metadata: {metadata_path}")

    matrix = np.load(vectors_path)
    metadata = load_json(metadata_path)

    names = metadata["invariant_names"]

    vectors: List[CriterionVector] = []

    for i, name in enumerate(names):
        direction = matrix[i]

        vectors.append(
            CriterionVector(
                invariant_name=name,
                direction=direction,
                preservation_pole=direction,
                inversion_pole=-direction,
                norm=2.0,
            )
        )

    return vectors


def embed_texts(texts: List[str]) -> List[np.ndarray]:
    if USE_REAL_EMBEDDINGS:
        embedder = OpenAIEmbedder()
        return embedder.embed_texts(texts)

    raise RuntimeError("Mock mode disabled in multi-field benchmark.")


def run_benchmark() -> None:
    thresholds = balanced_thresholds()

    paths = load_trajectory_files()

    if not paths:
        print("No trajectory files found.")
        return

    field_bases = load_field_bases()
    criterion_vectors = load_criterion_vectors()

    print("\nACA Multi-Field Drift Benchmark")
    print("=" * 50)
    print(f"Fields: {', '.join(FIELDS)}")
    print("Mode: REAL EMBEDDINGS")
    print("=" * 50)

    for path in paths:
        data = load_json(path)

        states = data["states"]
        texts = [state["text"] for state in states]
        embeddings = embed_texts(texts)

        trajectory = build_semantic_trajectory(
            texts=texts,
            embeddings=embeddings,
            metadata=[
                {
                    "source_file": str(path),
                    "trajectory_id": data["id"],
                    "trajectory_type": data["trajectory_type"],
                    "step": state["step"],
                }
                for state in states
            ],
        )

        result = analyze_trajectory(
            trajectory=trajectory,
            field_bases=field_bases,
            criterion_vectors=criterion_vectors,
            theta_origin=thresholds.theta_origin,
            theta_orientation=thresholds.theta_orientation,
            theta_weak_orientation=thresholds.theta_weak_orientation,
            theta_decay=thresholds.theta_decay,
        )

        summary = trajectory_summary(result)

        print(f"\nTrajectory: {data['id']}")
        print(f"Type: {data['trajectory_type']}")
        print(f"Expected: {data.get('expected_behavior', {})}")
        print(f"Summary: {summary}")

        for state_analysis in result.states:
            scores = state_analysis.field_selection.scores

            field_costs = ", ".join(
                f"{score.field_name}:{score.origin_cost:.3f}"
                for score in scores
            )

            print(
                f"  Step {state_analysis.state_index}: "
                f"field={state_analysis.selected_field}, "
                f"O={state_analysis.field_selection.selected_score.origin_cost:.4f}, "
                f"margin={state_analysis.field_selection.margin:.4f}, "
                f"Phi={state_analysis.orientation.aggregate_orientation:.4f}, "
                f"state={state_analysis.drift.state.value}, "
                f"preservation={state_analysis.preservation.preservation_score:.4f}"
            )

            print(f"      field_costs: {field_costs}")


if __name__ == "__main__":
    run_benchmark()