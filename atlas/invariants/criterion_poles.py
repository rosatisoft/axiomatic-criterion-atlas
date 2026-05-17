"""
ACA — Axiomatic Criterion Atlas

Criterion Poles
---------------

Canonical preservation/inversion semantic poles for the foundational
invariant space.
"""

FOUNDATIONAL_POLES = {
    "non_contradiction": {
        "preservation": (
            "A thing cannot be and not be in the same sense at the same time."
        ),
        "inversion": (
            "Contradictions may coexist without affecting coherence."
        ),
    },

    "identity": {
        "preservation": (
            "An entity is identical to itself and preserves reference."
        ),
        "inversion": (
            "An entity may arbitrarily lose identity without consequence."
        ),
    },

    "persistence": {
        "preservation": (
            "Entities maintain identity through time and change."
        ),
        "inversion": (
            "Identity may collapse across change without affecting meaning."
        ),
    },

    "relation": {
        "preservation": (
            "Everything exists in relation to other things."
        ),
        "inversion": (
            "Meaning can exist without relation or context."
        ),
    },

    "evidence_constraint": {
        "preservation": (
            "Interpretation must remain constrained by available evidence."
        ),
        "inversion": (
            "Interpretation may override or ignore available evidence."
        ),
    },

    "causal_continuity": {
        "preservation": (
            "Every effect requires a sufficient cause and coherent transition."
        ),
        "inversion": (
            "Conclusions may appear without cause, grounds, or continuity."
        ),
    },

    "semantic_stability": {
        "preservation": (
            "Meaning must remain stable within a defined context."
        ),
        "inversion": (
            "Meaning may shift arbitrarily without contextual constraint."
        ),
    },

    "interpretive_constraint": {
        "preservation": (
            "Interpretation must remain bounded by context, evidence, and meaning."
        ),
        "inversion": (
            "Interpretation may exceed context, evidence, and meaning without consequence."
        ),
    },

    "uncertainty_preservation": {
        "preservation": (
            "Uncertainty must be preserved when evidence or context is incomplete."
        ),
        "inversion": (
            "Incomplete evidence or context may be converted into certainty."
        ),
    },

    "field_boundary": {
        "preservation": (
            "Semantic movement must preserve awareness of field boundaries."
        ),
        "inversion": (
            "A trajectory may cross fields without recognizing boundary change."
        ),
    },

    "orientation_continuity": {
        "preservation": (
            "Criterion orientation must remain continuous across semantic evolution."
        ),
        "inversion": (
            "Criterion orientation may invert across a trajectory without being detected."
        ),
    },

    "correspondence": {
        "preservation": (
            "Truth requires correspondence between a claim and reality."
        ),
        "inversion": (
            "Truth may detach from reality, evidence, or valid deduction."
        ),
    },
}