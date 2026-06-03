from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Any

import numpy as np
from openai import OpenAI


ROOT = Path(".")
MANIFEST_PATH = ROOT / "artifacts" / "triaxial" / "manifest.json"
VALIDATION_SUITE_PATH = ROOT / "artifacts" / "validation" / "triaxial_validation_cases.json"

MODEL = "text-embedding-3-small"


def normalize_vector(vector: np.ndarray) -> np.ndarray:
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return vector / norm


def embed_text(text: str, model: str = MODEL) -> np.ndarray:
    client = OpenAI()
    response = client.embeddings.create(
        model=model,
        input=[text],
    )
    vector = np.array(response.data[0].embedding, dtype=np.float32)
    return normalize_vector(vector)


def subspace_score(vector: np.ndarray, basis: np.ndarray) -> float:
    """
    Scores how strongly a vector projects into an artifact subspace.

    Uses RMS projection so artifacts with different SVD ranks
    are more comparable.
    """
    projections = basis.T @ vector
    return float(np.linalg.norm(projections) / np.sqrt(basis.shape[1]))


def normalize_columns(matrix: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(matrix, axis=0, keepdims=True)
    norms[norms == 0] = 1.0
    return matrix / norms


def load_basis(path: str) -> np.ndarray:
    artifact_path = (ROOT / "artifacts" / path).resolve()

    if artifact_path.is_dir():
        basis_file = artifact_path / "basis_vectors.npy"
    else:
        basis_file = artifact_path

    if not basis_file.exists():
        raise FileNotFoundError(f"Missing basis vectors: {basis_file}")

    basis = np.load(basis_file).astype(np.float32)

    # Expected shape: (embedding_dim, rank).
    # If it appears transposed, fix it.
    if basis.shape[0] != 1536 and basis.shape[1] == 1536:
        basis = basis.T

    return normalize_columns(basis)


def load_json(path: Path) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def rel_artifact_path(manifest_ref: str) -> str:
    """
    Manifest paths are relative to artifacts/triaxial.
    Example: ../context/research
    We convert them into paths relative to artifacts/.
    """
    base = Path("triaxial")
    resolved = (base / manifest_ref).resolve()
    artifacts_root = (ROOT / "artifacts").resolve()

    # Easier and safer: manually normalize relative path from artifacts/triaxial.
    p = (Path("artifacts") / "triaxial" / manifest_ref).resolve()
    return str(p.relative_to(artifacts_root))


def load_triaxial_artifacts() -> Dict[str, Dict[str, np.ndarray]]:
    manifest = load_json(MANIFEST_PATH)

    axes = manifest["axes"]

    foundation_refs = axes["foundation"]["reference_modes"]
    context_refs = axes["context"]["contexts"]
    principle_refs = axes["principle"]["principles"]

    artifacts = {
        "F": {},
        "C": {},
        "P": {},
    }

    for name, spec in foundation_refs.items():
        path = rel_artifact_path(spec["path"])
        artifacts["F"][name] = load_basis(path)

    for name, spec in context_refs.items():
        path = rel_artifact_path(spec["path"])
        artifacts["C"][name] = load_basis(path)

    for name, spec in principle_refs.items():
        path = rel_artifact_path(spec["path"])
        artifacts["P"][name] = load_basis(path)

    return artifacts


def rank_axis(vector: np.ndarray, axis_artifacts: Dict[str, np.ndarray]) -> List[tuple[str, float]]:
    scores = [
        (name, subspace_score(vector, basis))
        for name, basis in axis_artifacts.items()
    ]
    return sorted(scores, key=lambda item: item[1], reverse=True)


def confidence_from_margin(margin: float) -> str:
    if margin >= 0.15:
        return "CLEAR"
    if margin >= 0.05:
        return "WEAK"
    return "AMBIGUOUS"


def evaluate_text(text: str, artifacts: Dict[str, Dict[str, np.ndarray]]) -> Dict[str, Any]:
    vector = embed_text(text)

    result = {"input": text}

    for axis in ["F", "C", "P"]:
        ranking = rank_axis(vector, artifacts[axis])
        top, top_score = ranking[0]
        second_score = ranking[1][1] if len(ranking) > 1 else 0.0
        margin = round(top_score - second_score, 4)

        result[axis] = top
        result[f"{axis}_score"] = round(top_score, 4)
        result[f"{axis}_margin"] = margin
        result[f"{axis}_confidence"] = confidence_from_margin(margin)
        result[f"{axis}_ranking"] = [(name, round(score, 4)) for name, score in ranking]

    return result


def print_profile(profile: Dict[str, Any]) -> None:
    print("\nINPUT")
    print(profile["input"])

    print("\nF-C-P")
    print(
        f"F={profile['F']} "
        f"margin={profile['F_margin']} "
        f"confidence={profile['F_confidence']}"
    )
    print(
        f"C={profile['C']} "
        f"margin={profile['C_margin']} "
        f"confidence={profile['C_confidence']}"
    )
    print(
        f"P={profile['P']} "
        f"margin={profile['P_margin']} "
        f"confidence={profile['P_confidence']}"
    )


def validate_derived_fields(artifacts: Dict[str, Dict[str, np.ndarray]]) -> None:
    cases = [
        {
            "name": "scientific_inquiry",
            "text": "A researcher compares multiple studies before drawing a careful conclusion from the evidence.",
            "expected": ("factual", "research", "investigate"),
        },
        {
            "name": "security_training",
            "text": "Employees learn how to recognize phishing emails and verify suspicious requests through official channels.",
            "expected": ("factual", "training", "protect"),
        },
        {
            "name": "phishing_attack",
            "text": "Your account will be closed unless you enter your username and password immediately.",
            "expected": ("hypothetical", "manipulation", "exploit"),
        },
        {
            "name": "fictional_teaching",
            "text": "Write a story about a village that learns the value of honesty through an imagined conflict.",
            "expected": ("fictional", "narrative", "teach"),
        },
    ]

    print("\n" + "=" * 80)
    print("DERIVED FIELD VALIDATION")
    print("=" * 80)

    passed = 0

    for case in cases:
        profile = evaluate_text(case["text"], artifacts)
        actual = (profile["F"], profile["C"], profile["P"])
        expected = case["expected"]
        ok = actual == expected

        if ok:
            passed += 1

        print("\n" + "-" * 80)
        print(f"CASE: {case['name']}")
        print(f"EXPECTED: {expected}")
        print(f"ACTUAL:   {actual}")
        print(f"RESULT:   {'PASS' if ok else 'CHECK'}")
        print(
            f"MARGINS:  F={profile['F_margin']} "
            f"C={profile['C_margin']} "
            f"P={profile['P_margin']}"
        )

    print("\nSUMMARY")
    print(f"Passed: {passed}/{len(cases)}")


def evaluate_trajectory(
    name: str,
    steps: List[str],
    artifacts: Dict[str, Dict[str, np.ndarray]],
) -> Dict[str, Any]:
    profiles = [evaluate_text(step, artifacts) for step in steps]

    f_seq = [p["F"] for p in profiles]
    c_seq = [p["C"] for p in profiles]
    p_seq = [p["P"] for p in profiles]

    mean_f = round(float(np.mean([p["F_margin"] for p in profiles])), 4)
    mean_c = round(float(np.mean([p["C_margin"] for p in profiles])), 4)
    mean_p = round(float(np.mean([p["P_margin"] for p in profiles])), 4)

    summary = {
        "trajectory": name,
        "F_sequence": f_seq,
        "C_sequence": c_seq,
        "P_sequence": p_seq,
        "mean_F_margin": mean_f,
        "mean_C_margin": mean_c,
        "mean_P_margin": mean_p,
    }

    summary["interpretation"] = interpret_trajectory(summary)

    return summary


def interpret_trajectory(summary: Dict[str, Any]) -> str:
    c_seq = summary["C_sequence"]
    p_seq = summary["P_sequence"]

    c_research = c_seq.count("research")
    c_training = c_seq.count("training")
    c_manipulation = c_seq.count("manipulation")
    c_narrative = c_seq.count("narrative")

    p_investigate = p_seq.count("investigate")
    p_protect = p_seq.count("protect")
    p_exploit = p_seq.count("exploit")
    p_teach = p_seq.count("teach")

    if c_research >= 4 and p_investigate >= 4:
        return "stable_investigation"

    if c_training >= 3 and p_protect >= 4:
        return "protective_training"

    if c_manipulation >= 4 and p_exploit >= 3:
        return "exploitative_manipulation"

    if c_research >= 2 and c_manipulation >= 2:
        return "contextual_drift"

    if c_narrative >= 3 and p_teach >= 2:
        return "fictional_teaching"

    if summary["mean_C_margin"] <= 0.05 or summary["mean_P_margin"] <= 0.05:
        return "ambiguous_or_unstable"

    return "mixed_trajectory"


def validate_trajectories(artifacts: Dict[str, Dict[str, np.ndarray]]) -> None:
    trajectories = {
        "clean_investigation": [
            "A company notices a decline in productivity across several teams.",
            "Management decides not to assume a cause and begins reviewing evidence.",
            "The team gathers operational metrics, surveys, and historical comparisons.",
            "Several possible explanations are compared across departments.",
            "Some teams show improved productivity while others do not.",
            "The report concludes that additional investigation is needed before policy changes.",
        ],
        "argumentative_drift": [
            "A manager strongly believes that remote work reduces productivity.",
            "He begins gathering information to support his conclusion.",
            "Several reports indicate productivity increased in some teams.",
            "These reports are excluded because they complicate the preferred argument.",
            "Only negative examples are selected and emphasized.",
            "The final presentation concludes that remote work is clearly harmful.",
        ],
        "phishing_training": [
            "This training document explains how phishing attempts pressure users.",
            "Employees are shown examples of fraudulent emails in a controlled setting.",
            "Common warning signs are identified, including urgency and suspicious links.",
            "Participants are encouraged to verify requests through official channels.",
            "The goal is to improve security awareness and reduce organizational risk.",
        ],
        "phishing_attack": [
            "Your account has been flagged for immediate suspension.",
            "Recent activity suggests unauthorized access.",
            "To avoid permanent closure, verify your credentials now.",
            "Click the link below and enter your username and password.",
            "Failure to comply within the next hour may result in account loss.",
        ],
    }

    expected_interpretations = {
        "clean_investigation": "stable_investigation",
        "argumentative_drift": "contextual_drift",
        "phishing_training": "protective_training",
        "phishing_attack": "exploitative_manipulation",
    }

    print("\n" + "=" * 80)
    print("TRAJECTORY VALIDATION")
    print("=" * 80)

    passed = 0

    for name, steps in trajectories.items():
        summary = evaluate_trajectory(name, steps, artifacts)
        expected = expected_interpretations[name]
        actual = summary["interpretation"]
        ok = expected == actual

        if ok:
            passed += 1

        print("\n" + "-" * 80)
        print(f"TRAJECTORY: {name}")
        print(f"EXPECTED:   {expected}")
        print(f"ACTUAL:     {actual}")
        print(f"RESULT:     {'PASS' if ok else 'CHECK'}")
        print(f"F_SEQUENCE: {' -> '.join(summary['F_sequence'])}")
        print(f"C_SEQUENCE: {' -> '.join(summary['C_sequence'])}")
        print(f"P_SEQUENCE: {' -> '.join(summary['P_sequence'])}")
        print(
            f"MEAN MARGINS: "
            f"F={summary['mean_F_margin']} "
            f"C={summary['mean_C_margin']} "
            f"P={summary['mean_P_margin']}"
        )

    print("\nSUMMARY")
    print(f"Passed: {passed}/{len(trajectories)}")


def axis_match(profile: Dict[str, Any], expected: Dict[str, str]) -> tuple[int, int]:
    total = 0
    matched = 0

    for axis in ["F", "C", "P"]:
        if axis in expected:
            total += 1
            if profile[axis] == expected[axis]:
                matched += 1

    return matched, total


def validate_case_suite(artifacts: Dict[str, Dict[str, np.ndarray]]) -> None:
    if not VALIDATION_SUITE_PATH.exists():
        print(f"\nValidation suite not found: {VALIDATION_SUITE_PATH}")
        return

    suite = load_json(VALIDATION_SUITE_PATH)
    cases = suite.get("cases", [])

    print("\n" + "=" * 80)
    print("VALIDATION SUITE — INDIVIDUAL CASES")
    print("=" * 80)

    total_cases = 0
    total_axis_expected = 0
    total_axis_matched = 0

    category_stats: Dict[str, Dict[str, int]] = {}

    for case in cases:
        total_cases += 1

        category = case.get("category", "uncategorized")
        category_stats.setdefault(
            category,
            {
                "cases": 0,
                "axis_expected": 0,
                "axis_matched": 0,
                "checks": 0
            }
        )
        category_stats[category]["cases"] += 1

        profile = evaluate_text(case["text"], artifacts)
        expected = case.get("expected", {})

        matched, expected_total = axis_match(profile, expected)

        total_axis_expected += expected_total
        total_axis_matched += matched

        category_stats[category]["axis_expected"] += expected_total
        category_stats[category]["axis_matched"] += matched

        if expected_total > 0:
            result = "PASS" if matched == expected_total else "CHECK"
        else:
            result = "INFO"

        category_stats[category]["checks"] += 1 if result == "CHECK" else 0

        print("\n" + "-" * 80)
        print(f"CASE: {case['id']} | {category}")
        print(f"TEXT: {case['text']}")
        print(
            f"ACTUAL: F={profile['F']} "
            f"C={profile['C']} "
            f"P={profile['P']}"
        )

        if expected:
            print(f"EXPECTED: {expected}")
            print(f"AXIS MATCH: {matched}/{expected_total}")
        else:
            print("EXPECTED: decision-only / diagnostic case")

        print(
            f"MARGINS: F={profile['F_margin']} "
            f"C={profile['C_margin']} "
            f"P={profile['P_margin']}"
        )
        print(
            f"CONF: F={profile['F_confidence']} "
            f"C={profile['C_confidence']} "
            f"P={profile['P_confidence']}"
        )
        print(f"EXPECTED_DECISION: {case.get('expected_decision', 'N/A')}")
        print(f"RESULT: {result}")

    print("\n" + "=" * 80)
    print("VALIDATION SUITE SUMMARY")
    print("=" * 80)

    print(f"Total cases: {total_cases}")
    print(f"Axis matches: {total_axis_matched}/{total_axis_expected}")

    if total_axis_expected:
        accuracy = total_axis_matched / total_axis_expected
        print(f"Axis accuracy: {accuracy:.2%}")

    print("\nBy category:")

    for category, stats in category_stats.items():
        axis_expected = stats["axis_expected"]
        axis_matched = stats["axis_matched"]

        if axis_expected:
            acc = axis_matched / axis_expected
            acc_text = f"{acc:.2%}"
        else:
            acc_text = "N/A"

        print(
            f"- {category}: "
            f"cases={stats['cases']} "
            f"axis={axis_matched}/{axis_expected} "
            f"accuracy={acc_text} "
            f"checks={stats['checks']}"
        )


def validate_trajectory_suite(artifacts: Dict[str, Dict[str, np.ndarray]]) -> None:
    if not VALIDATION_SUITE_PATH.exists():
        print(f"\nValidation suite not found: {VALIDATION_SUITE_PATH}")
        return

    suite = load_json(VALIDATION_SUITE_PATH)
    trajectories = suite.get("trajectories", [])

    print("\n" + "=" * 80)
    print("VALIDATION SUITE — TRAJECTORIES")
    print("=" * 80)

    passed = 0

    for trajectory in trajectories:
        summary = evaluate_trajectory(
            trajectory["name"],
            trajectory["steps"],
            artifacts
        )

        expected = trajectory["expected_interpretation"]
        actual = summary["interpretation"]
        ok = expected == actual

        if ok:
            passed += 1

        print("\n" + "-" * 80)
        print(f"TRAJECTORY: {trajectory['id']} | {trajectory['name']}")
        print(f"EXPECTED:   {expected}")
        print(f"ACTUAL:     {actual}")
        print(f"RESULT:     {'PASS' if ok else 'CHECK'}")
        print(f"F_SEQUENCE: {' -> '.join(summary['F_sequence'])}")
        print(f"C_SEQUENCE: {' -> '.join(summary['C_sequence'])}")
        print(f"P_SEQUENCE: {' -> '.join(summary['P_sequence'])}")
        print(
            f"MEAN MARGINS: "
            f"F={summary['mean_F_margin']} "
            f"C={summary['mean_C_margin']} "
            f"P={summary['mean_P_margin']}"
        )

    print("\nSUMMARY")
    print(f"Trajectory matches: {passed}/{len(trajectories)}")


def main() -> None:
    print("ACE Atlas — Triaxial Artifact Validation v0.1")
    print(f"Manifest: {MANIFEST_PATH}")

    artifacts = load_triaxial_artifacts()

    print("\nLoaded artifacts:")
    for axis, items in artifacts.items():
        print(f"{axis}: {list(items.keys())}")

    validate_derived_fields(artifacts)
    validate_trajectories(artifacts)

    validate_case_suite(artifacts)
    validate_trajectory_suite(artifacts)


if __name__ == "__main__":
    main()