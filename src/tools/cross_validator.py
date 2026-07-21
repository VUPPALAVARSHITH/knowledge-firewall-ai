"""
cross_validator.py

Knowledge Firewall AI

Performs cross-dataset integrity validation.

Checks:

1. Policy consistency
2. Chunk consistency
3. Relation consistency
4. Attack log consistency
5. SHA256 consistency
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


class CrossRepositoryValidator:

    def __init__(self, metadata_dir: Path):

        self.metadata_dir = metadata_dir

        self.errors = []
        self.warnings = []

    # =========================================================

    def load(self):

        self.policy_index = pd.read_csv(
            self.metadata_dir / "policy_index.csv"
        )

        self.fingerprint = pd.read_csv(
            self.metadata_dir / "fingerprint_database.csv"
        )

        self.chunk_fp = pd.read_csv(
            self.metadata_dir / "chunk_fingerprint_database.csv"
        )

        self.relations = pd.read_csv(
            self.metadata_dir / "document_relations.csv"
        )

        self.attack_log = pd.read_csv(
            self.metadata_dir / "attack_log.csv"
        )

    # =========================================================

    def validate(self):

        self.load()

        print("\nCross Repository Validation")
        print("-" * 70)

        self.validate_policy_index()

        self.validate_chunks()

        self.validate_relations()

        self.validate_attack_log()

        self.validate_sha256()

        print()

        print("Cross Validation Complete")

        print(f"Errors   : {len(self.errors)}")

        print(f"Warnings : {len(self.warnings)}")

        return self.errors, self.warnings

        # =========================================================

    def validate_policy_index(self):

        index = set(self.policy_index.policy_id)

        fingerprint = set(self.fingerprint.policy_id)

        missing = index - fingerprint

        if missing:

            self.errors.append(

                f"{len(missing)} policies missing fingerprints."

            )

            print(f"[ERROR] Missing fingerprints : {len(missing)}")

        else:

            print("[OK] Policy ↔ Fingerprint consistency")

        # =========================================================

    def validate_chunks(self):

        policies = set(self.policy_index.policy_id)

        chunks = set(self.chunk_fp.policy_id)

        orphan = chunks - policies

        if orphan:

            self.errors.append(

                f"{len(orphan)} orphan chunk policies."

            )

            print(f"[ERROR] Orphan chunks : {len(orphan)}")

        else:

            print("[OK] Chunk ↔ Policy consistency")

        # =========================================================

    def validate_relations(self):

        policies = set(self.policy_index.policy_id)

        source = set(self.relations.source_policy)

        target = set(self.relations.target_policy)

        bad_source = source - policies

        bad_target = target - policies

        if bad_source:

            self.errors.append(

                f"{len(bad_source)} invalid source policies."

            )

        if bad_target:

            self.errors.append(

                f"{len(bad_target)} invalid target policies."

            )

        if not bad_source and not bad_target:

            print("[OK] Relation consistency")

    
        # =========================================================

    def validate_relations(self):

        policies = set(self.policy_index.policy_id)

        source = set(self.relations.source_policy)

        target = set(self.relations.target_policy)

        bad_source = source - policies

        bad_target = target - policies

        if bad_source:

            self.errors.append(

                f"{len(bad_source)} invalid source policies."

            )

        if bad_target:

            self.errors.append(

                f"{len(bad_target)} invalid target policies."

            )

        if not bad_source and not bad_target:

            print("[OK] Relation consistency")

    
        # =========================================================

    def validate_attack_log(self):

        policies = set(self.policy_index.policy_id)

        attacks = set(self.attack_log.policy_id)

        orphan = attacks - policies

        if orphan:

            self.errors.append(

                f"{len(orphan)} orphan attacks."

            )

        else:

            print("[OK] Attack Log consistency")

    
        # =========================================================

    def validate_sha256(self):

        merged = self.policy_index.merge(

            self.fingerprint,

            on="policy_id",

            suffixes=("_index", "_fp")

        )

        mismatch = (

            merged.sha256_index !=

            merged.sha256_fp

        ).sum()

        if mismatch:

            self.errors.append(

                f"{mismatch} SHA256 mismatches."

            )

        else:

            print("[OK] SHA256 consistency")

    
    
