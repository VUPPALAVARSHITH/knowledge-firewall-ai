"""
find_missing_templates.py

Knowledge Firewall AI

Scans all blueprint rules and reports which rules
do not have a matching semantic attack template.
"""

from src.attacks.attack_templates import ATTACK_TEMPLATES

from src.config.blueprints.identity import IDENTITY_RULES
from src.config.blueprints.network import NETWORK_RULES
from src.config.blueprints.email import EMAIL_RULES
from src.config.blueprints.endpoint import ENDPOINT_RULES
from src.config.blueprints.human_resources import HR_RULES
from src.config.blueprints.incident_response import CYBER_RULES
from src.config.blueprints.compliance import COMPLIANCE_RULES
from src.config.blueprints.data_management import DATA_RULES
from src.config.blueprints.privacy import PRIVACY_RULES
from src.config.blueprints.physical_security import PHYSICAL_RULES
from src.config.blueprints.business_continuity import BC_RULES


RULE_GROUPS = {

    "Identity": IDENTITY_RULES,
    "Network": NETWORK_RULES,
    "Email": EMAIL_RULES,
    "Endpoint": ENDPOINT_RULES,
    "Human Resources": HR_RULES,
    "Cyber Security": CYBER_RULES,
    "Compliance": COMPLIANCE_RULES,
    "Data Management": DATA_RULES,
    "Privacy": PRIVACY_RULES,
    "Physical Security": PHYSICAL_RULES,
    "Business Continuity": BC_RULES

}


def has_template(rule):

    rule = rule.lower()

    for trigger in ATTACK_TEMPLATES.keys():

        if trigger.lower() in rule:
            return True

    return False


def main():

    total = 0
    covered = 0
    missing = []

    print("=" * 70)
    print("ATTACK TEMPLATE COVERAGE REPORT")
    print("=" * 70)

    for category, rules in RULE_GROUPS.items():

        print()
        print(category)

        for rule in rules:

            total += 1

            if has_template(rule):

                covered += 1
                print("  ✓", rule)

            else:

                missing.append(rule)
                print("  ❌", rule)

    print()
    print("=" * 70)

    print("Covered Rules :", covered)
    print("Missing Rules :", len(missing))
    print(f"Coverage      : {(covered/total)*100:.1f}%")

    print("=" * 70)

    print()
    print("MISSING RULES")
    print("-" * 70)

    for rule in sorted(set(missing)):
        print(rule)


if __name__ == "__main__":
    main()