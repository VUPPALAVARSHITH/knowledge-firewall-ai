"""
overall_runner.py

Knowledge Firewall AI

Runs all evaluation layers sequentially.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from src.evaluation.layer1_runner import BenchmarkRunner
from src.evaluation.layer2_runner import main as layer2_main
from src.evaluation.layer3_runner import Layer3Runner
from src.evaluation.layer4_runner import Layer4Runner

RESULT_DIR = Path(
    "src/evaluation/results"
)

RESULT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


class OverallRunner:

    def run(self):

        print()
        print("=" * 70)
        print("KNOWLEDGE FIREWALL AI")
        print("OVERALL FRAMEWORK EVALUATION")
        print("=" * 70)

        overall_start = time.perf_counter()

        print("\n[1/4] Layer 1")
        BenchmarkRunner().run()

        print("\n[2/4] Layer 2")
        layer2_main()

        print("\n[3/4] Layer 3")
        Layer3Runner().run()

        print("\n[4/4] Layer 4")
        Layer4Runner().run()

        elapsed = (
            time.perf_counter()
            - overall_start
        )

        summary = {

            "framework": "Knowledge Firewall AI",

            "layers_completed": 4,

            "status": "SUCCESS",

            "execution_time_seconds": round(
                elapsed,
                2,
            ),

        }

        output = (
            RESULT_DIR /
            "overall_results.json"
        )

        with open(
            output,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                summary,
                f,
                indent=4,
            )

        print()
        print("=" * 70)
        print("ALL EVALUATIONS COMPLETED")
        print("=" * 70)
        print(f"Execution Time : {elapsed:.2f} sec")
        print(f"Results        : {output}")
        print("=" * 70)


if __name__ == "__main__":

    OverallRunner().run()