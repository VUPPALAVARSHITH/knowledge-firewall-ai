"""
embedding_service.py

Knowledge Firewall AI

Centralized embedding service.

Loads the embedding model only once and shares it
across Dataset Generation, Fingerprinting,
Retrieval and Firewall.
"""

from __future__ import annotations

from sentence_transformers import SentenceTransformer


class EmbeddingService:

    _instance = None
    _model = None

    MODEL_NAME = "all-MiniLM-L6-v2"

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

        return cls._instance

    # --------------------------------------------------

    def model(self):

        if self._model is None:

            print()

            print("=" * 60)
            print("Loading Shared Embedding Model")
            print("=" * 60)

            self._model = SentenceTransformer(

                self.MODEL_NAME

            )

            print("Embedding Model Ready")

            print("=" * 60)

        return self._model

    # --------------------------------------------------

    def encode(

        self,

        text,

        normalize=True

    ):

        return self.model().encode(

            text,

            normalize_embeddings=normalize

        )

    # --------------------------------------------------

    def model_name(self):

        return self.MODEL_NAME