"""
ACA — Axiomatic Criterion Atlas

Build Invariant Registry
------------------------

Utilities for constructing an InvariantRegistry from semantic pole texts
and an embedding provider.

This module bridges:

- criterion poles
- embeddings
- directional invariants
- invariant registry
"""

from __future__ import annotations

from typing import Dict, Protocol

import numpy as np

from atlas.invariants.directional_invariant import DirectionalInvariant
from atlas.invariants.invariant_registry import InvariantRegistry


class EmbedderProtocol(Protocol):
    """
    Minimal protocol expected from an embedding provider.
    """

    def embed_text(self, text: str) -> np.ndarray:
        ...


def build_directional_invariant_from_texts(
    name: str,
    preservation_text: str,
    inversion_text: str,
    embedder: EmbedderProtocol,
    description: str = "",
) -> DirectionalInvariant:
    """
    Build a DirectionalInvariant from preservation and inversion pole texts.
    """

    preservation_embedding = embedder.embed_text(preservation_text)
    inversion_embedding = embedder.embed_text(inversion_text)

    return DirectionalInvariant.from_poles(
        name=name,
        description=description or name,
        preservation_pole=preservation_embedding,
        inversion_pole=inversion_embedding,
        normalize=True,
    )


def build_invariant_registry_from_poles(
    poles: Dict[str, Dict[str, str]],
    embedder: EmbedderProtocol,
) -> InvariantRegistry:
    """
    Build an InvariantRegistry from pole definitions.

    Expected pole format:

    {
        "evidence_constraint": {
            "preservation": "...",
            "inversion": "..."
        }
    }
    """

    registry = InvariantRegistry()

    for name, pole_pair in poles.items():

        if "preservation" not in pole_pair:
            raise ValueError(
                f"missing preservation pole for invariant: {name}"
            )

        if "inversion" not in pole_pair:
            raise ValueError(
                f"missing inversion pole for invariant: {name}"
            )

        invariant = build_directional_invariant_from_texts(
            name=name,
            preservation_text=pole_pair["preservation"],
            inversion_text=pole_pair["inversion"],
            embedder=embedder,
            description=f"Directional invariant for {name}",
        )

        registry.register(invariant)

    return registry


def invariant_direction_matrix(
    registry: InvariantRegistry,
) -> np.ndarray:
    """
    Return matrix of invariant direction vectors.

    Shape:

        (n_invariants, embedding_dim)
    """

    directional = registry.directional()

    if not directional:
        raise ValueError("registry contains no directional invariants.")

    directions = []

    for invariant in directional:
        if invariant.direction is None:
            raise ValueError(
                f"invariant has no direction: {invariant.name}"
            )

        directions.append(invariant.direction)

    return np.vstack(directions)


def invariant_names(
    registry: InvariantRegistry,
) -> list[str]:
    """
    Return invariant names in registry order.
    """

    return [
        invariant.name
        for invariant in registry.directional()
    ]