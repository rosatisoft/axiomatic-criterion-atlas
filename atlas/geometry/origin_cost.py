"""
ACA — Axiomatic Criterion Atlas

Origin Cost
-----------

Origin cost measures the geometric deviation of an input embedding from a
semantic field.

Given a semantic field basis B_S, the projection of z onto the field is:

    Pi_S(z) = B_S B_S^T z

The origin cost is:

    O_S(z) = || z - Pi_S(z) ||^2

Low origin cost indicates contextual compatibility.
High origin cost indicates semantic dispersion.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from atlas.geometry.projection import (
    normalize_vector,
    project_onto_basis,
    residual_from_basis,
)


@dataclass
class OriginCostResult:
    """
    Result of an origin-cost evaluation.
    """

    origin_cost: float
    residual_norm: float
    projection_norm: float
    total_norm: float


def compute_origin_cost(
    vector: np.ndarray,
    basis: np.ndarray,
    normalize_input: bool = True,
) -> OriginCostResult:
    """
    Compute origin cost relative to a semantic field basis.

    Parameters
    ----------
    vector:
        Input embedding with shape (embedding_dim,).

    basis:
        Orthonormal semantic field basis with shape (embedding_dim, rank).

    normalize_input:
        Whether to normalize the vector before evaluation.

    Returns
    -------
    OriginCostResult
        Origin cost and related geometric diagnostics.
    """

    z = np.asarray(vector, dtype=np.float64)

    if z.ndim != 1:
        raise ValueError("vector must be a 1D array.")

    if normalize_input:
        z = normalize_vector(z)

    projection = project_onto_basis(
        z,
        basis,
        normalize_input=False,
    )

    residual = residual_from_basis(
        z,
        basis,
        normalize_input=False,
    )

    residual_norm = float(np.linalg.norm(residual))
    projection_norm = float(np.linalg.norm(projection))
    total_norm = float(np.linalg.norm(z))

    origin_cost = float(residual_norm**2)

    return OriginCostResult(
        origin_cost=origin_cost,
        residual_norm=residual_norm,
        projection_norm=projection_norm,
        total_norm=total_norm,
    )


def origin_cost_value(
    vector: np.ndarray,
    basis: np.ndarray,
    normalize_input: bool = True,
) -> float:
    """
    Convenience function returning only the origin cost value.
    """

    result = compute_origin_cost(
        vector=vector,
        basis=basis,
        normalize_input=normalize_input,
    )

    return result.origin_cost


def normalized_origin_cost(
    vector: np.ndarray,
    basis: np.ndarray,
    normalize_input: bool = True,
    epsilon: float = 1e-12,
) -> float:
    """
    Compute origin cost normalized by total vector norm.

    Useful when comparing embeddings that may not be pre-normalized.
    """

    result = compute_origin_cost(
        vector=vector,
        basis=basis,
        normalize_input=normalize_input,
    )

    denom = max(result.total_norm**2, epsilon)

    return float(result.origin_cost / denom)