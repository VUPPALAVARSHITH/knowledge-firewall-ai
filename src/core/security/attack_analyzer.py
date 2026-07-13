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

        text = text.lower()

        detected = []

        highest = "Low"

        for attack in self.attacks:

            trigger = attack["trigger"].lower()
            poisoned = attack["poisoned"].lower()

            if trigger in text or poisoned in text:

                detected.append(attack)

                if attack["severity"] == "High":
                    highest = "High"

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

        best = detected[0]

        confidence = round(

            len(detected) /

            max(len(self.attacks), 1),

            4

        )

        recommendation = (

            "Reject Upload"

            if highest == "High"

            else "Manual Review"

        )

        return AttackResult(

            attack_id=best["attack_id"],

            category=best["category"],

            severity=highest,

            confidence=confidence,

            matched_text=best["poisoned"],

            recommendation=recommendation,

            is_attack=True

        )