"""
models.py

Knowledge Firewall AI

Security Result Models.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class RepositoryCheckResult:

    duplicate: bool

    similarity: float

    matched_policy: str | None

    recommendation: str


@dataclass(slots=True)
class AttackResult:

    attack_id: str | None

    category: str | None

    severity: str

    confidence: float

    matched_text: str

    recommendation: str

    is_attack: bool