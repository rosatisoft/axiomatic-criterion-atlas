"""
ACA Comparative Benchmark

Token Comparison
----------------

Compares estimated token cost between:

1. Prompt-heavy criterion strategy
2. ACA Runtime strategy

ACA moves criterion from repeated prompt text into reusable matrices.
"""

from __future__ import annotations

import csv
from pathlib import Path


RESULTS_DIR = Path("benchmarks/comparative/results")

PROMPT_BASELINE_FILE = RESULTS_DIR / "prompt_baseline_results.csv"
OUTPUT_FILE = RESULTS_DIR / "token_comparison_results.csv"


ACA_MINIMAL_SYSTEM_PROMPT_TOKENS = 12
ACA_RUNTIME_METADATA_TOKENS = 35


def load_csv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def run_token_comparison() -> None:
    rows = load_csv(PROMPT_BASELINE_FILE)

    output_rows = []

    total_prompt_heavy = 0
    total_aca = 0

    for row in rows:
        prompt_heavy_tokens = int(row["estimated_total_input_tokens"])

        user_tokens = int(row["user_tokens"])
        context_tokens = int(row["accumulated_context_tokens"])

        aca_tokens = (
            ACA_MINIMAL_SYSTEM_PROMPT_TOKENS
            + ACA_RUNTIME_METADATA_TOKENS
            + user_tokens
            + context_tokens
        )

        savings = prompt_heavy_tokens - aca_tokens

        savings_percent = (
            savings / prompt_heavy_tokens * 100
            if prompt_heavy_tokens > 0
            else 0
        )

        total_prompt_heavy += prompt_heavy_tokens
        total_aca += aca_tokens

        output_rows.append(
            {
                "scenario": row["scenario"],
                "turn": row["turn"],
                "prompt_heavy_tokens": prompt_heavy_tokens,
                "aca_runtime_tokens": aca_tokens,
                "token_savings": savings,
                "token_savings_percent": round(savings_percent, 2),
            }
        )

    total_savings = total_prompt_heavy - total_aca

    total_savings_percent = (
        total_savings / total_prompt_heavy * 100
        if total_prompt_heavy > 0
        else 0
    )

    output_rows.append(
        {
            "scenario": "TOTAL",
            "turn": "",
            "prompt_heavy_tokens": total_prompt_heavy,
            "aca_runtime_tokens": total_aca,
            "token_savings": total_savings,
            "token_savings_percent": round(total_savings_percent, 2),
        }
    )

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "scenario",
                "turn",
                "prompt_heavy_tokens",
                "aca_runtime_tokens",
                "token_savings",
                "token_savings_percent",
            ],
        )

        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Token comparison saved to: {OUTPUT_FILE}")
    print(f"Prompt-heavy total tokens: {total_prompt_heavy}")
    print(f"ACA runtime total tokens: {total_aca}")
    print(f"Token savings: {total_savings}")
    print(f"Token savings percent: {total_savings_percent:.2f}%")


if __name__ == "__main__":
    run_token_comparison()