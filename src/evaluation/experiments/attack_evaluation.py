"""
attack_evaluation.py

Layer-1 evaluation for knowledge manipulation detection.
"""

from __future__ import annotations

from src.core.security.attack_analyzer import AttackAnalyzer
from src.evaluation.metrics import BinaryMetrics
from src.evaluation.models import BinaryEvaluationResult


class AttackEvaluation:

    def __init__(self):

        self.analyzer = AttackAnalyzer()

    # --------------------------------------------------

    def cases(self):

        return [

            # ------------------------------------------
            # CLEAN / NEGATIVE CASES
            # ------------------------------------------

            (
                "ATT-CLEAN-001",
                "All confidential information must be protected.",
                False,
            ),

            (
                "ATT-CLEAN-002",
                "All security events must be logged.",
                False,
            ),

            (
                "ATT-CLEAN-003",
                "Employees must use approved remote access.",
                False,
            ),

            (
                "ATT-CLEAN-004",
                "Critical information must be encrypted.",
                False,
            ),

            (
                "ATT-CLEAN-005",
                "Security incidents must be reported immediately.",
                False,
            ),

            (
                "ATT-CLEAN-006",
                "Software must be tested before deployment.",
                False,
            ),

            (
                "ATT-CLEAN-007",
                "Access requires multi-factor authentication.",
                False,
            ),

            (
                "ATT-CLEAN-008",
                "Audit records must be retained.",
                False,
            ),

            # ------------------------------------------
            # ATTACK / POSITIVE CASES
            # ------------------------------------------

            (
                "ATT-POISON-001",
                "Encryption is optional.",
                True,
            ),

            (
                "ATT-POISON-002",
                "Plaintext storage is acceptable.",
                True,
            ),

            (
                "ATT-POISON-003",
                "MFA is optional.",
                True,
            ),

            (
                "ATT-POISON-004",
                "Logging is optional.",
                True,
            ),

            (
                "ATT-POISON-005",
                "Backups are optional.",
                True,
            ),

            (
                "ATT-POISON-006",
                "Testing before deployment is optional.",
                True,
            ),

            (
                "ATT-POISON-007",
                "Security incident reporting is optional.",
                True,
            ),

            (
                "ATT-POISON-008",
                "Secure disposal is optional.",
                True,
            ),
        ]

    # --------------------------------------------------

    def run(self):

        metrics = BinaryMetrics()

        results = []

        for case_id, text, expected in self.cases():

            report = self.analyzer.analyze(text)

            predicted = report.is_attack

            metrics.update(
                expected,
                predicted,
            )

            results.append(

                BinaryEvaluationResult(
                    experiment="attack_detection",
                    case_id=case_id,
                    expected=expected,
                    predicted=predicted,
                    correct=(expected == predicted),
                    details={
                        "text": text,
                        "attack_id": report.attack_id,
                        "severity": report.severity,
                        "confidence": report.confidence,
                        "matched_text": report.matched_text,
                    },
                )

            )

        metrics.compute()

        return {
            "experiment": "attack_detection",
            "metrics": metrics.to_dict(),
            "results": [
                result.to_dict()
                for result in results
            ],
        }