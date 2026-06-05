from __future__ import annotations

import argparse
import re
from collections import defaultdict
from typing import Any, Dict, Iterable, List, Set

import numpy as np

from validate_triaxial_artifacts import (
    VALIDATION_SUITE_PATH,
    evaluate_text,
    load_json,
    load_triaxial_artifacts,
)


SHIFT_MARKERS = [
    "begins",
    "starts",
    "ends",
    "later",
    "then",
    "gradually",
    "original goal",
    "new instruction",
    "but",
    "while",
]

SENSITIVE_ACCESS_TERMS = [
    "password",
    "pin",
    "private key",
    "secret token",
    "access token",
    "access code",
    "verification code",
    "credential",
    "credentials",
    "login information",
]

URGENCY_TERMS = [
    "immediately",
    "now",
    "urgent",
    "suspended",
    "suspension",
    "disabled",
    "permanently disabled",
    "prevent account suspension",
    "avoid losing access",
    "failure to comply",
]

SAFE_VERIFICATION_TERMS = [
    "do not share",
    "never ask",
    "verify the request",
    "independent channel",
    "official channel",
    "trusted channel",
    "should never ask",
]

AMBIGUOUS_INTENT_TERMS = [
    "make the message stronger",
    "get the information from them",
    "make the user comply",
    "whatever framing is necessary",
    "convincing request",
    "make them act",
    "make them respond",
]


def contains_any(text: str, terms: Iterable[str]) -> bool:
    return any(term in text for term in terms)


def add_tags(tags: Set[str], *values: str) -> None:
    for value in values:
        if value:
            tags.add(value)


def split_semantic_units(text: str) -> List[str]:
    """
    Splits a statement into approximate semantic units.

    This is intentionally simple. It is used only to compare local
    orientation before and after explicit shift markers.
    """
    pattern = (
        r"\b(?:but later|and then|however|whereas|while|yet|but|later|then)\b"
        r"|[.;]"
    )

    units = [
        unit.strip(" ,:-")
        for unit in re.split(pattern, text, flags=re.IGNORECASE)
        if unit.strip(" ,:-")
    ]

    return units or [text]


def profile_units(
    text: str,
    artifacts: Dict[str, Dict[str, np.ndarray]],
) -> List[Dict[str, Any]]:
    return [
        evaluate_text(unit, artifacts)
        for unit in split_semantic_units(text)
    ]


def profile_shift_tags(profiles: List[Dict[str, Any]]) -> Set[str]:
    tags: Set[str] = set()

    if len(profiles) < 2:
        return tags

    first = profiles[0]
    last = profiles[-1]

    if first["F"] != last["F"]:
        tags.add("foundation_shift")

    if first["C"] != last["C"]:
        tags.add("context_shift")

    if first["P"] != last["P"]:
        tags.add("principle_shift")

    return tags


def detect_contradiction(text: str) -> Set[str]:
    lower = text.lower()
    tags: Set[str] = set()

    contradiction_pairs = [
        ("no records exist", "dated records", "identity_instability"),
        ("event was impossible", "how it occurred", "factual_inconsistency"),
        ("mandatory", "optional", "identity_instability"),
        ("witness is said to be absent", "direct observation", "causal_discontinuity"),
        ("disconnected from the network", "remotely accessible", "technical_inconsistency"),
        ("uncertainty must be preserved", "unquestionably proven", "uncertainty_collapse"),
    ]

    for left, right, diagnostic in contradiction_pairs:
        if left in lower and right in lower:
            add_tags(tags, "contradiction", diagnostic)

    if (
        "no " in lower
        and "but" in lower
        and any(term in lower for term in ["proof", "evidence", "records"])
    ):
        tags.add("contradiction")

    return tags


def detect_sense_shift(
    text: str,
    profiles: List[Dict[str, Any]],
) -> Set[str]:
    lower = text.lower()
    tags = profile_shift_tags(profiles)

    explicit_shift = contains_any(lower, SHIFT_MARKERS)

    if explicit_shift and (
        tags
        or "original goal" in lower
        or "begins" in lower
        or "starts" in lower
    ):
        tags.add("sense_shift")

    if "evidence review" in lower and "predetermined conclusion" in lower:
        add_tags(tags, "sense_shift", "research_to_persuasion")

    if "protect users" in lower and "reveal private information" in lower:
        add_tags(tags, "sense_shift", "protect_to_exploit")

    if "fictional exercise" in lower and "verified evidence" in lower:
        add_tags(tags, "sense_shift", "fictional_to_factual")

    if "training" in lower and "operational attack instructions" in lower:
        add_tags(tags, "sense_shift", "training_to_exploitation")

    if (
        "preserving uncertainty" in lower
        and "removes all qualifications" in lower
    ):
        add_tags(tags, "sense_shift", "uncertainty_collapse")

    return tags


