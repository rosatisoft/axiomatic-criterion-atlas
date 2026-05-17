"""
ACA — Axiomatic Criterion Atlas

Save Field
----------

Utilities for saving ACA semantic field artifacts.

The serialized field may include:

- basis vectors
- singular values
- metadata
- criterion vectors
- thresholds
"""

from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any, Dict, Optional

import numpy as np


def _to_serializable(value: Any) -> Any:
    """
    Convert common Python objects into JSON-serializable structures.
    """

    if is_dataclass(value):
        return asdict(value)

    if isinstance(value, np.ndarray):
        return value.tolist()

    if isinstance(value, (np.float32, np.float64)):
        return float(value)

    if isinstance(value, (np.int32, np.int64)):
        return int(value)

    return value


def save_json(path: str | Path, data: Dict[str, Any]) -> None:
    """
    Save dictionary data as JSON.
    """

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    serializable = {
        key: _to_serializable(value)
        for key, value in data.items()
    }

    with path.open("w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=2, ensure_ascii=False)


def save_numpy(path: str | Path, array: np.ndarray) -> None:
    """
    Save a NumPy array to .npy format.
    """

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    np.save(path, np.asarray(array, dtype=np.float64))


def save_field_artifacts(
    output_dir: str | Path,
    basis: np.ndarray,
    metadata: Dict[str, Any],
    singular_values: Optional[np.ndarray] = None,
    criterion_vectors: Optional[np.ndarray] = None,
    thresholds: Optional[Dict[str, Any]] = None,
) -> None:
    """
    Save a complete ACA field artifact directory.

    Output structure:

        output_dir/
        ├── basis_vectors.npy
        ├── singular_values.npy
        ├── criterion_vectors.npy
        ├── field_metadata.json
        └── thresholds.json
    """

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    save_numpy(
        output_dir / "basis_vectors.npy",
        basis,
    )

    if singular_values is not None:
        save_numpy(
            output_dir / "singular_values.npy",
            singular_values,
        )

    if criterion_vectors is not None:
        save_numpy(
            output_dir / "criterion_vectors.npy",
            criterion_vectors,
        )

    save_json(
        output_dir / "field_metadata.json",
        metadata,
    )

    if thresholds is not None:
        save_json(
            output_dir / "thresholds.json",
            thresholds,
        )