"""
ACA Runtime Decisions

Hierarchical decision policy for ACA Runtime.

This layer interprets geometric measurements according to:

- selected semantic field
- origin cost
- epistemic orientation
- orientation decay
- drift state
- field transition

The goal is not to replace geometry, but to convert it into practical
runtime behavior.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from atlas.runtime.policies import RuntimeAction

from atlas.fields.field_topology import (
    FieldTransition,
    classify_field_transition,
)


@dataclass
class DecisionInput:
    """
    Inputs required for runtime decision interpretation.
    """

    selected_field: str
    origin_cost: float
    orientation: float
    orientation_decay: Optional[float]
    drift_state: str
    previous_field: Optional[str] = None
    margin: Optional[float] = None


@dataclass
class DecisionResult:
    """
    Runtime decision with explanation.
    """

    action: RuntimeAction
    reason: str


def decide_runtime_action(
    data: DecisionInput,
) -> DecisionResult:
    """
    Hierarchical ACA runtime decision policy.
    """

    field = data.selected_field
    state = data.drift_state
    orientation = data.orientation
    decay = data.orientation_decay
    origin_cost = data.origin_cost
    previous_field = data.previous_field

    transition = classify_field_transition(
        previous_field=previous_field,
        current_field=field,
    )

    if state == "reorienting":
        return DecisionResult(
            action=RuntimeAction.ALLOW_LIGHT,
            reason="neighboring field reorientation preserving criterion continuity",
        )


    # 1. Strong dispersion
    if state == "dispersed":
        if field == "rhetorical" and orientation < 0:
            return DecisionResult(
                action=RuntimeAction.FLAG_DRIFT,
                reason="rhetorical field with negative orientation under dispersion",
            )

        return DecisionResult(
            action=RuntimeAction.REJECT_OR_CLARIFY,
            reason="input is outside stable field compatibility",
        )

    # 2. Clear inversion
    if state == "inverted":
        if field == "rhetorical":
            return DecisionResult(
                action=RuntimeAction.FLAG_DRIFT,
                reason="rhetorical inversion detected",
            )

        if previous_field and previous_field != field:
            return DecisionResult(
                action=RuntimeAction.FLAG_DRIFT,
                reason="field transition with criterion inversion",
            )

        return DecisionResult(
            action=RuntimeAction.CLARIFY,
            reason="negative orientation requires clarification",
        )

    # 3. Strong orientation decay
    if decay is not None and decay <= -0.50:
        if field == "rhetorical":
            return DecisionResult(
                action=RuntimeAction.FLAG_DRIFT,
                reason="strong orientation decay into rhetorical field",
            )

        return DecisionResult(
            action=RuntimeAction.MONITOR,
            reason="strong orientation decay detected",
        )

    # 4. Field transition awareness
    if previous_field and previous_field != field:

        if transition == FieldTransition.NEIGHBOR:
            if orientation < 0:
                return DecisionResult(
                    action=RuntimeAction.MONITOR,
                    reason="neighbor field transition with negative orientation",
                )

            return DecisionResult(
                action=RuntimeAction.ALLOW_LIGHT,
                reason="neighbor field transition; constrained reasoning recommended",
            )

        if transition == FieldTransition.DISTANT:
            if orientation < 0:
                return DecisionResult(
                    action=RuntimeAction.FLAG_DRIFT,
                    reason="distant field transition with negative orientation",
                )

            return DecisionResult(
                action=RuntimeAction.CLARIFY,
                reason="distant field transition requires clarification",
            )

        return DecisionResult(
            action=RuntimeAction.CLARIFY,
            reason="unknown field transition requires clarification",
        )

    # 5. Weak orientation
    if state == "weak":
        return DecisionResult(
            action=RuntimeAction.ALLOW_LIGHT,
            reason="weak but non-inverted orientation",
        )

    # 6. Drifting
    if state == "drifting":
        return DecisionResult(
            action=RuntimeAction.MONITOR,
            reason="orientation decay detected",
        )

    # 7. Stable
    if state == "stable":
        return DecisionResult(
            action=RuntimeAction.ALLOW,
            reason="field compatibility and orientation preserved",
        )

    # 8. Fallback
    return DecisionResult(
        action=RuntimeAction.CLARIFY,
        reason="unrecognized state requires clarification",
    )
