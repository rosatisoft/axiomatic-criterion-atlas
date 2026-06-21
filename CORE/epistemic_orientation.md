# ACA — Axiomatic Criterion Atlas

## Epistemic Orientation

### Directional Semantic Stability in Generative Systems

---

## 1. Purpose

Epistemic Orientation defines whether a semantic trajectory preserves or inverts the criterion structure of its active field.

ACA proposes that contextual compatibility alone is insufficient for reliable reasoning.

A trajectory may remain:

* semantically compatible;
* rhetorically coherent;
* grammatically stable;
* geometrically close to a field;

while progressively weakening or inverting the invariant structures that originally preserved criterion.

Epistemic Orientation measures this directional condition.

---

## 2. Core Distinction

ACA formally separates:

```text
Contextual Compatibility
from
Epistemic Orientation
```

Contextual compatibility evaluates:

```text
where a trajectory belongs
```

Epistemic orientation evaluates:

```text
whether the trajectory preserves criterion
inside the active field
```

This distinction constitutes one of the central conceptual separations introduced by ACA.

---

## 3. Origin and Context Requirement

Epistemic orientation is not measured in isolation.

Before orientation can be interpreted, ACA must identify:

* declared origin of criterion;
* active semantic field;
* relevant context;
* applicable invariants;
* trajectory state or sequence under evaluation.

Without origin and context, orientation scores may be mathematically computable but operationally underdetermined.

Therefore:

```text
orientation requires declared origin and context
```

ACA does not treat orientation as an abstract moral or metaphysical score. It treats orientation as a field-relative measure of whether a trajectory preserves the invariant structures relevant to the declared evaluation context.

---

## 4. Relationship to Foundational Cores

Epistemic orientation operates over the foundational invariant structure of ACA.

The foundational layer is divided into two operational cores:

```text
Foundational Invariants =
Logical-Epistemic Core
+
Operational-Orientational Core
```

The Logical-Epistemic Core contains invariants required for reality-based evaluation:

* identity
* non_contradiction
* correspondence
* evidence_constraint
* causal_continuity
* uncertainty_preservation

The Operational-Orientational Core contains invariants required for stable semantic operation within a declared origin and context:

* persistence
* relation
* semantic_stability
* interpretive_constraint
* field_boundary
* orientation_continuity

Epistemic orientation evaluates whether a trajectory preserves or weakens these invariants during semantic evolution.

---

## 5. Foundational Hypothesis

ACA proposes:

```text
Reliable reasoning requires directional preservation
of invariant semantic structures.
```

Without directional preservation:

* contextual coherence becomes insufficient;
* semantic compatibility may hide inversion;
* uncertainty may be converted into certainty;
* correspondence may weaken while fluency remains high;
* trajectories may progressively destabilize criterion while remaining locally coherent.

Thus:

```text
semantic proximity
≠
epistemic stability
```

---

## 6. Orientation Space

Let:

```text
S ⊆ R^d
```

represent a semantic field generated from invariant anchors.

Let:

```text
D = {d_1, d_2, ..., d_n}
```

represent the directional invariant system.

Each:

```text
d_i
```

defines a criterion-preserving semantic axis.

Together, these vectors generate the orientation structure of the active field.

---

## 7. Directional Projection

For a normalized embedding `z`, ACA defines orientation relative to invariant `I_i` as:

```text
phi_i(z) = <normalize(z), d_i>
```

where:

* positive projection preserves invariant direction;
* near-zero projection indicates ambiguity or weak orientation;
* negative projection indicates inversion.

This directional projection is meaningful only relative to the active field, context, and relevant invariants.

---

## 8. Aggregate Epistemic Orientation

Since semantic systems depend on multiple invariants simultaneously, ACA defines aggregate orientation as:

```text
Phi(z) = sum_i w_i * phi_i(z)
```

where:

* `w_i` are invariant relevance weights;
* `phi_i(z)` are directional invariant projections.

This produces a global epistemic orientation metric for the active evaluation frame.

The relevance weights may depend on:

* declared origin;
* active field;
* context;
* trajectory type;
* domain-specific evaluation conditions.

---

## 9. Interpretation

| Aggregate Orientation | Interpretation                |
| --------------------- | ----------------------------- |
| `Phi(z) > 0`          | criterion preservation        |
| `Phi(z) ≈ 0`          | ambiguous or weak orientation |
| `Phi(z) < 0`          | criterion inversion           |

This allows ACA to distinguish:

```text
semantic coherence
from
criterion-preserving coherence
```

---

## 10. Orientation and Semantic Trajectories

