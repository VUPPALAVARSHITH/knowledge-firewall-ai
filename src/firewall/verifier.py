"""
verifier.py

Knowledge Firewall AI

Verifies retrieved semantic chunks against the
trusted fingerprint database.

Pipeline

Retrieved Chunk
      │
      ▼
Runtime Fingerprint
      │
      ▼
Trusted Fingerprint
      │
      ▼
Similarity Engine
      │
      ▼
Trust Engine
      │
      ▼
Verification Result
"""

from __future__ import annotations

from dataclasses import dataclass

from src.firewall.runtime_fingerprint import RuntimeFingerprintGenerator
from src.firewall.similarity import SimilarityEngine
from src.firewall.trust_engine import TrustEngine
from src.fingerprint.fingerprint_database import FingerprintDatabase


# ==========================================================
# Verification Result
# ==========================================================

@dataclass(slots=True)
class VerificationResult:

    policy_id: str

    chunk_id: str

    section: str

    sha_similarity: float

    simhash_similarity: float

    embedding_similarity: float

    trust_score: float

    decision: str

    reason: str


# ==========================================================
# Verifier
# ==========================================================

class ChunkVerifier:

    """
    Runtime integrity verifier.

    Generates a fresh fingerprint from the retrieved
    chunk and compares it against the trusted database.
    """

    def __init__(self):

        self.database = FingerprintDatabase()

        self.database.load()

        self.runtime = RuntimeFingerprintGenerator()

        self.similarity = SimilarityEngine()

        self.trust = TrustEngine()

    # ------------------------------------------------------

    def verify(self, chunk):

        # -----------------------------------------------
        # Trusted fingerprint
        # -----------------------------------------------

        trusted = self.database.get(chunk.chunk_id)

        if trusted is None:

            return VerificationResult(

                policy_id=chunk.policy_id,

                chunk_id=chunk.chunk_id,

                section=chunk.section,

                sha_similarity=0.0,

                simhash_similarity=0.0,

                embedding_similarity=0.0,

                trust_score=0.0,

                decision="BLOCKED",

                reason="Trusted fingerprint not found."

            )

        # -----------------------------------------------
        # Runtime fingerprint
        # -----------------------------------------------

        runtime = self.runtime.generate(chunk)

        # -----------------------------------------------
        # Similarities
        # -----------------------------------------------

        sha_score = self.similarity.sha_similarity(

            trusted.sha256,

            runtime.sha256

        )

        simhash_score = self.similarity.simhash_similarity(

            trusted.simhash,

            runtime.simhash

        )

        embedding_score = self.similarity.cosine_similarity(

            trusted.embedding,

            runtime.embedding

        )

        # -----------------------------------------------
        # Trust
        # -----------------------------------------------

        trust = self.trust.compute(

            sha_score,

            simhash_score,

            embedding_score,

            chunk.priority

        )

        # -----------------------------------------------
        # Explanation
        # -----------------------------------------------

        reasons = []

        if sha_score < 1.0:
            reasons.append("SHA256 mismatch")

        if simhash_score < 0.90:
            reasons.append("SimHash deviation")

        if embedding_score < 0.90:
            reasons.append("Semantic deviation")

        if not reasons:
            reasons.append(
                "Runtime fingerprint matches trusted fingerprint."
            )

        # -----------------------------------------------

        return VerificationResult(

            policy_id=chunk.policy_id,

            chunk_id=chunk.chunk_id,

            section=chunk.section,

            sha_similarity=round(sha_score, 4),

            simhash_similarity=round(simhash_score, 4),

            embedding_similarity=round(embedding_score, 4),

            trust_score=trust.trust_score,

            decision=trust.decision,

            reason=", ".join(reasons)

        )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    from src.vectorstore.vector_store import EnterpriseVectorStore
    from src.vectorstore.query_encoder import QueryEncoder

    store = EnterpriseVectorStore()

    store.load()

    encoder = QueryEncoder()

    query = encoder.encode(

        "Does VPN require authentication?"

    )

    result = store.search(

        query,

        top_k=1

    )[0]

    verifier = ChunkVerifier()

    report = verifier.verify(

        result["chunk"]

    )

    print()

    print("=" * 70)

    print("VERIFICATION REPORT")

    print("=" * 70)

    print(report)

    print("=" * 70)