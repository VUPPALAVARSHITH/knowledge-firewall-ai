"""
trust_score.py

Knowledge Firewall AI

Computes trust scores for enterprise documents
based on fingerprint similarity.
"""

import hashlib
from difflib import SequenceMatcher


class TrustScoreEngine:

    def __init__(self):
        pass

    # -------------------------------------------------------
    # SHA256 Similarity
    # -------------------------------------------------------

    def sha_match(self, sha1, sha2):

        return 1.0 if sha1 == sha2 else 0.0

    # -------------------------------------------------------
    # SimHash Similarity
    # -------------------------------------------------------

    def simhash_similarity(self, simhash1, simhash2):

        distance = sum(

            c1 != c2

            for c1, c2 in zip(simhash1, simhash2)

        )

        similarity = 1 - (distance / len(simhash1))

        return round(similarity, 4)

    # -------------------------------------------------------
    # Text Similarity
    # -------------------------------------------------------

    def text_similarity(self, text1, text2):

        return round(

            SequenceMatcher(

                None,

                text1,

                text2

            ).ratio(),

            4

        )

    # -------------------------------------------------------
    # Final Trust Score
    # -------------------------------------------------------

    def calculate(

        self,

        sha_score,

        simhash_score,

        text_score

    ):

        trust = (

            0.50 * sha_score +

            0.30 * simhash_score +

            0.20 * text_score

        )

        return round(trust, 4)