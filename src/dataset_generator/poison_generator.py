"""
poison_generator.py

Knowledge Firewall AI

Generates poisoned enterprise documents.
"""

from pathlib import Path
import csv
import hashlib

from src.config.path_config import (
    ENTERPRISE_DIR,
    POISONED_DIR,
    METADATA_DIR
)

from src.attacks.attack_engine import AttackEngine


class PoisonGenerator:

    def __init__(self):

        self.engine = AttackEngine()

    def sha256(self, text):

        return hashlib.sha256(

            text.encode()

        ).hexdigest()

    def generate(self):

        POISONED_DIR.mkdir(

            parents=True,

            exist_ok=True

        )

        attack_log = []

        total = 0

        attacked = 0

        for file in ENTERPRISE_DIR.rglob("*.txt"):

            total += 1

            with open(

                file,

                "r",

                encoding="utf-8"

            ) as f:

                text = f.read()

            result = self.engine.apply_attack(
                text,
                intensity="high"
            )
            
            poisoned = result["poisoned_text"]

            if result["success"]:

                attacked += 1

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

                f.write(poisoned)

            attack_log.append({
                
                "policy_id": file.stem,
                "attack_id": result["attack_id"],
                "attack_type": result["attack_type"],
                "category": result["category"],
                "severity": result["severity"],
                "attack_applied": result["success"],
                "poisoned_hash": self.sha256(poisoned)
            })

            print(

                f"[{total}] {file.stem} -> {result['attack_type']}"

            )

        log_path = METADATA_DIR / "attack_log.csv"

        with open(

            log_path,

            "w",

            newline="",

            encoding="utf-8"

        ) as csvfile:

            writer = csv.DictWriter(

                csvfile,

                fieldnames=[
                    "policy_id",
                    "attack_id",
                    "attack_type",
                    "category",
                    "severity",
                    "attack_applied",
                    "poisoned_hash"
                ]

            )

            writer.writeheader()

            writer.writerows(attack_log)

        print()

        print("=" * 60)

        print("Poison Dataset Generated")

        print("=" * 60)

        print("Enterprise Documents :", total)

        print("Successful Attacks   :", attacked)

        print("Poisoned Dataset     :", POISONED_DIR)

        print("Attack Log           :", log_path)

        print("=" * 60)


if __name__ == "__main__":

    PoisonGenerator().generate()