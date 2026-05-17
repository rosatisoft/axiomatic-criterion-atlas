"""
ACA — Axiomatic Criterion Atlas

Invariant
---------

Base invariant abstraction for ACA.

An invariant represents a persistent semantic structure required
for criterion-preserving reasoning.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class Invariant:
    """
    Base invariant representation.
    """

    name: str
    description: str

    metadata: Dict[str, Any] = field(default_factory=dict)

    preservation_definition: Optional[str] = None
    inversion_definition: Optional[str] = None

    def to_metadata(self) -> Dict[str, Any]:
        """
        Export invariant metadata.
        """

        return {
            "name": self.name,
            "description": self.description,
            "preservation_definition": self.preservation_definition,
            "inversion_definition": self.inversion_definition,
            "metadata": self.metadata,
        }