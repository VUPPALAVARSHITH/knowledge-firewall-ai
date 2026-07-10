"""
chunk_fingerprint_generator.py

Knowledge Firewall AI

Generates trusted fingerprints
for every semantic chunk.
"""

from __future__ import annotations

import csv
import hashlib
import json
import pickle
from dataclasses import asdict
from datetime import datetime

from tqdm import tqdm

from src.config.path_config import DATA_DIR

from src.fingerprint.embedding_engine import EmbeddingEngine
from src.fingerprint.models import ChunkFingerprint
from src.fingerprint.simhash_engine import SimHashEngine


VECTOR_DIR = DATA_DIR / "vector_store"

METADATA_DIR = DATA_DIR / "metadata"

CHUNK_FILE = VECTOR_DIR / "chunk_metadata.pkl"

OUTPUT_PKL = METADATA_DIR / "chunk_fingerprint_database.pkl"

OUTPUT_CSV = METADATA_DIR / "chunk_fingerprint_database.csv"

OUTPUT_STATS = METADATA_DIR / "fingerprint_statistics.json"


class ChunkFingerprintGenerator:

    def __init__(self):

        self.embedding = EmbeddingEngine()

        self.simhash = SimHashEngine()

    # -------------------------------------------------------

    @staticmethod
    def sha256(text: str):

        return hashlib.sha256(

            text.encode("utf-8")

        ).hexdigest()

    # -------------------------------------------------------

    def load_chunks(self):

        with open(

            CHUNK_FILE,

            "rb"

        ) as file:

            return pickle.load(file)

    # -------------------------------------------------------

    def generate(self):

        chunks = self.load_chunks()

        fingerprints = []

        print()

        print("=" * 70)

        print("Generating Chunk Fingerprints")

        print("=" * 70)

        for chunk in tqdm(chunks):

            fp = ChunkFingerprint(

                chunk_id=chunk.chunk_id,

                policy_id=chunk.policy_id,

                department=chunk.department,

                category=chunk.category,

                section=chunk.section,

                sha256=self.sha256(chunk.text),

                simhash=self.simhash.generate(

                    chunk.text

                ),

                embedding=self.embedding.generate(
                    chunk.text
                ),
                embedding_model=self.embedding.model_name_used(),
                embedding_dimension=len(chunk.embedding),

                word_count=chunk.word_count,

                character_count=chunk.character_count,

                created_at=datetime.now().isoformat(),

                source_file=chunk.source_file,

                is_poisoned=chunk.is_poisoned

            )

            fingerprints.append(fp)

        self.export(fingerprints)

    # -------------------------------------------------------

    def export(self, fingerprints):

        METADATA_DIR.mkdir(

            parents=True,

            exist_ok=True

        )

        with open(

            OUTPUT_PKL,

            "wb"

        ) as file:

            pickle.dump(

                fingerprints,

                file

            )

        rows = [

            asdict(fp)

            for fp in fingerprints

        ]

        with open(

            OUTPUT_CSV,

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

        stats = {

            "total_chunks": len(fingerprints),

            "embedding_model": self.embedding.model_name_used(),

            "fingerprint_version": "2.0"

        }

        with open(

            OUTPUT_STATS,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                stats,

                file,

                indent=4

            )

        print()

        print("=" * 70)

        print("Chunk Fingerprint Database Generated")

        print("=" * 70)

        print("Chunks :", len(fingerprints))

        print("Output :", OUTPUT_PKL)

        print("=" * 70)


if __name__ == "__main__":

    ChunkFingerprintGenerator().generate()