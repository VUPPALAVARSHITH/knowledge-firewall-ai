"""
benchmark_builder.py

Knowledge Firewall AI

Builds Dataset 6 - Benchmark QA Dataset
"""

from __future__ import annotations

from pathlib import Path
import random

from src.config.path_config import ENTERPRISE_DIR

from src.preprocessing.parser import PolicyParser

from src.benchmark.question_generator import QuestionGenerator
from src.benchmark.exporter import BenchmarkExporter


class BenchmarkDatasetBuilder:

    """
    Generates the benchmark QA dataset.

    Pipeline

    Enterprise Policies
            ↓
    Parse Policies
            ↓
    Generate Questions
            ↓
    Shuffle
            ↓
    Select Target Size
            ↓
    Export Dataset
    """

    def __init__(self):

        self.parser = PolicyParser()

        self.generator = QuestionGenerator()

        self.exporter = BenchmarkExporter()

        self.random = random.Random(42)

    # --------------------------------------------------

    def build(
        self,
        target_questions=300
    ):

        all_questions = []

        total_policies = 0

        print()

        print("=" * 70)
        print("GENERATING BENCHMARK QUESTIONS")
        print("=" * 70)

        for file in sorted(ENTERPRISE_DIR.rglob("*.txt")):

            policy = self.parser.parse(file)

            questions = self.generator.generate_policy_questions(
                policy
            )

            all_questions.extend(questions)

            total_policies += 1

            if total_policies % 50 == 0:

                print(

                    f"Processed {total_policies} policies..."

                )

        print()

        print(f"Candidate Questions : {len(all_questions)}")

        # ---------------------------------------------

        self.random.shuffle(all_questions)

        benchmark = all_questions[:target_questions]

        self.exporter.export(benchmark)

        print()

        print("=" * 70)
        print("DATASET 6 COMPLETED")
        print("=" * 70)

        print(f"Policies Processed : {total_policies}")

        print(f"Candidate Questions : {len(all_questions)}")

        print(f"Benchmark Questions : {len(benchmark)}")

        print("=" * 70)


# ------------------------------------------------------

if __name__ == "__main__":

    BenchmarkDatasetBuilder().build()