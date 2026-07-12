from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass(slots=True)
class ChunkFingerprint:
    """
    Trusted fingerprint for one semantic chunk.
    """

    # ----------------------------------------------------
    # Identity
    # ----------------------------------------------------

    chunk_id: str
    policy_id: str

    # ----------------------------------------------------
    # Enterprise Metadata
    # ----------------------------------------------------

    department: str
    category: str
    section: str

    # ----------------------------------------------------
    # Fingerprints
    # ----------------------------------------------------

    sha256: str
    simhash: str

    embedding: list[float] = field(default_factory=list)

    embedding_model: str = ""

    embedding_dimension: int = 384

    # ----------------------------------------------------
    # Statistics
    # ----------------------------------------------------

    word_count: int = 0

    character_count: int = 0

    # ----------------------------------------------------
    # Trust
    # ----------------------------------------------------

    trust_score: float = 1.0

    fingerprint_version: str = "2.0"

    created_at: str = ""

    # ----------------------------------------------------
    # Source
    # ----------------------------------------------------

    source_file: str = ""

    is_poisoned: bool = False

    # ----------------------------------------------------
    # Runtime
    # ----------------------------------------------------

    similarity_score: Optional[float] = None

    decision: Optional[str] = None