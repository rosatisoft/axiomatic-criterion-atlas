from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


EXPECTED_LANGUAGE_CODES = {"en", "es", "pt", "fr", "de", "it"}

EXPECTED_ARTIFACTS = {
    "sensitive_access_object",
    "unsafe_secret_extraction",
    "defensive_account_recovery",
    "safe_security_guidance",
    "ambiguous_sensitive_access",
    "manipulative_credential_pressure",
}

BOUNDARY_DECISIONS = {
    "BOUNDARY_SECRET_REQUEST",
    "SAFE_CREDENTIAL_GUIDANCE",
    "ASK_CLARIFICATION_SENSITIVE",
}

EXPECTED_DECISION_BY_ARTIFACT = {
    "unsafe_secret_extraction": "BOUNDARY_SECRET_REQUEST",
    "defensive_account_recovery": "SAFE_CREDENTIAL_GUIDANCE",
    "safe_security_guidance": "SAFE_CREDENTIAL_GUIDANCE",
    "ambiguous_sensitive_access": "ASK_CLARIFICATION_SENSITIVE",
    "manipulative_credential_pressure": "BOUNDARY_SECRET_REQUEST",
}


def fail(message: str, errors: list[str]) -> None:
    errors.append(f"ERROR: {message}")


def warn(message: str, warnings: list[str]) -> None:
    warnings.append(f"WARNING: {message}")


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_top_level(data: dict[str, Any], errors: list[str], warnings: list[str]) -> None:
    required = [
        "version",
        "embedding_model",
        "embedding_dim",
        "artifact_family",
        "runtime_layer",
        "languages",
        "decision_guidance",
        "artifacts",
        "probe_design",
    ]

    for key in required:
        if key not in data:
            fail(f"Missing top-level key: {key}", errors)

    if data.get("artifact_family") != "security_access_boundary":
        fail("artifact_family must be 'security_access_boundary'.", errors)

    if data.get("runtime_layer") != "access_gate":
        fail("runtime_layer must be 'access_gate'.", errors)

    if data.get("embedding_model") != "text-embedding-3-small":
        warn(
            "embedding_model is not text-embedding-3-small. "
            "This boundary source is intended to preserve the current ACA baseline.",
            warnings,
        )

    if data.get("embedding_dim") != 1536:
        warn(
            "embedding_dim is not 1536. "
            "The current general/foundational ACA baseline is 1536 dimensions.",
            warnings,
        )


def validate_languages(data: dict[str, Any], errors: list[str], warnings: list[str]) -> list[str]:
    languages = data.get("languages", [])

    if not isinstance(languages, list) or not languages:
        fail("languages must be a non-empty list.", errors)
        return []

    codes: list[str] = []

    for entry in languages:
        if not isinstance(entry, dict):
            fail("Each language entry must be an object.", errors)
            continue

        code = entry.get("code")
        name = entry.get("name")

        if not code:
            fail("Language entry missing code.", errors)
            continue

        if not name:
            warn(f"Language {code!r} is missing a display name.", warnings)

        codes.append(str(code))

    code_set = set(codes)

    missing = EXPECTED_LANGUAGE_CODES - code_set
    extra = code_set - EXPECTED_LANGUAGE_CODES

    if missing:
        fail(f"Missing expected language codes: {sorted(missing)}", errors)

    if extra:
        warn(f"Unexpected extra language codes: {sorted(extra)}", warnings)

    duplicates = [code for code, n in Counter(codes).items() if n > 1]
    if duplicates:
        fail(f"Duplicate language codes: {sorted(duplicates)}", errors)

    return codes


