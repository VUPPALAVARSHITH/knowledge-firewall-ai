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

        self.database_path = Path(
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

        if embedding1.shape != embedding2.shape:
            return 0.0

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
    ) -> RepositoryCheckResult:

        database = self.database

        if database.empty:

            return RepositoryCheckResult(
                duplicate=False,
                similarity=0.0,
                matched_policy=None,
                recommendation="Accept",
                reason="Repository empty",
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
                stored,
            )

            if score > best_score:

                best_score = score
                best_match = row

        if best_match is None:

            return RepositoryCheckResult(
                duplicate=False,
                similarity=0.0,
                matched_policy=None,
                recommendation="Accept",
                reason="No similar policy",
            )

        # ------------------------------------------
        # Decision based on similarity
        # ------------------------------------------

        if best_score >= 0.995:

            return RepositoryCheckResult(

                duplicate=True,

                similarity=round(best_score,4),

                matched_policy=best_match["policy_id"],

                recommendation="Reject Upload",

                reason="Exact duplicate",

            )

        elif best_score >= 0.94:

            return RepositoryCheckResult(

                duplicate=False,

                similarity=round(best_score,4),

                matched_policy=best_match["policy_id"],

                recommendation="Manual Review",

                reason="Near duplicate",

            )

        return RepositoryCheckResult(

            duplicate=False,

            similarity=round(best_score,4),

            matched_policy=best_match["policy_id"],

            recommendation="Accept",

            reason="Low similarity",

        )
        
    
    def check(self, document_fingerprint) -> RepositoryCheckResult:
        """
        Perform repository admission checks.

        Pipeline:
            1. Exact SHA-256 duplicate detection
            2. Existing Policy ID detection
            3. Semantic similarity comparison
        """

        # FingerprintEngine currently returns a dictionary.
        if isinstance(document_fingerprint, dict):

            policy_id = document_fingerprint.get(
                "policy_id"
            )

            sha256 = document_fingerprint.get(
                "sha256"
            )

            embedding = document_fingerprint.get(
                "embedding",
                []
            )

            simhash = document_fingerprint.get(
                "simhash"
            )

        else:

            policy_id = document_fingerprint.policy_id

            sha256 = document_fingerprint.sha256

            embedding = document_fingerprint.embedding

            simhash = document_fingerprint.simhash

        # --------------------------------------------------
        # Exact SHA duplicate
        # --------------------------------------------------

        sha_match = self.compare_sha(sha256)

        if sha_match is not None:

            matched_policy = str(
                sha_match.iloc[0]["policy_id"]
            )

            return RepositoryCheckResult(
                duplicate=True,
                similarity=1.0,
                matched_policy=matched_policy,
                recommendation="Reject Upload",
                reason="Exact document fingerprint already exists in repository",
            )

        # --------------------------------------------------
        # Existing Policy ID
        # --------------------------------------------------

        policy_match = self.compare_policy(policy_id)

        if policy_match is not None:

            return RepositoryCheckResult(
                duplicate=True,
                similarity=1.0,
                matched_policy=policy_id,
                recommendation="Reject Upload",
                reason="Policy ID already exists in repository",
            )

        # --------------------------------------------------
        # Semantic similarity
        # --------------------------------------------------

        embedding_result = self.compare_embedding(
            embedding
        )

        # Exact duplicate
        if embedding_result.duplicate:

            return embedding_result

        # Near duplicate
        if embedding_result.recommendation == "Manual Review":

            return embedding_result

        # SimHash fallback
        simhash_result = self.compare_simhash(
            simhash
        )

        if simhash_result.recommendation == "Manual Review":

            return simhash_result

        return embedding_result
    # ---------------------------------------------------------
    # SimHash Hamming Distance
    # ---------------------------------------------------------

    def hamming_distance(self, hash1: str, hash2: str) -> int:

        return bin(int(hash1, 16) ^ int(hash2, 16)).count("1")


    # ---------------------------------------------------------
    # SimHash Comparison
    # ---------------------------------------------------------

    def compare_simhash(self, simhash: str) -> RepositoryCheckResult:

        database = self.database

        if database.empty:

            return RepositoryCheckResult(
                duplicate=False,
                similarity=0.0,
                matched_policy=None,
                recommendation="Accept",
                reason="Repository is empty"
            )

        best_distance = 64
        best_match = None

        for _, row in database.iterrows():

            stored = str(row["simhash"])

            distance = self.hamming_distance(
                simhash,
                stored
            )

            if distance < best_distance:

                best_distance = distance
                best_match = row

        if best_match is None:

            return RepositoryCheckResult(
                duplicate=False,
                similarity=0.0,
                matched_policy=None,
                recommendation="Accept",
                reason="No similar policy found"
            )

        # 64-bit SimHash
        # <=3 bits difference = near duplicate

        if best_distance <= 6:

            return RepositoryCheckResult(

                duplicate=False,

                similarity=0.85,

                matched_policy=best_match["policy_id"],

                recommendation="Manual Review",

                reason=f"Near duplicate detected (SimHash distance={best_distance})"

            )

        return RepositoryCheckResult(

            duplicate=False,

            similarity=0.0,

            matched_policy=None,

            recommendation="Accept",

            reason="No near duplicate"

        )
        
