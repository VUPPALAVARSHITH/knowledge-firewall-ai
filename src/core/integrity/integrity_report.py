"""
integrity_report.py

Knowledge Firewall AI

Generates the final repository integrity report.
"""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
import json

from src.core.integrity.integrity_models import (
    IntegrityScanReport,
)

from src.core.integrity.integrity_alerts import (
    IntegrityAlert,
)


class IntegrityReportGenerator:

    def save(

        self,

        report: IntegrityScanReport,

        alerts: list[IntegrityAlert],

        output_path: str | Path,

    ):

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        payload = {

            "summary": {

                "scan_time": report.scan_time,

                "total_policies": report.total_policies,

                "average_trust": report.average_trust,

                "repository_health": report.repository_health,

            },

            "results": [

                asdict(result)

                for result in report.results

            ],

            "alerts": [

                asdict(alert)

                for alert in alerts

            ]

        }

        with open(

            output_path,

            "w",

            encoding="utf-8",

        ) as f:

            json.dump(

                payload,

                f,

                indent=4,

            )

        return output_path

    # -----------------------------------------------------

    def print_summary(

        self,

        report: IntegrityScanReport,

        alerts: list[IntegrityAlert],

    ):

        print()

        print("=" * 60)

        print("REPOSITORY INTEGRITY REPORT")

        print("=" * 60)

        print(f"Scan Time         : {report.scan_time}")

        print(f"Policies          : {report.total_policies}")

        print(f"Average Trust     : {report.average_trust:.2f}")

        print(f"Repository Health : {report.repository_health}")

        print(f"Alerts            : {len(alerts)}")

        print("=" * 60)