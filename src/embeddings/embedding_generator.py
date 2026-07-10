"""
embedding_generator.py

Knowledge Firewall AI

Generates sentence embeddings for Dataset 4 semantic chunks.
"""

import json
import pickle
from datetime import datetime

import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

from src.config.constants import (
    EMBEDDING_DIMENSION,
    EMBEDDING_MODEL
)

from src.config.path_config import DATA_DIR


VECTOR_STORE = DATA_DIR / "vector_store"

CHUNK_FILE = VECTOR_STORE / "chunk_metadata.pkl"

EMBEDDING_FILE = VECTOR_STORE / "embeddings.npy"

MODEL_INFO = VECTOR_STORE / "embedding_model.json"


class EmbeddingGenerator:

    def __init__(self):

        print("\nLoading embedding model...")

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    # -----------------------------------------------------

    def load_chunks(self):

        with open(CHUNK_FILE, "rb") as file:

            return pickle.load(file)

    # -----------------------------------------------------

    def generate_embeddings(self, chunks):

        corpus = [

            chunk.enriched_text

            for chunk in chunks

        ]

        print()

        print("=" * 70)
        print("Generating Embeddings")
        print("=" * 70)

        embeddings = self.model.encode(

            corpus,

            batch_size=32,

            show_progress_bar=True,

            convert_to_numpy=True,

            normalize_embeddings=True

        )

        embeddings = embeddings.astype(np.float32)

        for chunk, vector in zip(chunks, embeddings):

            chunk.embedding = vector.tolist()

        return chunks, embeddings

    # -----------------------------------------------------

    def save_embeddings(self, embeddings):

        np.save(

            EMBEDDING_FILE,

            embeddings

        )

    # -----------------------------------------------------

    def update_chunk_database(self, chunks):

        with open(

            CHUNK_FILE,

            "wb"

        ) as file:

            pickle.dump(

                chunks,

                file

            )

    # -----------------------------------------------------

    def save_model_info(self, chunks):

        info = {

            "model": EMBEDDING_MODEL,

            "dimension": EMBEDDING_DIMENSION,

            "normalized": True,

            "total_chunks": len(chunks),

            "created_at": datetime.now().isoformat()

        }

        with open(

            MODEL_INFO,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                info,

                file,

                indent=4

            )

    # -----------------------------------------------------

    def generate(self):

        chunks = self.load_chunks()

        print(f"\nLoaded {len(chunks)} chunks.")

        chunks, embeddings = self.generate_embeddings(chunks)

        self.save_embeddings(embeddings)

        self.update_chunk_database(chunks)

        self.save_model_info(chunks)

        print()

        print("=" * 70)
        print("EMBEDDING GENERATION COMPLETED")
        print("=" * 70)
        print(f"Chunks          : {len(chunks)}")
        print(f"Dimension       : {EMBEDDING_DIMENSION}")
        print(f"Model           : {EMBEDDING_MODEL}")
        print(f"Embeddings File : {EMBEDDING_FILE}")
        print(f"Chunk Database  : {CHUNK_FILE}")
        print(f"Model Info      : {MODEL_INFO}")
        print("=" * 70)


if __name__ == "__main__":

    EmbeddingGenerator().generate()