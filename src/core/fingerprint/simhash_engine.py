"""
simhash_engine.py

Knowledge Firewall AI

Generates SimHash fingerprints for enterprise documents.
"""

import hashlib


class SimHashEngine:

    def __init__(self, bits=64):
        self.bits = bits

    def _hash(self, token):
        return int(hashlib.md5(token.encode()).hexdigest(), 16)

    def generate(self, text):

        tokens = text.lower().split()

        vector = [0] * self.bits

        for token in tokens:

            h = self._hash(token)

            for i in range(self.bits):

                if h & (1 << i):
                    vector[i] += 1
                else:
                    vector[i] -= 1

        fingerprint = 0

        for i in range(self.bits):

            if vector[i] > 0:
                fingerprint |= (1 << i)

        return format(fingerprint, "016x")