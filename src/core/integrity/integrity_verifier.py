"""
integrity_verifier.py

Knowledge Firewall AI

Repository Integrity Verification Engine
"""

from datetime import datetime

from src.core.preprocessing.parser import PolicyParser
from src.core.security.attack_analyzer import AttackAnalyzer
from src.core.security.sensitive_detector import SensitiveDetector
from src.core.security.admission_trust_engine import AdmissionTrustEngine

from src.core.security.models import RepositoryCheckResult

from src.core.integrity.repository_scanner import RepositoryScanner
from src.core.integrity.integrity_models import (
    IntegrityResult,
    IntegrityScanReport,
)


class IntegrityVerifier:

    def __init__(self):

        self.scanner = RepositoryScanner()

        self.parser = PolicyParser()

        self.attack = AttackAnalyzer()

        self.sensitive = SensitiveDetector()

        self.trust = AdmissionTrustEngine()

    # -----------------------------------------------------

    def verify_policy(self, filepath):

        policy = self.parser.parse(filepath)

        document_text = "\n".join(
            policy.policy_statements
        )

        attack = self.attack.analyze(
            document_text
        )

        sensitive = self.sensitive.analyze(
            document_text
        )

        # ---------------------------------------------
        # Stored repository documents are NOT duplicates.
        # Repository score is always healthy.
        # ---------------------------------------------

        repository = RepositoryCheckResult(

            duplicate=False,

            similarity=0.0,

            matched_policy=policy.policy_id,

            recommendation="Accept",

            reason="Existing trusted repository document"

        )

        trust = self.trust.compute(

            repository,

            attack,

            sensitive

        )

        return IntegrityResult(

            policy_id=policy.policy_id,

            department=policy.department,

            category=policy.category,

            trust_score=trust.trust_score,

            repository_similarity=0.0,

            attack_detected=attack.is_attack,

            attack_confidence=attack.confidence,

            sensitive_data_detected=(
                sensitive.total_findings > 0
            ),

            sensitive_data_score=sensitive.risk_score,

            decision=trust.decision,

            recommendation=(
                "Repository Healthy"
                if trust.decision == "ACCEPT"
                else "Integrity Review Required"
            ),

            warnings=[]

        )

    # -----------------------------------------------------

    def verify_repository(self):

        files = self.scanner.scan()

        results = []

        trusted = 0

        review = 0

        rejected = 0

        total_trust = 0.0

        for file in files:

            result = self.verify_policy(file)

            results.append(result)

            total_trust += result.trust_score

            if result.decision == "ACCEPT":

                trusted += 1

            elif result.decision == "REVIEW":

                review += 1

            else:

                rejected += 1

        average = round(

            total_trust / len(results),

            2

        ) if results else 0.0

        if average >= 95:

            health = "Excellent"

        elif average >= 85:

            health = "Good"

        elif average >= 70:

            health = "Fair"

        else:

            health = "Poor"

        return IntegrityScanReport(

            scan_time=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            total_policies=len(results),

            average_trust=average,

            repository_health=health,

            results=results

        )