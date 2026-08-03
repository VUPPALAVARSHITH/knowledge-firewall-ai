"""
admission_evaluation.py

Layer-1 evaluation for final admission trust decisions.
"""

from __future__ import annotations

from src.core.security.admission_trust_engine import AdmissionTrustEngine

from src.core.security.models import (
    RepositoryCheckResult,
    AttackResult,
    SensitiveDataResult,
)

from src.evaluation.models import AdmissionEvaluationResult


class AdmissionEvaluation:

    def __init__(self):

        self.engine = AdmissionTrustEngine()

    # --------------------------------------------------

    @staticmethod
    def repository(
        similarity=0.0,
        duplicate=False,
    ):

        return RepositoryCheckResult(
            duplicate=duplicate,
            similarity=similarity,
            matched_policy=None,
            recommendation=(
                "Reject Upload"
                if duplicate
                else "Accept"
            ),
            reason="Evaluation case",
        )

    # --------------------------------------------------

    @staticmethod
    def attack(
        detected=False,
        confidence=0.0,
    ):

        return AttackResult(
            attack_id=(
                "EVAL-ATTACK"
                if detected
                else None
            ),
            category=(
                "Evaluation"
                if detected
                else None
            ),
            severity=(
                "High"
                if detected
                else "None"
            ),
            confidence=confidence,
            matched_text="",
            recommendation=(
                "Reject Upload"
                if detected
                else "Accept"
            ),
            is_attack=detected,
        )

    # --------------------------------------------------

    @staticmethod
    def sensitive(
        risk=0.0,
    ):

        return SensitiveDataResult(
            total_findings=(
                1
                if risk > 0
                else 0
            ),
            risk_score=risk,
            recommendation=(
                "Reject Upload"
                if risk >= 0.50
                else "Manual Review"
                if risk > 0
                else "Accept"
            ),
        )

    # --------------------------------------------------

    def cases(self):

        return [

            {
                "id": "ADM-CLEAN-001",
                "repository": self.repository(
                    similarity=0.20
                ),
                "attack": self.attack(),
                "sensitive": self.sensitive(),
                "expected": "ACCEPT",
            },

            {
                "id": "ADM-CLEAN-002",
                "repository": self.repository(
                    similarity=0.70
                ),
                "attack": self.attack(),
                "sensitive": self.sensitive(),
                "expected": "ACCEPT",
            },

            {
                "id": "ADM-SIMILAR-001",
                "repository": self.repository(
                    similarity=0.85
                ),
                "attack": self.attack(),
                "sensitive": self.sensitive(),
                "expected": "REVIEW",
            },

            {
                "id": "ADM-DUP-001",
                "repository": self.repository(
                    similarity=1.0,
                    duplicate=True,
                ),
                "attack": self.attack(),
                "sensitive": self.sensitive(),
                "expected": "REJECT",
            },

            {
                "id": "ADM-ATTACK-001",
                "repository": self.repository(
                    similarity=0.20
                ),
                "attack": self.attack(
                    detected=True,
                    confidence=0.95,
                ),
                "sensitive": self.sensitive(),
                "expected": "REJECT",
            },

            {
                "id": "ADM-SENSITIVE-001",
                "repository": self.repository(
                    similarity=0.20
                ),
                "attack": self.attack(),
                "sensitive": self.sensitive(
                    risk=0.60
                ),
                "expected": "REVIEW",
            },

            {
                "id": "ADM-MULTI-RISK-001",
                "repository": self.repository(
                    similarity=0.85
                ),
                "attack": self.attack(
                    detected=True,
                    confidence=0.75,
                ),
                "sensitive": self.sensitive(
                    risk=0.50
                ),
                "expected": "REJECT",
            },
        ]

    # --------------------------------------------------

    def run(self):

        results = []

        correct = 0

        for case in self.cases():

            report = self.engine.compute(
                case["repository"],
                case["attack"],
                case["sensitive"],
            )

            is_correct = (
                report.decision
                == case["expected"]
            )

            if is_correct:
                correct += 1

            results.append(

                AdmissionEvaluationResult(
                    case_id=case["id"],
                    expected=case["expected"],
                    predicted=report.decision,
                    correct=is_correct,
                    trust_score=report.trust_score,
                    details={
                        "repository_score": (
                            report.repository_score
                        ),
                        "attack_score": (
                            report.attack_score
                        ),
                        "sensitive_score": (
                            report.sensitive_score
                        ),
                    },
                )

            )

        total = len(results)

        accuracy = (
            correct / total
            if total
            else 0.0
        )

        return {
            "experiment": "admission_decision",
            "metrics": {
                "total": total,
                "correct": correct,
                "incorrect": total - correct,
                "accuracy": accuracy,
            },
            "results": [
                result.to_dict()
                for result in results
            ],
        }