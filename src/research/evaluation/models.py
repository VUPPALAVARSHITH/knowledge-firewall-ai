"""
models.py

Knowledge Firewall AI

Evaluation data models.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class EvaluationRecord:
    """
    One evaluation sample.
    """

    chunk_id: str

    policy_id: str

    department: str

    category: str

    section: str

    is_poisoned: bool

    attack_type: str

    severity: str

    expected_decision: str

    source_file: str


@dataclass(slots=True)
class EvaluationResult:
    """
    Output after firewall evaluation.
    """

    chunk_id: str

    policy_id: str

    expected_decision: str

    predicted_decision: str

    trust_score: float

    correct: bool