"""
ACA — Axiomatic Criterion Atlas

Criterion Vectors
-----------------

This module constructs directional invariant vectors from preservation and
inversion poles.

Each invariant is represented by two semantic poles:

    v_i^+  preservation pole
    v_i^-  inversion pole

The directional criterion vector is defined as:

    d_i = (v_i^+ - v_i^-) / ||v_i^+ - v_i^-||

These vectors define the orientation geometry used for epistemic orientation,
criterion drift detection, and trajectory preservation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

import numpy as np


@dataclass
class CriterionVector:
    """
    Directional invariant vector associated with a semantic invariant.
    """

    invariant_name: str
    direction: np.ndarray
    preservation_pole: np.ndarray
    inversion_pole: np.ndarray
    norm: float


def normalize_vector(vector: np.ndarray, epsilon: float = 1e-12) -> np.ndarray:
    """
    Normalize a vector using L2 norm.
    """

    v = np.asarray(vector, dtype=np.float64)

    if v.ndim != 1:
        raise ValueError("vector must be a 1D array.")

    norm = np.linalg.norm(v)

    if norm < epsilon:
        raise ValueError("cannot normalize a near-zero vector.")

    return v / norm


def build_criterion_vector(
    invariant_name: str,
    preservation_pole: np.ndarray,
    inversion_pole: np.ndarray,
    epsilon: float = 1e-12,
) -> CriterionVector:
    """
    Build a directional criterion vector from preservation and inversion poles.

    Parameters
    ----------
    invariant_name:
        Name of the invariant.

    preservation_pole:
        Embedding of the preservation pole.

    inversion_pole:
        Embedding of the inversion pole.

    epsilon:
        Numerical stability threshold.

    Returns
    -------
    CriterionVector
        Directional invariant vector and metadata.
    """

    v_plus = np.asarray(preservation_pole, dtype=np.float64)
    v_minus = np.asarray(inversion_pole, dtype=np.float64)

    if v_plus.ndim != 1:
        raise ValueError("preservation_pole must be a 1D array.")

    if v_minus.ndim != 1:
        raise ValueError("inversion_pole must be a 1D array.")

    if v_plus.shape != v_minus.shape:
        raise ValueError(
            "preservation_pole and inversion_pole must have the same shape."
        )

    delta = v_plus - v_minus
    norm = float(np.linalg.norm(delta))

    if norm < epsilon:
        raise ValueError(
            f"invariant '{invariant_name}' has nearly identical poles."
        )

    direction = delta / norm

    return CriterionVector(
        invariant_name=invariant_name,
        direction=direction,
        preservation_pole=v_plus,
        inversion_pole=v_minus,
        norm=norm,
    )


def build_criterion_vectors(
    poles: Dict[str, Dict[str, np.ndarray]],
) -> List[CriterionVector]:
    """
    Build criterion vectors from a dictionary of invariant poles.

    Expected structure:

    {
        "evidence": {
            "preservation": np.ndarray,
            "inversion": np.ndarray
        },
        "identity": {
            "preservation": np.ndarray,
            "inversion": np.ndarray
        }
    }
    """

    vectors: List[CriterionVector] = []

    for invariant_name, pole_pair in poles.items():

        if "preservation" not in pole_pair:
            raise ValueError(
                f"invariant '{invariant_name}' is missing preservation pole."
            )

        if "inversion" not in pole_pair:
            raise ValueError(
                f"invariant '{invariant_name}' is missing inversion pole."
            )

        vectors.append(
            build_criterion_vector(
                invariant_name=invariant_name,
                preservation_pole=pole_pair["preservation"],
                inversion_pole=pole_pair["inversion"],
            )
        )

    return vectors


def criterion_matrix(
    criterion_vectors: List[CriterionVector],
) -> np.ndarray:
    """
    Construct a matrix whose rows are criterion direction vectors.

    Shape:

        (n_invariants, embedding_dim)
    """

    if not criterion_vectors:
        raise ValueError("criterion_vectors cannot be empty.")

    directions = [cv.direction for cv in criterion_vectors]

    return np.vstack(directions)


def criterion_names(
    criterion_vectors: List[CriterionVector],
) -> List[str]:
    """
    Return invariant names in criterion-vector order.
    """

    return [cv.invariant_name for cv in criterion_vectors]