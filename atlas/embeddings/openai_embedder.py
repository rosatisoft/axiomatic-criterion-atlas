"""
ACA — Axiomatic Criterion Atlas

OpenAI Embedder
---------------

Real embedding provider for ACA using OpenAI embeddings.
"""

from __future__ import annotations

import os
from typing import Iterable, List

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI


DEFAULT_EMBEDDING_MODEL = "text-embedding-3-small"


class OpenAIEmbedder:
    """
    OpenAI embedding provider.
    """

    def __init__(
        self,
        model: str = DEFAULT_EMBEDDING_MODEL,
        normalize: bool = True,
    ) -> None:
        load_dotenv()

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY is missing. Add it to your .env file."
            )

        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.normalize = normalize

    def embed_text(self, text: str) -> np.ndarray:
        """
        Embed a single text.
        """

        response = self.client.embeddings.create(
            model=self.model,
            input=text,
        )

        vector = np.asarray(
            response.data[0].embedding,
            dtype=np.float64,
        )

        if self.normalize:
            vector = self._normalize(vector)

        return vector

    def embed_texts(self, texts: Iterable[str]) -> List[np.ndarray]:
        """
        Embed multiple texts in one API call.
        """

        text_list = list(texts)

        if not text_list:
            return []

        response = self.client.embeddings.create(
            model=self.model,
            input=text_list,
        )

        vectors: List[np.ndarray] = []

        for item in response.data:
            vector = np.asarray(item.embedding, dtype=np.float64)

            if self.normalize:
                vector = self._normalize(vector)

            vectors.append(vector)

        return vectors

    @staticmethod
    def _normalize(vector: np.ndarray, epsilon: float = 1e-12) -> np.ndarray:
        """
        L2 normalize vector.
        """

        norm = np.linalg.norm(vector)

        if norm < epsilon:
            return vector

        return vector / norm