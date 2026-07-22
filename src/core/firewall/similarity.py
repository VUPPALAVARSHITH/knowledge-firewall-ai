"""
similarity.py

Knowledge Firewall AI

Similarity computation engine.

Compares runtime fingerprints against trusted fingerprints.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np


@dataclass(slots=True)
class SimilarityResult:
    sha: float
    simhash: float
    embedding: float


class SimilarityEngine:
    """
    Computes similarity metrics between trusted and runtime fingerprints.
    """

    # --------------------------------------------------

    @staticmethod
    def sha_similarity(
        trusted_sha: str,
        runtime_sha: str,
    ) -> float:

        return 1.0 if trusted_sha == runtime_sha else 0.0

    # --------------------------------------------------

    @staticmethod
    def simhash_similarity(
        trusted: str,
        runtime: str,
    ) -> float:

        try:
            trusted_int = int(trusted, 16)
            runtime_int = int(runtime, 16)
        except ValueError:
            return 0.0

        xor = trusted_int ^ runtime_int

        hamming_distance = xor.bit_count()

        return 1.0 - (hamming_distance / 64)

    # --------------------------------------------------

    @staticmethod
    def cosine_similarity(
        trusted_embedding: Iterable[float],
        runtime_embedding: Iterable[float],
    ) -> float:

        a = np.asarray(
            trusted_embedding,
            dtype=np.float32,
        )

        b = np.asarray(
            runtime_embedding,
            dtype=np.float32,
        )

        if a.shape != b.shape:
            return 0.0

        denominator = np.linalg.norm(a) * np.linalg.norm(b)

        if denominator == 0:
            return 0.0

        return float(np.dot(a, b) / denominator)

    # --------------------------------------------------

    def compare(
        self,
        trusted_fp: RuntimeFingerprint,
        runtime_fp: RuntimeFingerprint,
    ) -> SimilarityResult:
        """
        Compare trusted fingerprint with runtime fingerprint.
        """

        return SimilarityResult(

            sha=self.sha_similarity(
                trusted_fp.sha256,
                runtime_fp.sha256,
            ),

            simhash=self.simhash_similarity(
                trusted_fp.simhash,
                runtime_fp.simhash,
            ),

            embedding=self.cosine_similarity(
                trusted_fp.embedding,
                runtime_fp.embedding,
            ),

        )


if __name__ == "__main__":

    print("Similarity Engine Ready")