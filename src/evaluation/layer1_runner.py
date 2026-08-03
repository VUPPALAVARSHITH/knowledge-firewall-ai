"""
benchmark_runner.py

Knowledge Firewall AI

Runs Layer-1 component evaluation.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from src.evaluation.experiments.attack_evaluation import (
    AttackEvaluation,
)

from src.evaluation.experiments.sensitive_evaluation import (
    SensitiveEvaluation,
)

from src.evaluation.experiments.similarity_evaluation import (
    SimilarityEvaluation,
)

from src.evaluation.experiments.admission_evaluation import (
    AdmissionEvaluation,
)


RESULT_DIR = Path(
    "src/evaluation/results"
)

RESULT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


class BenchmarkRunner:

    def __init__(self):

        self.experiments = [

            AttackEvaluation(),

            SensitiveEvaluation(),

            SimilarityEvaluation(),

            AdmissionEvaluation(),

        ]

    # --------------------------------------------------

    @staticmethod
    def print_binary(name, metrics):

        print()
        print("-" * 60)
        print(name.upper())
        print("-" * 60)

        print(f"Samples       : {metrics['tp'] + metrics['tn'] + metrics['fp'] + metrics['fn']}")
        print(f"TP            : {metrics['tp']}")
        print(f"TN            : {metrics['tn']}")
        print(f"FP            : {metrics['fp']}")
        print(f"FN            : {metrics['fn']}")

        print()

        print(f"Accuracy      : {metrics['accuracy']:.4f}")
        print(f"Precision     : {metrics['precision']:.4f}")
        print(f"Recall        : {metrics['recall']:.4f}")
        print(f"F1 Score      : {metrics['f1_score']:.4f}")
        print(f"False + Rate  : {metrics['false_positive_rate']:.4f}")
        print(f"False - Rate  : {metrics['false_negative_rate']:.4f}")

    # --------------------------------------------------

    @staticmethod
    def print_admission(metrics):

        print()
        print("-" * 60)
        print("ADMISSION DECISION")
        print("-" * 60)

        print(f"Samples       : {metrics['total']}")
        print(f"Correct       : {metrics['correct']}")
        print(f"Incorrect     : {metrics['incorrect']}")
        print(f"Accuracy      : {metrics['accuracy']:.4f}")

    # --------------------------------------------------

    def run(self):

        print()
        print("=" * 60)
        print("KNOWLEDGE FIREWALL AI")
        print("LAYER-1 COMPONENT EVALUATION")
        print("=" * 60)

        output = {
            "evaluation_layer": 1,
            "generated_at": datetime.now().isoformat(),
            "experiments": {},
        }

        for experiment in self.experiments:

            result = experiment.run()

            name = result["experiment"]

            output["experiments"][name] = result

            if name == "admission_decision":

                self.print_admission(
                    result["metrics"]
                )

            else:

                self.print_binary(
                    name,
                    result["metrics"],
                )

        # --------------------------------------------------
        # Export JSON
        # --------------------------------------------------

        output_file = (
            RESULT_DIR
            / "layer1_results.json"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                output,
                file,
                indent=4,
            )

        # --------------------------------------------------

        print()
        print("=" * 60)
        print("LAYER-1 EVALUATION COMPLETED")
        print("=" * 60)
        print(f"Results: {output_file}")
        print("=" * 60)

        return output


if __name__ == "__main__":

    BenchmarkRunner().run()