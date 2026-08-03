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
            "Critical": 4,
        }

        highest = "None"

        for attack in self.attacks:

            poisoned = str(
                attack.get("poisoned", "")
            ).strip().lower()

            # Do NOT treat the clean/original trigger
            # as evidence of an attack.
            if not poisoned:
                continue

            if poisoned in text:

                detected.append(attack)

                severity = attack.get(
                    "severity",
                    "Low"
                )

                if (
                    severity_rank.get(severity, 0)
                    > severity_rank.get(highest, 0)
                ):
                    highest = severity

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

            key=lambda attack: severity_rank.get(
                attack.get("severity", "Low"),
                0
            )

        )

        severity_confidence = {
            "Critical":1.00,
            "High":0.98,
            "Medium":0.90,
            "Low":0.80
        }

        confidence = round(
            severity_confidence.get(highest, 0.0),
            2
        )

        recommendation_map = {
            "Critical": "Reject Upload",
            "High": "Reject Upload",
            "Medium": "Manual Review",
            "Low": "Manual Review",
            "None": "Accept",
        }

        return AttackResult(

            attack_id=best.get("attack_id"),

            category=best.get("category"),

            severity=highest,

            confidence=confidence,

            matched_text=best.get(
                "poisoned",
                ""
            ),

            recommendation=recommendation_map.get(
                highest,
                "Manual Review"
            ),

            is_attack=True

        )