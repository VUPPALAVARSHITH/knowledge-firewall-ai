from pathlib import Path
import shutil
import json
import random

from src.config.path_config import ENTERPRISE_DIR

EVAL_REPO = Path("data/evaluation_repository")
GROUND_TRUTH = Path("data/evaluation_ground_truth.json")

class RepositoryBuilder:

    POISON_COUNT = 10
    SENSITIVE_COUNT = 5
    NEAR_DUPLICATE_COUNT = 5

    def __init__(self):

        random.seed(42)

        self.ground_truth = {}

        self.files = sorted(
            ENTERPRISE_DIR.rglob("*.txt")
        )

    def build(self):

        print("="*60)
        print("BUILDING EVALUATION REPOSITORY")
        print("="*60)

        self.prepare()

        self.copy_repository()

        self.inject_poisoned()

        self.inject_sensitive()

        self.inject_near_duplicates()

        self.save_ground_truth()

        print("Done.")  

    def prepare(self):

        if EVAL_REPO.exists():
            shutil.rmtree(EVAL_REPO)

        shutil.copytree(
            ENTERPRISE_DIR,
            EVAL_REPO
        )

    def register(
        self,
        filename,
        label,
        **extra,
    ):

        self.ground_truth[filename] = {

            "label": label,

            **extra
        }

    def save_ground_truth(self):

        with open(
            GROUND_TRUTH,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.ground_truth,
                f,
                indent=4
            )

    def copy_repository(self):

        for file in EVAL_REPO.rglob("*.txt"):

            self.register(

                file.name,

                "clean"

            )

    