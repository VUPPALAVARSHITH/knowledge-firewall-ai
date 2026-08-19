"""
upload_manager.py

Knowledge Firewall AI

Knowledge Admission Manager

Coordinates the complete Knowledge Admission Firewall pipeline.
"""

from pathlib import Path
import json
from datetime import datetime

from src.core.preprocessing.parser import PolicyParser
from src.core.preprocessing.chunk_builder import ChunkBuilder
from src.core.fingerprint.fingerprint_engine import FingerprintEngine

from src.core.security.repository_checker import RepositoryChecker
from src.core.security.attack_analyzer import AttackAnalyzer
from src.core.security.sensitive_detector import SensitiveDetector
from src.core.security.admission_trust_engine import AdmissionTrustEngine

from src.enterprise.models import AdmissionReport


class UploadManager:

    def __init__(self):

        self.parser = PolicyParser()
        self.chunk_builder = ChunkBuilder()
        self.fingerprint = FingerprintEngine()

        self.repository = RepositoryChecker()
        self.attack = AttackAnalyzer()
        self.sensitive = SensitiveDetector()
        self.trust_engine = AdmissionTrustEngine()

    # -----------------------------------------------------

    # -----------------------------------------------------

    HISTORY_PATH = Path(
        "data/metadata/admission_history.json"
    )

    # -----------------------------------------------------

    def _save_admission_result(
        self,
        report: AdmissionReport
    ):

        self.HISTORY_PATH.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if self.HISTORY_PATH.exists():

            try:

                history = json.loads(
                    self.HISTORY_PATH.read_text(
                        encoding="utf-8"
                    )
                )

            except (json.JSONDecodeError, OSError):

                history = []

        else:

            history = []

        history.append({

            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),

            "filename": report.filename,

            "policy_id": report.policy_id,

            "department": report.department,

            "category": report.category,

            "chunks_created": report.chunks_created,

            "repository_similarity":
                report.repository_similarity,

            "attack_detected":
                report.attack_detected,

            "attack_confidence":
                report.attack_confidence,

            "sensitive_data_detected":
                report.sensitive_data_detected,

            "sensitive_data_score":
                report.sensitive_data_score,

            "trust_score":
                report.trust_score,

            "decision":
                report.decision,

            "recommendation":
                report.recommendation,

            "warnings":
                report.warnings,

        })

        self.HISTORY_PATH.write_text(

            json.dumps(
                history,
                indent=4
            ),

            encoding="utf-8"

        )

    def analyze(self, filepath: str | Path) -> AdmissionReport:

        filepath = Path(filepath)
        document_text = filepath.read_text(
            encoding="utf-8"
        )

        # ---------------------------------------------
        # Parse
        # ---------------------------------------------

        policy = self.parser.parse(filepath)

        # ---------------------------------------------
        # Chunking
        # ---------------------------------------------

        chunks = self.chunk_builder.build(policy)

        # ---------------------------------------------
        # Fingerprint
        # ---------------------------------------------

        fingerprint = self.fingerprint.generate(
            filepath=filepath,
            department=policy.department,
            category=policy.category,
            policy_id=policy.policy_id,
        )

        # ---------------------------------------------
        # Repository
        # ---------------------------------------------

        repository = self.repository.check(
            fingerprint
        )

        # ---------------------------------------------
        # Attack Analysis
        # ---------------------------------------------

        attack = self.attack.analyze(
            document_text
        )

        # ---------------------------------------------
        # Sensitive Data
        # ---------------------------------------------


        sensitive = self.sensitive.analyze(
            document_text
        )

        # ---------------------------------------------
        # Trust
        # ---------------------------------------------

        trust = self.trust_engine.compute(
            repository,
            attack,
            sensitive,
        )

        # ---------------------------------------------
        # Final Decision
        # ---------------------------------------------

        final_decision = trust.decision

        # ---------------------------------------------
        # Recommendation
        # ---------------------------------------------

        recommendation_map = {

            "ACCEPT": "Store in Trusted Repository",

            "REVIEW": "Manual Security Review Required",

            "REJECT": "Reject Upload",

        }

        recommendation = recommendation_map[
            final_decision
        ]

        # ---------------------------------------------
        # Warnings
        # ---------------------------------------------

        warnings = []

        if repository.duplicate:

            warnings.append(
                f"Repository similarity detected ({repository.similarity:.2%})."
            )

        if attack.is_attack:

            warnings.append(
                f"Knowledge manipulation detected ({attack.attack_id})."
            )

        if sensitive.total_findings > 0:

            warnings.append(
                f"{sensitive.total_findings} sensitive information finding(s) detected."
            )

        # ---------------------------------------------
        # Report
        # ---------------------------------------------

        report = AdmissionReport(

            filename=filepath.name,

            policy_id=policy.policy_id,

            department=policy.department,

            category=policy.category,

            parser_completed=True,

            chunks_created=len(chunks),

            fingerprint_created=True,

            duplicate_found=repository.duplicate,

            repository_similarity=repository.similarity,

            attack_detected=attack.is_attack,

            attack_confidence=attack.confidence,

            sensitive_data_detected=(
                sensitive.total_findings > 0
            ),

            sensitive_data_score=sensitive.risk_score,

            trust_score=trust.trust_score,

            decision=final_decision,

            recommendation=recommendation,

            warnings=warnings,

        )

        self._save_admission_result(report)

        return report