def validate_decision_guidance(data: dict[str, Any], errors: list[str], warnings: list[str]) -> None:
    guidance = data.get("decision_guidance", {})

    if not isinstance(guidance, dict):
        fail("decision_guidance must be an object.", errors)
        return

    for key, value in guidance.items():
        if not isinstance(value, str):
            fail(f"decision_guidance.{key} must be a string.", errors)

    required_guidance = {
        "sensitive_object_plus_extraction",
        "sensitive_object_plus_defensive_recovery",
        "sensitive_object_plus_protection_or_detection",
        "sensitive_object_plus_ambiguous_access",
        "sensitive_object_plus_pressure_or_deception",
        "low_signal_without_sensitive_object",
    }

    missing = required_guidance - set(guidance.keys())
    if missing:
        fail(f"Missing decision guidance entries: {sorted(missing)}", errors)


def validate_artifacts(
    data: dict[str, Any],
    language_codes: list[str],
    errors: list[str],
    warnings: list[str],
) -> dict[str, dict[str, Any]]:
    artifacts = data.get("artifacts", {})

    if not isinstance(artifacts, dict) or not artifacts:
        fail("artifacts must be a non-empty object.", errors)
        return {}

    artifact_names = set(artifacts.keys())
    missing = EXPECTED_ARTIFACTS - artifact_names
    extra = artifact_names - EXPECTED_ARTIFACTS

    if missing:
        fail(f"Missing expected artifacts: {sorted(missing)}", errors)

    if extra:
        warn(f"Unexpected extra artifacts: {sorted(extra)}", warnings)

    language_count = max(len(language_codes), 1)

    for name, artifact in artifacts.items():
        if not isinstance(artifact, dict):
            fail(f"Artifact {name!r} must be an object.", errors)
            continue

        for key in ["axis", "artifact_path", "description", "invariants", "anchors"]:
            if key not in artifact:
                fail(f"Artifact {name!r} missing required key: {key}", errors)

        if artifact.get("axis") != "access_boundary":
            fail(f"Artifact {name!r} axis must be 'access_boundary'.", errors)

        artifact_path = artifact.get("artifact_path", "")
        if not isinstance(artifact_path, str) or "security_access_boundary" not in artifact_path:
            fail(
                f"Artifact {name!r} artifact_path should include 'security_access_boundary'.",
                errors,
            )

        invariants = artifact.get("invariants", [])
        if not isinstance(invariants, list) or len(invariants) < 3:
            fail(f"Artifact {name!r} should define at least 3 invariants.", errors)

        anchors = artifact.get("anchors", [])
        if not isinstance(anchors, list) or not anchors:
            fail(f"Artifact {name!r} must define a non-empty anchors list.", errors)
            continue

        non_string = [i for i, a in enumerate(anchors) if not isinstance(a, str)]
        if non_string:
            fail(f"Artifact {name!r} has non-string anchors at indexes: {non_string}", errors)

        blank = [i for i, a in enumerate(anchors) if isinstance(a, str) and not a.strip()]
        if blank:
            fail(f"Artifact {name!r} has blank anchors at indexes: {blank}", errors)

        duplicates = [a for a, n in Counter(anchors).items() if n > 1]
        if duplicates:
            fail(f"Artifact {name!r} has duplicate anchors: {duplicates[:5]}", errors)

        if len(anchors) < language_count:
            fail(
                f"Artifact {name!r} has fewer anchors ({len(anchors)}) than languages ({language_count}).",
                errors,
            )

        if len(anchors) % language_count != 0:
            warn(
                f"Artifact {name!r} has {len(anchors)} anchors, not divisible by "
                f"{language_count} languages. This may indicate uneven multilingual coverage.",
                warnings,
            )

        expected_decision = EXPECTED_DECISION_BY_ARTIFACT.get(name)
        actual_decision = artifact.get("expected_decision")

        if expected_decision and actual_decision != expected_decision:
            fail(
                f"Artifact {name!r} expected_decision should be {expected_decision}, "
                f"got {actual_decision!r}.",
                errors,
            )

        if actual_decision and actual_decision not in BOUNDARY_DECISIONS:
            fail(
                f"Artifact {name!r} has unsupported expected_decision: {actual_decision}",
                errors,
            )

    return artifacts


