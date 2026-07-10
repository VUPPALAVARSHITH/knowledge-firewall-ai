"""
embedding_engine.py

Knowledge Firewall AI

Embedding wrapper around the shared embedding service.
"""

from src.services.embedding_service import EmbeddingService


class EmbeddingEngine:

    def __init__(self):

        self.service = EmbeddingService()

    # --------------------------------------------------

    def generate(self, text):

        return self.service.encode(

            text

        ).tolist()

    # --------------------------------------------------

    def model_name_used(self):

        return self.service.model_name()