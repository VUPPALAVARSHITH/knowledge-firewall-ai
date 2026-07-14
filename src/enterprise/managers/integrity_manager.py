"""
integrity_manager.py

Knowledge Firewall AI

Repository Integrity Scanner Manager.
"""

from pathlib import Path

from src.enterprise.managers.repository_manager import RepositoryManager

from src.core.preprocessing.parser import PolicyParser
from src.core.fingerprint.fingerprint_engine import FingerprintEngine

from src.core.security.repository_checker import RepositoryChecker
from src.core.security.attack_analyzer import AttackAnalyzer
from src.core.security.sensitive_detector import SensitiveDetector
from src.core.security.admission_trust_engine import AdmissionTrustEngine

from src.enterprise.models import IntegrityReport


class IntegrityManager:

    def __init__(self):

        self.repository = RepositoryManager()

        self.parser = PolicyParser()

        self.fingerprint = FingerprintEngine()

        self.repository_checker = RepositoryChecker()

        self.attack = AttackAnalyzer()

        self.sensitive = SensitiveDetector()

        self.trust = AdmissionTrustEngine()

    # -----------------------------------------------------

    def scan_repository(self):

        reports = []

        policies = self.repository.list_policies()

        for _, row in policies.iterrows():

            filepath = Path(row["filepath"])

            if not filepath.exists():
                continue

            policy = self.parser.parse(filepath)

            fingerprint = self.fingerprint.generate(

                filepath=filepath,

                department=policy.department,

                category=policy.category,

                policy_id=policy.policy_id

            )

            repository = self.repository_checker.compare_embedding(

                fingerprint["embedding"]

            )

            attack = self.attack.analyze(

                "\n".join(policy.policy_statements)

            )

            sensitive = self.sensitive.analyze(

                "\n".join(policy.policy_statements)

            )

            trust = self.trust.compute(

                repository_similarity=repository.similarity,

                attack_confidence=attack.confidence,

                sensitive_risk=sensitive.risk_score

            )

            reports.append(

                IntegrityReport(

                    policy_id=policy.policy_id,

                    department=policy.department,

                    category=policy.category,

                    trust_score=trust.trust_score,

                    repository_similarity=repository.similarity,

                    attack_detected=attack.is_attack,

                    decision=trust.decision

                )

            )

        return reports