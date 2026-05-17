"""
ACA — Axiomatic Criterion Atlas

Criterion Drift Detection
-------------------------

Criterion drift occurs when a semantic trajectory remains contextually
compatible with a field while losing or inverting epistemic orientation.

Core condition:

    O(z_t) <= theta_O
    and
    Phi(z_t) < 0

This module provides utilities for detecting:

- directional inversion,
- weak orientation,
- orientation decay,
- progressive drift,
- and criterion destabilization.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, List, Optional

import numpy as np


class DriftState(str, Enum):
    """
    Semantic trajectory state relative to criterion preservation.
    """

    STABLE = "stable"
    WEAK = "weak"
    AMBIGUOUS = "ambiguous"
    DRIFTING = "drifting"
    INVERTED = "inverted"
    DISPERSED = "dispersed"


@dataclass
class DriftDetectionResult:
    """
    Result of criterion drift evaluation.
    """

    state: DriftState
    origin_cost: float
    orientation: float
    orientation_decay: Optional[float]
    is_contextually_compatible: bool
    is_orientation_preserved: bool
    is_inverted: bool
    is_drifting: bool


def compute_orientation_decay(
    current_orientation: float,
    previous_orientation: float,
) -> float:
    """
    Compute orientation decay between two trajectory states.

    Delta Phi_t = Phi_t - Phi_{t-1}

    Negative values indicate orientation weakening.
    """

    return float(current_orientation - previous_orientation)


def classify_drift_state(
    origin_cost: float,
    orientation: float,
    theta_origin: float,
    theta_orientation: float,
    theta_weak_orientation: float = 0.0,
    orientation_decay: Optional[float] = None,
    theta_decay: float = -0.05,
) -> DriftState:
    """
    Classify semantic state according to origin cost, orientation, and decay.

    Parameters
    ----------
    origin_cost:
        Origin cost relative to the selected semantic field.

    orientation:
        Aggregate epistemic orientation.

    theta_origin:
        Maximum origin cost for contextual compatibility.

    theta_orientation:
        Minimum orientation for strong criterion preservation.

    theta_weak_orientation:
        Lower bound for weak but non-inverted orientation.

    orientation_decay:
        Optional orientation decay from previous state.

    theta_decay:
        Negative threshold used to flag progressive drift.

    Returns
    -------
    DriftState
        Classified semantic state.
    """

    if origin_cost > theta_origin:
        return DriftState.DISPERSED

    if orientation < 0:
        return DriftState.INVERTED

    if orientation_decay is not None and orientation_decay <= theta_decay:
        return DriftState.DRIFTING

    if orientation >= theta_orientation:
        return DriftState.STABLE

    if orientation >= theta_weak_orientation:
        return DriftState.WEAK

    return DriftState.AMBIGUOUS


def detect_criterion_drift(
    origin_cost: float,
    orientation: float,
    theta_origin: float,
    theta_orientation: float,
    theta_weak_orientation: float = 0.0,
    previous_orientation: Optional[float] = None,
    theta_decay: float = -0.05,
) -> DriftDetectionResult:
    """
    Detect criterion drift for a single trajectory state.
    """

    orientation_decay: Optional[float] = None

    if previous_orientation is not None:
        orientation_decay = compute_orientation_decay(
            current_orientation=orientation,
            previous_orientation=previous_orientation,
        )

    state = classify_drift_state(
        origin_cost=origin_cost,
        orientation=orientation,
        theta_origin=theta_origin,
        theta_orientation=theta_orientation,
        theta_weak_orientation=theta_weak_orientation,
        orientation_decay=orientation_decay,
        theta_decay=theta_decay,
    )

    is_contextually_compatible = origin_cost <= theta_origin
    is_orientation_preserved = orientation >= theta_orientation
    is_inverted = orientation < 0
    is_drifting = state == DriftState.DRIFTING

    return DriftDetectionResult(
        state=state,
        origin_cost=float(origin_cost),
        orientation=float(orientation),
        orientation_decay=orientation_decay,
        is_contextually_compatible=bool(is_contextually_compatible),
        is_orientation_preserved=bool(is_orientation_preserved),
        is_inverted=bool(is_inverted),
        is_drifting=bool(is_drifting),
    )


def detect_orientation_decay_sequence(
    orientations: Iterable[float],
) -> List[float]:
    """
    Compute orientation decay across a full trajectory.

    Returns a list of length n - 1.
    """

    values = [float(x) for x in orientations]

    if len(values) < 2:
        return []

    return [
        values[i] - values[i - 1]
        for i in range(1, len(values))
    ]


def has_persistent_negative_decay(
    orientations: Iterable[float],
    theta_decay: float = -0.05,
    min_steps: int = 2,
) -> bool:
    """
    Detect whether a trajectory contains persistent negative orientation decay.
    """

    decays = detect_orientation_decay_sequence(orientations)

    if len(decays) < min_steps:
        return False

    count = sum(1 for d in decays if d <= theta_decay)

    return bool(count >= min_steps)