"""
monitor_runner.py

Knowledge Firewall AI

Continuously monitors the enterprise repository
for policy changes.
"""

from __future__ import annotations

import time

from src.core.monitoring.repository_monitor import RepositoryMonitor
from src.core.monitoring.change_detector import ChangeDetector
from src.core.monitoring.event_processor import EventProcessor

from src.core.integrity.integrity_history import IntegrityHistory
from src.core.integrity.trust_recalculator import TrustRecalculator
from src.core.integrity.integrity_alerts import IntegrityAlertEngine


class MonitorRunner:

    def __init__(self):

        self.monitor = RepositoryMonitor()

        self.detector = ChangeDetector()

        self.processor = EventProcessor()

        self.history = IntegrityHistory()

        self.recalculator = TrustRecalculator()

        self.alert_engine = IntegrityAlertEngine()

        self.previous_scan = None

    # ---------------------------------------------------------

    def run(self, interval: int = 5):

        print("=" * 60)
        print("KNOWLEDGE FIREWALL AI")
        print("CONTINUOUS REPOSITORY MONITOR")
        print("=" * 60)

        self.monitor.build_snapshot()

        print("Monitoring started...\n")

        try:

            while True:

                changes = self.monitor.detect_changes()

                if changes:

                    events = self.detector.process(changes)

                    for event in events:

                        print()

                        print("=" * 60)

                        # -------------------------------------
                        # Verify changed policy
                        # -------------------------------------

                        result = self.processor.process(event)

                        print(f"Event        : {event.event}")
                        print(f"Policy ID    : {result.policy_id}")
                        print(f"Trust Score  : {result.trust_score:.2f}")
                        print(f"Decision     : {result.decision}")

                        if result.alert_generated:

                            print("Security Alert : YES")

                        else:

                            print("Security Alert : NO")

                        # -------------------------------------
                        # Repository Scan
                        # -------------------------------------

                        report = self.processor.verifier.verify_repository()

                        # -------------------------------------
                        # Trust Drift
                        # -------------------------------------

                        drift = []

                        if self.previous_scan is not None:

                            drift = self.recalculator.compare(

                                self.previous_scan,

                                report,

                            )

                            significant = [

                                d

                                for d in drift

                                if d.status != "Stable"

                            ]

                            if significant:

                                print()

                                print("Trust Drift")

                                print("-" * 40)

                                for item in significant:

                                    print(

                                        f"{item.policy_id} | "

                                        f"{item.previous_trust:.2f} -> "

                                        f"{item.current_trust:.2f} | "

                                        f"{item.status}"

                                    )

                        # -------------------------------------
                        # Alerts
                        # -------------------------------------

                        alerts = self.alert_engine.generate(

                            report.results,

                            drift,

                        )

                        if alerts:

                            print()

                            print("Integrity Alerts")

                            print("-" * 40)

                            for alert in alerts[:10]:

                                print(

                                    f"[{alert.severity}] "

                                    f"{alert.policy_id} "

                                    f"- {alert.title}"

                                )

                            if len(alerts) > 10:

                                print(

                                    f"... {len(alerts)-10} more alerts"

                                )

                        # -------------------------------------
                        # Save History
                        # -------------------------------------

                        self.history.save(report)

                        self.previous_scan = report

                        print("=" * 60)

                time.sleep(interval)

        except KeyboardInterrupt:

            print()

            print("=" * 60)

            print("Repository Monitor Stopped")
            print("=" * 60)


if __name__ == "__main__":

    MonitorRunner().run()