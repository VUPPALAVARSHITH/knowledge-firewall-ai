"""
vector_store.py

Knowledge Firewall AI

Production Vector Store
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import faiss
import numpy as np
import pandas as pd

from src.config.path_config import DATA_DIR


VECTOR_STORE_DIR = DATA_DIR / "vector_store"

INDEX_PATH = VECTOR_STORE_DIR / "faiss.index"
CHUNK_PATH = VECTOR_STORE_DIR / "chunk_metadata.csv"


# ==========================================================
# Chunk Model
# ==========================================================

@dataclass(slots=True)
class Chunk:

    chunk_id: str

    policy_id: str

    department: str

    category: str

    section: str

    text: str

    trust_score: float

    decision: str

    risk_level: str


# ==========================================================
# Enterprise Vector Store
# ==========================================================

class EnterpriseVectorStore:
    """
    Wrapper around FAISS.

    Responsibilities
    ----------------
    1. Load vector index
    2. Load chunk metadata
    3. Perform semantic search
    4. Return enterprise chunk objects
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

        df = pd.read_csv(CHUNK_PATH)

        self.chunks = []

        for _, row in df.iterrows():

            status = row["status"]

            if status == "Trusted":
                trust = 100.0
            elif status == "Suspicious":
                trust = 60.0
            elif status == "Blocked":
                trust = 0.0
            else:
                trust = 80.0

            self.chunks.append(

                Chunk(

                    chunk_id=row["chunk_id"],

                    policy_id=row["policy_id"],

                    department=row["department"],

                    category=row["category"],

                    section=row["section"],

                    text=row["text"],

                    trust_score=trust,

                    decision=status,

                    risk_level=row["risk_level"]

                )

            )

        self.loaded = True

        print("=" * 60)
        print("Vector Store Loaded")
        print("=" * 60)
        print(f"Vectors : {self.index.ntotal}")
        print(f"Chunks  : {len(self.chunks)}")
        print("=" * 60)

    # ---------------------------------------------------------
    # Size
    # ---------------------------------------------------------

    @property
    def size(self):

        if not self.loaded:
            self.load()

        return self.index.ntotal

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    def search(

        self,

        query_embedding: np.ndarray,

        top_k: int = 5,

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

            results.append(

                {

                    "score": float(score),

                    "chunk": self.chunks[idx]

                }

            )

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

        risk_level=None,

    ):

        if not self.loaded:
            self.load()

        results = []

        for chunk in self.chunks:

            if department and chunk.department != department:
                continue

            if category and chunk.category != category:
                continue

            if risk_level and chunk.risk_level != risk_level:
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