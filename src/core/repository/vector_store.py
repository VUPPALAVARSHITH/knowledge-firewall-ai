"""
vector_store.py

Knowledge Firewall AI

Production Vector Store
"""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import List, Optional

import faiss
import numpy as np

from src.config.path_config import DATA_DIR


VECTOR_STORE_DIR = DATA_DIR / "vector_store"

INDEX_PATH = VECTOR_STORE_DIR / "faiss.index"
CHUNK_PATH = VECTOR_STORE_DIR / "chunk_metadata.pkl"


class EnterpriseVectorStore:
    """
    Wrapper around FAISS.

    Responsibilities
    ----------------
    1. Load index
    2. Load chunk metadata
    3. Search vectors
    4. Return Chunk objects
    """

    def __init__(self):

        self.index: Optional[faiss.Index] = None

        self.chunks = []

        self.loaded = False

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def load(self):

        if self.loaded:
            return

        if not INDEX_PATH.exists():
            raise FileNotFoundError(INDEX_PATH)

        if not CHUNK_PATH.exists():
            raise FileNotFoundError(CHUNK_PATH)

        self.index = faiss.read_index(str(INDEX_PATH))

        with open(CHUNK_PATH, "rb") as f:

            self.chunks = pickle.load(f)

        self.loaded = True

        print("=" * 60)
        print("Vector Store Loaded")
        print("=" * 60)
        print(f"Vectors : {self.index.ntotal}")
        print(f"Chunks  : {len(self.chunks)}")
        print("=" * 60)

    # ---------------------------------------------------------
    # Total vectors
    # ---------------------------------------------------------

    @property
    def size(self):

        return self.index.ntotal

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    def search(
        self,
        query_embedding: np.ndarray,
        top_k: int = 5
    ):

        if not self.loaded:
            self.load()

        if query_embedding.ndim == 1:
            query_embedding = query_embedding.reshape(1, -1)

        scores, indices = self.index.search(
            query_embedding.astype(np.float32),
            top_k
        )

        results = []

        for score, idx in zip(scores[0], indices[0]):

            if idx == -1:
                continue

            results.append({

                "score": float(score),

                "chunk": self.chunks[idx]

            })

        return results

    # ---------------------------------------------------------
    # Get Chunk
    # ---------------------------------------------------------

    def get_chunk(
        self,
        chunk_id: str
    ):

        if not self.loaded:
            self.load()

        for chunk in self.chunks:

            if chunk.chunk_id == chunk_id:

                return chunk

        return None

    # ---------------------------------------------------------
    # Filter
    # ---------------------------------------------------------

    def filter(
        self,
        department=None,
        category=None,
        risk_level=None
    ):

        if not self.loaded:
            self.load()

        results = []

        for chunk in self.chunks:

            if department:

                if chunk.department != department:
                    continue

            if category:

                if chunk.category != category:
                    continue

            if risk_level:

                if chunk.risk_level != risk_level:
                    continue

            results.append(chunk)

        return results

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def statistics(self):

        if not self.loaded:
            self.load()

        return {

            "vectors": self.index.ntotal,

            "chunks": len(self.chunks)

        }


# ---------------------------------------------------------
# Test
# ---------------------------------------------------------

if __name__ == "__main__":

    store = EnterpriseVectorStore()

    store.load()

    print(store.statistics())