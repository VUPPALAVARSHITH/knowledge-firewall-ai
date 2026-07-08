"""
blueprint_attack_generator.py

Knowledge Firewall AI

Generates a semantic attack library from
all enterprise policy catalogs.
"""

import json
from pathlib import Path

from src.attacks.attack_templates import ATTACK_TEMPLATES

from src.config.policy_catalog.it import IT_POLICIES
from src.config.policy_catalog.administration import ADMINISTRATION_POLICIES
from src.config.policy_catalog.customer_support import CUSTOMER_SUPPORT_POLICIES
from src.config.policy_catalog.operations import OPERATIONS_POLICIES
from src.config.policy_catalog.finance import FINANCE_POLICIES
from src.config.policy_catalog.human_resources import HUMAN_RESOURCE_POLICIES
from src.config.policy_catalog.legal import LEGAL_POLICIES
from src.config.policy_catalog.research import RESEARCH_POLICIES
from src.config.policy_catalog.cyber_security import CYBER_SECURITY_POLICIES


OUTPUT = Path("src/attacks/attack_library.json")


ALL_POLICIES = {}

ALL_POLICIES.update(IT_POLICIES)
ALL_POLICIES.update(ADMINISTRATION_POLICIES)
ALL_POLICIES.update(CUSTOMER_SUPPORT_POLICIES)
ALL_POLICIES.update(CYBER_SECURITY_POLICIES)
ALL_POLICIES.update(OPERATIONS_POLICIES)
ALL_POLICIES.update(FINANCE_POLICIES)
ALL_POLICIES.update(HUMAN_RESOURCE_POLICIES)
ALL_POLICIES.update(LEGAL_POLICIES)
ALL_POLICIES.update(RESEARCH_POLICIES)


def generate():

    attacks = []

    attack_id = 1

    seen = set()

    for category, config in ALL_POLICIES.items():

        rules = config["rules"]

        for rule in rules:

            if rule in seen:
                continue

            seen.add(rule)

            matched = False

            for trigger, cfg in ATTACK_TEMPLATES.items():

                if trigger.lower() in rule.lower():

                    matched = True

                    subject = rule[len(trigger):].strip()

                    for template in cfg["variants"]:

                        poisoned = template.format(subject=subject)

                        attacks.append({

                            "attack_id": f"ATT-{attack_id:04d}",

                            "category": category,

                            "severity": cfg["severity"],

                            "trigger": trigger,

                            "subject": subject,

                            "template_used": template,

                            "original": rule,

                            "poisoned": poisoned

                        })

                        attack_id += 1

                    break

            if not matched:
                print(f"[NO TEMPLATE] {rule}")

    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            attacks,
            f,
            indent=4,
            ensure_ascii=False
        )

    print("=" * 60)
    print("Blueprint Attack Library Generated")
    print("=" * 60)
    print("Unique Rules Covered :", len(seen))
    print("Attack Rules Generated :", len(attacks))
    print("Saved :", OUTPUT)
    print("=" * 60)


if __name__ == "__main__":
    generate()