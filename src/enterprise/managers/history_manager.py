"""
history_manager.py

Knowledge Firewall AI

Enterprise Version History Manager.
"""

import pandas as pd

from src.enterprise.managers.repository_manager import RepositoryManager


class HistoryManager:

    def __init__(self):

        self.repository = RepositoryManager()

    # ---------------------------------------------------------

    def get_versions(self):

        chunks = self.repository.list_chunks()

        if chunks.empty:

            return pd.DataFrame()

        columns = [

            "policy_id",

            "fingerprint_version",

            "trust_score",

            "created_at"

        ]

        available = [

            column

            for column in columns

            if column in chunks.columns

        ]

        history = chunks[available].copy()

        history = history.sort_values(

            by="created_at",

            ascending=False

        )

        return history

    # ---------------------------------------------------------

    def get_policy_history(

        self,

        policy_id: str

    ):

        history = self.get_versions()

        if history.empty:

            return history

        return history[

            history["policy_id"] == policy_id

        ]

    # ---------------------------------------------------------

    def latest_versions(self):

        history = self.get_versions()

        if history.empty:

            return history

        return (

            history

            .groupby("policy_id")

            .head(1)

            .reset_index(drop=True)

        )