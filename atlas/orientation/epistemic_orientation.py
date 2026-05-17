"""
ACA — Axiomatic Criterion Atlas

Epistemic Orientation
---------------------

This module measures directional invariant preservation.

Given a normalized embedding z and a directional invariant vector d_i:

    phi_i(z) = <z, d_i>

Aggregate epistemic orientation is defined as:

    Phi(z) = sum_i w_i phi_i(z)

Positive orientation indicates criterion preservation.
Negative orientation indicates criterion inversion.
Near-zero orientation indicates ambiguity or weak orientation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional

import numpy as np

from atlas.orientation.criterion_vectors import CriterionVector


@dataclass
class OrientationScore:
    """
    Orientation score for a single invariant.
    """

    invariant_name: str
    phi: float
    weight: float
    weighted_phi: float


@dataclass
class EpistemicOrientationResult:
    """
    Full epistemic orientation evaluation.
    """

    aggregate_orientation: float
    scores: List[OrientationScore]


def normalize_vector(vector: np.ndarray, epsilon: float = 1e-12) -> np.ndarray:
    """
    Normalize a vector using L2 norm.
    """

    z = np.asarray(vector, dtype=np.float64)

    if z.ndim != 1:
        raise ValueError("vector must be a 1D array.")

    norm = np.linalg.norm(z)

    if norm < epsilon:
        raise ValueError("cannot normalize a near-zero vector.")

    return z / norm


def invariant_orientation(
    vector: np.ndarray,
    criterion_vector: CriterionVector,
    normalize_input: bool = True,
) -> float:
    """
    Compute orientation relative to a single directional invariant.

    Parameters
    ----------
    vector:
        Input embedding.

    criterion_vector:
        Directional invariant vector.

    normalize_input:
        Whether to normalize the input embedding.

    Returns
    -------
    float
        Orientation projection phi_i(z).
    """

    z = np.asarray(vector, dtype=np.float64)

    if normalize_input:
        z = normalize_vector(z)

    d = np.asarray(criterion_vector.direction, dtype=np.float64)

    if z.shape != d.shape:
        raise ValueError(
            f"dimension mismatch: vector has shape {z.shape}, "
            f"criterion direction has shape {d.shape}."
        )

    return float(np.dot(z, d))


def evaluate_epistemic_orientation(
    vector: np.ndarray,
    criterion_vectors: Iterable[CriterionVector],
    weights: Optional[Dict[str, float]] = None,
    normalize_input: bool = True,
) -> EpistemicOrientationResult:
    """
    Evaluate aggregate epistemic orientation across multiple invariants.

    Parameters
    ----------
    vector:
        Input embedding.

    criterion_vectors:
        Iterable of CriterionVector objects.

    weights:
        Optional dictionary mapping invariant names to relevance weights.
        Missing weights default to 1.0.

    normalize_input:
        Whether to normalize the input embedding.

    Returns
    -------
    EpistemicOrientationResult
        Aggregate orientation and per-invariant scores.
    """

    criterion_vectors = list(criterion_vectors)

    if not criterion_vectors:
        raise ValueError("criterion_vectors cannot be empty.")

    z = np.asarray(vector, dtype=np.float64)

    if normalize_input:
        z = normalize_vector(z)

    scores: List[OrientationScore] = []
    aggregate = 0.0

    for cv in criterion_vectors:

        phi = invariant_orientation(
            vector=z,
            criterion_vector=cv,
            normalize_input=False,
        )

        weight = 1.0

        if weights is not None:
            weight = float(weights.get(cv.invariant_name, 1.0))

        weighted_phi = weight * phi
        aggregate += weighted_phi

        scores.append(
            OrientationScore(
                invariant_name=cv.invariant_name,
                phi=phi,
                weight=weight,
                weighted_phi=weighted_phi,
            )
        )

    return EpistemicOrientationResult(
        aggregate_orientation=float(aggregate),
        scores=scores,
    )


def aggregate_orientation_value(
    vector: np.ndarray,
    criterion_vectors: Iterable[CriterionVector],
    weights: Optional[Dict[str, float]] = None,
    normalize_input: bool = True,
) -> float:
    """
    Convenience function returning only aggregate orientation.
    """

    result = evaluate_epistemic_orientation(
        vector=vector,
        criterion_vectors=criterion_vectors,
        weights=weights,
        normalize_input=normalize_input,
    )

    return result.aggregate_orientation