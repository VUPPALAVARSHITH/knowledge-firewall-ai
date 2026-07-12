"""
evaluation_dataset_builder.py

Knowledge Firewall AI

Builds Dataset 7:
Poison Detection Evaluation Dataset
"""

from __future__ import annotations

import csv
import pickle

from dataclasses import asdict

from src.config.path_config import (
    DATA_DIR,
    METADATA_DIR
)

from src.evaluation.models import EvaluationRecord


CLEAN_DATASET = DATA_DIR / "vector_store" / "chunk_metadata.pkl"

POISONED_DATASET = DATA_DIR / "poisoned_vector_store" / "chunk_metadata.pkl"

ATTACK_LOG = METADATA_DIR / "attack_log.csv"

OUTPUT_DIR = DATA_DIR / "evaluation"

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


class EvaluationDatasetBuilder:

    def load_chunks(self, path):

        with open(path, "rb") as file:

            return pickle.load(file)

    # --------------------------------------------------

    def load_attack_log(self):

        attacks = {}

        with open(
            ATTACK_LOG,
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                attacks[row["policy_id"]] = row

        return attacks

    # --------------------------------------------------

    def build(self):

        clean_chunks = self.load_chunks(CLEAN_DATASET)

        poisoned_chunks = self.load_chunks(POISONED_DATASET)

        attacks = self.load_attack_log()

        dataset = []

        # -----------------------------

        for chunk in clean_chunks:

            dataset.append(

                EvaluationRecord(

                    chunk_id=chunk.chunk_id,

                    policy_id=chunk.policy_id,

                    department=chunk.department,

                    category=chunk.category,

                    section=chunk.section,

                    is_poisoned=False,

                    attack_type="None",

                    severity="None",

                    expected_decision="TRUSTED",

                    source_file=chunk.source_file

                )

            )

        # -----------------------------

        for chunk in poisoned_chunks:

            attack = attacks.get(chunk.policy_id, {})

            dataset.append(

                EvaluationRecord(

                    chunk_id=chunk.chunk_id,

                    policy_id=chunk.policy_id,

                    department=chunk.department,

                    category=chunk.category,

                    section=chunk.section,

                    is_poisoned=True,

                    attack_type=attack.get("attack_type", "Unknown"),

                    severity=attack.get("severity", "Unknown"),

                    expected_decision="BLOCKED",

                    source_file=chunk.source_file

                )

            )

        self.export(dataset)

    # --------------------------------------------------

    def export(self, dataset):

        csv_file = OUTPUT_DIR / "poison_detection_dataset.csv"

        with open(
            csv_file,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=asdict(dataset[0]).keys()
            )

            writer.writeheader()

            for row in dataset:

                writer.writerow(asdict(row))

        print()

        print("=" * 70)

        print("DATASET 7 GENERATED")

        print("=" * 70)

        print(f"Samples : {len(dataset)}")

        print(f"Output  : {csv_file}")

        print("=" * 70)


if __name__ == "__main__":

    EvaluationDatasetBuilder().build()