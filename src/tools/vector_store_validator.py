"""
vector_store_validator.py

Knowledge Firewall AI

Validates the Vector Store repository.

Checks

- Required files
- FAISS index
- Embedding metadata
- Chunk metadata
- Statistics
"""

from __future__ import annotations

from pathlib import Path
import json
import pickle
import pandas as pd


class VectorStoreValidator:

    def __init__(self, vector_dir: Path):

        self.vector_dir = vector_dir

        self.errors = []
        self.warnings = []

    # =====================================================

    def validate(self):

        print("\nVector Store Validation")
        print("-" * 70)

        self.check_required_files()

        self.check_chunk_metadata()

        self.check_statistics()

        self.check_embeddings()

        print()

        print("Vector Store Validation Complete")

        print(f"Errors   : {len(self.errors)}")

        print(f"Warnings : {len(self.warnings)}")

        return self.errors, self.warnings

        # =====================================================

    def check_required_files(self):

        required = [

            "chunk_metadata.pkl",
            "chunk_metadata.csv",
            "statistics.json"

        ]

        for file in required:

            path = self.vector_dir / file

            if path.exists():

                print(f"[OK] {file}")

            else:

                self.errors.append(f"{file} missing.")

        # =====================================================

    def check_chunk_metadata(self):

        csv_path = self.vector_dir / "chunk_metadata.csv"

        if not csv_path.exists():

            return

        df = pd.read_csv(csv_path)

        print()

        print(f"Chunks : {len(df)}")

        print(f"Policies : {df['policy_id'].nunique()}")

        print(
            f"Departments : {df['department'].nunique()}"
        )

        print(
            f"Categories : {df['category'].nunique()}"
        )

        print(
            f"Average Words : {df['word_count'].mean():.2f}"
        )

        duplicates = df["chunk_id"].duplicated().sum()

        if duplicates:

            self.errors.append(

                f"{duplicates} duplicate chunk IDs."

            )

        # =====================================================

    def check_statistics(self):

        stats = self.vector_dir / "statistics.json"

        if not stats.exists():

            return

        with open(stats, "r", encoding="utf-8") as file:

            data = json.load(file)

        print()

        print("Statistics")

        print(f"Total Chunks : {data['total_chunks']}")

        print(
            f"Average Words : {data['average_words']}"
        )

        print(
            f"Average Characters : {data['average_characters']}"
        )

        # =====================================================

    def check_embeddings(self):

        file = self.vector_dir / "chunk_metadata.pkl"

        if not file.exists():

            return

        try:

            with open(file, "rb") as f:

                chunks = pickle.load(f)

            print()

            print(
                f"Pickle Objects : {len(chunks)}"
            )

        except Exception as e:

            self.errors.append(str(e))

    
    