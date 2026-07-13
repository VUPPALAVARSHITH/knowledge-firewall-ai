"""
admission_trust_engine.py

Knowledge Firewall AI

Computes document trust during the Knowledge
Admission process.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class AdmissionTrustResult:

    repository_score: float

    attack_score: float

    sensitive_score: float

    trust_score: float

    decision: str


class AdmissionTrustEngine:

    """
    Computes admission trust.

    Repository Similarity : 40%
    Attack Analysis       : 40%
    Sensitive Data        : 20%
    """

    REPOSITORY_WEIGHT = 0.40

    ATTACK_WEIGHT = 0.40

    SENSITIVE_WEIGHT = 0.20

    ACCEPT_THRESHOLD = 90

    REVIEW_THRESHOLD = 70

    # -----------------------------------------------------

    def compute(

        self,

        repository_similarity: float,

        attack_confidence: float,

        sensitive_risk: float,

    ) -> AdmissionTrustResult:

        repository_score = (
            1.0 - repository_similarity
        ) * 100

        attack_score = (
            1.0 - attack_confidence
        ) * 100

        sensitive_score = (
            1.0 - sensitive_risk
        ) * 100

        trust = (

            repository_score * self.REPOSITORY_WEIGHT +

            attack_score * self.ATTACK_WEIGHT +

            sensitive_score * self.SENSITIVE_WEIGHT

        )

        trust = round(trust, 2)

        if trust >= self.ACCEPT_THRESHOLD:

            decision = "ACCEPT"

        elif trust >= self.REVIEW_THRESHOLD:

            decision = "REVIEW"

        else:

            decision = "REJECT"

        return AdmissionTrustResult(

            repository_score=round(repository_score, 2),

            attack_score=round(attack_score, 2),

            sensitive_score=round(sensitive_score, 2),

            trust_score=trust,

            decision=decision,

        )