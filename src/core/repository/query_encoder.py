"""
query_encoder.py

Knowledge Firewall AI

Encodes user queries into embeddings.
"""

from __future__ import annotations

import numpy as np

from src.services.embedding_service import EmbeddingService


class QueryEncoder:

    """
    Converts user queries into normalized embeddings.
    """

    def __init__(self):

        self.embedding_service = EmbeddingService()

    # ----------------------------------------------------

    def encode(
        self,
        query: str
    ) -> np.ndarray:

        embedding = self.embedding_service.encode(

            query,

            normalize=True

        )

        return embedding.astype(np.float32)


# --------------------------------------------------------

if __name__ == "__main__":

    encoder = QueryEncoder()

    vector = encoder.encode(

        "Does VPN require MFA?"

    )

    print(vector.shape)