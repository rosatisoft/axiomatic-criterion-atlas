"""
ACA — Axiomatic Criterion Atlas

Preservation Metrics
--------------------

This module combines contextual compatibility and epistemic orientation into
criterion-preservation measurements.

ACA defines geometric preservation as:

    O(z_t) <= theta_O
    and
    Phi(z_t) >= theta_Phi

where:

    O(z_t) measures semantic field compatibility.
    Phi(z_t) measures directional criterion preservation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np


@dataclass
class PreservationMetrics:
    """
    Combined preservation metrics for a semantic state.
    """

    origin_cost: float
    orientation: float
    preservation_score: float
    compatibility_score: float
    orientation_score: float
    is_preserved: bool


def compatibility_score_from_origin_cost(
    origin_cost: float,
    theta_origin: float,
    epsilon: float = 1e-12,
) -> float:
    """
    Convert origin cost into a normalized compatibility score.

    Higher is better.

    A value near 1 indicates strong compatibility.
    A value near 0 indicates weak compatibility.
    """

    if theta_origin <= 0:
        raise ValueError("theta_origin must be positive.")

    score = 1.0 - (origin_cost / max(theta_origin, epsilon))

    return float(np.clip(score, 0.0, 1.0))


def orientation_score_from_phi(
    orientation: float,
    theta_orientation: float,
    epsilon: float = 1e-12,
) -> float:
    """
    Convert epistemic orientation into a normalized orientation score.

    Higher is better.

    Negative orientation maps to 0.
    Orientation equal to theta_orientation maps approximately to 1.
    """

    if theta_orientation <= 0:
        raise ValueError("theta_orientation must be positive.")

    score = orientation / max(theta_orientation, epsilon)

    return float(np.clip(score, 0.0, 1.0))


def compute_preservation_score(
    origin_cost: float,
    orientation: float,
    theta_origin: float,
    theta_orientation: float,
    compatibility_weight: float = 0.5,
    orientation_weight: float = 0.5,
) -> PreservationMetrics:
    """
    Compute combined criterion-preservation metrics.

    Parameters
    ----------
    origin_cost:
        Origin cost relative to the active semantic field.

    orientation:
        Aggregate epistemic orientation.

    theta_origin:
        Maximum origin cost for contextual compatibility.

    theta_orientation:
        Minimum orientation for criterion preservation.

    compatibility_weight:
        Weight assigned to contextual compatibility.

    orientation_weight:
        Weight assigned to epistemic orientation.

    Returns
    -------
    PreservationMetrics
        Combined preservation diagnostics.
    """

    total_weight = compatibility_weight + orientation_weight

    if total_weight <= 0:
        raise ValueError("combined weights must be positive.")

    compatibility_weight = compatibility_weight / total_weight
    orientation_weight = orientation_weight / total_weight

    compatibility_score = compatibility_score_from_origin_cost(
        origin_cost=origin_cost,
        theta_origin=theta_origin,
    )

    orientation_score = orientation_score_from_phi(
        orientation=orientation,
        theta_orientation=theta_orientation,
    )

    preservation_score = (
        compatibility_weight * compatibility_score
        + orientation_weight * orientation_score
    )

    is_preserved = (
        origin_cost <= theta_origin
        and orientation >= theta_orientation
    )

    return PreservationMetrics(
        origin_cost=float(origin_cost),
        orientation=float(orientation),
        preservation_score=float(preservation_score),
        compatibility_score=float(compatibility_score),
        orientation_score=float(orientation_score),
        is_preserved=bool(is_preserved),
    )


def trajectory_preservation_average(
    preservation_scores: list[float],
) -> Optional[float]:
    """
    Compute the average preservation score across a trajectory.
    """

    if not preservation_scores:
        return None

    return float(np.mean(preservation_scores))


def trajectory_minimum_preservation(
    preservation_scores: list[float],
) -> Optional[float]:
    """
    Compute the weakest preservation point across a trajectory.
    """

    if not preservation_scores:
        return None

    return float(np.min(preservation_scores))