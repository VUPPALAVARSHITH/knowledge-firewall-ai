"""
Metadata Generator

Creates metadata for every enterprise document.
"""

import hashlib
import csv
from pathlib import Path

from src.config.path_config import (
    ENTERPRISE_DIR,
    METADATA_DIR
)


class MetadataGenerator:

    def sha256(self, filepath):

        with open(filepath, "rb") as file:
            return hashlib.sha256(
                file.read()
            ).hexdigest()

    def generate(self):

        rows = []

        for txt_file in ENTERPRISE_DIR.rglob("*.txt"):

            category = txt_file.parent.name

            department = txt_file.parent.parent.name

            policy_id = txt_file.stem

            rows.append({

                "policy_id": policy_id,

                "department": department,

                "category": category,

                "filepath": str(txt_file),

                "sha256": self.sha256(txt_file)

            })

        METADATA_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        output = METADATA_DIR / "policy_index.csv"

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
                    "filepath",
                    "sha256"
                ]
            )

            writer.writeheader()

            writer.writerows(rows)

        print()

        print("=" * 50)

        print("Metadata Generated")

        print("Documents :", len(rows))

        print("Saved To :", output)

        print("=" * 50)


if __name__ == "__main__":

    MetadataGenerator().generate()