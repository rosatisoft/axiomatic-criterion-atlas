"""
ACA — Axiomatic Criterion Atlas

Load Field
----------

Utilities for loading serialized ACA semantic field artifacts.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

import numpy as np


@dataclass
class LoadedField:
    """
    Fully loaded ACA field artifact.
    """

    basis: np.ndarray
    metadata: Dict[str, Any]
    singular_values: Optional[np.ndarray] = None
    criterion_vectors: Optional[np.ndarray] = None
    thresholds: Optional[Dict[str, Any]] = None


def load_json(path: str | Path) -> Dict[str, Any]:
    """
    Load a JSON file.
    """

    path = Path(path)

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_numpy(path: str | Path) -> np.ndarray:
    """
    Load a NumPy .npy file.
    """

    path = Path(path)

    return np.load(path)


def load_optional_numpy(path: str | Path) -> Optional[np.ndarray]:
    """
    Load a NumPy file if it exists.
    """

    path = Path(path)

    if not path.exists():
        return None

    return np.load(path)


def load_optional_json(path: str | Path) -> Optional[Dict[str, Any]]:
    """
    Load a JSON file if it exists.
    """

    path = Path(path)

    if not path.exists():
        return None

    return load_json(path)


def load_field_artifacts(
    input_dir: str | Path,
) -> LoadedField:
    """
    Load a serialized ACA field artifact directory.

    Expected structure:

        input_dir/
        ├── basis_vectors.npy
        ├── singular_values.npy
        ├── criterion_vectors.npy
        ├── field_metadata.json
        └── thresholds.json
    """

    input_dir = Path(input_dir)

    if not input_dir.exists():
        raise FileNotFoundError(f"directory not found: {input_dir}")

    basis_path = input_dir / "basis_vectors.npy"
    metadata_path = input_dir / "field_metadata.json"

    if not basis_path.exists():
        raise FileNotFoundError(
            f"missing required artifact: {basis_path.name}"
        )

    if not metadata_path.exists():
        raise FileNotFoundError(
            f"missing required artifact: {metadata_path.name}"
        )

    basis = load_numpy(basis_path)
    metadata = load_json(metadata_path)

    singular_values = load_optional_numpy(
        input_dir / "singular_values.npy"
    )

    criterion_vectors = load_optional_numpy(
        input_dir / "criterion_vectors.npy"
    )

    thresholds = load_optional_json(
        input_dir / "thresholds.json"
    )

    return LoadedField(
        basis=basis,
        metadata=metadata,
        singular_values=singular_values,
        criterion_vectors=criterion_vectors,
        thresholds=thresholds,
    )