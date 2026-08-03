"""
models.py

Knowledge Firewall AI

Shared models for Layer-1 component evaluation.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


@dataclass(slots=True)
class BinaryEvaluationResult:
    """
    Result of one binary classification case.
    """

    experiment: str
    case_id: str
    expected: bool
    predicted: bool
    correct: bool
    details: dict[str, Any]

    def to_dict(self):
        return asdict(self)


@dataclass(slots=True)
class AdmissionEvaluationResult:
    """
    Result of one final admission decision case.
    """

    case_id: str
    expected: str
    predicted: str
    correct: bool
    trust_score: float
    details: dict[str, Any]

    def to_dict(self):
        return asdict(self)