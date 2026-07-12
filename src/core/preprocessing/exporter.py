"""
exporter.py

Knowledge Firewall AI

Exports semantic chunk datasets.
"""

import csv
import json
import pickle

from dataclasses import asdict

from src.config.path_config import DATA_DIR


class ChunkExporter:

    # ---------------------------------------------------

    def export_pickle(self, chunks, output_dir):

        with open(
            output_dir / "chunk_metadata.pkl",
            "wb"
        ) as file:

            pickle.dump(chunks, file)

    # ---------------------------------------------------

    def export_csv(self, chunks, output_dir):

        rows = [asdict(chunk) for chunk in chunks]

        with open(
            output_dir / "chunk_metadata.csv",
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

    def export_statistics(self, chunks, output_dir):

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

            stats["sections"][chunk.section] = (
                stats["sections"].get(chunk.section, 0) + 1
            )

            stats["departments"][chunk.department] = (
                stats["departments"].get(chunk.department, 0) + 1
            )

            stats["categories"][chunk.category] = (
                stats["categories"].get(chunk.category, 0) + 1
            )

            priority = str(chunk.priority)

            stats["priorities"][priority] = (
                stats["priorities"].get(priority, 0) + 1
            )

        with open(
            output_dir / "statistics.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                stats,
                file,
                indent=4
            )

    # ---------------------------------------------------

    def export(
        self,
        chunks,
        dataset_name="vector_store"
    ):

        output_dir = DATA_DIR / dataset_name

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.export_pickle(
            chunks,
            output_dir
        )

        self.export_csv(
            chunks,
            output_dir
        )

        self.export_statistics(
            chunks,
            output_dir
        )

        print()

        print("=" * 65)

        print("DATASET EXPORTED SUCCESSFULLY")

        print("=" * 65)

        print(f"Dataset           : {dataset_name}")

        print(f"Total Chunks      : {len(chunks)}")

        print(f"PKL               : {output_dir/'chunk_metadata.pkl'}")

        print(f"CSV               : {output_dir/'chunk_metadata.csv'}")

        print(f"Statistics        : {output_dir/'statistics.json'}")

        print("=" * 65)