"""
metadata_generator.py

Knowledge Firewall AI

Generates metadata for every enterprise document.

Outputs:

1. policy_index.csv
2. document_relations.csv
3. generation_log.csv
"""

from pathlib import Path
from datetime import datetime
import csv

from src.config.path_config import (
    ENTERPRISE_DIR,
    METADATA_DIR
)

from src.utils.metadata_utils import parse_document


class MetadataGenerator:

    def __init__(self):

        self.documents = []

    # ----------------------------------------------------
    # Load Enterprise Documents
    # ----------------------------------------------------

    def load_documents(self):

        print("\nScanning Enterprise Dataset...\n")

        for file in ENTERPRISE_DIR.rglob("*.txt"):

            metadata = parse_document(file)

            self.documents.append(metadata)

        print(f"Loaded {len(self.documents)} documents.")

    # ----------------------------------------------------
    # Policy Index
    # ----------------------------------------------------

    def generate_policy_index(self):

        output = METADATA_DIR / "policy_index.csv"

        fields = [

            "policy_id",
            "title",
            "department",
            "category",
            "security_domain",
            "classification",
            "risk_level",
            "owner",
            "effective_date",
            "review_date",
            "word_count",
            "char_count",
            "sha256",
            "filepath",
            "keywords"

        ]

        with open(

            output,

            "w",

            newline="",

            encoding="utf-8"

        ) as csvfile:

            writer = csv.DictWriter(

                csvfile,

                fieldnames=fields

            )

            writer.writeheader()

            for doc in self.documents:

                row = doc.copy()

                row["keywords"] = ", ".join(doc["keywords"])

                writer.writerow(row)

        print("✓ policy_index.csv generated")

    # ----------------------------------------------------
    # Document Relations
    # ----------------------------------------------------

    def generate_document_relations(self):

        output = METADATA_DIR / "document_relations.csv"

        with open(

            output,

            "w",

            newline="",

            encoding="utf-8"

        ) as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(

                [

                    "source_policy",

                    "target_policy",

                    "relation"

                ]

            )

            docs = self.documents

            for i in range(len(docs)):

                for j in range(i + 1, len(docs)):

                    a = docs[i]

                    b = docs[j]

                    if a["department"] == b["department"]:

                        writer.writerow([

                            a["policy_id"],

                            b["policy_id"],

                            "shared_department"

                        ])

                    elif a["category"] == b["category"]:

                        writer.writerow([

                            a["policy_id"],

                            b["policy_id"],

                            "shared_category"

                        ])

                    elif len(

                        set(a["keywords"]) &

                        set(b["keywords"])

                    ) > 0:

                        writer.writerow([

                            a["policy_id"],

                            b["policy_id"],

                            "shared_keyword"

                        ])

        print("✓ document_relations.csv generated")

    # ----------------------------------------------------
    # Generation Log
    # ----------------------------------------------------

    def generate_log(self):

        output = METADATA_DIR / "generation_log.csv"

        exists = output.exists()

        with open(

            output,

            "a",

            newline="",

            encoding="utf-8"

        ) as csvfile:

            writer = csv.writer(csvfile)

            if not exists:

                writer.writerow(

                    [

                        "timestamp",

                        "documents",

                        "generator",

                        "version"

                    ]

                )

            writer.writerow(

                [

                    datetime.now().strftime(

                        "%Y-%m-%d %H:%M:%S"

                    ),

                    len(self.documents),

                    "MetadataGenerator",

                    "1.0"

                ]

            )

        print("✓ generation_log.csv updated")

    # ----------------------------------------------------
    # Generate Everything
    # ----------------------------------------------------

    def generate(self):

        METADATA_DIR.mkdir(

            parents=True,

            exist_ok=True

        )

        self.load_documents()

        self.generate_policy_index()

        self.generate_document_relations()

        self.generate_log()

        print()

        print("=" * 60)

        print("Metadata Generation Completed")

        print("=" * 60)

        print("Documents :", len(self.documents))

        print("Output :", METADATA_DIR)

        print("=" * 60)

        print()


if __name__ == "__main__":

    MetadataGenerator().generate()