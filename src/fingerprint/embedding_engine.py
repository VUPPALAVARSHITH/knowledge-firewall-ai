"""
embedding_engine.py

Knowledge Firewall AI

Generates semantic embeddings for enterprise
knowledge documents.
"""

from sentence_transformers import SentenceTransformer


class EmbeddingEngine:

    def __init__(self):

        self.model_name = "all-MiniLM-L6-v2"

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            self.model_name
        )

        print("Embedding model loaded.")

    def generate(self, text):

        embedding = self.model.encode(

            text,

            normalize_embeddings=True

        )

        return embedding.tolist()

    def model_name_used(self):

        return self.model_name