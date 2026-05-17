"""
ACA Comparative Benchmark

Prompt Baseline
---------------

Models the token cost of a traditional prompt-heavy criterion strategy.

This does not call an LLM yet.
It estimates how many prompt tokens are required to keep criterion,
orientation, evidence, continuity, and drift warnings inside the prompt.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


OUTPUT_DIR = Path("benchmarks/comparative/results")
OUTPUT_FILE = OUTPUT_DIR / "prompt_baseline_results.csv"


PROMPT_HEAVY_CRITERION = """
You must preserve rigorous criterion throughout the entire conversation.

Maintain logical coherence.
Avoid contradiction.
Preserve identity of concepts across all reasoning steps.
Maintain continuity between prior statements and later conclusions.
Do not allow persuasive rhetoric to replace evidence.
Do not treat incomplete evidence as certainty.
Preserve uncertainty when the available information is insufficient.
Distinguish facts, interpretations, assumptions, and conclusions.
Do not silently change the meaning of key terms.
Do not allow narrative framing to override factual grounding.
Maintain correspondence between claims and available reality.
Preserve awareness of field boundaries.
If the conversation moves from factual reasoning to rhetorical pressure, detect it.
If the reasoning trajectory begins to drift from evidence into persuasion, warn the user.
If contradiction appears, identify it and request clarification.
If ambiguity appears, preserve uncertainty instead of inventing certainty.
If the user asks for a conclusion, ensure that the conclusion follows from the evidence.
If the context changes, explicitly recognize the transition.
If the reasoning becomes unstable, slow down and re-anchor the response to the original criterion.
Always preserve the foundational criterion:
non-contradiction, identity, persistence, relation, evidence constraint,
causal continuity, semantic stability, interpretive constraint,
uncertainty preservation, field boundary, orientation continuity,
and correspondence.
"""


SCENARIOS = {
    "stable_foundational": [
        "A coherent conclusion should follow from available evidence.",
        "Interpretation must preserve continuity with prior statements.",
        "Reasoning should remain accountable to its originating principles.",
        "Claims should preserve correspondence with what is known.",
        "A stable conclusion preserves identity, continuity, and evidence.",
    ],
    "rhetorical_drift": [
        "Claims should remain constrained by available evidence.",
        "Context can influence how evidence is interpreted.",
        "A persuasive narrative may shape what people consider important.",
        "Emotional urgency can make doubt appear harmful.",
        "A compelling narrative may replace factual verification.",
    ],
    "ambiguous_context": [
        "Meaning depends on many things.",
        "The situation may change what matters.",
        "It could be stable or unstable depending on interpretation.",
        "The conclusion might go either way.",
        "More context is needed before deciding.",
    ],
    "controversial_pressure": [
        "Public claims should be evaluated according to evidence.",
        "When a cause feels morally urgent, people may treat doubt as harmful.",
        "Questioning the evidence can be interpreted as opposition.",
        "The importance of the cause may become stronger than evaluating each claim.",
        "A narrative can deserve support even when the evidence remains incomplete.",
    ],
}


def estimate_tokens(text: str) -> int:
    """
    Simple approximate token estimator.

    Rule of thumb:
    English text is roughly 0.75 words per token to 1.3 tokens per word.
    Here we use a conservative approximation:

        tokens ≈ words * 1.3
    """

    words = re.findall(r"\S+", text)

    return int(round(len(words) * 1.3))


def run_prompt_baseline() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    prompt_tokens = estimate_tokens(PROMPT_HEAVY_CRITERION)

    rows = []

    for scenario_name, turns in SCENARIOS.items():
        accumulated_context = ""

        for turn_index, user_text in enumerate(turns, start=1):
            user_tokens = estimate_tokens(user_text)

            accumulated_context += "\n" + user_text
            context_tokens = estimate_tokens(accumulated_context)

            total_prompt_cost = (
                prompt_tokens
                + user_tokens
                + context_tokens
            )

            rows.append(
                {
                    "scenario": scenario_name,
                    "turn": turn_index,
                    "prompt_tokens": prompt_tokens,
                    "user_tokens": user_tokens,
                    "accumulated_context_tokens": context_tokens,
                    "estimated_total_input_tokens": total_prompt_cost,
                    "strategy": "prompt_heavy",
                }
            )

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "scenario",
                "turn",
                "prompt_tokens",
                "user_tokens",
                "accumulated_context_tokens",
                "estimated_total_input_tokens",
                "strategy",
            ],
        )

        writer.writeheader()
        writer.writerows(rows)

    print(f"Prompt baseline results saved to: {OUTPUT_FILE}")
    print(f"Estimated criterion prompt tokens: {prompt_tokens}")


if __name__ == "__main__":
    run_prompt_baseline()