"""
constants.py

Knowledge Firewall AI

Global constants used across the project.
"""

# ==========================================================
# Document Types
# ==========================================================

DOCUMENT_TYPE_ENTERPRISE = "enterprise_policy"
DOCUMENT_TYPE_POISONED = "poisoned_policy"
DOCUMENT_TYPE_REPOISONED = "repoisoned_policy"
DOCUMENT_TYPE_PROMPT = "prompt_injection"
DOCUMENT_TYPE_SENSITIVE = "sensitive_document"

# ==========================================================
# Chunk Priorities
# ==========================================================

SECTION_PRIORITY = {

    "METADATA": 0.60,

    "TITLE": 0.55,

    "PURPOSE": 0.75,

    "SCOPE": 0.80,

    "DEFINITIONS": 0.65,

    "POLICY_STATEMENT": 1.00,

    "RESPONSIBILITIES": 0.90,

    "EXCEPTIONS": 0.85,

    "COMPLIANCE": 0.95,

    "REVIEW_CYCLE": 0.70,

    "KEYWORDS": 0.50

}

# ==========================================================
# Trust Thresholds
# ==========================================================

TRUST_THRESHOLD = 0.85

SUSPICIOUS_THRESHOLD = 0.65

BLOCK_THRESHOLD = 0.50

# ==========================================================
# Embedding Model
# ==========================================================

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

EMBEDDING_DIMENSION = 384