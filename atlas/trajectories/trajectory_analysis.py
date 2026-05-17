"""
ACA — Axiomatic Criterion Atlas

Trajectory Analysis
-------------------

This module evaluates semantic trajectories using:

- field selection
- origin cost
- epistemic orientation
- criterion drift detection
- preservation metrics

It connects geometry, orientation, and trajectory evolution into a unified
analysis layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional

import numpy as np

from atlas.geometry.field_selection import FieldSelectionResult, select_field
from atlas.orientation.criterion_vectors import CriterionVector
from atlas.orientation.epistemic_orientation import (
    EpistemicOrientationResult,
    evaluate_epistemic_orientation,
)
from atlas.orientation.drift_detection import (
    DriftDetectionResult,
    detect_criterion_drift,
)
from atlas.orientation.preservation_metrics import (
    PreservationMetrics,
    compute_preservation_score,
)
from atlas.trajectories.semantic_trajectory import (
    SemanticState,
    SemanticTrajectory,
)


@dataclass
class TrajectoryStateAnalysis:
    """
    Full ACA analysis for one semantic trajectory state.
    """

    state_index: int
    text: str
    selected_field: str
    field_selection: FieldSelectionResult
    orientation: EpistemicOrientationResult
    drift: DriftDetectionResult
    preservation: PreservationMetrics


@dataclass
class TrajectoryAnalysisResult:
    """
    Full ACA trajectory analysis.
    """

    states: List[TrajectoryStateAnalysis]

    def orientations(self) -> List[float]:
        """
        Return aggregate orientation values across the trajectory.
        """

        return [
            state.orientation.aggregate_orientation
            for state in self.states
        ]

    def origin_costs(self) -> List[float]:
        """
        Return selected-field origin costs across the trajectory.
        """

        return [
            state.field_selection.selected_score.origin_cost
            for state in self.states
        ]

    def preservation_scores(self) -> List[float]:
        """
        Return preservation scores across the trajectory.
        """

        return [
            state.preservation.preservation_score
            for state in self.states
        ]

    def drift_states(self) -> List[str]:
        """
        Return drift state labels across the trajectory.
        """

        return [
            state.drift.state.value
            for state in self.states
        ]


def analyze_trajectory(
    trajectory: SemanticTrajectory,
    field_bases: Dict[str, np.ndarray],
    criterion_vectors: Iterable[CriterionVector],
    theta_origin: float,
    theta_orientation: float,
    theta_weak_orientation: float = 0.0,
    theta_decay: float = -0.05,
    weights: Optional[Dict[str, float]] = None,
    normalize_input: bool = True,
) -> TrajectoryAnalysisResult:
    """
    Analyze a semantic trajectory across ACA geometry and orientation.

    Parameters
    ----------
    trajectory:
        SemanticTrajectory object.

    field_bases:
        Dictionary mapping field names to semantic bases.

    criterion_vectors:
        Directional invariant vectors.

    theta_origin:
        Maximum origin cost for contextual compatibility.

    theta_orientation:
        Minimum aggregate orientation for criterion preservation.

    theta_weak_orientation:
        Lower orientation threshold for weak but non-inverted states.

    theta_decay:
        Threshold for detecting negative orientation decay.

    weights:
        Optional invariant relevance weights.

    normalize_input:
        Whether to normalize embeddings before analysis.

    Returns
    -------
    TrajectoryAnalysisResult
        Full trajectory analysis.
    """

    criterion_vectors = list(criterion_vectors)

    analyses: List[TrajectoryStateAnalysis] = []
    previous_orientation: Optional[float] = None

    for state in trajectory.states:

        field_selection = select_field(
            vector=state.embedding,
            field_bases=field_bases,
            normalize_input=normalize_input,
        )

        orientation = evaluate_epistemic_orientation(
            vector=state.embedding,
            criterion_vectors=criterion_vectors,
            weights=weights,
            normalize_input=normalize_input,
        )

        aggregate_orientation = orientation.aggregate_orientation

        drift = detect_criterion_drift(
            origin_cost=field_selection.selected_score.origin_cost,
            orientation=aggregate_orientation,
            theta_origin=theta_origin,
            theta_orientation=theta_orientation,
            theta_weak_orientation=theta_weak_orientation,
            previous_orientation=previous_orientation,
            theta_decay=theta_decay,
        )

        preservation = compute_preservation_score(
            origin_cost=field_selection.selected_score.origin_cost,
            orientation=aggregate_orientation,
            theta_origin=theta_origin,
            theta_orientation=theta_orientation,
        )

        analyses.append(
            TrajectoryStateAnalysis(
                state_index=state.index,
                text=state.text,
                selected_field=field_selection.selected_field,
                field_selection=field_selection,
                orientation=orientation,
                drift=drift,
                preservation=preservation,
            )
        )

        previous_orientation = aggregate_orientation

    return TrajectoryAnalysisResult(states=analyses)


def trajectory_summary(
    result: TrajectoryAnalysisResult,
) -> Dict[str, object]:
    """
    Build a compact dictionary summary of a trajectory analysis.
    """

    orientations = result.orientations()
    origin_costs = result.origin_costs()
    preservation_scores = result.preservation_scores()
    drift_states = result.drift_states()

    return {
        "n_states": len(result.states),
        "mean_orientation": float(np.mean(orientations)) if orientations else None,
        "min_orientation": float(np.min(orientations)) if orientations else None,
        "max_origin_cost": float(np.max(origin_costs)) if origin_costs else None,
        "mean_origin_cost": float(np.mean(origin_costs)) if origin_costs else None,
        "mean_preservation": (
            float(np.mean(preservation_scores))
            if preservation_scores
            else None
        ),
        "min_preservation": (
            float(np.min(preservation_scores))
            if preservation_scores
            else None
        ),
        "drift_states": drift_states,
        "has_inversion": "inverted" in drift_states,
        "has_drift": "drifting" in drift_states,
        "has_dispersion": "dispersed" in drift_states,
    }