"""
models.py

Knowledge Firewall AI

Shared models for the Knowledge Admission Firewall.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


# ============================================================
# Repository Checker
# ============================================================

@dataclass(slots=True)
class RepositoryCheckResult:
    """
    Result of repository similarity analysis.
    """

    duplicate: bool

    similarity: float

    matched_policy: Optional[str]

    recommendation: str

    reason: str = ""


# ============================================================
# Attack Detection
# ============================================================

@dataclass(slots=True)
class AttackResult:
    """
    Result of semantic attack detection.
    """

    attack_id: Optional[str]

    category: Optional[str]

    severity: str

    confidence: float

    matched_text: str

    recommendation: str

    is_attack: bool


# ============================================================
# Sensitive Data Detection
# ============================================================

@dataclass(slots=True)
class SensitiveDataResult:
    """
    Sensitive information discovered during upload.
    """

    emails: list[str] = field(default_factory=list)

    urls: list[str] = field(default_factory=list)

    ipv4_addresses: list[str] = field(default_factory=list)

    api_keys: list[str] = field(default_factory=list)

    bearer_tokens: list[str] = field(default_factory=list)

    private_keys: list[str] = field(default_factory=list)

    total_findings: int = 0

    risk_score: float = 0.0

    recommendation: str = "Accept"


# ============================================================
# Admission Trust
# ============================================================

@dataclass(slots=True)
class AdmissionTrustResult:
    """
    Final trust score for uploaded knowledge.
    """

    repository_score: float

    attack_score: float

    sensitive_score: float

    trust_score: float

    decision: str


# ============================================================
# Final Firewall Report
# ============================================================

@dataclass(slots=True)
class AdmissionReport:
    """
    Final output produced by the
    Knowledge Admission Firewall.
    """

    document_id: str

    filename: str

    repository_result: RepositoryCheckResult

    attack_result: AttackResult

    sensitive_result: SensitiveDataResult

    trust_result: AdmissionTrustResult

    decision: str

    processing_time: float

    timestamp: datetime = field(default_factory=datetime.utcnow)