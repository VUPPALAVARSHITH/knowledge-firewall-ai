# src/enterprise/models.py

from dataclasses import dataclass, field
from typing import List, Optional


# -----------------------------
# Policy Summary
# -----------------------------
@dataclass
class PolicySummary:
    policy_id: str
    title: str
    department: str
    category: str
    trust_score: float
    status: str


# -----------------------------
# Chunk Summary
# -----------------------------
@dataclass
class ChunkSummary:
    chunk_id: str
    policy_id: str
    section: str
    trust_score: float
    status: str


# -----------------------------
# Scan Result
# -----------------------------
@dataclass
class ScanResult:
    total_policies: int
    trusted: int
    suspicious: int
    blocked: int
    average_trust: float


# -----------------------------
# Dashboard Summary
# -----------------------------
@dataclass
class DashboardSummary:
    total_policies: int
    total_chunks: int
    trusted_chunks: int
    suspicious_chunks: int
    blocked_chunks: int
    average_trust: float
    system_health: float


# -----------------------------
# Alert
# -----------------------------
@dataclass
class Alert:
    severity: str
    title: str
    description: str


# -----------------------------
# Assistant Response
# -----------------------------
@dataclass
class AssistantResponse:
    answer: str
    trust_score: float
    trusted_chunks: List[str] = field(default_factory=list)
    blocked_chunks: List[str] = field(default_factory=list)