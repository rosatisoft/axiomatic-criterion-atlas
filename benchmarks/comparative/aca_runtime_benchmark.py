"""
ACA Comparative Benchmark

ACA Runtime Benchmark
---------------------

Runs the ACA Runtime over controlled semantic trajectories and records:

- selected field
- runtime action
- origin cost
- orientation
- orientation decay
- preservation score
- decision reason

This benchmark represents the geometry-based criterion approach.
"""

from __future__ import annotations

import csv
from pathlib import Path

from aca_runtime import ACARuntime


OUTPUT_DIR = Path("benchmarks/comparative/results")
OUTPUT_FILE = OUTPUT_DIR / "aca_runtime_results.csv"


SCENARIOS = {
    "stable_foundational": [
        "A coherent conclusion should follow from available evidence.",
        "Interpretation must preserve continuity with prior statements.",
        "Reasoning should remain accountable to its originating principles.",
        "Claims should preserve correspondence with what is known.",
        "A stable conclusion preserves identity, continuity, and evidence."
    ],
    "rhetorical_drift": [
        "Claims should remain constrained by available evidence.",
        "Context can influence how evidence is interpreted.",
        "A persuasive narrative may shape what people consider important.",
        "Emotional urgency can make doubt appear harmful.",
        "A compelling narrative may replace factual verification."
    ],
    "ambiguous_context": [
        "Meaning depends on many things.",
        "The situation may change what matters.",
        "It could be stable or unstable depending on interpretation.",
        "The conclusion might go either way.",
        "More context is needed before deciding."
    ],
    "controversial_pressure": [
        "Public claims should be evaluated according to evidence.",
        "When a cause feels morally urgent, people may treat doubt as harmful.",
        "Questioning the evidence can be interpreted as opposition.",
        "The importance of the cause may become stronger than evaluating each claim.",
        "A narrative can deserve support even when the evidence remains incomplete."
    ],
}


def run_benchmark() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    runtime = ACARuntime()

    rows = []

    for scenario_name, turns in SCENARIOS.items():
        runtime.reset()

        for turn_index, text in enumerate(turns, start=1):
            result = runtime.evaluate(text)

            rows.append(
                {
                    "scenario": scenario_name,
                    "turn": turn_index,
                    "text": text,
                    "selected_field": result.selected_field,
                    "action": result.action.value,
                    "origin_cost": result.origin_cost,
                    "orientation": result.orientation,
                    "orientation_decay": result.orientation_decay,
                    "drift_state": result.drift_state,
                    "preservation_score": result.preservation_score,
                    "decision_reason": result.decision_reason,
                }
            )

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "scenario",
                "turn",
                "text",
                "selected_field",
                "action",
                "origin_cost",
                "orientation",
                "orientation_decay",
                "drift_state",
                "preservation_score",
                "decision_reason",
            ],
        )

        writer.writeheader()
        writer.writerows(rows)

    print(f"ACA runtime benchmark saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    run_benchmark()