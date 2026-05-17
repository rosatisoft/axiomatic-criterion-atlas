"""
ACA — Axiomatic Criterion Atlas

Reproducibility Utilities
-------------------------

This module provides hashing and fingerprint utilities for serialized ACA
artifacts.

The purpose is to make semantic fields reproducible, comparable, and
versionable across machines, notebooks, repositories, and runtime systems.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Iterable

import numpy as np


def hash_bytes(data: bytes, algorithm: str = "sha256") -> str:
    """
    Hash raw bytes using the selected algorithm.
    """

    h = hashlib.new(algorithm)
    h.update(data)

    return h.hexdigest()


def hash_numpy_array(
    array: np.ndarray,
    algorithm: str = "sha256",
) -> str:
    """
    Hash a NumPy array deterministically.
    """

    arr = np.asarray(array)

    payload = arr.tobytes()
    shape_payload = json.dumps(arr.shape).encode("utf-8")
    dtype_payload = str(arr.dtype).encode("utf-8")

    return hash_bytes(
        payload + shape_payload + dtype_payload,
        algorithm=algorithm,
    )


def hash_json_dict(
    data: Dict[str, Any],
    algorithm: str = "sha256",
) -> str:
    """
    Hash a JSON-serializable dictionary deterministically.
    """

    payload = json.dumps(
        data,
        sort_keys=True,
        ensure_ascii=False,
        default=str,
    ).encode("utf-8")

    return hash_bytes(payload, algorithm=algorithm)


def file_hash(
    path: str | Path,
    algorithm: str = "sha256",
) -> str:
    """
    Hash a file by reading its bytes.
    """

    path = Path(path)

    with path.open("rb") as f:
        return hash_bytes(f.read(), algorithm=algorithm)


def directory_fingerprint(
    directory: str | Path,
    include_extensions: Iterable[str] = (".json", ".npy", ".npz"),
    algorithm: str = "sha256",
) -> Dict[str, str]:
    """
    Compute hashes for reproducible artifact files inside a directory.

    Returns a dictionary:

        relative_path -> hash
    """

    directory = Path(directory)

    if not directory.exists():
        raise FileNotFoundError(f"directory not found: {directory}")

    extensions = set(include_extensions)
    fingerprints: Dict[str, str] = {}

    for path in sorted(directory.rglob("*")):

        if not path.is_file():
            continue

        if path.suffix not in extensions:
            continue

        relative = str(path.relative_to(directory)).replace("\\", "/")

        fingerprints[relative] = file_hash(
            path,
            algorithm=algorithm,
        )

    return fingerprints


def combined_fingerprint(
    fingerprints: Dict[str, str],
    algorithm: str = "sha256",
) -> str:
    """
    Compute a single combined fingerprint from file fingerprints.
    """

    payload = json.dumps(
        fingerprints,
        sort_keys=True,
        ensure_ascii=False,
    ).encode("utf-8")

    return hash_bytes(payload, algorithm=algorithm)


def build_reproducibility_manifest(
    artifact_dir: str | Path,
    metadata: Dict[str, Any] | None = None,
    algorithm: str = "sha256",
) -> Dict[str, Any]:
    """
    Build a reproducibility manifest for an ACA artifact directory.
    """

    fingerprints = directory_fingerprint(
        directory=artifact_dir,
        algorithm=algorithm,
    )

    manifest = {
        "algorithm": algorithm,
        "files": fingerprints,
        "combined_fingerprint": combined_fingerprint(
            fingerprints,
            algorithm=algorithm,
        ),
    }

    if metadata is not None:
        manifest["metadata"] = metadata

    return manifest


def save_reproducibility_manifest(
    artifact_dir: str | Path,
    metadata: Dict[str, Any] | None = None,
    filename: str = "reproducibility_manifest.json",
    algorithm: str = "sha256",
) -> Dict[str, Any]:
    """
    Build and save a reproducibility manifest.
    """

    artifact_dir = Path(artifact_dir)

    manifest = build_reproducibility_manifest(
        artifact_dir=artifact_dir,
        metadata=metadata,
        algorithm=algorithm,
    )

    output_path = artifact_dir / filename

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(
            manifest,
            f,
            indent=2,
            ensure_ascii=False,
        )

    return manifest