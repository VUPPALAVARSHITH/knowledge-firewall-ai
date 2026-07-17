"""
fingerprint_database.py

Knowledge Firewall AI

Loads the trusted fingerprint database from CSV
and provides O(1) lookup by chunk_id.
"""

from __future__ import annotations

import ast
from typing import Dict, Optional

import pandas as pd

from src.config.path_config import METADATA_DIR
from src.core.fingerprint.models import ChunkFingerprint


DATABASE_PATH = METADATA_DIR / "chunk_fingerprint_database.csv"


class FingerprintDatabase:
    """
    Trusted fingerprint database.

    Stores fingerprints in memory using:

        chunk_id -> ChunkFingerprint
    """

    def __init__(self):

        self.database: Dict[str, ChunkFingerprint] = {}

        self.loaded = False

    # --------------------------------------------------

    def load(self):

        if self.loaded:
            return

        if not DATABASE_PATH.exists():
            raise FileNotFoundError(
                f"Fingerprint database not found:\n{DATABASE_PATH}"
            )

        df = pd.read_csv(DATABASE_PATH)

        self.database = {}

        for _, row in df.iterrows():

            # ------------------------------------------
            # Parse embedding
            # ------------------------------------------

            embedding = row["embedding"]

            if isinstance(embedding, str):

                try:
                    embedding = ast.literal_eval(embedding)
                except Exception:
                    embedding = []

            # ------------------------------------------
            # Parse boolean safely
            # ------------------------------------------

            poisoned = row["is_poisoned"]

            if isinstance(poisoned, str):
                poisoned = poisoned.strip().lower() == "true"

            fp = ChunkFingerprint(

                chunk_id=str(row["chunk_id"]),

                policy_id=str(row["policy_id"]),

                department=str(row["department"]),

                category=str(row["category"]),

                section=str(row["section"]),

                sha256=str(row["sha256"]),

                simhash=str(row["simhash"]),

                embedding=embedding,

                embedding_model=str(row["embedding_model"]),

                embedding_dimension=int(row["embedding_dimension"]),

                word_count=int(row["word_count"]),

                character_count=int(row["character_count"]),

                trust_score=float(row["trust_score"]),

                fingerprint_version=str(row["fingerprint_version"]),

                created_at=str(row["created_at"]),

                source_file=str(row["source_file"]),

                is_poisoned=poisoned,

                similarity_score=float(row["similarity_score"])
                if pd.notna(row["similarity_score"])
                else None,

                decision=str(row["decision"])
                if pd.notna(row["decision"])
                else None,

            )

            self.database[fp.chunk_id] = fp

        self.loaded = True

        print()
        print("=" * 60)
        print("Trusted Fingerprint Database Loaded")
        print("=" * 60)
        print(f"Fingerprints : {len(self.database)}")
        print("=" * 60)

    # --------------------------------------------------

    def get(self, chunk_id: str) -> Optional[ChunkFingerprint]:

        if not self.loaded:
            self.load()

        return self.database.get(chunk_id)

    # --------------------------------------------------

    def exists(self, chunk_id: str) -> bool:

        if not self.loaded:
            self.load()

        return chunk_id in self.database

    # --------------------------------------------------

    def total(self):

        if not self.loaded:
            self.load()

        return len(self.database)

    # --------------------------------------------------

    def statistics(self):

        if not self.loaded:
            self.load()

        return {

            "fingerprints": len(self.database)

        }


# ------------------------------------------------------

if __name__ == "__main__":

    db = FingerprintDatabase()

    db.load()

    print(db.statistics())