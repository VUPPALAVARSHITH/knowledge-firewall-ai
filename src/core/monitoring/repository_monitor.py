"""
repository_monitor.py

Knowledge Firewall AI

Repository Monitor

Detects newly created or modified policies.
"""

from pathlib import Path

from src.config.path_config import ENTERPRISE_DIR


class RepositoryMonitor:

    def __init__(self):

        self.repository = ENTERPRISE_DIR

        self.snapshot = {}

    # -----------------------------------------------------

    def build_snapshot(self):

        snapshot = {}

        for file in self.repository.rglob("*.txt"):

            snapshot[str(file)] = file.stat().st_mtime

        self.snapshot = snapshot

        return snapshot

    # -----------------------------------------------------

    def detect_changes(self):

        changes = []

        current = {}

        for file in self.repository.rglob("*.txt"):

            path = str(file)

            modified = file.stat().st_mtime

            current[path] = modified

            if path not in self.snapshot:

                changes.append(

                    ("CREATED", file)

                )

            elif self.snapshot[path] != modified:

                changes.append(

                    ("MODIFIED", file)

                )

        self.snapshot = current

        return changes