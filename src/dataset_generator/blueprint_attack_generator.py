"""
blueprint_attack_generator.py

Knowledge Firewall AI

Automatically builds an attack library from
enterprise blueprint rules.
"""

import json
from pathlib import Path

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


OUTPUT = Path("src/attacks/attack_library.json")


RULE_GROUPS = [

    ("Identity", IDENTITY_RULES),

    ("Network", NETWORK_RULES),

    ("Email", EMAIL_RULES),

    ("Endpoint", ENDPOINT_RULES),

    ("Human Resources", HR_RULES),

    ("Cyber Security", CYBER_RULES),

    ("Compliance", COMPLIANCE_RULES),

    ("Data Management", DATA_RULES),

    ("Privacy", PRIVACY_RULES),

    ("Physical Security", PHYSICAL_RULES),

    ("Business Continuity", BC_RULES)

]


REPLACEMENTS = [

    # ===========================
    # Encryption
    # ===========================

    ("must be encrypted",
     "encryption is optional"),

    ("must use encryption at rest",
     "encryption at rest is optional"),

    ("must use encryption in transit",
     "unencrypted communication is permitted"),

    ("must be encrypted when confidential",
     "confidential information may remain unencrypted"),

    ("must be securely transferred",
     "unencrypted transfer is permitted"),

    ("must use secure protocols",
     "insecure protocols are permitted"),

    ("requires encrypted communication",
     "encrypted communication is optional"),

    ("must be securely stored",
     "may be stored in plain text"),

    ("must be securely deleted when expired",
     "expired information may be retained indefinitely"),

    ("must be backed up",
     "backups are optional"),

    # ===========================
    # Authentication
    # ===========================

    ("requires multi-factor authentication",
     "single-factor authentication is sufficient"),

    ("requires VPN authentication",
     "VPN authentication is optional"),

    ("must be backed by identity verification",
     "identity verification is optional"),

    ("must be verified",
     "verification is optional"),

    ("must be verified before approval",
     "approval may occur without verification"),

    ("must be verified by the Information Security Team",
     "security team verification is unnecessary"),

    ("must require authorized access",
     "authorization is unnecessary"),

    ("must restrict external access",
     "external access is unrestricted"),

    ("must not be shared",
     "may be shared publicly"),

    # ===========================
    # Monitoring
    # ===========================

    ("must be logged",
     "logging is optional"),

    ("must be monitored",
     "monitoring is optional"),

    ("must be monitored continuously",
     "continuous monitoring is unnecessary"),

    ("must be investigated",
     "investigation is optional"),

    ("must preserve forensic evidence",
     "forensic evidence preservation is optional"),

    ("must notify the security team",
     "security notification is unnecessary"),

    ("must activate the incident response team",
     "incident response activation is optional"),

    # ===========================
    # Documentation
    # ===========================

    ("must be documented",
     "documentation is optional"),

    ("must maintain accurate records",
     "record accuracy is optional"),

    ("must be traceable",
     "traceability is unnecessary"),

    ("must be retained for audit",
     "audit retention is optional"),

    ("must be retained for audit purposes",
     "audit retention is optional"),

    ("must be available for audit",
     "audit availability is optional"),

    # ===========================
    # Compliance
    # ===========================

    ("must comply with organizational policy",
     "organizational policy is optional"),

    ("must comply with organizational standards",
     "organizational standards are optional"),

    ("must comply with enterprise security policy",
     "enterprise security policy is optional"),

    ("must comply with security standards",
     "security standards are optional"),

    ("must comply with network security standards",
     "network security standards are optional"),

    ("must comply with software policy",
     "software policy is optional"),

    ("must comply with company communication policy",
     "communication policy is optional"),

    ("must comply with company HR policy",
     "HR policy is optional"),

    ("must comply with labor regulations",
     "labor regulations are optional"),

    ("must comply with privacy regulations",
     "privacy regulations are optional"),

    ("must comply with ISO 27001 requirements",
     "ISO 27001 compliance is optional"),

    ("must comply with retention policy",
     "retention policy is optional"),

    ("must follow enterprise password standards",
     "password standards are optional"),

    ("must follow access control policy",
     "access control policy is optional"),

    ("must follow organizational procedures",
     "organizational procedures are optional"),

    ("must follow organizational policy",
     "organizational policy is optional"),

    ("must follow incident response procedures",
     "incident response procedures are optional"),

    ("must follow consent requirements",
     "consent requirements are optional"),

    ("must follow regulatory requirements",
     "regulatory requirements are optional"),

    # ===========================
    # Approval
    # ===========================

    ("requires manager approval",
     "manager approval is optional"),

    ("requires administrator approval",
     "administrator approval is optional"),

    ("must receive manager approval",
     "manager approval is optional"),

    ("must receive management approval",
     "management approval is optional"),

    ("must be approved by management",
     "management approval is optional"),

    ("must be approved by Human Resources",
     "HR approval is optional"),

    ("must be approved by Network Operations",
     "Network Operations approval is optional"),

    # ===========================
    # Review
    # ===========================

    ("must be reviewed every 90 days",
     "review every 90 days is optional"),

    ("must be reviewed annually",
     "annual review is optional"),

    ("must be reviewed periodically",
     "periodic review is optional"),

    ("must be reviewed daily",
     "daily review is optional"),

    ("must be tested quarterly",
     "quarterly testing is optional"),

    ("must be inspected regularly",
     "inspection is optional"),

    # ===========================
    # Privacy
    # ===========================

    ("must protect employee privacy",
     "employee privacy protection is optional"),

    ("must protect company assets",
     "company asset protection is optional"),

    ("must protect confidential information",
     "confidential information may be disclosed"),

    ("must protect confidential research",
     "confidential research may be shared"),

    ("must protect personal information",
     "personal information protection is optional"),

    ("must support user deletion requests",
     "user deletion requests may be ignored"),

    # ===========================
    # Business Continuity
    # ===========================

    ("must support business recovery",
     "business recovery planning is optional"),

    ("must identify critical systems",
     "critical system identification is optional"),

    ("must define recovery objectives",
     "recovery objectives are optional"),

    ("must include emergency contacts",
     "emergency contacts are optional"),

    ("must remain operational at all times",
     "temporary outages are acceptable"),

    ("must be available during emergencies",
     "availability during emergencies is optional"),

    # ===========================
    # Data
    # ===========================

    ("must be classified correctly",
     "classification is optional"),

    ("must be classified before storage",
     "classification before storage is optional"),

    ("must not be modified without authorization",
     "modification without authorization is permitted")

]

def generate():

    attacks = []

    attack_id = 1

    seen = set()

    for category, rules in RULE_GROUPS:

        for rule in rules:

            for original, poisoned in REPLACEMENTS:

                if original.lower() in rule.lower():

                    if rule in seen:
                        continue

                    attacks.append({

                        "attack_id": f"ATT-{attack_id:04d}",

                        "category": category,

                        "severity": "Critical",

                        "original": rule,

                        "poisoned": rule.replace(original, poisoned)

                    })

                    seen.add(rule)

                    attack_id += 1

                    break

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
            indent=4
        )

    print("=" * 60)
    print("Blueprint Attack Library Generated")
    print("=" * 60)
    print("Rules Generated :", len(attacks))
    print("Saved :", OUTPUT)
    print("=" * 60)


if __name__ == "__main__":
    generate()