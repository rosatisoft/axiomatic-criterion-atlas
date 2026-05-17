"""
ACA — Axiomatic Criterion Atlas

Field Hierarchy
---------------

Defines the hierarchical organization of semantic fields.

ACA distinguishes between:

1. Foundational fields
   - criterion-preserving invariant structure

2. Epistemic fields
   - factual, scientific, legal, operational reasoning

3. Expressive fields
   - rhetorical, narrative, persuasive, symbolic reasoning

This hierarchy allows ACA to separate:

- structural criterion
- evidential grounding
- rhetorical or narrative movement
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional

from atlas.fields.field import SemanticField


class FieldLayer(str, Enum):
    """
    Canonical ACA field layers.
    """

    FOUNDATIONAL = "foundational"
    EPISTEMIC = "epistemic"
    EXPRESSIVE = "expressive"
    DOMAIN = "domain"


FIELD_LAYER_MAP = {
    "foundational": FieldLayer.FOUNDATIONAL,
    "fundamental": FieldLayer.FOUNDATIONAL,

    "factual": FieldLayer.EPISTEMIC,
    "scientific": FieldLayer.EPISTEMIC,
    "legal": FieldLayer.EPISTEMIC,
    "operational": FieldLayer.EPISTEMIC,

    "rhetorical": FieldLayer.EXPRESSIVE,
    "narrative": FieldLayer.EXPRESSIVE,
    "persuasive": FieldLayer.EXPRESSIVE,
    "fiction": FieldLayer.EXPRESSIVE,

    "business": FieldLayer.DOMAIN,
    "conceptual": FieldLayer.DOMAIN,
}


@dataclass
class FieldHierarchy:
    """
    Registry and hierarchy manager for semantic fields.
    """

    fields: Dict[str, SemanticField] = field(default_factory=dict)

    def register(self, field_obj: SemanticField) -> None:
        """
        Register a semantic field.
        """

        self.fields[field_obj.field_type] = field_obj

    def get(self, field_type: str) -> SemanticField:
        """
        Get field by type.
        """

        if field_type not in self.fields:
            raise KeyError(f"field not registered: {field_type}")

        return self.fields[field_type]

    def layer_of(self, field_type: str) -> FieldLayer:
        """
        Return hierarchy layer for a field type.
        """

        return FIELD_LAYER_MAP.get(
            field_type,
            FieldLayer.DOMAIN,
        )

    def fields_by_layer(self, layer: FieldLayer | str) -> List[SemanticField]:
        """
        Return all registered fields belonging to a given layer.
        """

        layer = FieldLayer(layer)

        return [
            field_obj
            for field_type, field_obj in self.fields.items()
            if self.layer_of(field_type) == layer
        ]

    def field_types(self) -> List[str]:
        """
        Return registered field types.
        """

        return list(self.fields.keys())

    def has_field(self, field_type: str) -> bool:
        """
        Return True if field type is registered.
        """

        return field_type in self.fields

    def primary_foundational_field(self) -> Optional[SemanticField]:
        """
        Return the primary foundational field if registered.
        """

        foundational_fields = self.fields_by_layer(FieldLayer.FOUNDATIONAL)

        if not foundational_fields:
            return None

        return foundational_fields[0]

    def epistemic_fields(self) -> List[SemanticField]:
        """
        Return all epistemic fields.
        """

        return self.fields_by_layer(FieldLayer.EPISTEMIC)

    def expressive_fields(self) -> List[SemanticField]:
        """
        Return all expressive fields.
        """

        return self.fields_by_layer(FieldLayer.EXPRESSIVE)