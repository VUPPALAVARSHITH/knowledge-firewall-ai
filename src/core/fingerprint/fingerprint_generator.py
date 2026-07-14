"""
fingerprint_generator.py

Knowledge Firewall AI

Generates fingerprint database for all enterprise
knowledge documents.
"""

import csv

from src.config.path_config import (
    ENTERPRISE_DIR,
    METADATA_DIR
)

from src.core.fingerprint.fingerprint_engine import (
    FingerprintEngine
)


class FingerprintGenerator:

    def __init__(self):

        self.engine = FingerprintEngine()

    def generate(self):

        rows = []

        total = 0

        for file in ENTERPRISE_DIR.rglob("*.txt"):

            total += 1

            category = file.parent.name

            department = file.parent.parent.name

            policy_id = file.stem

            fingerprint = self.engine.generate(

                filepath=file,

                department=department,

                category=category,

                policy_id=policy_id

            )

            rows.append(fingerprint)

            print(f"[{total}] {policy_id}")

        METADATA_DIR.mkdir(

            parents=True,

            exist_ok=True

        )

        output = METADATA_DIR / "fingerprint_database.csv"

        with open(

            output,

            "w",

            newline="",

            encoding="utf-8"

        ) as csvfile:

            writer = csv.DictWriter(

                csvfile,

                fieldnames=[
                    "policy_id",
                    "department",
                    "category",
                    "title",
                    "sha256",
                    "simhash",
                    "embedding",
                    "embedding_model",
                    "word_count",
                    "policy_statement_words",
                    "character_count",
                    "character_count",
                    "sentence_count",
                    "file_size",
                    "trust_score",
                    "document_version",
                    "fingerprint_version",
                    "created_at"
                ]

            )

            writer.writeheader()

            writer.writerows(rows)

        print()

        print("=" * 60)

        print("Fingerprint Database Generated")

        print("=" * 60)

        print("Documents :", total)

        print("Output    :", output)

        print("=" * 60)


if __name__ == "__main__":

    FingerprintGenerator().generate()