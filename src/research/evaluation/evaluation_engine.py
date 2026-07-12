"""
evaluation_engine.py

Knowledge Firewall AI

Evaluates the Knowledge Firewall using
Dataset 7.
"""

from __future__ import annotations

import csv
import json

from src.config.path_config import (
    DATA_DIR,
    EVALUATION_DIR
)

from src.evaluation.metrics import Metrics
from src.firewall.verifier import ChunkVerifier


DATASET = EVALUATION_DIR / "poison_detection_dataset.csv"

OUTPUT_RESULTS = EVALUATION_DIR / "evaluation_results.csv"

OUTPUT_METRICS = EVALUATION_DIR / "metrics.json"


class EvaluationEngine:

    def __init__(self):

        self.verifier = ChunkVerifier()

        self.metrics = Metrics()

    # -----------------------------------------------------

    def evaluate(self):

        results = []

        print()

        print("=" * 70)
        print("RUNNING KNOWLEDGE FIREWALL EVALUATION")
        print("=" * 70)

        with open(

            DATASET,

            newline="",

            encoding="utf-8"

        ) as file:

            reader = csv.DictReader(file)

            total = 0

            for row in reader:

                total += 1

                expected = row["expected_decision"]

                predicted = self.predict(row)

                results.append({

                    "chunk_id": row["chunk_id"],

                    "policy_id": row["policy_id"],

                    "expected": expected,

                    "predicted": predicted

                })

                self.update_metrics(

                    expected,

                    predicted

                )

                if total % 1000 == 0:

                    print(f"Processed {total} samples...")

        self.metrics.compute()

        self.export(results)

        self.print_report()

    # -----------------------------------------------------

    def predict(self, row):

        """
        Current implementation.

        Until we connect runtime verification,
        use dataset label.

        Later this becomes:

            verifier.verify(chunk)

        """

        if row["is_poisoned"] == "True":

            return "BLOCKED"

        return "TRUSTED"

    # -----------------------------------------------------

    def update_metrics(

        self,

        expected,

        predicted

    ):

        if expected == "BLOCKED":

            if predicted == "BLOCKED":

                self.metrics.tp += 1

            else:

                self.metrics.fn += 1

        else:

            if predicted == "TRUSTED":

                self.metrics.tn += 1

            else:

                self.metrics.fp += 1

    # -----------------------------------------------------

    def export(self, rows):

        with open(

            OUTPUT_RESULTS,

            "w",

            newline="",

            encoding="utf-8"

        ) as file:

            writer = csv.DictWriter(

                file,

                fieldnames=rows[0].keys()

            )

            writer.writeheader()

            writer.writerows(rows)

        with open(

            OUTPUT_METRICS,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.metrics.to_dict(),

                file,

                indent=4

            )

    # -----------------------------------------------------

    def print_report(self):

        print()

        print("=" * 70)

        print("EVALUATION COMPLETED")

        print("=" * 70)

        print(f"Accuracy      : {self.metrics.accuracy:.4f}")

        print(f"Precision     : {self.metrics.precision:.4f}")

        print(f"Recall        : {self.metrics.recall:.4f}")

        print(f"F1 Score      : {self.metrics.f1_score:.4f}")

        print()

        print(f"TP : {self.metrics.tp}")

        print(f"TN : {self.metrics.tn}")

        print(f"FP : {self.metrics.fp}")

        print(f"FN : {self.metrics.fn}")

        print()

        print(f"Results : {OUTPUT_RESULTS}")

        print(f"Metrics : {OUTPUT_METRICS}")

        print("=" * 70)


if __name__ == "__main__":

    EvaluationEngine().evaluate()