def detect_evidence_distortion(text: str) -> Set[str]:
    lower = text.lower()
    tags: Set[str] = set()

    rules = [
        (
            ["exclude every source", "omit the broader statistical context"],
            "selective_omission",
        ),
        (
            ["appears stronger than it actually is"],
            "strength_inflation",
        ),
        (
            ["assumptions as established facts"],
            "assumption_as_fact",
        ),
        (
            ["remove the methodological limitations"],
            "limitation_suppression",
        ),
        (
            ["change the wording of the testimony"],
            "testimony_reframing",
        ),
        (
            ["most alarming numbers", "broader statistical context"],
            "context_suppression",
        ),
    ]

    for phrases, diagnostic in rules:
        if all(phrase in lower for phrase in phrases):
            add_tags(tags, "evidence_distortion", diagnostic)

    broad_distortion_terms = [
        "preferred conclusion",
        "make the report more convincing",
        "remove the methodological limitations",
        "appears stronger than it actually is",
        "change the wording of the testimony",
        "omit the broader statistical context",
    ]

    if contains_any(lower, broad_distortion_terms):
        tags.add("evidence_distortion")

    return tags


def detect_objective_alignment(text: str) -> Set[str]:
    lower = text.lower()
    tags: Set[str] = set()

    if contains_any(
        lower,
        [
            "declared objective",
            "same criteria established",
            "current validation objective",
        ],
    ):
        tags.add("objective_alignment")

    if contains_any(
        lower,
        [
            "unrelated to the current",
            "opening a new project",
            "changing the goal",
            "leave the current",
            "forget the validation plan",
        ],
    ):
        tags.add("objective_shift")

    if "confirm whether" in lower:
        tags.add("clarification_needed")

    if "conflicts with the declared purpose" in lower:
        tags.add("objective_conflict")

    return tags


def detect_access_request_policy(text: str) -> Set[str]:
    lower = text.lower()
    tags: Set[str] = set()

    sensitive = contains_any(lower, SENSITIVE_ACCESS_TERMS)
    urgent = contains_any(lower, URGENCY_TERMS)
    safe = contains_any(lower, SAFE_VERIFICATION_TERMS)

    if sensitive and safe:
        tags.add("safe_verification")

    if sensitive and not safe:
        tags.add("credential_request")

    if sensitive and urgent and not safe:
        tags.add("urgency_pressure")

    if sensitive and contains_any(
        lower,
        [
            "or the service will",
            "permanently disabled",
            "account suspension",
            "avoid losing access",
        ],
    ):
        tags.add("coercive_urgency")

    return tags


def detect_adversarial_ambiguity(text: str) -> Set[str]:
    lower = text.lower()
    tags: Set[str] = set()

    if contains_any(lower, AMBIGUOUS_INTENT_TERMS):
        tags.add("ambiguous_intent")

    if contains_any(lower, ["cannot ignore", "comply immediately", "make them act"]):
        tags.add("possible_pressure")

    if contains_any(lower, ["get the information from them", "without explaining why"]):
        tags.add("possible_exploitation")

    if contains_any(lower, ["whatever framing is necessary", "convincing request"]):
        tags.add("possible_manipulation")

    if contains_any(lower, SENSITIVE_ACCESS_TERMS):
        tags.add("credential_request")

    return tags


def detect_semantic_instability(profile: Dict[str, Any]) -> Set[str]:
    """
    Experimental out-of-field baseline.

    This does not prove that a statement is meaningless.
    It only flags statements whose F-C-P orientation is weak across all axes.
    """
    margins = [
        float(profile["F_margin"]),
        float(profile["C_margin"]),
        float(profile["P_margin"]),
    ]

    confidences = [
        profile["F_confidence"],
        profile["C_confidence"],
        profile["P_confidence"],
    ]

    low_margin_count = sum(margin <= 0.02 for margin in margins)
    all_ambiguous = all(conf == "AMBIGUOUS" for conf in confidences)

    if all_ambiguous and low_margin_count >= 2:
        return {"semantic_instability"}

    return set()


def suggest_decision(tags: Set[str]) -> str:
    if "safe_verification" in tags:
        return "ALLOW_WITH_BOUNDARIES"

    if "credential_request" in tags and (
        "urgency_pressure" in tags or "coercive_urgency" in tags
    ):
        return "VERIFY_OR_RESTRICT"

    if "credential_request" in tags:
        return "VERIFY_OR_RESTRICT"

    if "objective_conflict" in tags:
        return "REORIENT_OR_CLARIFY"

    if "objective_shift" in tags and "clarification_needed" in tags:
        return "ASK_CONFIRMATION"

    if "objective_shift" in tags:
        return "OPEN_NEW_OBJECTIVE_OR_CONFIRM_SHIFT"

    if "objective_alignment" in tags:
        return "ALLOW"

    if "evidence_distortion" in tags:
        return "REORIENT"

    if "contradiction" in tags:
        return "REORIENT_OR_CLARIFY"

    if "protect_to_exploit" in tags or "training_to_exploitation" in tags:
        return "RESTRICT_OR_REORIENT"

    if "sense_shift" in tags:
        return "REORIENT"

    if "semantic_instability" in tags:
        return "FLAG_OUT_OF_FIELD"

    if "ambiguous_intent" in tags:
        return "ASK_CLARIFICATION_OR_RESTRICT"

    return "CONTINUE_MONITORING"


