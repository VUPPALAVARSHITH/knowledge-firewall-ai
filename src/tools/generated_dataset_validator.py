"""
generated_dataset_validator.py

Knowledge Firewall AI

Validates generated attack datasets.
"""

from pathlib import Path


class GeneratedDatasetValidator:

    def __init__(self, generated_dir: Path):

        self.generated_dir = generated_dir

        self.errors = []
        self.warnings = []

    def validate(self):

        print("\nGenerated Dataset Validation")
        print("-" * 70)

        self.check_directories()

        self.check_empty_files()

        self.check_statistics()

        print()

        print("Generated Dataset Validation Complete")

        print(f"Errors   : {len(self.errors)}")
        print(f"Warnings : {len(self.warnings)}")

        return self.errors, self.warnings

    def check_directories(self):

        required = [
            "poisoned",
            "repoisoned",
            "prompt_injection",
            "sensitive_data",
            "jailbreak",
            "attack_statistics",
        ]

        for folder in required:

            path = self.generated_dir / folder

            if path.exists():

                print(f"[OK] {folder}")

            else:

                self.errors.append(f"{folder} missing")

    def check_empty_files(self):

        empty = 0

        for file in self.generated_dir.rglob("*"):

            if file.is_file() and file.stat().st_size == 0:

                empty += 1

        print(f"Empty Files : {empty}")

        if empty:

            self.warnings.append(
                f"{empty} empty generated files."
            )

    
    def check_statistics(self):

        total = 0

        for folder in self.generated_dir.iterdir():

            if folder.is_dir():

                count = len(list(folder.rglob("*.*")))

                print(f"{folder.name:<25} {count}")

                total += count

        print("-" * 40)

        print(f"Total Generated Files : {total}")

    
    

    