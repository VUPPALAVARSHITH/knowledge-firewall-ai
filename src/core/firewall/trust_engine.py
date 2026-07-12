"""
trust_engine.py

Knowledge Firewall AI

Computes trust scores from similarity metrics.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class TrustResult:

    sha_score: float

    simhash_score: float

    embedding_score: float

    section_priority: float

    trust_score: float

    decision: str


class TrustEngine:

    """
    Computes weighted trust scores.

    Weights:

    SHA256      : 40%
    SimHash     : 25%
    Embedding   : 30%
    Priority    : 5%
    """

    SHA_WEIGHT = 0.40

    SIMHASH_WEIGHT = 0.25

    EMBEDDING_WEIGHT = 0.30

    PRIORITY_WEIGHT = 0.05

    # ----------------------------------------------------

    TRUST_THRESHOLD = 0.90

    SUSPICIOUS_THRESHOLD = 0.70

    # ----------------------------------------------------

    def compute(

        self,

        sha_score: float,

        simhash_score: float,

        embedding_score: float,

        section_priority: float

    ) -> TrustResult:

        trust = (

            sha_score * self.SHA_WEIGHT +

            simhash_score * self.SIMHASH_WEIGHT +

            embedding_score * self.EMBEDDING_WEIGHT +

            section_priority * self.PRIORITY_WEIGHT

        )

        trust = round(trust, 4)

        if trust >= self.TRUST_THRESHOLD:

            decision = "TRUSTED"

        elif trust >= self.SUSPICIOUS_THRESHOLD:

            decision = "SUSPICIOUS"

        else:

            decision = "BLOCKED"

        return TrustResult(

            sha_score=round(sha_score, 4),

            simhash_score=round(simhash_score, 4),

            embedding_score=round(embedding_score, 4),

            section_priority=section_priority,

            trust_score=trust,

            decision=decision

        )


# ----------------------------------------------------------

if __name__ == "__main__":

    engine = TrustEngine()

    result = engine.compute(

        sha_score=1.0,

        simhash_score=0.95,

        embedding_score=0.91,

        section_priority=1.0

    )

    print(result)