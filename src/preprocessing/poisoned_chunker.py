"""
poisoned_chunker.py

Knowledge Firewall AI

Generates semantic chunks for the poisoned dataset.
"""

from src.config.path_config import POISONED_DIR

from src.preprocessing.parser import PolicyParser
from src.preprocessing.chunk_builder import ChunkBuilder
from src.preprocessing.validator import ChunkValidator
from src.preprocessing.exporter import ChunkExporter


class PoisonedDatasetBuilder:

    def __init__(self):

        self.parser = PolicyParser()
        self.builder = ChunkBuilder()
        self.validator = ChunkValidator()
        self.exporter = ChunkExporter()

    def build(self):

        chunks = []

        total = 0

        for file in POISONED_DIR.rglob("*.txt"):

            policy = self.parser.parse(file)

            built = self.builder.build(policy)

            # --------------------------------------
            # Mark every chunk as poisoned
            # --------------------------------------

            for chunk in built:

                chunk.is_poisoned = True

            chunks.extend(built)

            total += 1

            print(f"[{total}] {policy.policy_id}")

        errors = self.validator.validate(chunks)

        if errors:

            print("\nValidation Failed\n")

            for error in errors:

                print(error)

            return

        self.exporter.export(

            chunks,

            dataset_name="poisoned_vector_store"

        )

        print()

        print("=" * 70)

        print("POISONED CHUNK DATASET GENERATED")

        print("=" * 70)

        print(f"Policies : {total}")

        print(f"Chunks   : {len(chunks)}")

        print("=" * 70)


if __name__ == "__main__":

    PoisonedDatasetBuilder().build()