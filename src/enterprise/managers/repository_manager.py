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

    # =========================================================
    # Raw Data
    # =========================================================

    def list_policies(self):

        if not self.policy_index.exists():
            return pd.DataFrame()

        return pd.read_csv(self.policy_index)

    # ---------------------------------------------------------

    def list_chunks(self):

        if not self.chunk_database.exists():
            return pd.DataFrame()

        return pd.read_csv(self.chunk_database)

    # =========================================================
    # Repository Counts
    # =========================================================

    def total_policies(self):

        return len(self.list_policies())

    # ---------------------------------------------------------

    def total_chunks(self):

        return len(self.list_chunks())

    # =========================================================
    # Trust
    # =========================================================

    def average_trust(self):

        chunks = self.list_chunks()

        if chunks.empty:
            return 0.0

        if "trust_score" not in chunks.columns:
            return 100.0

        trust = pd.to_numeric(
            chunks["trust_score"],
            errors="coerce"
        ).dropna()

        if trust.empty:
            return 100.0

        # Repository stores trust as 0.0 - 1.0.
        # Dashboard/API uses 0 - 100.
        if trust.max() <= 1.0:
            trust = trust * 100

        return round(trust.mean(), 2)

    # =========================================================
    # Security Status
    # =========================================================

    def trusted_chunks(self):

        chunks = self.list_chunks()

        if chunks.empty:
            return 0

        # Existing repository chunks do not have decisions.
        # Their trust_score is the source of truth.
        if "decision" in chunks.columns:

            decisions = chunks["decision"].astype(str).str.upper()

            accepted = decisions.eq("ACCEPT").sum()

            if accepted > 0:
                return int(accepted)

        if "trust_score" in chunks.columns:

            trust = pd.to_numeric(
                chunks["trust_score"],
                errors="coerce"
            )

            return int((trust >= 0.90).sum())

        return 0

    # ---------------------------------------------------------

    def suspicious_chunks(self):

        chunks = self.list_chunks()

        if chunks.empty:
            return 0

        if "decision" in chunks.columns:

            decisions = chunks["decision"].astype(str).str.upper()

            review = decisions.eq("REVIEW").sum()

            if review > 0:
                return int(review)

        if "trust_score" in chunks.columns:

            trust = pd.to_numeric(
                chunks["trust_score"],
                errors="coerce"
            )

            return int(
                ((trust >= 0.70) & (trust < 0.90)).sum()
            )

        return 0

    # ---------------------------------------------------------

    def blocked_chunks(self):

        chunks = self.list_chunks()

        if chunks.empty:
            return 0

        if "decision" in chunks.columns:

            decisions = chunks["decision"].astype(str).str.upper()

            rejected = decisions.eq("REJECT").sum()

            if rejected > 0:
                return int(rejected)

        if "trust_score" in chunks.columns:

            trust = pd.to_numeric(
                chunks["trust_score"],
                errors="coerce"
            )

            return int((trust < 0.70).sum())

        return 0

    # =========================================================
    # Policy Table
    # =========================================================

    def get_policy_table(self):

        policies = self.list_policies()

        if policies.empty:
            return pd.DataFrame()

        columns = [
            "policy_id",
            "title",
            "department",
            "category",
            "classification",
            "risk_level",
            "owner",
            "effective_date",
            "review_date",
        ]

        available = [
            column
            for column in columns
            if column in policies.columns
        ]

        return policies[available]

    # =========================================================
    # Chunk Table
    # =========================================================

    def get_chunk_table(self):

        chunks = self.list_chunks()

        if chunks.empty:
            return pd.DataFrame()

        columns = [
            "chunk_id",
            "policy_id",
            "department",
            "category",
            "section",
            "trust_score",
            "decision",
        ]

        available = [
            column
            for column in columns
            if column in chunks.columns
        ]

        table = chunks[available].copy()

        # Convert repository trust to percentage for display.
        if "trust_score" in table.columns:

            trust = pd.to_numeric(
                table["trust_score"],
                errors="coerce"
            )

            if trust.max() <= 1.0:
                table["trust_score"] = trust * 100

        return table

    # =========================================================
    # Department Statistics
    # =========================================================

    def department_statistics(self):

        chunks = self.list_chunks()

        if chunks.empty:
            return pd.DataFrame()

        return (
            chunks
            .groupby("department")
            .size()
            .reset_index(name="Chunks")
        )

    # =========================================================
    # Trust Distribution
    # =========================================================

    def trust_distribution(self):

        chunks = self.list_chunks()

        if chunks.empty:
            return pd.DataFrame()

        # If decisions already exist, use them.
        if "decision" in chunks.columns:

            decisions = (
                chunks["decision"]
                .dropna()
                .astype(str)
                .str.upper()
            )

            if not decisions.empty:

                distribution = (
                    decisions
                    .value_counts()
                    .reindex(
                        ["ACCEPT", "REVIEW", "REJECT"],
                        fill_value=0
                    )
                    .reset_index()
                )

                distribution.columns = [
                    "Decision",
                    "Count"
                ]

                return distribution

        # Existing baseline repository has no decisions.
        # Derive repository status from trust score.
        if "trust_score" in chunks.columns:

            trust = pd.to_numeric(
                chunks["trust_score"],
                errors="coerce"
            ).dropna()

            if not trust.empty:

                if trust.max() <= 1.0:
                    trust = trust * 100

                distribution = pd.DataFrame({
                    "Decision": [
                        "ACCEPT",
                        "REVIEW",
                        "REJECT",
                    ],
                    "Count": [
                        int((trust >= 90).sum()),
                        int(
                            ((trust >= 70) & (trust < 90))
                            .sum()
                        ),
                        int((trust < 70).sum()),
                    ],
                })

                return distribution

        return pd.DataFrame()