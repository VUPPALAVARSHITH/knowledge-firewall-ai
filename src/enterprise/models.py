from dataclasses import dataclass, field


# ==========================================================
# Dashboard
# ==========================================================

@dataclass(slots=True)
class DashboardSummary:
    total_policies: int
    total_chunks: int
    trusted_chunks: int
    suspicious_chunks: int
    blocked_chunks: int
    average_trust: float
    repository_health: str
    last_scan: str = "Never"


@dataclass(slots=True)
class Activity:
    timestamp: str
    title: str
    status: str


@dataclass(slots=True)
class Alert:
    severity: str
    title: str
    description: str


# ==========================================================
# Knowledge Admission
# ==========================================================

@dataclass(slots=True)
class AdmissionReport:

    filename: str

    policy_id: str

    department: str

    category: str

    parser_completed: bool

    chunks_created: int

    fingerprint_created: bool

    duplicate_found: bool
    repository_similarity: float

    attack_detected: bool
    attack_confidence: float

    sensitive_data_detected: bool
    sensitive_data_score: float

    trust_score: float

    decision: str

    recommendation: str

    warnings: list[str] = field(default_factory=list)


# ==========================================================
# Repository Integrity
# ==========================================================

@dataclass(slots=True)
class IntegrityReport:

    policy_id: str

    department: str

    category: str

    trust_score: float

    repository_similarity: float

    attack_detected: bool

    sensitive_data_detected: bool

    decision: str


# ==========================================================
# Comparison Report
# ==========================================================

@dataclass(slots=True)
class ComparisonReport:

    policy_a: str

    policy_b: str

    semantic_similarity: float

    repository_similarity: float

    attack_detected: bool

    sensitive_data_detected: bool

    trust_score: float

    decision: str

    recommendation: str