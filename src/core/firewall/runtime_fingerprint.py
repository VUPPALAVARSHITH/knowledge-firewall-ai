"""
runtime_fingerprint.py

Knowledge Firewall AI

Generates runtime fingerprints for retrieved chunks.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass

from src.core.fingerprint.embedding_engine import EmbeddingEngine
from src.core.fingerprint.simhash_engine import SimHashEngine


@dataclass(slots=True)
class RuntimeFingerprint:

    sha256: str

    simhash: str

    embedding: list[float]


class RuntimeFingerprintGenerator:

    """
    Generates a fresh fingerprint from a retrieved chunk.

    This is used by the Knowledge Firewall to detect
    unauthorized modifications after indexing.
    """

    def __init__(self):

        self.embedding_engine = EmbeddingEngine()

        self.simhash_engine = SimHashEngine()

    # ----------------------------------------------------

    @staticmethod
    def sha256(text: str) -> str:

        return hashlib.sha256(

            text.encode("utf-8")

        ).hexdigest()

    # ----------------------------------------------------

    def generate(self, chunk):

        return RuntimeFingerprint(

            sha256=self.sha256(

                chunk.text

            ),

            simhash=self.simhash_engine.generate(

                chunk.text

            ),

            embedding=self.embedding_engine.generate(

                chunk.text

            )

        )


# ---------------------------------------------------------

if __name__ == "__main__":

    print("Runtime Fingerprint Generator Ready")