"""
event_processor.py

Knowledge Firewall AI

Processes repository monitoring events.
"""

from pathlib import Path

from src.core.integrity.integrity_verifier import IntegrityVerifier

from src.core.monitoring.monitor_models import (
    FileChange,
    MonitorEvent,
)


class EventProcessor:

    def __init__(self):

        self.verifier = IntegrityVerifier()

    # ---------------------------------------------------------

    def process(
        self,
        event: FileChange,
    ) -> MonitorEvent:

        report = self.verifier.verify_policy(
            Path(event.filepath)
        )

        return MonitorEvent(

            filepath=event.filepath,

            policy_id=report.policy_id,

            trust_score=report.trust_score,

            decision=report.decision,

            alert_generated=(
                report.decision != "ACCEPT"
            ),

        )