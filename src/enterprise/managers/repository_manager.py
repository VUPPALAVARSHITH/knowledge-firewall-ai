# src/enterprise/repository_manager.py

from pathlib import Path
import pandas as pd


class RepositoryManager:

    def __init__(self):

        self.metadata_path = Path("data/metadata")

        self.policy_index = self.metadata_path / "policy_index.csv"

        self.chunk_database = self.metadata_path / "chunk_fingerprint_database.csv"

    # -------------------------------------

    def list_policies(self):

        if not self.policy_index.exists():
            return pd.DataFrame()

        return pd.read_csv(self.policy_index)

    # -------------------------------------

    def list_chunks(self):

        if not self.chunk_database.exists():
            return pd.DataFrame()

        return pd.read_csv(self.chunk_database)

    # -------------------------------------

    def total_policies(self):

        return len(self.list_policies())

    # -------------------------------------

    def total_chunks(self):

        return len(self.list_chunks())