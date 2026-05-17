"""
ACA — Axiomatic Criterion Atlas

Invariant Registry
------------------

Registry for managing ACA invariants.

The registry allows runtime systems, benchmarks, and field definitions
to retrieve invariant structures by name.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List

from atlas.invariants.invariant import Invariant
from atlas.invariants.directional_invariant import DirectionalInvariant


@dataclass
class InvariantRegistry:
    """
    Registry of semantic invariants.
    """

    invariants: Dict[str, Invariant] = field(default_factory=dict)

    def register(self, invariant: Invariant) -> None:
        """
        Register an invariant by name.
        """

        self.invariants[invariant.name] = invariant

    def get(self, name: str) -> Invariant:
        """
        Retrieve an invariant by name.
        """

        if name not in self.invariants:
            raise KeyError(f"invariant not registered: {name}")

        return self.invariants[name]

    def has(self, name: str) -> bool:
        """
        Return True if invariant exists.
        """

        return name in self.invariants

    def names(self) -> List[str]:
        """
        Return registered invariant names.
        """

        return list(self.invariants.keys())

    def all(self) -> List[Invariant]:
        """
        Return all registered invariants.
        """

        return list(self.invariants.values())

    def directional(self) -> List[DirectionalInvariant]:
        """
        Return all directional invariants.
        """

        return [
            invariant
            for invariant in self.invariants.values()
            if isinstance(invariant, DirectionalInvariant)
        ]

    @classmethod
    def from_invariants(
        cls,
        invariants: Iterable[Invariant],
    ) -> "InvariantRegistry":
        """
        Build registry from an iterable of invariants.
        """

        registry = cls()

        for invariant in invariants:
            registry.register(invariant)

        return registry