# src/enterprise/managers/repository_manager.py

from pathlib import Path

import pandas as pd


class RepositoryManager:

    def __init__(self):

        self.metadata_path = Path("data/metadata")

        self.policy_index = self.metadata_path / "policy_index.csv"

        self.chunk_database = (
            self.metadata_path / "chunk_fingerprint_database.csv"
        )

    # ---------------------------------------------------------

    def list_policies(self):

        if not self.policy_index.exists():
            return pd.DataFrame()

        return pd.read_csv(self.policy_index)

    # ---------------------------------------------------------

    def list_chunks(self):

        if not self.chunk_database.exists():
            return pd.DataFrame()

        return pd.read_csv(self.chunk_database)

    # ---------------------------------------------------------

    def total_policies(self):

        return len(self.list_policies())

    # ---------------------------------------------------------

    def total_chunks(self):

        return len(self.list_chunks())

    # ---------------------------------------------------------

    def trusted_chunks(self):

        chunks = self.list_chunks()

        if chunks.empty:
            return 0

        if "decision" in chunks.columns:
            return len(chunks[chunks["decision"] == "Trusted"])

        if "status" in chunks.columns:
            return len(chunks[chunks["status"] == "Trusted"])

        return len(chunks)

    # ---------------------------------------------------------

    def suspicious_chunks(self):

        chunks = self.list_chunks()

        if chunks.empty:
            return 0

        if "decision" in chunks.columns:
            return len(chunks[chunks["decision"] == "Suspicious"])

        if "status" in chunks.columns:
            return len(chunks[chunks["status"] == "Suspicious"])

        return 0

    # ---------------------------------------------------------

    def blocked_chunks(self):

        chunks = self.list_chunks()

        if chunks.empty:
            return 0

        if "decision" in chunks.columns:
            return len(chunks[chunks["decision"] == "Blocked"])

        if "status" in chunks.columns:
            return len(chunks[chunks["status"] == "Blocked"])

        return 0

    # ---------------------------------------------------------

    def average_trust(self):

        chunks = self.list_chunks()

        if chunks.empty:
            return 0.0

        if "trust_score" in chunks.columns:
            return round(chunks["trust_score"].mean(), 2)

        return 100.0

    # ---------------------------------------------------------

    def get_policy_table(self):

        policies = self.list_policies()

        if policies.empty:
            return pd.DataFrame()

        return policies[
            [
                "policy_id",
                "title",
                "department",
                "category",
                "classification",
                "risk_level",
            ]
        ]

    # ---------------------------------------------------------

    def get_chunk_table(self):

        chunks = self.list_chunks()

        if chunks.empty:
            return pd.DataFrame()

        return chunks[
            [
                "chunk_id",
                "policy_id",
                "department",
                "section",
                "trust_score",
                "decision",
            ]
        ]

    # ---------------------------------------------------------

    def department_statistics(self):

        chunks = self.list_chunks()

        if chunks.empty:
            return pd.DataFrame()

        return (
            chunks.groupby("department")
            .size()
            .reset_index(name="Chunks")
        )

    # ---------------------------------------------------------

    def trust_distribution(self):

        chunks = self.list_chunks()

        if chunks.empty:
            return pd.DataFrame()

        distribution = (
            chunks["decision"]
            .value_counts()
            .reset_index()
        )

        distribution.columns = ["Decision", "Count"]

        return distribution