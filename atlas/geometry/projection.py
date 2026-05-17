"""
ACA — Axiomatic Criterion Atlas

Projection Geometry
-------------------

This module implements semantic projection onto an orthonormal field basis.

Projection is the geometric operation that allows ACA to evaluate how much
of an input embedding belongs to a semantic field and how much remains
outside that field.
"""

from __future__ import annotations

import numpy as np


def normalize_vector(vector: np.ndarray, epsilon: float = 1e-12) -> np.ndarray:
    """
    Normalize a single vector using L2 norm.
    """

    v = np.asarray(vector, dtype=np.float64)

    if v.ndim != 1:
        raise ValueError("vector must be a 1D array.")

    norm = np.linalg.norm(v)

    if norm < epsilon:
        return v

    return v / norm


def project_onto_basis(
    vector: np.ndarray,
    basis: np.ndarray,
    normalize_input: bool = True,
) -> np.ndarray:
    """
    Project a vector onto an orthonormal semantic basis.

    Parameters
    ----------
    vector:
        Input embedding with shape (embedding_dim,).

    basis:
        Orthonormal basis matrix with shape (embedding_dim, rank).

    normalize_input:
        Whether to normalize the input vector before projection.

    Returns
    -------
    np.ndarray
        Projection of the vector onto the semantic field.
    """

    z = np.asarray(vector, dtype=np.float64)
    B = np.asarray(basis, dtype=np.float64)

    if z.ndim != 1:
        raise ValueError("vector must be a 1D array.")

    if B.ndim != 2:
        raise ValueError("basis must be a 2D array.")

    if B.shape[0] != z.shape[0]:
        raise ValueError(
            f"dimension mismatch: vector has dim {z.shape[0]}, "
            f"basis has dim {B.shape[0]}."
        )

    if normalize_input:
        z = normalize_vector(z)

    return B @ (B.T @ z)


def residual_from_basis(
    vector: np.ndarray,
    basis: np.ndarray,
    normalize_input: bool = True,
) -> np.ndarray:
    """
    Compute the residual component outside the semantic field.

    The residual is defined as:

    z - Pi_S(z)
    """

    z = np.asarray(vector, dtype=np.float64)

    if normalize_input:
        z = normalize_vector(z)

    projection = project_onto_basis(
        z,
        basis,
        normalize_input=False,
    )

    return z - projection


def projection_norm(
    vector: np.ndarray,
    basis: np.ndarray,
    normalize_input: bool = True,
) -> float:
    """
    Compute the norm of the projected component.
    """

    projection = project_onto_basis(
        vector,
        basis,
        normalize_input=normalize_input,
    )

    return float(np.linalg.norm(projection))


def residual_norm(
    vector: np.ndarray,
    basis: np.ndarray,
    normalize_input: bool = True,
) -> float:
    """
    Compute the norm of the residual component.
    """

    residual = residual_from_basis(
        vector,
        basis,
        normalize_input=normalize_input,
    )

    return float(np.linalg.norm(residual))


def projection_ratio(
    vector: np.ndarray,
    basis: np.ndarray,
    normalize_input: bool = True,
    epsilon: float = 1e-12,
) -> float:
    """
    Compute how much of the vector norm is captured by the projection.

    A value close to 1 indicates strong field compatibility.
    A value close to 0 indicates weak compatibility.
    """

    z = np.asarray(vector, dtype=np.float64)

    if normalize_input:
        z = normalize_vector(z)

    total_norm = np.linalg.norm(z)

    if total_norm < epsilon:
        return 0.0

    projected = project_onto_basis(
        z,
        basis,
        normalize_input=False,
    )

    return float(np.linalg.norm(projected) / total_norm)