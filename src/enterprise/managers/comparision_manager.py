"""
comparison_manager.py

Knowledge Firewall AI

Enterprise Policy Comparison Manager.
"""

from pathlib import Path

from src.core.preprocessing.parser import PolicyParser
from src.core.fingerprint.fingerprint_engine import FingerprintEngine

from src.core.security.repository_checker import RepositoryChecker
from src.core.security.attack_analyzer import AttackAnalyzer
from src.core.security.sensitive_detector import SensitiveDetector
from src.core.security.admission_trust_engine import AdmissionTrustEngine

from src.enterprise.models import ComparisonReport


class ComparisonManager:

    def __init__(self):

        self.parser = PolicyParser()

        self.fingerprint = FingerprintEngine()

        self.repository = RepositoryChecker()

        self.attack = AttackAnalyzer()

        self.sensitive = SensitiveDetector()

        self.trust = AdmissionTrustEngine()

    # -----------------------------------------------------

    def compare(self, file_a, file_b):

        file_a = Path(file_a)
        file_b = Path(file_b)

        policy_a = self.parser.parse(file_a)
        policy_b = self.parser.parse(file_b)

        fp_a = self.fingerprint.generate(
            filepath=file_a,
            department=policy_a.department,
            category=policy_a.category,
            policy_id=policy_a.policy_id
        )

        fp_b = self.fingerprint.generate(
            filepath=file_b,
            department=policy_b.department,
            category=policy_b.category,
            policy_id=policy_b.policy_id
        )

        comparison = self.repository.compare_embedding(
            fp_b["embedding"]
        )

        attack = self.attack.analyze(
            "\n".join(policy_b.policy_statements)
        )

        sensitive = self.sensitive.analyze(
            "\n".join(policy_b.policy_statements)
        )

        trust = self.trust.compute(
            repository_similarity=comparison.similarity,
            attack_confidence=attack.confidence,
            sensitive_risk=sensitive.risk_score
        )

        if trust.decision == "ACCEPT":
            recommendation = "Policies are consistent."
        elif trust.decision == "REVIEW":
            recommendation = "Manual review recommended."
        else:
            recommendation = "Potential knowledge manipulation."

        return ComparisonReport(

            policy_a=policy_a.policy_id,

            policy_b=policy_b.policy_id,

            semantic_similarity=comparison.similarity,

            repository_similarity=comparison.similarity,

            attack_detected=attack.is_attack,

            sensitive_data_detected=(
                sensitive.total_findings > 0
            ),

            trust_score=trust.trust_score,

            decision=trust.decision,

            recommendation=recommendation

        )