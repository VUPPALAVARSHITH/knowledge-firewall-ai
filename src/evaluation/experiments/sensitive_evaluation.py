"""
sensitive_evaluation.py

Layer-1 evaluation for sensitive information detection.
"""

from __future__ import annotations

from src.core.security.sensitive_detector import SensitiveDetector
from src.evaluation.metrics import BinaryMetrics
from src.evaluation.models import BinaryEvaluationResult


class SensitiveEvaluation:

    def __init__(self):

        self.detector = SensitiveDetector()

    # --------------------------------------------------

    def cases(self):

        return [

            # ------------------------------------------
            # CLEAN / NEGATIVE
            # ------------------------------------------

            (
                "SEN-CLEAN-001",
                "Employees must follow the corporate security policy.",
                False,
            ),

            (
                "SEN-CLEAN-002",
                "Passwords must be changed according to company policy.",
                False,
            ),

            (
                "SEN-CLEAN-003",
                "The system supports version 12 of the application.",
                False,
            ),

            (
                "SEN-CLEAN-004",
                "Network access must follow approved procedures.",
                False,
            ),

            (
                "SEN-CLEAN-005",
                "Customer records must remain confidential.",
                False,
            ),

            (
                "SEN-CLEAN-006",
                "The security team performs annual reviews.",
                False,
            ),

            # ------------------------------------------
            # SENSITIVE / POSITIVE
            # ------------------------------------------

            (
                "SEN-EMAIL-001",
                "Contact admin@example.com for access.",
                True,
            ),

            (
                "SEN-IP-001",
                "Internal server address is 192.168.10.25.",
                True,
            ),

            (
                "SEN-AWS-001",
                "AWS key: AKIAIOSFODNN7EXAMPLE",
                True,
            ),

            (
                "SEN-BEARER-001",
                "Authorization: Bearer abc123XYZ",
                True,
            ),

            (
                "SEN-SSN-001",
                "Employee SSN: 123-45-6789",
                True,
            ),

            (
                "SEN-PASSWORD-001",
                "Password = Admin@123",
                True,
            ),

            (
                "SEN-CARD-001",
                "Credit Card: 4111 1111 1111 1111",
                True,
            ),

            (
                "SEN-KEY-001",
                "-----BEGIN PRIVATE KEY-----",
                True,
            ),

            (
                "SEN-URL-001",
                "Internal documentation: https://internal.example.com/admin",
                True,
            ),
        ]

    # --------------------------------------------------

    def run(self):

        metrics = BinaryMetrics()

        results = []

        for case_id, text, expected in self.cases():

            report = self.detector.analyze(text)

            predicted = report.total_findings > 0

            metrics.update(
                expected,
                predicted,
            )

            results.append(

                BinaryEvaluationResult(
                    experiment="sensitive_detection",
                    case_id=case_id,
                    expected=expected,
                    predicted=predicted,
                    correct=(expected == predicted),
                    details={
                        "text": text,
                        "total_findings": report.total_findings,
                        "risk_score": report.risk_score,
                        "recommendation": report.recommendation,
                    },
                )

            )

        metrics.compute()

        return {
            "experiment": "sensitive_detection",
            "metrics": metrics.to_dict(),
            "results": [
                result.to_dict()
                for result in results
            ],
        }