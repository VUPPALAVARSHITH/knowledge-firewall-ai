"""
index_builder.py

Knowledge Firewall AI

Builds the FAISS index from Dataset 4 embeddings.
"""

import json
import faiss
import numpy as np

from src.config.path_config import DATA_DIR


VECTOR_STORE = DATA_DIR / "vector_store"

EMBEDDINGS_FILE = VECTOR_STORE / "embeddings.npy"

INDEX_FILE = VECTOR_STORE / "faiss.index"

INFO_FILE = VECTOR_STORE / "faiss_info.json"


class FaissIndexBuilder:

    def __init__(self):

        self.embeddings = None

        self.index = None

    # --------------------------------------------------------

    def load_embeddings(self):

        print("Loading embeddings...")

        self.embeddings = np.load(EMBEDDINGS_FILE)

        print(f"Loaded {len(self.embeddings)} embeddings.")

    # --------------------------------------------------------

    def build_index(self):

        dimension = self.embeddings.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(self.embeddings)

        print("FAISS index built successfully.")

    # --------------------------------------------------------

    def save_index(self):

        faiss.write_index(

            self.index,

            str(INDEX_FILE)

        )

        print(f"Saved index -> {INDEX_FILE}")

    # --------------------------------------------------------

    def save_metadata(self):

        info = {

            "index_type": "IndexFlatIP",

            "dimension": int(self.embeddings.shape[1]),

            "total_vectors": int(self.embeddings.shape[0]),

            "metric": "Cosine Similarity (Normalized Inner Product)"

        }

        with open(

            INFO_FILE,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                info,

                file,

                indent=4

            )

    # --------------------------------------------------------

    def build(self):

        print("\n" + "=" * 65)

        print("BUILDING FAISS VECTOR INDEX")

        print("=" * 65)

        self.load_embeddings()

        self.build_index()

        self.save_index()

        self.save_metadata()

        print("\n" + "=" * 65)

        print("VECTOR DATABASE READY")

        print("=" * 65)

        print(f"Vectors : {len(self.embeddings)}")

        print(f"Dimension : {self.embeddings.shape[1]}")

        print("=" * 65)


if __name__ == "__main__":

    FaissIndexBuilder().build()