"""
attack_engine.py

Knowledge Firewall AI

Applies semantic poisoning attacks using
the generated attack library.
"""

import json
import random
from pathlib import Path


ATTACK_LIBRARY = Path("src/attacks/attack_library.json")

class AttackEngine:

    def __init__(self):

        self.random = random.Random(42)

        with open(
            ATTACK_LIBRARY,
            "r",
            encoding="utf-8"
        ) as f:

            self.attacks = json.load(f)
    
    # ---------------------------------------------------------
    # Extract Policy Statements Section
    # ---------------------------------------------------------
    
    def extract_policy_section(self, text):
        start = "4. POLICY STATEMENTS"
        end = "5. RESPONSIBILITIES"
     
        if start not in text or end not in text:
               return None

        before = text.split(start, 1)[0]

        middle = text.split(start, 1)[1].split(end, 1)[0]

        after = text.split(end, 1)[1]

        return before, middle, after

    def apply_attack(self, text, intensity="medium"):
        
        section = self.extract_policy_section(text)
        
        if section is None:
            
            return {
                "poisoned_text": text,
                "attack_id": None,
                "attack_type": None,
                "category": None,
                "severity": None,
                "success": False
            }
            
        before, policy_text, after = section
        
        matches = []

        for attack in self.attacks:

            if attack["original"] in policy_text:
                matches.append(attack)

        if not matches:

            return {
                "poisoned_text": text,
                "attack_id": None,
                "attack_type": None,
                "category": None,
                "severity": None,
                "success": False
            }

        if intensity == "low":
            num_attacks = 1

        elif intensity == "medium":
            num_attacks = min(2, len(matches))

        elif intensity == "high":
            num_attacks = min(
                self.random.randint(3, 5),
                len(matches)
            )

        else:
            num_attacks = 1

        selected = self.random.sample(
            matches,
            num_attacks
        )

        poisoned_text = policy_text

        applied_ids = []
        categories = []
        severities = []

        for attack in selected:

            poisoned_text = poisoned_text.replace(
                attack["original"],
                attack["poisoned"],
                1
            )

            applied_ids.append(attack["attack_id"])
            categories.append(attack["category"])
            severities.append(attack["severity"])

        poisoned_text = (
            before +
            "4. POLICY STATEMENTS\n\n" +
            poisoned_text +
            "\n\n5. RESPONSIBILITIES" +
            after
        )
        
        return {
            "poisoned_text": poisoned_text,
            "attack_id": ",".join(applied_ids),
            "attack_type": ",".join(categories),
            "category": ",".join(categories),
            "severity": ",".join(severities),
            "success": True
        }