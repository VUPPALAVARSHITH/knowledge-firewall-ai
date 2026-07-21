"""
repository_writer.py

Knowledge Firewall AI

Repository Writer

Provides a single interface for modifying the
trusted enterprise knowledge repository.
"""

from __future__ import annotations

import csv
from dataclasses import asdict

from src.config.path_config import METADATA_DIR
from src.core.repository.models import PolicyMetadata


class RepositoryWriter:

    def __init__(self):

        self.policy_index = (
            METADATA_DIR / "policy_index.csv"
        )

    # ---------------------------------------------------------

    def append_policy(
        self,
        metadata: PolicyMetadata
    ):

        row = asdict(metadata)

        # Convert keyword list to CSV string
        row["keywords"] = ", ".join(metadata.keywords)

        with open(
            self.policy_index,
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=row.keys()
            )

            writer.writerow(row)