ACA models reasoning as:

```text
trajectory evolution
inside semantic fields
```

Each trajectory evolves relative to:

* contextual geometry;
* semantic attractors;
* invariant structures;
* directional orientation;
* declared origin and context.

A trajectory is epistemically stable when it remains contextually compatible and preserves positive invariant orientation.

---

## 11. Epistemic Stability Condition

ACA defines epistemic stability as:

```text
O(z_t) <= theta_O
```

and:

```text
Phi(z_t) >= theta_Phi
```

where:

* `O(z_t)` measures contextual compatibility;
* `Phi(z_t)` measures directional preservation.

Thus:

```text
stable reasoning =
semantic compatibility
+
positive orientation
```

This condition is evaluated only after the active field and relevant invariants have been identified.

---

## 12. Criterion Drift

Criterion drift occurs when:

```text
O(z_t)
```

remains low while:

```text
Phi(z_t)
```

progressively weakens or becomes negative.

This means:

```text
the trajectory still belongs to the field,
but no longer preserves the field's criterion
```

ACA identifies this as:

```text
epistemic destabilization
inside coherent semantic space
```

---

## 13. Progressive Drift

Drift frequently emerges gradually rather than catastrophically.

Examples include:

* rhetorical reinterpretation;
* emotional substitution;
* contradiction normalization;
* evidence weakening;
* contextual reframing;
* semantic inversion;
* interpretive displacement;
* uncertainty converted into certainty;
* correspondence loss;
* unnoticed field crossing.

A trajectory may appear coherent while progressively losing orientation.

This is one of the central failure modes ACA is designed to detect.

---

## 14. Orientation Decay

ACA evaluates not only instantaneous orientation but also orientation evolution across time.

Let:

```text
Phi_t = Phi(z_t)
```

represent orientation at trajectory state `t`.

Orientation decay is modeled as:

```text
Delta Phi_t = Phi_t - Phi_{t-1}
```

Persistent negative decay indicates:

```text
directional destabilization
```

even before explicit inversion occurs.

---

## 15. Orientation Zones

Directional semantic geometry naturally generates zones:

| Zone             | Description                       |
| ---------------- | --------------------------------- |
| Stable Region    | positive orientation              |
| Weak Region      | low orientation                   |
| Ambiguity Region | unstable or near-zero orientation |
| Drift Region     | decaying orientation              |
| Inversion Region | negative orientation              |

These zones allow runtime systems to monitor semantic evolution dynamically.

---

## 16. Orientation and Runtime Policies

Runtime systems may use epistemic orientation to trigger:

* clarification requests;
* constrained inference;
* trajectory monitoring;
* semantic routing;
* drift alerts;
* criterion-preserving intervention.

Example policy mapping:

| Condition             | Runtime Action |
| --------------------- | -------------- |
| stable orientation    | ALLOW          |
| weak orientation      | ALLOW_LIGHT    |
| ambiguous orientation | CLARIFY        |
| persistent decay      | MONITOR        |
| negative orientation  | FLAG_DRIFT     |

These policies should be interpreted relative to declared origin, active field, context, and relevant invariants.

---

## 17. Epistemic Orientation vs Similarity Systems

Traditional embedding systems primarily evaluate:

* similarity;
* proximity;
* clustering;
* semantic overlap.

ACA introduces a different capability:

```text
directional semantic evaluation
```

Two trajectories may occupy nearby semantic regions while preserving opposite criterion orientations.

Thus:

```text
semantic closeness
does not guarantee
epistemic continuity
```

---

## 18. Relationship to the Atlas

Semantic fields define:

```text
contextual structure
```

Ontological invariants define:

```text
what must remain stable
```

Directional invariants define:

```text
criterion-preserving direction
```

Epistemic orientation defines:

```text
whether semantic evolution preserves
or inverts that direction
```

Together, these layers form the criterion geometry of ACA.

---

## 19. Foundational Principle

ACA proposes the following principle:

```text
Reliable semantic systems require persistent preservation
of directional invariant orientation
during contextual evolution.
```

Without epistemic orientation:

* contextual coherence becomes insufficient;
* semantic fields lose criterion continuity;
* reasoning trajectories become directionally unstable despite local compatibility;
* fluent systems may remain persuasive while weakening their own criterion.

Therefore:

```text
Reliable reasoning requires
not only semantic location,
but semantic orientation.
```

At this stage, ACA treats observed drift as the primary signal of orientation loss. Broader concepts such as orientational entropy may be explored later, after origin, context, and invariant relevance are operationally defined.
