"""
integrity_models.py

Knowledge Firewall AI

Data models used by the Integrity Verification Engine.
"""

from dataclasses import dataclass, field


# ---------------------------------------------------------
# Individual Policy Integrity Result
# ---------------------------------------------------------

@dataclass(slots=True)
class IntegrityResult:

    policy_id: str

    department: str

    category: str

    trust_score: float

    repository_similarity: float

    attack_detected: bool

    attack_confidence: float

    sensitive_data_detected: bool

    sensitive_data_score: float

    decision: str

    recommendation: str

    warnings: list[str] = field(default_factory=list)


# ---------------------------------------------------------
# Repository Summary
# ---------------------------------------------------------

@dataclass(slots=True)
class RepositoryIntegritySummary:

    total_policies: int

    trusted_policies: int

    review_required: int

    rejected_policies: int

    average_trust_score: float

    repository_health: str


# ---------------------------------------------------------
# Trust Drift
# ---------------------------------------------------------

@dataclass(slots=True)
class TrustDrift:

    policy_id: str

    previous_trust: float

    current_trust: float

    drift: float

    status: str


# ---------------------------------------------------------
# Integrity Scan Report
# ---------------------------------------------------------

@dataclass(slots=True)
class IntegrityScanReport:

    scan_time: str

    total_policies: int

    average_trust: float

    repository_health: str

    results: list[IntegrityResult]