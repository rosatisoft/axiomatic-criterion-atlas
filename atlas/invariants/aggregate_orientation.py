"""
ACA — Axiomatic Criterion Atlas

Aggregate Orientation
---------------------

Utilities for evaluating multi-invariant epistemic orientation.

Aggregate orientation combines multiple directional invariant projections:

    Phi(z) = sum_i w_i phi_i(z)

where:

    phi_i(z) = <z, d_i>
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional

import numpy as np

from atlas.invariants.directional_invariant import DirectionalInvariant


@dataclass
class InvariantOrientationScore:
    """
    Orientation score for a single directional invariant.
    """

    invariant_name: str
    phi: float
    weight: float
    weighted_phi: float


@dataclass
class AggregateOrientationResult:
    """
    Aggregate orientation evaluation result.
    """

    aggregate_orientation: float
    scores: List[InvariantOrientationScore]


def evaluate_aggregate_orientation(
    vector: np.ndarray,
    invariants: Iterable[DirectionalInvariant],
    weights: Optional[Dict[str, float]] = None,
    normalize_input: bool = True,
) -> AggregateOrientationResult:
    """
    Evaluate aggregate orientation across directional invariants.
    """

    invariants = list(invariants)

    if not invariants:
        raise ValueError("invariants cannot be empty.")

    scores: List[InvariantOrientationScore] = []
    aggregate = 0.0

    for invariant in invariants:
        phi = invariant.orientation(
            vector=vector,
            normalize_input=normalize_input,
        )

        weight = 1.0

        if weights is not None:
            weight = float(weights.get(invariant.name, 1.0))

        weighted_phi = weight * phi
        aggregate += weighted_phi

        scores.append(
            InvariantOrientationScore(
                invariant_name=invariant.name,
                phi=float(phi),
                weight=float(weight),
                weighted_phi=float(weighted_phi),
            )
        )

    return AggregateOrientationResult(
        aggregate_orientation=float(aggregate),
        scores=scores,
    )