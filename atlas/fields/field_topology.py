"""
ACA — Semantic Field Topology

Defines semantic adjacency between fields.

Field transition is not automatically criterion drift.
ACA distinguishes:

- same field
- neighboring transition
- distant transition
- unknown transition
"""

from __future__ import annotations

from enum import Enum


class FieldTransition(str, Enum):
    SAME = "same"
    NEIGHBOR = "neighbor"
    DISTANT = "distant"
    UNKNOWN = "unknown"


FIELD_RELATIONS = {
    "foundational": {
        "neighbors": ["factual"],
        "distant": ["rhetorical", "narrative"],
    },
    "factual": {
        "neighbors": ["foundational", "scientific", "legal", "operational"],
        "distant": ["rhetorical", "narrative"],
    },
    "rhetorical": {
        "neighbors": ["narrative"],
        "distant": ["foundational", "factual", "scientific", "legal"],
    },
    "narrative": {
        "neighbors": ["rhetorical"],
        "distant": ["factual", "scientific", "legal"],
    },
    "scientific": {
        "neighbors": ["factual", "operational"],
        "distant": ["rhetorical", "narrative"],
    },
    "legal": {
        "neighbors": ["factual", "operational"],
        "distant": ["rhetorical", "narrative"],
    },
    "operational": {
        "neighbors": ["factual", "scientific", "legal", "business"],
        "distant": ["rhetorical"],
    },
    "business": {
        "neighbors": ["operational", "factual"],
        "distant": ["rhetorical"],
    },
}


def classify_field_transition(
    previous_field: str | None,
    current_field: str,
) -> FieldTransition:
    """
    Classify transition between semantic fields.
    """

    if previous_field is None:
        return FieldTransition.SAME

    if previous_field == current_field:
        return FieldTransition.SAME

    previous_relations = FIELD_RELATIONS.get(previous_field, {})

    if current_field in previous_relations.get("neighbors", []):
        return FieldTransition.NEIGHBOR

    if current_field in previous_relations.get("distant", []):
        return FieldTransition.DISTANT

    return FieldTransition.UNKNOWN


def field_transition_distance(
    previous_field: str | None,
    current_field: str,
) -> float:
    """
    Return a coarse semantic transition distance.

    0.0 = same field
    0.5 = neighboring field
    1.0 = distant field
    0.75 = unknown transition
    """

    transition = classify_field_transition(
        previous_field=previous_field,
        current_field=current_field,
    )

    if transition == FieldTransition.SAME:
        return 0.0

    if transition == FieldTransition.NEIGHBOR:
        return 0.5

    if transition == FieldTransition.DISTANT:
        return 1.0

    return 0.75


def is_neighbor_transition(
    previous_field: str | None,
    current_field: str,
) -> bool:
    return (
        classify_field_transition(previous_field, current_field)
        == FieldTransition.NEIGHBOR
    )


def is_distant_transition(
    previous_field: str | None,
    current_field: str,
) -> bool:
    return (
        classify_field_transition(previous_field, current_field)
        == FieldTransition.DISTANT
    )