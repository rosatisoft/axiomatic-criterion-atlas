"""
ACA — Axiomatic Criterion Atlas

Semantic Field
--------------

Base semantic field abstraction.

A semantic field is a structured geometric region generated from anchor
embeddings. It provides:

- field identity
- anchor texts
- context matrix
- orthonormal basis
- metadata
- compatibility evaluation
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

import numpy as np

from atlas.geometry.origin_cost import OriginCostResult, compute_origin_cost
from atlas.geometry.svd_basis import SVDBasis, build_svd_basis


@dataclass
class SemanticField:
    """
    Base semantic field representation.
    """

    name: str
    field_type: str
    anchors: List[str]
    context_matrix: np.ndarray
    basis: np.ndarray
    metadata: Dict[str, Any] = field(default_factory=dict)
    singular_values: Optional[np.ndarray] = None
    svd_rank: Optional[int] = None
    explained_energy: Optional[float] = None

    def evaluate_compatibility(
        self,
        vector: np.ndarray,
        normalize_input: bool = True,
    ) -> OriginCostResult:
        """
        Evaluate contextual compatibility through origin cost.
        """

        return compute_origin_cost(
            vector=vector,
            basis=self.basis,
            normalize_input=normalize_input,
        )

    @classmethod
    def from_anchor_embeddings(
        cls,
        name: str,
        field_type: str,
        anchors: List[str],
        anchor_embeddings: List[np.ndarray],
        metadata: Optional[Dict[str, Any]] = None,
        energy_threshold: float = 0.95,
        normalize: bool = True,
    ) -> "SemanticField":
        """
        Build a semantic field from anchor texts and embeddings.
        """

        if not anchors:
            raise ValueError("anchors cannot be empty.")

        if len(anchors) != len(anchor_embeddings):
            raise ValueError(
                "anchors and anchor_embeddings must have the same length."
            )

        context_matrix = np.vstack(
            [np.asarray(vector, dtype=np.float64) for vector in anchor_embeddings]
        )

        svd_basis: SVDBasis = build_svd_basis(
            context_matrix=context_matrix,
            energy_threshold=energy_threshold,
            normalize=normalize,
        )

        return cls(
            name=name,
            field_type=field_type,
            anchors=anchors,
            context_matrix=context_matrix,
            basis=svd_basis.basis,
            metadata=metadata or {},
            singular_values=svd_basis.singular_values,
            svd_rank=svd_basis.rank,
            explained_energy=svd_basis.explained_energy,
        )

    def to_metadata(self) -> Dict[str, Any]:
        """
        Export field metadata.
        """

        return {
            "name": self.name,
            "field_type": self.field_type,
            "n_anchors": len(self.anchors),
            "embedding_dim": int(self.context_matrix.shape[1]),
            "svd_rank": self.svd_rank,
            "explained_energy": self.explained_energy,
            "metadata": self.metadata,
        }