def validate_probe_design(
    data: dict[str, Any],
    artifacts: dict[str, dict[str, Any]],
    errors: list[str],
    warnings: list[str],
) -> None:
    probe_design = data.get("probe_design", {})

    if not isinstance(probe_design, dict):
        fail("probe_design must be an object.", errors)
        return

    must_not_create_origin_for = probe_design.get("must_not_create_origin_for", [])

    if not isinstance(must_not_create_origin_for, list):
        fail("probe_design.must_not_create_origin_for must be a list.", errors)
    else:
        missing = set(must_not_create_origin_for) - set(artifacts.keys())
        if missing:
            fail(
                "probe_design.must_not_create_origin_for references missing artifacts: "
                f"{sorted(missing)}",
                errors,
            )

    primary_metrics = probe_design.get("primary_metrics", [])
    if not isinstance(primary_metrics, list) or not primary_metrics:
        warn("probe_design.primary_metrics should be a non-empty list.", warnings)

    initial_languages = probe_design.get("initial_languages", [])
    if set(initial_languages) != EXPECTED_LANGUAGE_CODES:
        warn(
            "probe_design.initial_languages differs from the expected initial set "
            f"{sorted(EXPECTED_LANGUAGE_CODES)}.",
            warnings,
        )


def print_report(
    path: Path,
    data: dict[str, Any],
    artifacts: dict[str, dict[str, Any]],
    errors: list[str],
    warnings: list[str],
) -> None:
    print("=" * 100)
    print("ACA Security Access Boundary Source Validator")
    print("=" * 100)
    print(f"Source:          {path}")
    print(f"Version:         {data.get('version')}")
    print(f"Artifact family: {data.get('artifact_family')}")
    print(f"Runtime layer:   {data.get('runtime_layer')}")
    print(f"Embedding model: {data.get('embedding_model')}")
    print(f"Embedding dim:   {data.get('embedding_dim')}")
    print()

    languages = data.get("languages", [])
    if isinstance(languages, list):
        print("Languages:")
        for language in languages:
            if isinstance(language, dict):
                print(f"  - {language.get('code')}: {language.get('name')}")
        print()

    print("Artifact anchor counts:")
    total_anchors = 0
    for name, artifact in artifacts.items():
        anchors = artifact.get("anchors", []) if isinstance(artifact, dict) else []
        invariants = artifact.get("invariants", []) if isinstance(artifact, dict) else []
        expected_decision = artifact.get("expected_decision", "(none)")
        total_anchors += len(anchors)
        print(
            f"  - {name:<35} anchors={len(anchors):>3} "
            f"invariants={len(invariants):>2} expected={expected_decision}"
        )

    print(f"\nTotal anchors: {total_anchors}")
    print()

    if warnings:
        print("Warnings:")
        for item in warnings:
            print(f"  {item}")
        print()

    if errors:
        print("Errors:")
        for item in errors:
            print(f"  {item}")
        print()
        print("RESULT: FAIL")
        raise SystemExit(1)

    print("RESULT: PASS")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate ACA security_access_boundary_sources.json."
    )
    parser.add_argument(
        "source",
        nargs="?",
        default="source_definitions/security_access_boundary_sources.json",
        help="Path to security_access_boundary_sources.json",
    )

    args = parser.parse_args()

    path = Path(args.source)

    errors: list[str] = []
    warnings: list[str] = []

    if not path.exists():
        fail(f"Source file does not exist: {path}", errors)
        print_report(path, {}, {}, errors, warnings)
        return

    try:
        data = load_json(path)
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON: {exc}", errors)
        print_report(path, {}, {}, errors, warnings)
        return

    if not isinstance(data, dict):
        fail("Root JSON value must be an object.", errors)
        print_report(path, {}, {}, errors, warnings)
        return

    validate_top_level(data, errors, warnings)
    language_codes = validate_languages(data, errors, warnings)
    validate_decision_guidance(data, errors, warnings)
    artifacts = validate_artifacts(data, language_codes, errors, warnings)
    validate_probe_design(data, artifacts, errors, warnings)

    print_report(path, data, artifacts, errors, warnings)


if __name__ == "__main__":
    main()
