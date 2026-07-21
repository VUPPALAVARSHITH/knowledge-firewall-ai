"""
models.py

Knowledge Firewall AI

Common data models used across the preprocessing pipeline.
"""

from dataclasses import dataclass, field
from typing import List, Optional


# ==========================================================
# Policy Model
# ==========================================================

@dataclass
class Policy:

    # ----------------------------
    # Enterprise Metadata
    # ----------------------------

    policy_id: str

    department: str

    category: str

    security_domain: str

    classification: str

    risk_level: str

    version: str

    status: str

    owner: str

    # ----------------------------
    # Sections
    # ----------------------------

    title: str

    purpose: str

    scope: str

    definitions: List[str] = field(default_factory=list)

    policy_statements: List[str] = field(default_factory=list)

    responsibilities: List[str] = field(default_factory=list)

    exceptions: List[str] = field(default_factory=list)

    compliance: List[str] = field(default_factory=list)

    review_cycle: str = ""

    keywords: List[str] = field(default_factory=list)

    source_file: str = ""


# ==========================================================
# Chunk Model
# ==========================================================

@dataclass
class Chunk:

    # ----------------------------
    # Identity
    # ----------------------------

    chunk_id: str

    policy_id: str

    # ----------------------------
    # Enterprise Metadata
    # ----------------------------

    department: str

    category: str

    security_domain: str

    classification: str

    risk_level: str

    version: str

    status: str

    owner: str

    # ----------------------------
    # Chunk Metadata
    # ----------------------------

    section: str
    chunk_order: int
    priority: float = 1.0
    statement_number: Optional[int] = None
    
    # ----------------------------
    # Content
    # ----------------------------
     
    text: str = ""
    enriched_text: str = ""
    keywords: List[str] = field(default_factory=list)

    word_count: int = 0

    character_count: int = 0

    # ----------------------------
    # Source
    # ----------------------------

    source_file: str = ""

    # ----------------------------
    # Dataset Metadata
    # ----------------------------

    document_type: str = "enterprise_policy"

    is_poisoned: bool = False

    created_from: str = "Dataset-1"

    embedding: Optional[List[float]] = None