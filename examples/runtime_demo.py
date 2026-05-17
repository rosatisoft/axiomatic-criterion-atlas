"""
ACA Runtime Demo

Minimal conversational trajectory demo for ACA Runtime.
"""

from aca_runtime import ACARuntime


def print_turn(turn, index: int) -> None:
    print("\n" + "=" * 60)
    print(f"TURN {index}")
    print("=" * 60)

    print(f"Text: {turn.text}")
    print(f"Field: {turn.selected_field}")
    print(f"Action: {turn.action.value}")

    print(f"Origin Cost: {turn.origin_cost:.4f}")
    print(f"Orientation: {turn.orientation:.4f}")

    if turn.orientation_decay is not None:
        print(f"Orientation Decay: {turn.orientation_decay:.4f}")

    print(f"Drift State: {turn.drift_state}")
    print(f"Preservation Score: {turn.preservation_score:.4f}")

    print("\nField Costs:")

    for field_name, cost in turn.field_costs.items():
        print(f"  {field_name:<15} {cost:.4f}")

    print(f"Decision Reason: {turn.decision_reason}")


def main() -> None:
    runtime = ACARuntime()

    conversation = [
        "A coherent conclusion should follow from available evidence.",

        "Interpretation must preserve continuity with prior statements.",

        "People are emotionally pressured to accept conclusions without evidence.",

        "A persuasive narrative may replace factual verification.",

        "Contradictions should not be ignored for social convenience.",
    ]

    for i, text in enumerate(conversation, start=1):
        turn = runtime.evaluate(text)
        print_turn(turn, i)

    print("\n" + "=" * 60)
    print("RUNTIME SUMMARY")
    print("=" * 60)

    summary = runtime.summary()

    for key, value in summary.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()