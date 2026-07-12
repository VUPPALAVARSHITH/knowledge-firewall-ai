"""
similarity.py

Knowledge Firewall AI

Similarity computation engine.
"""

from __future__ import annotations

import hashlib
from typing import Iterable

import numpy as np


class SimilarityEngine:
    """
    Computes similarity metrics between
    trusted fingerprints and retrieved chunks.
    """

    # --------------------------------------------------

    @staticmethod
    def sha256(text: str) -> str:

        return hashlib.sha256(

            text.encode("utf-8")

        ).hexdigest()

    # --------------------------------------------------

    @staticmethod
    def sha_similarity(

        trusted_sha: str,

        current_sha: str

    ) -> float:

        return 1.0 if trusted_sha == current_sha else 0.0

    # --------------------------------------------------

    @staticmethod
    def simhash_similarity(

        trusted: str,

        current: str

    ) -> float:

        if len(trusted) != len(current):

            return 0.0

        matches = sum(

            a == b

            for a, b in zip(trusted, current)

        )

        return matches / len(trusted)

    # --------------------------------------------------

    @staticmethod
    def cosine_similarity(

        trusted_embedding: Iterable[float],

        current_embedding: Iterable[float]

    ) -> float:

        a = np.asarray(

            trusted_embedding,

            dtype=np.float32

        )

        b = np.asarray(

            current_embedding,

            dtype=np.float32

        )

        denominator = (

            np.linalg.norm(a)

            * np.linalg.norm(b)

        )

        if denominator == 0:

            return 0.0

        return float(

            np.dot(a, b) / denominator

        )

    # --------------------------------------------------

    def compare(

        self,

        trusted_fp,

        current_chunk

    ):

        sha = self.sha_similarity(

            trusted_fp.sha256,

            self.sha256(

                current_chunk.text

            )

        )

        simhash = self.simhash_similarity(

            trusted_fp.simhash,

            trusted_fp.simhash
        )

        embedding = self.cosine_similarity(

            trusted_fp.embedding,

            current_chunk.embedding

        )

        return {

            "sha": round(sha, 4),

            "simhash": round(simhash, 4),

            "embedding": round(embedding, 4)

        }


if __name__ == "__main__":

    print("Similarity Engine Ready")