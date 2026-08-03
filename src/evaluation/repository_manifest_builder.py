from pathlib import Path
import json
import random

from src.config.path_config import ENTERPRISE_DIR


MANIFEST_PATH = Path(
    "src/evaluation/evaluation_manifest.json"
)


class RepositoryManifestBuilder:

    POISONED = 10
    SENSITIVE = 5
    NEAR_DUPLICATE = 5

    RANDOM_SEED = 42

    def __init__(self):

        random.seed(self.RANDOM_SEED)

        self.files = sorted(
            ENTERPRISE_DIR.rglob("*.txt")
        )

        self.manifest = {

            "seed": self.RANDOM_SEED,

            "metadata": {

                "total_policies": len(self.files),

                "clean": 0,

                "poisoned": self.POISONED,

                "sensitive": self.SENSITIVE,

                "near_duplicates": self.NEAR_DUPLICATE,

            },

            "clean": [],

            "poisoned": [],

            "sensitive": [],

            "near_duplicates": [],

        }

    def build(self):

        print("=" * 60)
        print("BUILDING EVALUATION MANIFEST")
        print("=" * 60)

        available = self.files.copy()

        random.shuffle(available)

        poisoned = available[: self.POISONED]
        available = available[self.POISONED :]

        sensitive = available[: self.SENSITIVE]
        available = available[self.SENSITIVE :]

        near = available[: self.NEAR_DUPLICATE]
        available = available[self.NEAR_DUPLICATE :]

        self.manifest["clean"] = [

            {

                "file": str(
                    p.relative_to(
                        ENTERPRISE_DIR
                    )
                ),

                "expected": "ACCEPT"

            }

            for p in available

        ]

        self.manifest["poisoned"] = [

            {

                "file": str(
                    p.relative_to(
                        ENTERPRISE_DIR
                    )
                ),

                "mode": "poisoned",

                "expected": "REJECT"

            }

            for p in poisoned

        ]

        self.manifest["sensitive"] = [

            {

                "file": str(
                    p.relative_to(
                        ENTERPRISE_DIR
                    )
                ),

                "mode": "sensitive",

                "expected": "REJECT"

            }

            for p in sensitive

        ]

        self.manifest["near_duplicates"] = [

            {

                "file": str(
                    p.relative_to(
                        ENTERPRISE_DIR
                    )
                ),

                "mode": "near_duplicate",

                "expected": "REVIEW"

            }

            for p in near

        ]

        self.manifest["metadata"]["clean"] = len(
            self.manifest["clean"]
        )

        self.save()

        self.summary()

    def save(self):

        MANIFEST_PATH.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(

            MANIFEST_PATH,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                self.manifest,

                f,

                indent=4

            )

    def summary(self):

        print()

        print(
            f"Clean            : {len(self.manifest['clean'])}"
        )

        print(
            f"Poisoned         : {len(self.manifest['poisoned'])}"
        )

        print(
            f"Sensitive        : {len(self.manifest['sensitive'])}"
        )

        print(
            f"Near Duplicate   : {len(self.manifest['near_duplicates'])}"
        )

        print()

        print(
            "Manifest Saved:"
        )

        print(
            MANIFEST_PATH
        )

    

if __name__ == "__main__":

    RepositoryManifestBuilder().build()

