"""
exporter.py

Knowledge Firewall AI

Exports Dataset 4.
"""

import csv
import json
import pickle

from dataclasses import asdict

from src.config.path_config import DATA_DIR


VECTOR_DIR = DATA_DIR / "vector_store"
VECTOR_DIR.mkdir(parents=True, exist_ok=True)


class ChunkExporter:

    def export_pickle(self, chunks):

        with open(
            VECTOR_DIR / "chunk_metadata.pkl",
            "wb"
        ) as file:

            pickle.dump(chunks, file)

    # ---------------------------------------------------

    def export_csv(self, chunks):

        rows = [asdict(chunk) for chunk in chunks]

        with open(
            VECTOR_DIR / "chunk_metadata.csv",
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

    # ---------------------------------------------------

    def export_statistics(self, chunks):

        stats = {

            "total_chunks": len(chunks),

            "average_words": round(

                sum(c.word_count for c in chunks) / len(chunks),

                2

            ),

            "average_characters": round(

                sum(c.character_count for c in chunks) / len(chunks),

                2

            ),

            "sections": {},

            "departments": {},

            "categories": {},

            "priorities": {}

        }

        for chunk in chunks:

            stats["sections"][chunk.section] = stats["sections"].get(chunk.section,0)+1

            stats["departments"][chunk.department] = stats["departments"].get(chunk.department,0)+1

            stats["categories"][chunk.category] = stats["categories"].get(chunk.category,0)+1

            key=str(chunk.priority)

            stats["priorities"][key]=stats["priorities"].get(key,0)+1

        with open(

            VECTOR_DIR/"statistics.json",

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                stats,

                file,

                indent=4

            )

    # ---------------------------------------------------

    def export(self,chunks):

        self.export_pickle(chunks)

        self.export_csv(chunks)

        self.export_statistics(chunks)

        print()

        print("="*65)

        print("DATASET 4 GENERATED SUCCESSFULLY")

        print("="*65)

        print(f"Total Chunks      : {len(chunks)}")

        print(f"PKL               : {VECTOR_DIR/'chunk_metadata.pkl'}")

        print(f"CSV               : {VECTOR_DIR/'chunk_metadata.csv'}")

        print(f"Statistics        : {VECTOR_DIR/'statistics.json'}")

        print("="*65)