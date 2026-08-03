"""
similarity_evaluation.py

Layer-1 evaluation for repository similarity logic.
"""

from __future__ import annotations

from src.core.security.repository_checker import RepositoryChecker
from src.evaluation.metrics import BinaryMetrics
from src.evaluation.models import BinaryEvaluationResult


class SimilarityEvaluation:

    DUPLICATE_THRESHOLD = 0.90

    def __init__(self):

        self.checker = RepositoryChecker()

    # --------------------------------------------------

    def cases(self):

        return [

            (
                "SIM-EXACT-001",
                [1.0, 0.0, 0.0],
                [1.0, 0.0, 0.0],
                True,
            ),

            (
                "SIM-EXACT-002",
                [0.0, 1.0, 0.0],
                [0.0, 1.0, 0.0],
                True,
            ),

            (
                "SIM-NEAR-001",
                [1.0, 0.0, 0.0],
                [0.99, 0.10, 0.0],
                True,
            ),

            (
                "SIM-NEAR-002",
                [0.0, 1.0, 0.0],
                [0.10, 0.99, 0.0],
                True,
            ),

            (
                "SIM-DIFF-001",
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                False,
            ),

            (
                "SIM-DIFF-002",
                [0.0, 0.0, 1.0],
                [1.0, 0.0, 0.0],
                False,
            ),

            (
                "SIM-DIFF-003",
                [1.0, 1.0, 0.0],
                [-1.0, -1.0, 0.0],
                False,
            ),
        ]

    # --------------------------------------------------

    def run(self):

        metrics = BinaryMetrics()

        results = []

        for (
            case_id,
            embedding_a,
            embedding_b,
            expected,
        ) in self.cases():

            score = self.checker.cosine_similarity(
                embedding_a,
                embedding_b,
            )

            predicted = (
                score >= self.DUPLICATE_THRESHOLD
            )

            metrics.update(
                expected,
                predicted,
            )

            results.append(

                BinaryEvaluationResult(
                    experiment="similarity",
                    case_id=case_id,
                    expected=expected,
                    predicted=predicted,
                    correct=(expected == predicted),
                    details={
                        "similarity": round(score, 4),
                        "threshold": self.DUPLICATE_THRESHOLD,
                    },
                )

            )

        metrics.compute()

        return {
            "experiment": "similarity",
            "metrics": metrics.to_dict(),
            "results": [
                result.to_dict()
                for result in results
            ],
        }