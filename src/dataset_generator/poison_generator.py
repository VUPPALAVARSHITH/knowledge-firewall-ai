"""
Poison Generator

Generates poisoned enterprise policies
using semantic attack templates.
"""

from pathlib import Path
import random
import shutil

from src.config.path_config import (
    ENTERPRISE_DIR,
    POISONED_DIR
)

from src.dataset_generator.attack_templates import ATTACK_PATTERNS


class PoisonGenerator:

    def __init__(self):

        self.random = random.Random(42)

    def poison_text(self, text):

        attack = self.random.choice(ATTACK_PATTERNS)

        poisoned = text

        for original, replacement in attack["replacements"].items():

            poisoned = poisoned.replace(
                original,
                replacement
            )

        return poisoned, attack["attack_type"]

    def generate(self):

        POISONED_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        count = 0

        for file in ENTERPRISE_DIR.rglob("*.txt"):

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                text = f.read()

            poisoned_text, attack = self.poison_text(text)

            relative = file.relative_to(ENTERPRISE_DIR)

            output = POISONED_DIR / relative

            output.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            with open(
                output,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(poisoned_text)

            count += 1

            print(
                f"[{count}] {relative} -> {attack}"
            )

        print()

        print("=" * 50)

        print("Poison Generation Completed")

        print("Generated:", count)

        print("=" * 50)


if __name__ == "__main__":

    PoisonGenerator().generate()