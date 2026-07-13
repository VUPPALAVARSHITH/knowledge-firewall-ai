"""
upload_manager.py

Knowledge Firewall AI

Knowledge Admission Manager

Coordinates the complete Knowledge Admission Firewall
pipeline.
"""

from pathlib import Path

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

    def analyze(self, filepath: str | Path) -> AdmissionReport:

        filepath = Path(filepath)

        # -------------------------------------------------
        # Parse Policy
        # -------------------------------------------------

        policy = self.parser.parse(filepath)

        # -------------------------------------------------
        # Build Semantic Chunks
        # -------------------------------------------------

        chunks = self.chunk_builder.build(policy)

        # -------------------------------------------------
        # Generate Fingerprint
        # -------------------------------------------------

        fingerprint = self.fingerprint.generate(

            filepath=filepath,

            department=policy.department,

            category=policy.category,

            policy_id=policy.policy_id

        )

        # -------------------------------------------------
        # Repository Similarity
        # -------------------------------------------------

        repository = self.repository.compare_embedding(

            fingerprint["embedding"]

        )

        # -------------------------------------------------
        # Knowledge Manipulation Analysis
        # -------------------------------------------------

        attack = self.attack.analyze(

            "\n".join(policy.policy_statements)

        )

        # -------------------------------------------------
        # Sensitive Data Detection
        # -------------------------------------------------

        sensitive = self.sensitive.analyze(

            "\n".join(policy.policy_statements)

        )

        # -------------------------------------------------
        # Admission Trust
        # -------------------------------------------------

        trust = self.trust_engine.compute(

            repository_similarity=repository.similarity,

            attack_confidence=attack.confidence,

            sensitive_risk=sensitive.risk_score

        )

        # -------------------------------------------------
        # Recommendation
        # -------------------------------------------------

        if trust.decision == "ACCEPT":

            recommendation = (
                "Store in Trusted Repository"
            )

        elif trust.decision == "REVIEW":

            recommendation = (
                "Manual Security Review Required"
            )

        else:

            recommendation = (
                "Reject Upload"
            )

        # -------------------------------------------------
        # Warnings
        # -------------------------------------------------

        warnings = []

        if repository.duplicate:

            warnings.append(

                f"Repository similarity detected "
                f"({repository.similarity:.2%})."

            )

        if attack.is_attack:

            warnings.append(

                f"Knowledge manipulation detected "
                f"({attack.attack_id})."

            )

        if sensitive.total_findings > 0:

            warnings.append(

                f"{sensitive.total_findings} sensitive "
                f"information finding(s) detected."

            )

        # -------------------------------------------------
        # Final Report
        # -------------------------------------------------

        return AdmissionReport(

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

            decision=trust.decision,

            recommendation=recommendation,

            warnings=warnings

        )