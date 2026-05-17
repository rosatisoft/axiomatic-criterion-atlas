"""
ACA — Axiomatic Criterion Atlas

Directional Invariant
---------------------

Directional invariants define semantic orientation geometry.

Each invariant contains:

- preservation pole
- inversion pole
- directional vector
- orientation evaluation
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np

from atlas.invariants.invariant import Invariant


@dataclass
class DirectionalInvariant(Invariant):
    """
    Directional semantic invariant.
    """

    preservation_pole: np.ndarray | None = None
    inversion_pole: np.ndarray | None = None

    direction: np.ndarray | None = None

    norm: Optional[float] = None

    @classmethod
    def from_poles(
        cls,
        name: str,
        description: str,
        preservation_pole: np.ndarray,
        inversion_pole: np.ndarray,
        normalize: bool = True,
    ) -> "DirectionalInvariant":
        """
        Build directional invariant from semantic poles.
        """

        preservation_pole = np.asarray(
            preservation_pole,
            dtype=np.float64,
        )

        inversion_pole = np.asarray(
            inversion_pole,
            dtype=np.float64,
        )

        direction = preservation_pole - inversion_pole

        norm = np.linalg.norm(direction)

        if normalize and norm > 1e-12:
            direction = direction / norm

        return cls(
            name=name,
            description=description,
            preservation_pole=preservation_pole,
            inversion_pole=inversion_pole,
            direction=direction,
            norm=float(norm),
        )

    def orientation(
        self,
        vector: np.ndarray,
        normalize_input: bool = True,
    ) -> float:
        """
        Compute invariant orientation score.
        """

        if self.direction is None:
            raise ValueError("direction is not initialized.")

        vector = np.asarray(vector, dtype=np.float64)

        if normalize_input:
            vector_norm = np.linalg.norm(vector)

            if vector_norm > 1e-12:
                vector = vector / vector_norm

        return float(np.dot(vector, self.direction))