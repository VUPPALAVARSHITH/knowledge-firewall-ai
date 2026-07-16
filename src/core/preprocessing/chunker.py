"""
chunker.py

Knowledge Firewall AI

Dataset 4 Builder
"""

from src.config.path_config import ENTERPRISE_DIR

from src.core.preprocessing.parser import PolicyParser
from src.core.preprocessing.chunk_builder import ChunkBuilder
from src.core.preprocessingocessing.validator import ChunkValidator
from src.core.preprocessing.exporter import ChunkExporter


class Dataset4Builder:

    def __init__(self):

        self.parser = PolicyParser()

        self.builder = ChunkBuilder()

        self.validator = ChunkValidator()

        self.exporter = ChunkExporter()

    # --------------------------------------------------

    def build(self):

        chunks = []

        total = 0

        print("\n" + "="*70)

        print("GENERATING DATASET 4 - ENTERPRISE VECTOR DATASET")

        print("="*70 + "\n")

        for file in sorted(ENTERPRISE_DIR.rglob("*.txt")):

            policy = self.parser.parse(file)

            policy_chunks = self.builder.build(policy)

            chunks.extend(policy_chunks)

            total += 1

            print(

                f"[{total:03d}] "

                f"{policy.policy_id}"

                f" -> "

                f"{len(policy_chunks)} chunks"

            )

        print()

        print("="*70)

        print("VALIDATING DATASET")

        print("="*70)

        errors = self.validator.validate(chunks)

        if errors:

            print(f"\nValidation Failed ({len(errors)} Errors)\n")

            for error in errors:

                print(error)

            return

        print("Validation Passed")

        print()

        self.exporter.export(chunks)

        print()

        print("="*70)

        print(f"Policies Processed : {total}")

        print(f"Chunks Generated   : {len(chunks)}")

        print("="*70)


if __name__ == "__main__":

    Dataset4Builder().build()