"""
admission_trust_engine.py

Knowledge Firewall AI

Computes document trust during the Knowledge
Admission process.
"""

from __future__ import annotations

from src.core.security.models import AdmissionTrustResult


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

        repository_result,
        attack_result,
        sensitive_result,

    ) -> AdmissionTrustResult:

        repository_similarity = repository_result.similarity
        attack_confidence = attack_result.confidence
        sensitive_risk = sensitive_result.risk_score

        repository_similarity = max(0.0, min(repository_similarity, 1.0))
        attack_confidence = max(0.0, min(attack_confidence, 1.0))
        sensitive_risk = max(0.0, min(sensitive_risk, 1.0))

        # Repository similarity is not automatically malicious.
        # Risk is applied only when similarity approaches
        # duplicate / re-poisoning levels.

        # -----------------------------------------------------
        # Repository Trust
        #
        # Enterprise policies naturally have high semantic
        # similarity. Penalize only documents that are
        # extremely similar but not exact duplicates.
        # -----------------------------------------------------

        if repository_result.duplicate:

            repository_score = 0.0

        elif repository_similarity >= 0.99:

            repository_score = 20.0

        elif repository_similarity >= 0.97:

            repository_score = 80.0

        else:

            repository_score = 100.0


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

        # ------------------------------------
        # Enterprise Decision Policy
        # ------------------------------------

        # -----------------------------------------------------
        # Decision
        # -----------------------------------------------------

        # Hard rejects
        if repository_result.duplicate:

            decision = "REJECT"

        elif attack_confidence >= 0.90:

            decision = "REJECT"

        elif sensitive_risk >= 0.80:

            decision = "REJECT"

        # Trust-based decision
        elif trust >= self.ACCEPT_THRESHOLD:

            decision = "ACCEPT"

        elif trust >= self.REVIEW_THRESHOLD:

            decision = "REVIEW"

        else:

            decision = "REJECT"

        return AdmissionTrustResult(

            repository_score=round(
                repository_score,
                2
            ),

            attack_score=round(
                attack_score,
                2
            ),

            sensitive_score=round(
                sensitive_score,
                2
            ),

            trust_score=trust,

            decision=decision,

        )