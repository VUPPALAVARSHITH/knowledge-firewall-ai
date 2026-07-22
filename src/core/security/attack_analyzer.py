"""
attack_analyzer.py

Knowledge Firewall AI

Detects enterprise knowledge manipulation attacks
using the semantic attack library.
"""

import json
from pathlib import Path
from src.core.security.models import AttackResult

class AttackAnalyzer:

    def __init__(self):

        self.attack_library = Path(
            "src/research/attacks/attack_library.json"
        )

        self.attacks = self.load()

    # ---------------------------------------------------------

    def load(self):

        if not self.attack_library.exists():
            return []

        with open(
            self.attack_library,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    # ---------------------------------------------------------

        # ---------------------------------------------------------

    def analyze(self, text) -> AttackResult:

        text = getattr(
            text,
            "content",
            str(text)
        ).lower()

        detected = []


        severity_rank = {
            "None": 0,
            "Low": 1,
            "Medium": 2,
            "High": 3,
        }

        highest = "None"

        for attack in self.attacks:

            trigger = attack["trigger"].lower()
            poisoned = attack["poisoned"].lower()

            if trigger in text or poisoned in text:

                detected.append(attack)

                if (
                    severity_rank[attack["severity"]]
                    > severity_rank[highest]
                ):
                    highest = attack["severity"]

        if not detected:

            return AttackResult(

                attack_id=None,

                category=None,

                severity="None",

                confidence=0.0,

                matched_text="",

                recommendation="Accept",

                is_attack=False

            )

        best = max(
            detected,
            key=lambda attack: severity_rank[attack["severity"]]
        )

        severity_confidence = {
            "High": 0.95,
            "Medium": 0.75,
            "Low": 0.50,
        }

        confidence = severity_confidence.get(highest, 0.0)

        confidence = round(confidence, 2)

        recommendation_map = {
            "High": "Reject Upload",
            "Medium": "Manual Review",
            "Low": "Manual Review",
            "None": "Accept",
        }

        recommendation = recommendation_map[highest]

        return AttackResult(

            attack_id=best["attack_id"],

            category=best["category"],

            severity=highest,

            confidence=confidence,

            matched_text=best["poisoned"],

            recommendation=recommendation,

            is_attack=True

        )