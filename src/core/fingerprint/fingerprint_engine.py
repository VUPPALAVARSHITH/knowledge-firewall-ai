"""
fingerprint_engine.py

Knowledge Firewall AI

Generates structural fingerprints for enterprise documents.
"""

import hashlib
from pathlib import Path
import re
from src.core.fingerprint.simhash_engine import SimHashEngine
from datetime import datetime
import json

from src.core.fingerprint.embedding_engine import EmbeddingEngine

class FingerprintEngine:

    def __init__(self):

        self.simhash = SimHashEngine()
        self.embedding = EmbeddingEngine()

    # ---------------------------------------------------------
    # SHA256
    # ---------------------------------------------------------

    def sha256(self, filepath):

        with open(filepath, "rb") as f:

            return hashlib.sha256(
                f.read()
            ).hexdigest()

    # ---------------------------------------------------------
    # Extract Title
    # ---------------------------------------------------------

    def extract_title(self, text):

        lines = text.splitlines()

        for i, line in enumerate(lines):

            if line.strip() == "TITLE":

                if i + 2 < len(lines):

                    return lines[i + 2].strip()

        return ""
    # ---------------------------------------------------------
    # Extract Policy Statements
    # ---------------------------------------------------------

    def extract_policy_statements(self, text):
        
        start = "4. POLICY STATEMENTS"
        end = "5. RESPONSIBILITIES"
        
        if start not in text or end not in text:
            return text
        
        section = text.split(start, 1)[1]
        section = section.split(end, 1)[0]
        
        return section.strip()

    # ---------------------------------------------------------
    # Generate Fingerprint
    # ---------------------------------------------------------

    def generate(
        self,
        filepath,
        department,
        category,
        policy_id
    ):

        filepath = Path(filepath)

        text = filepath.read_text(
            encoding="utf-8"
        )
        policy_text = self.extract_policy_statements(text)
        
        embedding = self.embedding.generate(
            policy_text
        )

        return {
            "policy_id": policy_id,
            "department": department,
            "category": category,
            "title": self.extract_title(text),
            "sha256": self.sha256(filepath),
            "simhash": self.simhash.generate(policy_text),
            "embedding": json.dumps(embedding),
            "embedding_model": self.embedding.model_name_used(),
            "word_count": len(text.split()),
            "policy_statement_words": len(policy_text.split()),
            "character_count": len(text),
            "sentence_count": len(
                [s for s in re.split(r"[.!?]+", text) if s.strip()]
            ),
            "file_size": filepath.stat().st_size,
            "trust_score": 1.0,
            "document_version": "original",
            "fingerprint_version": "v1.0",
            "created_at": datetime.now().isoformat()
        }