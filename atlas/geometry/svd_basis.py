"""
ACA — Axiomatic Criterion Atlas

SVD Basis Construction
----------------------

This module builds orthonormal semantic bases from context matrices.

A semantic field is represented by anchor embeddings arranged as a context
matrix. Singular Value Decomposition is used to extract the dominant
orthonormal directions of the field.

These basis vectors define the geometric subspace used for projection,
origin cost, field selection, and criterion preservation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np


@dataclass
class SVDBasis:
    """
    Represents the orthonormal basis of a semantic field.

    Attributes
    ----------
    basis:
        Matrix whose columns form an orthonormal basis for the semantic field.

    singular_values:
        Singular values obtained from the context matrix decomposition.

    rank:
        Effective rank selected for the semantic field.

    explained_energy:
        Fraction of total singular-value energy preserved by the basis.
    """

    basis: np.ndarray
    singular_values: np.ndarray
    rank: int
    explained_energy: float


def normalize_rows(matrix: np.ndarray, epsilon: float = 1e-12) -> np.ndarray:
    """
    Normalize each row vector of a matrix.

    Parameters
    ----------
    matrix:
        Input matrix of shape (n_vectors, embedding_dim).

    epsilon:
        Numerical stability constant.

    Returns
    -------
    np.ndarray
        Row-normalized matrix.
    """

    matrix = np.asarray(matrix, dtype=np.float64)

    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms = np.maximum(norms, epsilon)

    return matrix / norms


def estimate_rank_from_energy(
    singular_values: np.ndarray,
    energy_threshold: float = 0.95,
) -> int:
    """
    Estimate the effective rank required to preserve a target amount of energy.

    Parameters
    ----------
    singular_values:
        Singular values from SVD.

    energy_threshold:
        Fraction of total singular-value energy to preserve.

    Returns
    -------
    int
        Effective rank.
    """

    singular_values = np.asarray(singular_values, dtype=np.float64)

    if singular_values.size == 0:
        raise ValueError("singular_values cannot be empty.")

    if not 0 < energy_threshold <= 1:
        raise ValueError("energy_threshold must be in the interval (0, 1].")

    energy = singular_values**2
    total_energy = np.sum(energy)

    if total_energy <= 0:
        return 1

    cumulative_energy = np.cumsum(energy) / total_energy

    rank = int(np.searchsorted(cumulative_energy, energy_threshold) + 1)

    return max(1, min(rank, singular_values.size))


def build_svd_basis(
    context_matrix: np.ndarray,
    rank: Optional[int] = None,
    energy_threshold: float = 0.95,
    normalize: bool = True,
) -> SVDBasis:
    """
    Build an orthonormal semantic basis from a context matrix.

    Parameters
    ----------
    context_matrix:
        Matrix of anchor embeddings with shape:

        (n_anchors, embedding_dim)

    rank:
        Optional fixed rank. If not provided, rank is estimated from
        singular-value energy.

    energy_threshold:
        Energy threshold used when rank is not explicitly provided.

    normalize:
        Whether to L2-normalize anchor embeddings before SVD.

    Returns
    -------
    SVDBasis
        Orthonormal basis and associated metadata.

    Notes
    -----
    Given a context matrix C:

    C = U Σ V^T

    The semantic field basis is extracted from the right singular vectors:

    B_S = V_r

    where V_r contains the first r right-singular directions as columns.
    """

    C = np.asarray(context_matrix, dtype=np.float64)

    if C.ndim != 2:
        raise ValueError("context_matrix must be a 2D array.")

    n_anchors, embedding_dim = C.shape

    if n_anchors == 0:
        raise ValueError("context_matrix must contain at least one anchor.")

    if embedding_dim == 0:
        raise ValueError("context_matrix must contain non-empty embeddings.")

    if normalize:
        C = normalize_rows(C)

    _, singular_values, vh = np.linalg.svd(C, full_matrices=False)

    max_rank = min(n_anchors, embedding_dim)

    if rank is None:
        selected_rank = estimate_rank_from_energy(
            singular_values,
            energy_threshold=energy_threshold,
        )
    else:
        selected_rank = int(rank)

    if selected_rank < 1:
        raise ValueError("rank must be at least 1.")

    selected_rank = min(selected_rank, max_rank)

    # vh has shape (rank_full, embedding_dim).
    # Right singular vectors are rows of vh.
    # We transpose them so basis columns are orthonormal directions.
    basis = vh[:selected_rank].T

    energy = singular_values**2
    total_energy = float(np.sum(energy))

    if total_energy > 0:
        explained_energy = float(np.sum(energy[:selected_rank]) / total_energy)
    else:
        explained_energy = 0.0

    return SVDBasis(
        basis=basis,
        singular_values=singular_values,
        rank=selected_rank,
        explained_energy=explained_energy,
    )


def validate_orthonormal_basis(
    basis: np.ndarray,
    tolerance: float = 1e-6,
) -> bool:
    """
    Validate whether the basis columns are approximately orthonormal.

    Parameters
    ----------
    basis:
        Basis matrix with shape (embedding_dim, rank).

    tolerance:
        Numerical tolerance for orthonormality.

    Returns
    -------
    bool
        True if basis is approximately orthonormal.
    """

    B = np.asarray(basis, dtype=np.float64)

    if B.ndim != 2:
        return False

    rank = B.shape[1]

    identity = np.eye(rank)
    gram = B.T @ B

    return bool(np.allclose(gram, identity, atol=tolerance))