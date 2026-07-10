"""
knowledge_firewall.py

Knowledge Firewall AI

Secure Retrieval Orchestrator.

Pipeline

User Query
    │
    ▼
Retriever
    │
    ▼
Top-K Chunks
    │
    ▼
Verifier
    │
    ▼
Trusted Context
"""

from __future__ import annotations

from dataclasses import dataclass, field

from src.retriever.secure_retriever import SecureRetriever
from src.firewall.verifier import ChunkVerifier, VerificationResult


# ============================================================
# Firewall Result
# ============================================================

@dataclass(slots=True)
class FirewallResult:

    query: str

    trusted_chunks: list = field(default_factory=list)

    suspicious_chunks: list = field(default_factory=list)

    blocked_chunks: list = field(default_factory=list)

    verification_reports: list[VerificationResult] = field(default_factory=list)

    context: str = ""

    statistics: dict = field(default_factory=dict)


# ============================================================
# Knowledge Firewall
# ============================================================

class KnowledgeFirewall:

    """
    Secure retrieval layer.

    Retrieves semantic chunks,
    verifies them,
    removes poisoned chunks,
    builds trusted context.
    """

    def __init__(self):

        self.retriever = SecureRetriever()

        self.verifier = ChunkVerifier()

    # ------------------------------------------------------

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

        # --------------------------------------------------

        for retrieval in retrieval_results:

            chunk = retrieval["chunk"]

            report = self.verifier.verify(chunk)

            result.verification_reports.append(report)

            if report.decision == "TRUSTED":

                result.trusted_chunks.append(chunk)

                trusted_context.append(chunk.text)

            elif report.decision == "SUSPICIOUS":

                result.suspicious_chunks.append(chunk)

                if include_suspicious:

                    trusted_context.append(chunk.text)

            else:

                result.blocked_chunks.append(chunk)

        # --------------------------------------------------

        result.context = "\n\n".join(trusted_context)

        result.statistics = {

            "retrieved": len(retrieval_results),

            "trusted": len(result.trusted_chunks),

            "suspicious": len(result.suspicious_chunks),

            "blocked": len(result.blocked_chunks)

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