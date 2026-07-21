"""
knowledge_admission_firewall.py

Knowledge Firewall AI

Knowledge Admission Firewall

Validates enterprise knowledge before it is admitted
into the Trusted Knowledge Repository.
"""

from __future__ import annotations

import time

from src.core.security.repository_checker import RepositoryChecker
from src.core.security.attack_analyzer import AttackAnalyzer
from src.core.security.sensitive_detector import SensitiveDetector
from src.core.security.admission_trust_engine import AdmissionTrustEngine
from src.core.security.models import AdmissionReport


class KnowledgeAdmissionFirewall:
    """
    Enterprise Knowledge Admission Firewall.

    Pipeline

    Policy
        ↓
    Repository Similarity
        ↓
    Attack Detection
        ↓
    Sensitive Data Detection
        ↓
    Trust Evaluation
        ↓
    Admission Report
    """

    def __init__(self):

        self.repository_checker = RepositoryChecker()

        self.attack_analyzer = AttackAnalyzer()

        self.sensitive_detector = SensitiveDetector()

        self.trust_engine = AdmissionTrustEngine()

    # ---------------------------------------------------------

    def verify(
        self,
        policy,
        document_fingerprint,
        filename: str,
    ) -> AdmissionReport:

        start = time.perf_counter()

        text = getattr(
            policy,
            "content",
            str(policy)
        )

        # -----------------------------------------------------
        # Repository Similarity
        # -----------------------------------------------------

        repository_result = self.repository_checker.check(
            document_fingerprint
        )

        # -----------------------------------------------------
        # Attack Analysis
        # -----------------------------------------------------

        attack_result = self.attack_analyzer.analyze(
            policy
        )

        # -----------------------------------------------------
        # Sensitive Data Detection
        # -----------------------------------------------------

        sensitive_result = self.sensitive_detector.analyze(
            policy
        )

        # -----------------------------------------------------
        # Trust Evaluation
        # -----------------------------------------------------

        trust_result = self.trust_engine.compute(

            repository_result,

            attack_result,

            sensitive_result,

        )

        elapsed = round(

            time.perf_counter() - start,

            4

        )

        return AdmissionReport(

            document_id=document_fingerprint.document_id,

            filename=filename,

            repository_result=repository_result,

            attack_result=attack_result,

            sensitive_result=sensitive_result,

            trust_result=trust_result,

            decision=trust_result.decision,

            processing_time=elapsed,

        )