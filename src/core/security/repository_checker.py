"""
repository_checker.py

Knowledge Firewall AI

Repository Similarity Checker

Compares uploaded document fingerprints against the
trusted fingerprint database to detect duplicate,
modified and potential re-poisoning attempts.
"""

from pathlib import Path
import json
import numpy as np
import pandas as pd
from src.core.security.constants import REPOISONING_THRESHOLD
from src.core.security.models import RepositoryCheckResult

class RepositoryChecker:

    def __init__(self):

        self.database = Path(
            "data/metadata/chunk_fingerprint_database.csv"
        )

        self.database = self.load_database()

    # ---------------------------------------------------------

    def load_database(self):

        if not self.database_path.exists():
            return pd.DataFrame()

        return pd.read_csv(self.database_path)

    # ---------------------------------------------------------

    def compare_sha(self, sha256):

        database = self.database

        if database.empty:
            return None

        if "sha256" not in database.columns:
            return None

        matches = database[
            database["sha256"] == sha256
        ]

        if matches.empty:
            return None

        return matches

    # ---------------------------------------------------------

    def compare_policy(self, policy_id):

        database = self.database

        if database.empty:
            return None

        matches = database[
            database["policy_id"] == policy_id
        ]

        if matches.empty:
            return None

        return matches

    # ---------------------------------------------------------

    def duplicate_exists(
        self,
        policy_id,
        sha256
    ):

        if self.compare_sha(sha256) is not None:
            return True

        if self.compare_policy(policy_id) is not None:
            return True

        return False

        # ---------------------------------------------------------

    def cosine_similarity(self, embedding1, embedding2):

        embedding1 = np.array(embedding1, dtype=float)
        embedding2 = np.array(embedding2, dtype=float)

        denominator = (
            np.linalg.norm(embedding1)
            * np.linalg.norm(embedding2)
        )

        if denominator == 0:
            return 0.0

        return float(
            np.dot(embedding1, embedding2) / denominator
        )
    
        # ---------------------------------------------------------

        # ---------------------------------------------------------

    def compare_embedding(
        self,
        embedding,
        threshold=REPOISONING_THRESHOLD,
    ) -> RepositoryCheckResult:

        database = self.database

        if database.empty:

            return RepositoryCheckResult(
                duplicate=False,
                similarity=0.0,
                matched_policy=None,
                recommendation="Repository Empty"
            )

        best_match = None
        best_score = 0.0

        for _, row in database.iterrows():

            try:

                stored = json.loads(row["embedding"])

            except Exception:
                continue

            score = self.cosine_similarity(
                embedding,
                stored
            )

            if score > best_score:

                best_score = score
                best_match = row

        if best_match is None:

            return RepositoryCheckResult(
                duplicate=False,
                similarity=0.0,
                matched_policy=None,
                recommendation="No Similar Policy"
            )

        duplicate = best_score >= threshold

        recommendation = (
            "Reject Upload"
            if duplicate
            else "Accept"
        )

        return RepositoryCheckResult(

            duplicate=duplicate,

            similarity=round(best_score, 4),

            matched_policy=best_match["policy_id"],

            recommendation=recommendation

        )