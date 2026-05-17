"""
ACA — Axiomatic Criterion Atlas

Semantic Trajectory
-------------------

This module defines the basic data structures for representing semantic
trajectory evolution.

A semantic trajectory is an ordered sequence of embedded states:

    T = {z_1, z_2, ..., z_T}

Each state may later be evaluated through:

- origin cost
- semantic field selection
- epistemic orientation
- criterion drift
- preservation metrics
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional

import numpy as np


@dataclass
class SemanticState:
    """
    A single semantic trajectory state.
    """

    index: int
    text: str
    embedding: np.ndarray
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SemanticTrajectory:
    """
    Ordered semantic trajectory.
    """

    states: List[SemanticState]

    def __post_init__(self) -> None:
        if not self.states:
            raise ValueError("SemanticTrajectory must contain at least one state.")

        indices = [state.index for state in self.states]

        if len(indices) != len(set(indices)):
            raise ValueError("SemanticTrajectory contains duplicate state indices.")

        self.states.sort(key=lambda state: state.index)

    def embeddings(self) -> np.ndarray:
        """
        Return trajectory embeddings as a matrix.

        Shape:

            (n_states, embedding_dim)
        """

        return np.vstack([state.embedding for state in self.states])

    def texts(self) -> List[str]:
        """
        Return trajectory texts in order.
        """

        return [state.text for state in self.states]

    def length(self) -> int:
        """
        Return trajectory length.
        """

        return len(self.states)

    def get_state(self, index: int) -> SemanticState:
        """
        Return a state by index.
        """

        for state in self.states:
            if state.index == index:
                return state

        raise KeyError(f"state index not found: {index}")


def build_semantic_trajectory(
    texts: Iterable[str],
    embeddings: Iterable[np.ndarray],
    metadata: Optional[Iterable[Dict[str, Any]]] = None,
) -> SemanticTrajectory:
    """
    Build a SemanticTrajectory from ordered texts and embeddings.

    Parameters
    ----------
    texts:
        Ordered text states.

    embeddings:
        Ordered embedding vectors.

    metadata:
        Optional ordered metadata dictionaries.

    Returns
    -------
    SemanticTrajectory
        Ordered semantic trajectory.
    """

    text_list = list(texts)
    embedding_list = [np.asarray(e, dtype=np.float64) for e in embeddings]

    if len(text_list) != len(embedding_list):
        raise ValueError("texts and embeddings must have the same length.")

    if metadata is None:
        metadata_list = [{} for _ in text_list]
    else:
        metadata_list = list(metadata)

    if len(metadata_list) != len(text_list):
        raise ValueError("metadata must match the number of texts.")

    states: List[SemanticState] = []

    for i, (text, embedding, meta) in enumerate(
        zip(text_list, embedding_list, metadata_list),
        start=1,
    ):
        if embedding.ndim != 1:
            raise ValueError("each embedding must be a 1D array.")

        states.append(
            SemanticState(
                index=i,
                text=text,
                embedding=embedding,
                metadata=meta,
            )
        )

    return SemanticTrajectory(states=states)


def trajectory_embedding_deltas(
    trajectory: SemanticTrajectory,
) -> List[np.ndarray]:
    """
    Compute embedding deltas between consecutive trajectory states.

    Returns:

        z_t - z_{t-1}
    """

    embeddings = trajectory.embeddings()

    if embeddings.shape[0] < 2:
        return []

    return [
        embeddings[i] - embeddings[i - 1]
        for i in range(1, embeddings.shape[0])
    ]


def trajectory_step_norms(
    trajectory: SemanticTrajectory,
) -> List[float]:
    """
    Compute norm of each trajectory step delta.
    """

    deltas = trajectory_embedding_deltas(trajectory)

    return [float(np.linalg.norm(delta)) for delta in deltas]