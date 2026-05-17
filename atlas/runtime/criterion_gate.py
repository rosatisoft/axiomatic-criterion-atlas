"""
ACA — Axiomatic Criterion Atlas

Criterion Gate
--------------

This module provides the primary runtime gate for ACA.

The gate combines:

- semantic field selection,
- origin cost,
- epistemic orientation,
- criterion drift detection,
- preservation metrics,
- and runtime policy mapping.

It is the minimal operational bridge between ACA geometry and a future
Criterion Gateway.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Optional

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
from atlas.runtime.policies import RuntimeAction, action_from_drift_state
from atlas.runtime.thresholds import DEFAULT_THRESHOLDS, ThresholdConfig


@dataclass
class CriterionGateResult:
    """
    Full runtime criterion gate result.
    """

    selected_field: str
    action: RuntimeAction
    field_selection: FieldSelectionResult
    orientation: EpistemicOrientationResult
    drift: DriftDetectionResult
    preservation: PreservationMetrics


def evaluate_criterion_gate(
    vector: np.ndarray,
    field_bases: Dict[str, np.ndarray],
    criterion_vectors: Iterable[CriterionVector],
    thresholds: ThresholdConfig = DEFAULT_THRESHOLDS,
    weights: Optional[Dict[str, float]] = None,
    previous_orientation: Optional[float] = None,
    normalize_input: bool = True,
) -> CriterionGateResult:
    """
    Evaluate an input embedding through the ACA Criterion Gate.

    Parameters
    ----------
    vector:
        Input embedding.

    field_bases:
        Dictionary mapping field names to semantic bases.

    criterion_vectors:
        Directional invariant vectors.

    thresholds:
        ThresholdConfig object.

    weights:
        Optional invariant relevance weights.

    previous_orientation:
        Optional previous aggregate orientation for decay detection.

    normalize_input:
        Whether to normalize the input embedding.

    Returns
    -------
    CriterionGateResult
        Runtime action and full ACA diagnostics.
    """

    field_selection = select_field(
        vector=vector,
        field_bases=field_bases,
        normalize_input=normalize_input,
    )

    orientation = evaluate_epistemic_orientation(
        vector=vector,
        criterion_vectors=criterion_vectors,
        weights=weights,
        normalize_input=normalize_input,
    )

    aggregate_orientation = orientation.aggregate_orientation
    origin_cost = field_selection.selected_score.origin_cost

    drift = detect_criterion_drift(
        origin_cost=origin_cost,
        orientation=aggregate_orientation,
        theta_origin=thresholds.theta_origin,
        theta_orientation=thresholds.theta_orientation,
        theta_weak_orientation=thresholds.theta_weak_orientation,
        previous_orientation=previous_orientation,
        theta_decay=thresholds.theta_decay,
    )

    preservation = compute_preservation_score(
        origin_cost=origin_cost,
        orientation=aggregate_orientation,
        theta_origin=thresholds.theta_origin,
        theta_orientation=thresholds.theta_orientation,
    )

    action = action_from_drift_state(drift.state)

    return CriterionGateResult(
        selected_field=field_selection.selected_field,
        action=action,
        field_selection=field_selection,
        orientation=orientation,
        drift=drift,
        preservation=preservation,
    )