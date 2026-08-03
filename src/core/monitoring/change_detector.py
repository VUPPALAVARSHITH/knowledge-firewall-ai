"""
change_detector.py

Knowledge Firewall AI

Converts repository changes into structured events.
"""

from __future__ import annotations

from datetime import datetime

from src.core.monitoring.monitor_models import FileChange


class ChangeDetector:

    """
    Converts raw filesystem events into
    FileChange objects.
    """

    # -----------------------------------------------------

    def process(self, changes):

        events = []

        for event_type, filepath in changes:

            events.append(

                FileChange(

                    filepath=str(filepath),

                    event=event_type,

                    timestamp=datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )

                )

            )

        return events