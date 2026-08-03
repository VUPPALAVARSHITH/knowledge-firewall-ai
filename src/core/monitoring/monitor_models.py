"""
monitor_models.py

Knowledge Firewall AI

Models used by Continuous Monitoring.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class FileChange:

    filepath: str

    event: str

    timestamp: str


@dataclass(slots=True)
class MonitorEvent:

    filepath: str

    policy_id: str

    trust_score: float

    decision: str

    alert_generated: bool