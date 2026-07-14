"""
test_fingerprint.py

Knowledge Firewall AI

Compares one clean enterprise document with its
poisoned version and computes fingerprint similarity.
"""

from pathlib import Path
from difflib import SequenceMatcher
import torch
import json
from sentence_transformers import util

from src.config.path_config import (
    ENTERPRISE_DIR,
    POISONED_DIR
)

from src.core.fingerprint.embedding_engine import EmbeddingEngine
from src.core.fingerprint.fingerprint_engine import FingerprintEngine
from src.core.fingerprint.trust_score import TrustScoreEngine


def main():

    engine = FingerprintEngine()

    trust = TrustScoreEngine()


    # ---------------------------------------------------
    # Pick one document
    # ---------------------------------------------------

    clean_file = None
    poisoned_file = None
    
    for candidate in ENTERPRISE_DIR.rglob("*.txt"):
        
        poisoned = POISONED_DIR / candidate.relative_to(ENTERPRISE_DIR)
        
        if not poisoned.exists():
            continue
        
        clean = candidate.read_text(encoding="utf-8")
        poison = poisoned.read_text(encoding="utf-8")
        
        if clean != poison:
            clean_file = candidate
            poisoned_file = poisoned
            break
    
    if clean_file is None:
        raise Exception("No poisoned documents found.")

    print("=" * 60)
    print("Testing Knowledge Fingerprint")
    print("=" * 60)

    print("Policy :", clean_file.stem)
    print()

    # ---------------------------------------------------
    # Read text
    # ---------------------------------------------------

    clean_text = clean_file.read_text(
        encoding="utf-8"
    )

    poisoned_text = poisoned_file.read_text(
        encoding="utf-8"
    )

    print("Are both texts identical?")
    print(clean_text == poisoned_text)
    print()
    print("========== CLEAN ==========")
    print(clean_text)
    print()
    print("========== POISONED ==========")
    print(poisoned_text)
    print()

    # ---------------------------------------------------
    # Fingerprints
    # ---------------------------------------------------

    clean_fp = engine.generate(

        clean_file,

        clean_file.parent.parent.name,

        clean_file.parent.name,

        clean_file.stem

    )

    poison_fp = engine.generate(

        poisoned_file,

        poisoned_file.parent.parent.name,

        poisoned_file.parent.name,

        poisoned_file.stem

    )

    # ---------------------------------------------------
    # Similarities
    # ---------------------------------------------------

    sha = trust.sha_match(

        clean_fp["sha256"],

        poison_fp["sha256"]

    )

    simhash = trust.simhash_similarity(

        clean_fp["simhash"],

        poison_fp["simhash"]

    )

    text = trust.text_similarity(

        clean_text,

        poisoned_text

    )
    
    emb1 = torch.tensor(
        json.loads(clean_fp["embedding"])
    )
    
    emb2 = torch.tensor(
        json.loads(poison_fp["embedding"])
    )

    print()
    print("Embedding Shape 1:", emb1.shape)
    print("Embedding Shape 2:", emb2.shape)
    print()
    print("First 10 Values")
    print(emb1[:10])
    print()
    print(emb2[:10])
    print()

    embedding_similarity = util.cos_sim(
        emb1,
        emb2
    ).item()

    final_score = (

        0.30 * sha +

        0.20 * simhash +

        0.20 * text +

        0.30 * embedding_similarity

    )

    print(f"SHA256 Match         : {sha:.3f}")
    print(f"SimHash Similarity   : {simhash:.3f}")
    print(f"Text Similarity      : {text:.3f}")
    print(f"Embedding Similarity : {embedding_similarity:.3f}")
    print()

    print(f"Trust Score          : {final_score:.3f}")

    if final_score > 0.90:
        status = "TRUSTED"

    elif final_score > 0.70:
        status = "WARNING"

    else:
        status = "SUSPICIOUS"

    print(f"Status               : {status}")

    print("=" * 60)


if __name__ == "__main__":
    main()