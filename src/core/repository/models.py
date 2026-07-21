"""
models.py

Knowledge Firewall AI

Repository Models

Canonical models used for storing and managing
trusted enterprise knowledge.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class PolicyMetadata:
    """
    Canonical metadata representation of an enterprise policy.

    This model mirrors the structure of policy_index.csv and is
    used by RepositoryWriter for repository persistence.
    """

    policy_id: str

    title: str

    department: str

    category: str

    security_domain: str

    classification: str

    risk_level: str

    owner: str

    effective_date: str

    review_date: str

    word_count: int

    char_count: int

    sha256: str

    filepath: str

    keywords: list[str]