"""
knowledge_firewall.py

Knowledge Firewall AI

Secure retrieval orchestrator.

Pipeline

User Query
    |
    v
Semantic Retrieval
    |
    v
Relevance Gate
    |
    v
Fingerprint Verification
    |
    v
Trust Computation
    |
    v
Trusted Context
"""

from __future__ import annotations

from dataclasses import dataclass, field

from src.core.retriever.secure_retriever import SecureRetriever
from src.core.firewall.verifier import ChunkVerifier, VerificationResult


# ============================================================
# Firewall Result
# ============================================================

@dataclass(slots=True)
class FirewallResult:

    query: str

    trusted_chunks: list = field(default_factory=list)

    suspicious_chunks: list = field(default_factory=list)

    blocked_chunks: list = field(default_factory=list)

    verification_reports: list[VerificationResult] = field(
        default_factory=list
    )

    context: str = ""

    statistics: dict = field(default_factory=dict)


# ============================================================
# Knowledge Firewall
# ============================================================

class KnowledgeFirewall:

    """
    Secure retrieval layer.

    Pipeline:

        1. Semantic retrieval
        2. Relevance filtering
        3. Runtime fingerprint verification
        4. Trust computation
        5. Trusted context construction

    A chunk must therefore satisfy TWO conditions:

        Relevance:
            The chunk must be sufficiently related to
            the user's query.

        Integrity:
            The chunk must match its trusted fingerprint.

    Only chunks satisfying both conditions are allowed
    into the trusted context.
    """

    # --------------------------------------------------------
    # Retrieval relevance threshold
    #
    # FAISS scores are cosine-similarity-like scores because
    # the embedding service uses normalized embeddings.
    #
    # This is intentionally configurable so it can be tuned
    # during evaluation.
    # --------------------------------------------------------

    RELEVANCE_THRESHOLD = 0.45

    # --------------------------------------------------------

    def __init__(self):

        self.retriever = SecureRetriever()

        self.verifier = ChunkVerifier()

    # --------------------------------------------------------

    def verify_query(

        self,

        query: str,

        top_k: int = 5,

        include_suspicious: bool = False

    ) -> FirewallResult:

        retrieval_results = self.retriever.retrieve(

            query,

            top_k=top_k

        )

        result = FirewallResult(

            query=query

        )

        trusted_context = []

        relevant_results = []

        # ====================================================
        # Stage 1: Relevance Gate
        # ====================================================

        for retrieval in retrieval_results:

            score = float(
                retrieval.get("score", 0.0)
            )

            if score >= self.RELEVANCE_THRESHOLD:

                relevant_results.append(retrieval)

        # ====================================================
        # Stage 2: Fingerprint Verification
        # ====================================================

        for retrieval in relevant_results:

            chunk = retrieval["chunk"]

            report = self.verifier.verify(chunk)

            result.verification_reports.append(report)

            # -----------------------------------------------
            # Trusted
            # -----------------------------------------------

            if report.decision == "TRUSTED":

                result.trusted_chunks.append(chunk)

                trusted_context.append(chunk.text)

            # -----------------------------------------------
            # Suspicious
            # -----------------------------------------------

            elif report.decision == "SUSPICIOUS":

                result.suspicious_chunks.append(chunk)

                if include_suspicious:

                    trusted_context.append(chunk.text)

            # -----------------------------------------------
            # Blocked
            # -----------------------------------------------

            else:

                result.blocked_chunks.append(chunk)

        # ====================================================
        # Context
        # ====================================================

        result.context = "\n\n".join(
            trusted_context
        )

        # ====================================================
        # Statistics
        # ====================================================

        result.statistics = {

            "retrieved": len(retrieval_results),

            "relevant": len(relevant_results),

            "trusted": len(result.trusted_chunks),

            "suspicious": len(result.suspicious_chunks),

            "blocked": len(result.blocked_chunks),

        }

        return result


# ============================================================
# Test
# ============================================================

if __name__ == "__main__":

    firewall = KnowledgeFirewall()

    result = firewall.verify_query(

        "Does VPN require authentication?",

        top_k=5

    )

    print()

    print("=" * 70)

    print("KNOWLEDGE FIREWALL REPORT")

    print("=" * 70)

    print(result.statistics)

    print()

    for report in result.verification_reports:

        print(report)

    print()

    print("=" * 70)

    print("TRUSTED CONTEXT")

    print("=" * 70)

    print(result.context)

    print("=" * 70)