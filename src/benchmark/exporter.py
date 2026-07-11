"""
exporter.py

Exports Dataset 6.
"""

from __future__ import annotations

import csv
import json
from dataclasses import asdict

from src.config.path_config import DATA_DIR


BENCHMARK_DIR = DATA_DIR / "benchmark"

BENCHMARK_DIR.mkdir(

    parents=True,

    exist_ok=True

)


class BenchmarkExporter:

    def export(self, questions):

        rows = [

            asdict(q)

            for q in questions

        ]

        # -----------------------------------------

        with open(

            BENCHMARK_DIR / "benchmark_dataset.csv",

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

        # -----------------------------------------

        with open(

            BENCHMARK_DIR / "benchmark_dataset.json",

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                rows,

                file,

                indent=4

            )

        # -----------------------------------------

        stats = {

            "questions": len(rows),

            "departments": {},

            "difficulty": {}

        }

        for row in rows:

            stats["departments"][

                row["department"]

            ] = stats["departments"].get(

                row["department"],

                0

            ) + 1

            stats["difficulty"][

                row["difficulty"]

            ] = stats["difficulty"].get(

                row["difficulty"],

                0

            ) + 1

        with open(

            BENCHMARK_DIR / "benchmark_statistics.json",

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

        print("BENCHMARK DATASET EXPORTED")

        print("=" * 70)

        print(f"CSV   : {BENCHMARK_DIR/'benchmark_dataset.csv'}")

        print(f"JSON  : {BENCHMARK_DIR/'benchmark_dataset.json'}")

        print(f"Stats : {BENCHMARK_DIR/'benchmark_statistics.json'}")

        print("=" * 70)