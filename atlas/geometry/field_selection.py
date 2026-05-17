"""
ACA — Axiomatic Criterion Atlas

Semantic Field Selection
------------------------

This module evaluates contextual compatibility across multiple semantic
fields and selects the dominant field according to minimum origin cost.

ACA defines the dominant semantic field as:

    S*(z) = argmin O_S(z)

where:

    O_S(z)

is the origin cost relative to semantic field S.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

import numpy as np

from atlas.geometry.origin_cost import (
    OriginCostResult,
    compute_origin_cost,
)


@dataclass
class FieldScore:
    """
    Evaluation score for a single semantic field.
    """

    field_name: str
    origin_cost: float
    residual_norm: float
    projection_norm: float
    total_norm: float


@dataclass
class FieldSelectionResult:
    """
    Result of semantic field selection.
    """

    selected_field: str
    selected_score: FieldScore
    second_best_score: FieldScore
    margin: float
    scores: List[FieldScore]


def evaluate_fields(
    vector: np.ndarray,
    field_bases: Dict[str, np.ndarray],
    normalize_input: bool = True,
) -> List[FieldScore]:
    """
    Evaluate origin cost against all semantic fields.

    Parameters
    ----------
    vector:
        Input embedding.

    field_bases:
        Dictionary mapping field names to orthonormal bases.

    normalize_input:
        Whether to normalize the input vector.

    Returns
    -------
    List[FieldScore]
        Scores sorted by ascending origin cost.
    """

    z = np.asarray(vector, dtype=np.float64)

    if z.ndim != 1:
        raise ValueError("vector must be a 1D array.")

    if not field_bases:
        raise ValueError("field_bases cannot be empty.")

    scores: List[FieldScore] = []

    for field_name, basis in field_bases.items():

        result: OriginCostResult = compute_origin_cost(
            vector=z,
            basis=basis,
            normalize_input=normalize_input,
        )

        scores.append(
            FieldScore(
                field_name=field_name,
                origin_cost=result.origin_cost,
                residual_norm=result.residual_norm,
                projection_norm=result.projection_norm,
                total_norm=result.total_norm,
            )
        )

    scores.sort(key=lambda x: x.origin_cost)

    return scores


def select_field(
    vector: np.ndarray,
    field_bases: Dict[str, np.ndarray],
    normalize_input: bool = True,
) -> FieldSelectionResult:
    """
    Select the dominant semantic field.

    The dominant field is the field with minimum origin cost.

    Returns
    -------
    FieldSelectionResult
        Full selection diagnostics.
    """

    scores = evaluate_fields(
        vector=vector,
        field_bases=field_bases,
        normalize_input=normalize_input,
    )

    selected_score = scores[0]

    if len(scores) > 1:
        second_best_score = scores[1]
    else:
        second_best_score = scores[0]

    margin = (
        second_best_score.origin_cost
        - selected_score.origin_cost
    )

    return FieldSelectionResult(
        selected_field=selected_score.field_name,
        selected_score=selected_score,
        second_best_score=second_best_score,
        margin=float(margin),
        scores=scores,
    )


def field_margin(
    vector: np.ndarray,
    field_bases: Dict[str, np.ndarray],
    normalize_input: bool = True,
) -> float:
    """
    Convenience function returning only the field competition margin.
    """

    result = select_field(
        vector=vector,
        field_bases=field_bases,
        normalize_input=normalize_input,
    )

    return result.margin


def dominant_field(
    vector: np.ndarray,
    field_bases: Dict[str, np.ndarray],
    normalize_input: bool = True,
) -> str:
    """
    Convenience function returning only the dominant field name.
    """

    result = select_field(
        vector=vector,
        field_bases=field_bases,
        normalize_input=normalize_input,
    )

    return result.selected_field