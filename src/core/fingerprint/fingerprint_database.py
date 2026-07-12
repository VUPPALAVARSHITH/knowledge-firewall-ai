"""
fingerprint_database.py

Knowledge Firewall AI

Loads the trusted fingerprint database and provides
fast O(1) lookup by chunk_id.
"""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Dict, Optional

from src.config.path_config import METADATA_DIR
from src.fingerprint.models import ChunkFingerprint


DATABASE_PATH = METADATA_DIR / "chunk_fingerprint_database.pkl"


class FingerprintDatabase:
    """
    Trusted fingerprint database.

    Stores fingerprints in memory using:

        chunk_id -> ChunkFingerprint

    for constant-time lookup.
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

        with open(DATABASE_PATH, "rb") as file:

            fingerprints = pickle.load(file)

        self.database = {

            fp.chunk_id: fp

            for fp in fingerprints

        }

        self.loaded = True

        print()

        print("=" * 60)
        print("Trusted Fingerprint Database Loaded")
        print("=" * 60)
        print(f"Fingerprints : {len(self.database)}")
        print("=" * 60)

    # --------------------------------------------------

    def get(

        self,

        chunk_id: str

    ) -> Optional[ChunkFingerprint]:

        if not self.loaded:

            self.load()

        return self.database.get(chunk_id)

    # --------------------------------------------------

    def exists(

        self,

        chunk_id: str

    ) -> bool:

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