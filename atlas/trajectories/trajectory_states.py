"""
ACA — Axiomatic Criterion Atlas

Trajectory States
-----------------

This module defines canonical semantic trajectory state labels used across
ACA analysis, runtime policies, and benchmarks.
"""

from __future__ import annotations

from enum import Enum


class TrajectoryState(str, Enum):
    """
    Canonical trajectory state labels.
    """

    STABLE = "stable"
    WEAK = "weak"
    AMBIGUOUS = "ambiguous"
    DRIFTING = "drifting"
    INVERTED = "inverted"
    DISPERSED = "dispersed"


STABLE_STATES = {
    TrajectoryState.STABLE,
}

MONITOR_STATES = {
    TrajectoryState.WEAK,
    TrajectoryState.DRIFTING,
}

UNSTABLE_STATES = {
    TrajectoryState.AMBIGUOUS,
    TrajectoryState.INVERTED,
    TrajectoryState.DISPERSED,
}


def is_stable_state(state: TrajectoryState | str) -> bool:
    """
    Return True if the state is considered stable.
    """

    state = TrajectoryState(state)

    return state in STABLE_STATES


def requires_monitoring(state: TrajectoryState | str) -> bool:
    """
    Return True if the state should be monitored.
    """

    state = TrajectoryState(state)

    return state in MONITOR_STATES


def is_unstable_state(state: TrajectoryState | str) -> bool:
    """
    Return True if the state is considered unstable.
    """

    state = TrajectoryState(state)

    return state in UNSTABLE_STATES