"""
ACA Runtime

Minimal operational runtime for Axiomatic Criterion Atlas.

This runtime evaluates each input as part of a semantic trajectory:

1. Embed input text.
2. Select closest semantic field.
3. Evaluate invariant orientation.
4. Detect drift against previous orientation.
5. Return a runtime decision.

This is the first bridge between ACA artifacts and a practical LLM gateway.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np

from atlas.embeddings.openai_embedder import OpenAIEmbedder
from atlas.orientation.criterion_vectors import CriterionVector
from atlas.runtime.criterion_gate import CriterionGateResult, evaluate_criterion_gate
from atlas.runtime.policies import RuntimeAction
from atlas.runtime.thresholds import ThresholdConfig, balanced_thresholds
from aca_runtime.decisions import DecisionInput, decide_runtime_action


DEFAULT_FIELDS = [
    "foundational",
    "factual",
    "rhetorical",
]


@dataclass
class RuntimeTurn:
    """
    One evaluated turn in a semantic trajectory.
    """

    text: str
    selected_field: str
    action: RuntimeAction
    origin_cost: float
    orientation: float
    orientation_decay: Optional[float]
    drift_state: str
    preservation_score: float
    field_costs: Dict[str, float]
    decision_reason: str


@dataclass
class RuntimeState:
    """
    Persistent runtime state across a dialogue.
    """

    turns: List[RuntimeTurn]

    @property
    def previous_orientation(self) -> Optional[float]:
        if not self.turns:
            return None

        return self.turns[-1].orientation


class ACARuntime:
    """
    Minimal ACA runtime evaluator.
    """

    def __init__(
        self,
        artifacts_dir: str | Path = "artifacts",
        fields: Optional[List[str]] = None,
        thresholds: Optional[ThresholdConfig] = None,
    ) -> None:
        self.artifacts_dir = Path(artifacts_dir)
        self.fields = fields or DEFAULT_FIELDS
        self.thresholds = thresholds or balanced_thresholds()

        self.embedder = OpenAIEmbedder()
        self.field_bases = self._load_field_bases()
        self.criterion_vectors = self._load_criterion_vectors()

        self.state = RuntimeState(turns=[])

    def evaluate(self, text: str) -> RuntimeTurn:
        """
        Evaluate one input text and append it to runtime state.
        """

        vector = self.embedder.embed_text(text)

        result: CriterionGateResult = evaluate_criterion_gate(
            vector=vector,
            field_bases=self.field_bases,
            criterion_vectors=self.criterion_vectors,
            thresholds=self.thresholds,
            previous_orientation=self.state.previous_orientation,
            normalize_input=True,
        )

        field_costs = {
            score.field_name: float(score.origin_cost)
            for score in result.field_selection.scores
        }

        previous_field = (
            self.state.turns[-1].selected_field
            if self.state.turns
            else None
        )

        from atlas.fields.field_topology import FieldTransition, classify_field_transition

        transition = classify_field_transition(
            previous_field=previous_field,
            current_field=result.selected_field,
        )

        effective_state = result.drift.state.value

        if (
            effective_state == "dispersed"
            and transition == FieldTransition.NEIGHBOR
            and result.orientation.aggregate_orientation > 0
            and result.preservation.preservation_score > 0.45
        ):
            effective_state = "reorienting"

        decision = decide_runtime_action(
            DecisionInput(
                selected_field=result.selected_field,
                origin_cost=float(result.field_selection.selected_score.origin_cost),
                orientation=float(result.orientation.aggregate_orientation),
                orientation_decay=result.drift.orientation_decay,
                drift_state=effective_state,
                previous_field=previous_field,
                margin=float(result.field_selection.margin),
            )
        )

        turn = RuntimeTurn(
            text=text,
            selected_field=result.selected_field,
            action=decision.action,
            origin_cost=float(result.field_selection.selected_score.origin_cost),
            orientation=float(result.orientation.aggregate_orientation),
            orientation_decay=result.drift.orientation_decay,
            drift_state=effective_state,
            preservation_score=float(result.preservation.preservation_score),
            field_costs=field_costs,
            decision_reason=decision.reason,
        )

        self.state.turns.append(turn)

        return turn

    def reset(self) -> None:
        """
        Reset runtime trajectory memory.
        """

        self.state = RuntimeState(turns=[])

    def summary(self) -> Dict[str, object]:
        """
        Return compact runtime summary.
        """

        return {
            "n_turns": len(self.state.turns),
            "last_field": (
                self.state.turns[-1].selected_field
                if self.state.turns
                else None
            ),
            "last_action": (
                self.state.turns[-1].action.value
                if self.state.turns
                else None
            ),
            "last_orientation": (
                self.state.turns[-1].orientation
                if self.state.turns
                else None
            ),
            "last_drift_state": (
                self.state.turns[-1].drift_state
                if self.state.turns
                else None
            ),
            "has_flagged_drift": any(
                turn.action == RuntimeAction.FLAG_DRIFT
                for turn in self.state.turns
            ),
            "has_requested_clarification": any(
                turn.action.value in {"clarify", "reject_or_clarify"}
                for turn in self.state.turns
            ),
        }

    def _load_field_bases(self) -> Dict[str, np.ndarray]:
        """
        Load semantic field bases from artifacts.
        """

        field_bases: Dict[str, np.ndarray] = {}

        for field in self.fields:
            path = self.artifacts_dir / field / "basis_vectors.npy"

            if not path.exists():
                raise FileNotFoundError(f"Missing field basis: {path}")

            field_bases[field] = np.load(path)

        return field_bases

    def _load_criterion_vectors(self) -> List[CriterionVector]:
        """
        Load invariant directions from foundational artifacts.
        """

        vectors_path = (
            self.artifacts_dir
            / "foundational"
            / "criterion_vectors.npy"
        )

        metadata_path = (
            self.artifacts_dir
            / "foundational"
            / "criterion_vector_metadata.json"
        )

        if not vectors_path.exists():
            raise FileNotFoundError(f"Missing criterion vectors: {vectors_path}")

        if not metadata_path.exists():
            raise FileNotFoundError(f"Missing criterion metadata: {metadata_path}")

        matrix = np.load(vectors_path)

        with metadata_path.open("r", encoding="utf-8") as f:
            metadata = json.load(f)

        names = metadata["invariant_names"]

        criterion_vectors: List[CriterionVector] = []

        for i, name in enumerate(names):
            direction = matrix[i]

            criterion_vectors.append(
                CriterionVector(
                    invariant_name=name,
                    direction=direction,
                    preservation_pole=direction,
                    inversion_pole=-direction,
                    norm=2.0,
                )
            )

        return criterion_vectors