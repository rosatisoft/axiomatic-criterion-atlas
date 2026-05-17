"""
ACA — Axiomatic Criterion Atlas

Runtime Policies
----------------

This module maps ACA semantic states into runtime actions.

The Criterion Gateway may use these actions to decide whether to:

- allow reasoning,
- use lightweight reasoning,
- request clarification,
- monitor trajectory drift,
- flag criterion inversion,
- or reject/clarify dispersed input.
"""

from __future__ import annotations

from enum import Enum

from atlas.orientation.drift_detection import DriftState


class RuntimeAction(str, Enum):
    """
    Runtime actions available to ACA-compatible gateways.
    """

    ALLOW = "allow"
    ALLOW_LIGHT = "allow_light"
    CLARIFY = "clarify"
    MONITOR = "monitor"
    FLAG_DRIFT = "flag_drift"
    REJECT_OR_CLARIFY = "reject_or_clarify"


def action_from_drift_state(state: DriftState | str) -> RuntimeAction:
    """
    Map a drift state to a runtime action.
    """

    state = DriftState(state)

    if state == DriftState.STABLE:
        return RuntimeAction.ALLOW

    if state == DriftState.WEAK:
        return RuntimeAction.ALLOW_LIGHT

    if state == DriftState.AMBIGUOUS:
        return RuntimeAction.CLARIFY

    if state == DriftState.DRIFTING:
        return RuntimeAction.MONITOR

    if state == DriftState.INVERTED:
        return RuntimeAction.FLAG_DRIFT

    if state == DriftState.DISPERSED:
        return RuntimeAction.REJECT_OR_CLARIFY

    return RuntimeAction.CLARIFY


def should_execute_reasoning(action: RuntimeAction | str) -> bool:
    """
    Return whether full reasoning should execute.
    """

    action = RuntimeAction(action)

    return action == RuntimeAction.ALLOW


def should_execute_light_reasoning(action: RuntimeAction | str) -> bool:
    """
    Return whether constrained or lightweight reasoning should execute.
    """

    action = RuntimeAction(action)

    return action in {
        RuntimeAction.ALLOW,
        RuntimeAction.ALLOW_LIGHT,
        RuntimeAction.MONITOR,
    }


def requires_user_clarification(action: RuntimeAction | str) -> bool:
    """
    Return whether the system should request clarification.
    """

    action = RuntimeAction(action)

    return action in {
        RuntimeAction.CLARIFY,
        RuntimeAction.REJECT_OR_CLARIFY,
    }


def requires_drift_flag(action: RuntimeAction | str) -> bool:
    """
    Return whether the system should flag criterion drift.
    """

    action = RuntimeAction(action)

    return action == RuntimeAction.FLAG_DRIFT