"""
Cyber Security Department Policy Catalog

Knowledge Firewall AI

Defines all Cyber Security related enterprise policy categories.
"""

from src.config.blueprints.incident_response import (
    CYBER_ACTIONS,
    CYBER_OBJECTS,
    CYBER_PURPOSES,
    CYBER_RULES,
    CYBER_KEYWORDS
)

from src.config.title_templates.cyber_titles import (
    INCIDENT_RESPONSE_TITLES,
    CLOUD_SECURITY_TITLES,
    DATA_CLASSIFICATION_TITLES,
    DATA_RETENTION_TITLES,
    AI_GOVERNANCE_TITLES,
    THREAT_INTELLIGENCE_TITLES
)

CYBER_SECURITY_POLICIES = {

    ###########################################################################
    # INCIDENT RESPONSE
    ###########################################################################

    "Incident_Response": {

        "title_templates": INCIDENT_RESPONSE_TITLES,
        "department": "Cyber Security",
        "folder_name": "Cyber_Security",

        "security_domain": "Incident Response",

        "owner": "Security Operations Center",

        "classification": "Confidential",

        "risk_level": "Critical",

        "document_prefix": "CS-INC",

        "documents_to_generate": 25,

        "actions": CYBER_ACTIONS,

        "objects": CYBER_OBJECTS + [
            "Security Incident",
            "Cyber Attack",
            "Security Alert",
            "Threat Event"
        ],

        "purposes": CYBER_PURPOSES,

        "rules": CYBER_RULES + [
            "must activate the incident response team",
            "must notify executive management",
            "must preserve forensic evidence"
        ],

        "keywords": CYBER_KEYWORDS + [
            "incident response",
            "SOC",
            "forensics"
        ]
    },

    ###########################################################################
    # CLOUD SECURITY
    ###########################################################################

    "Cloud_Security": {

        "title_templates": CLOUD_SECURITY_TITLES,
        "department": "Cyber Security",
        "folder_name": "Cyber_Security",

        "security_domain": "Cloud Security",

        "owner": "Cloud Security Team",

        "classification": "Confidential",

        "risk_level": "High",

        "document_prefix": "CS-CLD",

        "documents_to_generate": 25,

        "actions": CYBER_ACTIONS,

        "objects": CYBER_OBJECTS + [
            "Cloud Instance",
            "Cloud Storage",
            "Virtual Machine",
            "Cloud Account",
            "Container"
        ],

        "purposes": CYBER_PURPOSES,

        "rules": CYBER_RULES + [
            "must enforce least privilege access",
            "must use encryption at rest",
            "must enable audit logging"
        ],

        "keywords": CYBER_KEYWORDS + [
            "AWS",
            "Azure",
            "Cloud",
            "IAM"
        ]
    },

    ###########################################################################
    # DATA CLASSIFICATION
    ###########################################################################

    "Data_Classification": {

        "title_templates": DATA_CLASSIFICATION_TITLES,
        "department": "Cyber Security",
        "folder_name": "Cyber_Security",

        "security_domain": "Data Protection",

        "owner": "Information Security Team",

        "classification": "Internal",

        "risk_level": "High",

        "document_prefix": "CS-DCL",

        "documents_to_generate": 25,

        "actions": CYBER_ACTIONS,

        "objects": CYBER_OBJECTS + [
            "Confidential Data",
            "Internal Data",
            "Restricted Information",
            "Business Records"
        ],

        "purposes": CYBER_PURPOSES,

        "rules": CYBER_RULES + [
            "must be classified before storage",
            "must follow organizational data classification policy",
            "must be reviewed annually"
        ],

        "keywords": CYBER_KEYWORDS + [
            "classification",
            "confidential",
            "restricted"
        ]
    },

    ###########################################################################
    # DATA RETENTION
    ###########################################################################

    "Data_Retention": {

        "title_templates": DATA_RETENTION_TITLES,
        "department": "Cyber Security",
        "folder_name": "Cyber_Security",

        "security_domain": "Data Governance",

        "owner": "Data Governance Team",

        "classification": "Internal",

        "risk_level": "Medium",

        "document_prefix": "CS-RET",

        "documents_to_generate": 25,

        "actions": CYBER_ACTIONS,

        "objects": CYBER_OBJECTS + [
            "Archived Data",
            "Business Records",
            "Audit Logs",
            "Customer Records"
        ],

        "purposes": CYBER_PURPOSES,

        "rules": CYBER_RULES + [
            "must comply with retention schedule",
            "must be securely destroyed after retention period",
            "must satisfy regulatory requirements"
        ],

        "keywords": CYBER_KEYWORDS + [
            "retention",
            "records",
            "archive"
        ]
    },

    ###########################################################################
    # AI USAGE
    ###########################################################################

    "AI_Governance": {

        "title_templates": AI_GOVERNANCE_TITLES,
        "department": "Cyber Security",
        "folder_name": "Cyber_Security",

        "security_domain": "AI Governance",

        "owner": "AI Governance Committee",

        "classification": "Internal",

        "risk_level": "High",

        "document_prefix": "CS-AIG",

        "documents_to_generate": 25,

        "actions": CYBER_ACTIONS,

        "objects": CYBER_OBJECTS + [
            "Generative AI System",
            "Large Language Model",
            "AI Assistant",
            "AI Generated Content"
        ],

        "purposes": CYBER_PURPOSES + [
            "Ensure responsible AI usage."
        ],

        "rules": CYBER_RULES + [
            "must not expose confidential information to public AI systems",
            "must comply with AI governance policies",
            "requires human review for high-risk decisions"
        ],

        "keywords": CYBER_KEYWORDS + [
            "AI",
            "LLM",
            "Generative AI",
            "Responsible AI"
        ]
    },

    ###############################################################################
# THREAT INTELLIGENCE
###############################################################################

"Threat_Intelligence": {

    "title_templates": THREAT_INTELLIGENCE_TITLES,
    "department": "Cyber Security",

    "folder_name": "Cyber_Security",

    "security_domain": "Threat Intelligence",

    "owner": "Threat Intelligence Team",

    "classification": "Confidential",

    "risk_level": "Critical",

    "document_prefix": "CS-THR",

    "documents_to_generate": 25,

    "actions": CYBER_ACTIONS,

    "objects": CYBER_OBJECTS + [

        "Threat Feed",

        "Indicator of Compromise",

        "Threat Report",

        "Malware Campaign",

        "Attack Pattern"

    ],

    "purposes": CYBER_PURPOSES + [

        "Improve cyber threat detection."

    ],

    "rules": CYBER_RULES + [

        "must be reviewed daily",

        "must validate threat intelligence sources",

        "must distribute critical alerts immediately"

    ],

    "keywords": CYBER_KEYWORDS + [

        "threat intelligence",

        "IOC",

        "malware",

        "APT",

        "threat feed"

    ]

}

}