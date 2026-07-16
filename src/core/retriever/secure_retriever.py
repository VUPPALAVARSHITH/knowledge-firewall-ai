"""
secure_retriever.py

Knowledge Firewall AI

Semantic Retriever built on top of the
Enterprise Vector Store.
"""

from __future__ import annotations

from src.core.repository.query_encoder import QueryEncoder
from src.core.repository.vector_store import EnterpriseVectorStore


class SecureRetriever:

    """
    Enterprise semantic retriever.

    Current Stage:
        - Semantic Retrieval

    Next Stage:
        - Knowledge Firewall
        - Trust Verification
    """

    def __init__(self):

        self.encoder = QueryEncoder()

        self.store = EnterpriseVectorStore()

        self.store.load()

    # ----------------------------------------------------

    def retrieve(

        self,

        query: str,

        top_k: int = 5

    ):

        embedding = self.encoder.encode(query)

        return self.store.search(

            embedding,

            top_k

        )


# --------------------------------------------------------
# Test
# --------------------------------------------------------

if __name__ == "__main__":

    retriever = SecureRetriever()

    results = retriever.retrieve(

        "Does VPN require multi-factor authentication?"

    )

    print("\nTop Results\n")

    for rank, result in enumerate(results, start=1):

        chunk = result["chunk"]

        print("=" * 60)

        print(f"Rank : {rank}")

        print(f"Score : {result['score']:.4f}")

        print(f"Policy : {chunk.policy_id}")

        print(f"Section : {chunk.section}")

        print()

        print(chunk.text)

        print()