def diagnose_case(
    case: Dict[str, Any],
    artifacts: Dict[str, Dict[str, np.ndarray]],
) -> Dict[str, Any]:
    text = case["text"]
    profile = evaluate_text(text, artifacts)
    unit_profiles = profile_units(text, artifacts)

    tags: Set[str] = set()

    tags.update(detect_contradiction(text))
    tags.update(detect_sense_shift(text, unit_profiles))
    tags.update(detect_evidence_distortion(text))
    tags.update(detect_objective_alignment(text))
    tags.update(detect_access_request_policy(text))
    tags.update(detect_adversarial_ambiguity(text))
    tags.update(detect_semantic_instability(profile))

    return {
        "id": case["id"],
        "category": case.get("category", "uncategorized"),
        "text": text,
        "profile": profile,
        "unit_profiles": unit_profiles,
        "expected_diagnostic": set(case.get("expected_diagnostic", [])),
        "expected_decision": case.get("expected_decision"),
        "detected_diagnostic": tags,
        "suggested_decision": suggest_decision(tags),
    }


def validate_diagnostics(verbose: bool = False) -> None:
    artifacts = load_triaxial_artifacts()
    suite = load_json(VALIDATION_SUITE_PATH)

    cases = [
        case
        for case in suite.get("cases", [])
        if case.get("expected_diagnostic")
    ]

    print("ACE Atlas — Triaxial Diagnostic Validation v0.1")
    print(f"Suite: {VALIDATION_SUITE_PATH}")
    print(f"Diagnostic cases: {len(cases)}")

    total_expected = 0
    total_detected = 0
    total_matched = 0

    category_stats: Dict[str, Dict[str, int]] = defaultdict(
        lambda: {
            "cases": 0,
            "expected": 0,
            "detected": 0,
            "matched": 0,
        }
    )

    for case in cases:
        result = diagnose_case(case, artifacts)

        expected = result["expected_diagnostic"]
        detected = result["detected_diagnostic"]
        matched = expected & detected

        total_expected += len(expected)
        total_detected += len(detected)
        total_matched += len(matched)

        stats = category_stats[result["category"]]
        stats["cases"] += 1
        stats["expected"] += len(expected)
        stats["detected"] += len(detected)
        stats["matched"] += len(matched)

        profile = result["profile"]

        print("\n" + "-" * 80)
        print(f"CASE: {result['id']} | {result['category']}")
        print(f"TEXT: {result['text']}")
        print(
            f"BASE PROFILE: "
            f"F={profile['F']} "
            f"C={profile['C']} "
            f"P={profile['P']}"
        )
        print(
            f"MARGINS: "
            f"F={profile['F_margin']} "
            f"C={profile['C_margin']} "
            f"P={profile['P_margin']}"
        )
        print(f"EXPECTED TAGS: {sorted(expected)}")
        print(f"DETECTED TAGS: {sorted(detected)}")
        print(f"MATCHED TAGS:  {sorted(matched)}")
        print(f"EXPECTED DECISION: {result['expected_decision']}")
        print(f"SUGGESTED DECISION: {result['suggested_decision']}")

        if verbose:
            print("UNIT PROFILES:")
            for index, unit_profile in enumerate(result["unit_profiles"], start=1):
                print(
                    f"  {index}. {unit_profile['input']} "
                    f"-> F={unit_profile['F']} "
                    f"C={unit_profile['C']} "
                    f"P={unit_profile['P']}"
                )

    recall = total_matched / total_expected if total_expected else 0.0
    precision = total_matched / total_detected if total_detected else 0.0

    print("\n" + "=" * 80)
    print("DIAGNOSTIC VALIDATION SUMMARY")
    print("=" * 80)
    print(f"Cases: {len(cases)}")
    print(f"Matched diagnostic tags: {total_matched}/{total_expected}")
    print(f"Diagnostic tag recall: {recall:.2%}")
    print(f"Diagnostic tag precision: {precision:.2%}")

    print("\nBy category:")

    for category, stats in sorted(category_stats.items()):
        category_recall = (
            stats["matched"] / stats["expected"]
            if stats["expected"]
            else 0.0
        )

        category_precision = (
            stats["matched"] / stats["detected"]
            if stats["detected"]
            else 0.0
        )

        print(
            f"- {category}: "
            f"cases={stats['cases']} "
            f"matched={stats['matched']}/{stats['expected']} "
            f"recall={category_recall:.2%} "
            f"precision={category_precision:.2%}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate ACE Atlas triaxial diagnostic layers."
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print semantic unit profiles for each diagnostic case.",
    )

    args = parser.parse_args()

    validate_diagnostics(verbose=args.verbose)


if __name__ == "__main__":
    main()