from dataclasses import dataclass
from typing import List


@dataclass
class DashboardSummary:
    total_policies: int
    total_chunks: int

    trusted_chunks: int
    suspicious_chunks: int
    blocked_chunks: int

    average_trust: float

    repository_health: str

    last_scan: str = "Never"


@dataclass
class Activity:
    timestamp: str
    title: str
    status: str


@dataclass
class Alert:
    severity: str
    title: str
    description: str

from dataclasses import dataclass


@dataclass
class AdmissionReport:

    filename: str

    policy_id: str

    department: str

    category: str

    chunks_created: int

    parser_status: str

    fingerprint_status: str

    repository_similarity: float

    prompt_injection_score: float

    sensitive_data_score: float

    trust_score: float

    decision: str

    recommendation: str

    warnings: list[str]

    processing_time: float

from dataclasses import dataclass, field


@dataclass(slots=True)
class AdmissionReport:

    # Document
    filename: str
    policy_id: str
    department: str
    category: str

    # Parsing
    parser_completed: bool

    # Chunking
    chunks_created: int

    # Fingerprinting
    fingerprint_created: bool

    # Repository
    duplicate_found: bool
    repository_similarity: float

    # Security
    attack_detected: bool
    attack_confidence: float

    sensitive_data_detected: bool
    sensitive_data_score: float

    # Trust
    trust_score: float

    decision: str

    recommendation: str

    warnings: list[str] = field(default_factory=list)

    
from dataclasses import dataclass

@dataclass(slots=True)
class IntegrityReport:

    policy_id: str

    department: str

    trust_score: float

    repository_similarity: float

    attack_detected: bool

    sensitive_data: bool

    decision: str

from dataclasses import dataclass


@dataclass(slots=True)
class IntegrityReport:

    policy_id: str

    department: str

    category: str

    trust_score: float

    repository_similarity: float

    attack_detected: bool

    decision: str