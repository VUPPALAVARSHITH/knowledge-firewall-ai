"""
integrity_history.py

Knowledge Firewall AI

Stores repository integrity scan history.
"""

from __future__ import annotations

from pathlib import Path
from datetime import datetime
import json

from src.core.integrity.integrity_models import (
    IntegrityScanReport,
)


class IntegrityHistory:

    def __init__(self):

        self.history_dir = Path(
            "data/history"
        )

        self.history_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    # -----------------------------------------------------

    def save(

        self,

        report: IntegrityScanReport,

    ) -> Path:

        filename = datetime.now().strftime(
            "integrity_%Y%m%d_%H%M%S.json"
        )

        path = self.history_dir / filename

        payload = {

            "scan_time": report.scan_time,

            "total_policies": report.total_policies,

            "average_trust": report.average_trust,

            "repository_health": report.repository_health,

            "results": [

                {

                    "policy_id": r.policy_id,

                    "department": r.department,

                    "category": r.category,

                    "trust_score": r.trust_score,

                    "repository_similarity": r.repository_similarity,

                    "attack_detected": r.attack_detected,

                    "attack_confidence": r.attack_confidence,

                    "sensitive_data_detected": (
                        r.sensitive_data_detected
                    ),

                    "sensitive_data_score": (
                        r.sensitive_data_score
                    ),

                    "decision": r.decision,

                    "recommendation": (
                        r.recommendation
                    ),

                    "warnings": r.warnings,

                }

                for r in report.results

            ]

        }

        with open(

            path,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                payload,

                f,

                indent=4

            )

        return path

    # -----------------------------------------------------

    def list_history(self):

        return sorted(

            self.history_dir.glob(
                "integrity_*.json"
            )

        )

    # -----------------------------------------------------

    def latest(self):

        history = self.list_history()

        if not history:

            return None

        return history[-1]

    # -----------------------------------------------------

    def load(self, filepath):

        with open(

            filepath,

            "r",

            encoding="utf-8"

        ) as f:

            return json.load(f)