"""
ACA — Axiomatic Criterion Atlas

Runtime Thresholds
------------------

This module defines threshold configurations used for:

- semantic field compatibility
- epistemic orientation
- criterion drift detection
- runtime routing
- trajectory monitoring
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ThresholdConfig:
    """
    ACA runtime threshold configuration.
    """

    # Maximum origin cost for contextual compatibility
    theta_origin: float = 0.35

    # Minimum orientation for strong criterion preservation
    theta_orientation: float = 0.15

    # Weak-but-non-inverted orientation threshold
    theta_weak_orientation: float = 0.0

    # Orientation decay threshold
    theta_decay: float = -0.05


DEFAULT_THRESHOLDS = ThresholdConfig()


def strict_thresholds() -> ThresholdConfig:
    """
    Conservative criterion-preservation thresholds.
    """

    return ThresholdConfig(
        theta_origin=0.25,
        theta_orientation=0.20,
        theta_weak_orientation=0.05,
        theta_decay=-0.03,
    )


def balanced_thresholds() -> ThresholdConfig:
    """
    Balanced runtime thresholds.
    """

    return ThresholdConfig(
        theta_origin=0.35,
        theta_orientation=0.15,
        theta_weak_orientation=0.0,
        theta_decay=-0.05,
    )


def permissive_thresholds() -> ThresholdConfig:
    """
    More permissive thresholds for exploratory systems.
    """

    return ThresholdConfig(
        theta_origin=0.50,
        theta_orientation=0.05,
        theta_weak_orientation=-0.05,
        theta_decay=-0.10,
    )