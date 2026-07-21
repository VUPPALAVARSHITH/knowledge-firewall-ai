"""
Knowledge Repository Auditor
============================

Performs integrity and quality checks on the Knowledge Firewall AI repository.

Checks:
- Directory structure
- CSV integrity
- Duplicate columns
- Duplicate rows
- Missing values
- Metadata validation
- Enterprise corpus validation

Author: Knowledge Firewall AI
"""

from __future__ import annotations
from src.tools.cross_validator import CrossRepositoryValidator
from pathlib import Path
from collections import Counter
from datetime import datetime
from src.tools.vector_store_validator import VectorStoreValidator
import pandas as pd
from src.tools.generated_dataset_validator import GeneratedDatasetValidator


class KnowledgeRepositoryAuditor:
    """Audits the Knowledge Firewall repository."""

    def __init__(self, project_root: Path | None = None):
        if project_root is None:
            project_root = Path(__file__).resolve().parents[2]

        self.project_root = project_root
        self.data_dir = self.project_root / "data"
        self.audit_dir = self.project_root / "audit"

        self.audit_dir.mkdir(exist_ok=True)

        self.report: list[str] = []
        self.warning_count = 0
        self.error_count = 0
        self.success_count = 0

    # ==========================================================
    # Public Entry
    # ==========================================================

    def audit(self):
        print("=" * 70)
        print("Knowledge Repository Auditor")
        print("=" * 70)

        self.report.append("# Knowledge Repository Audit Report\n")
        self.report.append(f"Generated: {datetime.now()}\n")

        self.audit_directories()
        self.audit_metadata()
        self.audit_enterprise()

        cross_validator = CrossRepositoryValidator(
            self.data_dir / "metadata"
        )

        errors, warnings = cross_validator.validate()

        self.error_count += len(errors)
        self.warning_count += len(warnings)


        vector_validator = VectorStoreValidator(
            self.data_dir / "vector_store"
        )

        errors, warnings = vector_validator.validate()

        self.error_count += len(errors)
        self.warning_count += len(warnings)


        generated_validator = GeneratedDatasetValidator(
            self.data_dir / "generated"
        )

        errors, warnings = generated_validator.validate()

        self.error_count += len(errors)
        self.warning_count += len(warnings)

        # ----------------------------------------

        self.write_report()

        print("\nSummary")
        print("-" * 70)
        print(f"Passed   : {self.success_count}")
        print(f"Warnings : {self.warning_count}")
        print(f"Errors   : {self.error_count}")

    # ==========================================================
    # Directory Checks
    # ==========================================================

    def audit_directories(self):
        print("\nDirectory Check")
        print("-" * 70)

        required = [
            "metadata",
            "enterprise",
            "generated",
            "vector_store",
        ]

        for folder in required:
            path = self.data_dir / folder

            if path.exists():
                self.success(f"Directory exists : {folder}")
            else:
                self.error(f"Missing directory : {folder}")

    # ==========================================================
    # Metadata
    # ==========================================================

    def audit_metadata(self):
        metadata = self.data_dir / "metadata"

        if not metadata.exists():
            self.error("Metadata directory missing.")
            return

        print("\nMetadata")
        print("-" * 70)

        for csv_file in sorted(metadata.glob("*.csv")):
            self.audit_csv(csv_file)

    # ==========================================================
    # Generic CSV Audit
    # ==========================================================

    def audit_csv(self, csv_path: Path):

        print(f"\n{csv_path.name}")

        # -----------------------------
        # Duplicate header detection
        # -----------------------------

        with open(csv_path, "r", encoding="utf-8") as f:
            header = f.readline().strip().split(",")

        duplicates = [
            col
            for col, count in Counter(header).items()
            if count > 1
        ]

        if duplicates:
            self.warning(
                f"{csv_path.name}: Duplicate columns -> {duplicates}"
            )

        # -----------------------------
        # Safe CSV loading
        # -----------------------------

        try:
            df = pd.read_csv(csv_path)

        except Exception as e:
            self.error(f"{csv_path.name}: Cannot read CSV")
            print(e)
            return

        rows, cols = df.shape

        # -----------------------------
        # Print Schema
        # -----------------------------

        print("\nColumns:")

        for col in df.columns:
            print(f"  • {col}")

        self.report.append("\nColumns:")
        
        for col in df.columns:
            self.report.append(f"- {col}")

        print(f"Rows    : {rows}")
        print(f"Columns : {cols}")

        self.report.append(f"\n## {csv_path.name}")
        self.report.append(f"- Rows: {rows}")
        self.report.append(f"- Columns: {cols}")

        # -----------------------------
        # Missing Values
        # -----------------------------

        ignore_missing = {
            "similarity_score",
            "decision",
        }

        missing = int(
            df.drop(
                columns=[c for c in ignore_missing if c in df.columns]
            ).isna().sum().sum()
        )

        print(f"Missing Values : {missing}")

        if missing:
            self.warning(
                f"{csv_path.name}: {missing} missing values"
            )

        # -----------------------------
        # Duplicate Rows
        # -----------------------------

        duplicate_rows = int(df.duplicated().sum())

        print(f"Duplicate Rows : {duplicate_rows}")

        if duplicate_rows:
            self.warning(
                f"{csv_path.name}: {duplicate_rows} duplicate rows"
            )

        # -----------------------------
        # Metadata Specific Checks
        # -----------------------------
        
        # -----------------------------
        # # Dataset Specific Validation
        # # -----------------------------

        match csv_path.stem:
            case "fingerprint_database":
                self.audit_fingerprint_database(df)
                
            case "chunk_fingerprint_database":
                self.audit_chunk_fingerprint_database(df)
                
            case "policy_index":
                self.audit_policy_index(df)

            case "document_relations":
                self.audit_document_relations(df)

            case "attack_log":
                self.audit_attack_log(df)

            case "generation_log":
                self.audit_generation_log(df)

        self.success(f"{csv_path.name} audited.")

    # ==========================================================
    # Metadata Validation
    # ==========================================================

    

    # ==========================================================
    # Dataset Specific Validators
    # ==========================================================

    def audit_fingerprint_database(self, df):
        
        print("Running fingerprint validation...")

        self.report.append("\nFingerprint Database")
        self.report.append("-" * 40)

        total = len(df)

        print(f"Documents : {total}")
        self.report.append(f"Documents : {total}")
        self.report.append(
            f"Unique Policy IDs : {df['policy_id'].nunique()}"
        )
        
        self.report.append(
            f"Unique SHA256 : {df['sha256'].nunique()}"
        )
        
        self.report.append(
            f"Unique SimHash : {df['simhash'].nunique()}"
        )

        self.report.append(
            f"Embedding Model : {df['embedding_model'].iloc[0]}"
        )
        
        self.report.append(
            f"Average Trust Score : {df['trust_score'].mean():.3f}"
        )
        
        self.report.append(
            f"Document Versions : {sorted(df['document_version'].unique())}"
        )
        
        self.report.append(
            f"Fingerprint Versions : {sorted(df['fingerprint_version'].unique())}"
        )
        
        duplicate_sha = total - df["sha256"].nunique()
        
        if duplicate_sha:
            self.warning(
                f"{duplicate_sha} duplicate SHA256 fingerprints."
            )
            
        

        
    # ==========================================================
    # Enterprise Dataset
    # ==========================================================

    def audit_enterprise(self):

        enterprise = self.data_dir / "enterprise"

        if not enterprise.exists():
            return

        print("\nEnterprise Dataset")
        print("-" * 70)

        txt_files = list(enterprise.rglob("*.txt"))

        print(f"Policies : {len(txt_files)}")

        empty = 0

        for file in txt_files:
            if file.stat().st_size == 0:
                empty += 1

        print(f"Empty Files : {empty}")

        if empty:
            self.warning(f"{empty} empty policy files.")

        self.success("Enterprise dataset audited.")

    # ==========================================================
    # Report
    # ==========================================================

    def write_report(self):

        report_file = (
            self.audit_dir /
            "knowledge_repository_report.md"
        )

        self.report.append("\n---")
        self.report.append(f"\nWarnings : {self.warning_count}")
        self.report.append(f"\nErrors : {self.error_count}")

        report_file.write_text(
            "\n".join(self.report),
            encoding="utf-8",
        )

        print(f"\nReport written to:\n{report_file}")


    def audit_chunk_fingerprint_database(self, df):

        print("Running chunk validation...")

        self.report.append("\nChunk Fingerprint Database")
        self.report.append("-" * 40)

        chunks = len(df)
        policies = df["policy_id"].nunique()

        self.report.append(f"Chunks : {chunks}")
        self.report.append(f"Policies : {policies}")
        self.report.append(
            f"Average Chunks / Policy : {chunks/policies:.2f}"
        )

        chunk_sizes = df.groupby("policy_id").size()

        self.report.append(
            f"Largest Policy : {chunk_sizes.max()} chunks"
        )

        self.report.append(
            f"Smallest Policy : {chunk_sizes.min()} chunks"
        )

        self.report.append(
            f"Embedding Dimension : {df['embedding_dimension'].iloc[0]}"
        )

        self.report.append(
            f"Poisoned Chunks : {int(df['is_poisoned'].sum())}"
        )

        self.report.append("\nDecision Distribution")

        for decision, count in df["decision"].value_counts().items():
            self.report.append(f"{decision} : {count}")

        
    def audit_policy_index(self, df):

        print("Running policy index validation...")

        self.report.append("\nPolicy Index")
        self.report.append("-" * 40)

        self.report.append(f"Policies : {len(df)}")
        self.report.append(f"Departments : {df['department'].nunique()}")
        self.report.append(f"Categories : {df['category'].nunique()}")
        self.report.append(f"Security Domains : {df['security_domain'].nunique()}")
        self.report.append(f"Owners : {df['owner'].nunique()}")
        self.report.append(f"Average Words : {df['word_count'].mean():.2f}")
        self.report.append(f"Average Characters : {df['char_count'].mean():.2f}")

        

    
    def audit_document_relations(self, df):

        print("Running relation validation...")

        self.report.append("\nDocument Relations")
        self.report.append("-" * 40)

        self.report.append(f"Relations : {len(df)}")

        relation_counts = df["relation"].value_counts()

        self.report.append("\nRelation Types")

        for relation, count in relation_counts.items():
            self.report.append(f"{relation} : {count}")

        


    def audit_attack_log(self, df):

        print("Running attack validation...")

        self.report.append("\nAttack Log")
        self.report.append("-" * 40)

        self.report.append(f"Attacks : {len(df)}")

        self.report.append("\nAttack Types")

        for attack, count in df["attack_type"].value_counts().items():
            self.report.append(f"{attack} : {count}")

        self.report.append("\nSeverity")

        for sev, count in df["severity"].value_counts().items():
            self.report.append(f"{sev} : {count}")

        

    
    def audit_generation_log(self, df):

        print("Running generation log validation...")

        latest = df.iloc[-1]

        self.report.append("\nGeneration Log")
        self.report.append("-" * 40)

        self.report.append(f"Timestamp : {latest['timestamp']}")
        self.report.append(f"Documents : {latest['documents']}")
        self.report.append(f"Generator : {latest['generator']}")
        self.report.append(f"Version : {latest['version']}")

        

    


    # ==========================================================
    # Helpers
    # ==========================================================

    def success(self, msg):
        self.success_count += 1
        print(f"[OK] {msg}")

    def warning(self, msg):
        self.warning_count += 1
        print(f"[WARNING] {msg}")

    def error(self, msg):
        self.error_count += 1
        print(f"[ERROR] {msg}")


def main():
    auditor = KnowledgeRepositoryAuditor()
    auditor.audit()


if __name__ == "__main__":
    main()