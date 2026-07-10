"""
query_encoder.py

Knowledge Firewall AI

Encodes user queries into embeddings for semantic retrieval.
"""

from __future__ import annotations

import numpy as np
from sentence_transformers import SentenceTransformer

from src.config.constants import (
    EMBEDDING_MODEL
)


class QueryEncoder:

    """
    Converts natural language queries into
    normalized embedding vectors.
    """

    def __init__(self):

        print("Loading Query Encoder...")

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

        print("Query Encoder Ready.\n")

    # ----------------------------------------------------

    def encode(
        self,
        query: str
    ) -> np.ndarray:

        embedding = self.model.encode(

            query,

            convert_to_numpy=True,

            normalize_embeddings=True

        )

        return embedding.astype(np.float32)


# --------------------------------------------------------
# Test
# --------------------------------------------------------

if __name__ == "__main__":

    encoder = QueryEncoder()

    vector = encoder.encode(

        "Does VPN require multi factor authentication?"

    )

    print(vector.shape)