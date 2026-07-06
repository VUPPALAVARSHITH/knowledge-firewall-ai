"""
Legal Department Policy Catalog

Knowledge Firewall AI
"""

from src.config.blueprints.compliance import *
from src.config.blueprints.privacy import *
from src.config.title_templates.legal_titles import (
    COMPLIANCE_TITLES,
    VENDOR_MANAGEMENT_TITLES,
    CONTRACT_MANAGEMENT_TITLES,
    INTELLECTUAL_PROPERTY_TITLES,
    DATA_PRIVACY_TITLES
)

LEGAL_POLICIES = {

    ###########################################################################
    # COMPLIANCE
    ###########################################################################

    "Compliance": {

        "title_templates": COMPLIANCE_TITLES,
        "department": "Legal",
        "folder_name": "Legal",

        "security_domain": "Regulatory Compliance",

        "owner": "Legal Compliance Team",

        "classification": "Confidential",

        "risk_level": "High",

        "document_prefix": "LEG-CMP",

        "documents_to_generate": 25,

        "actions": COMPLIANCE_ACTIONS,

        "objects": COMPLIANCE_OBJECTS,

        "purposes": COMPLIANCE_PURPOSES,

        "rules": COMPLIANCE_RULES,

        "keywords": COMPLIANCE_KEYWORDS

    },

    ###########################################################################
    # VENDOR MANAGEMENT
    ###########################################################################

    "Vendor_Management": {

        "title_templates": VENDOR_MANAGEMENT_TITLES,
        "department": "Legal",
        "folder_name": "Legal",

        "security_domain": "Vendor Governance",

        "owner": "Vendor Compliance Team",

        "classification": "Internal",

        "risk_level": "Medium",

        "document_prefix": "LEG-VEN",

        "documents_to_generate": 25,

        "actions": COMPLIANCE_ACTIONS,

        "objects": COMPLIANCE_OBJECTS + [
            "Vendor Contract",
            "Supplier Agreement",
            "Third Party Assessment"
        ],

        "purposes": COMPLIANCE_PURPOSES,

        "rules": COMPLIANCE_RULES + [
            "must undergo legal review",
            "must complete vendor risk assessment"
        ],

        "keywords": COMPLIANCE_KEYWORDS + [
            "vendor",
            "supplier",
            "third party"
        ]

    },

    ###########################################################################
    # CONTRACT MANAGEMENT
    ###########################################################################

    "Contract_Management": {

        "title_templates": CONTRACT_MANAGEMENT_TITLES,
        "department": "Legal",
        "folder_name": "Legal",

        "security_domain": "Contract Governance",

        "owner": "Corporate Legal Team",

        "classification": "Confidential",

        "risk_level": "High",

        "document_prefix": "LEG-CON",

        "documents_to_generate": 25,

        "actions": COMPLIANCE_ACTIONS,

        "objects": [
            "Contract",
            "Service Agreement",
            "Business Agreement",
            "Legal Document"
        ],

        "purposes": COMPLIANCE_PURPOSES,

        "rules": COMPLIANCE_RULES + [
            "must receive legal approval",
            "must be archived after expiration"
        ],

        "keywords": COMPLIANCE_KEYWORDS + [
            "contract",
            "agreement",
            "legal"
        ]

    },

    ###########################################################################
    # INTELLECTUAL PROPERTY
    ###########################################################################

    "Intellectual_Property": {

        "title_templates": INTELLECTUAL_PROPERTY_TITLES,
        "department": "Legal",
        "folder_name": "Legal",

        "security_domain": "Intellectual Property",

        "owner": "IP Protection Team",

        "classification": "Confidential",

        "risk_level": "Critical",

        "document_prefix": "LEG-IP",

        "documents_to_generate": 25,

        "actions": PRIVACY_ACTIONS,

        "objects": [
            "Patent",
            "Trademark",
            "Copyright",
            "Trade Secret"
        ],

        "purposes": PRIVACY_PURPOSES,

        "rules": PRIVACY_RULES + [
            "must not be disclosed publicly",
            "must be protected against unauthorized sharing"
        ],

        "keywords": PRIVACY_KEYWORDS + [
            "IP",
            "patent",
            "copyright"
        ]

    },

    ###########################################################################
    # DATA PRIVACY
    ###########################################################################

    "Data_Privacy": {

        "title_templates": DATA_PRIVACY_TITLES,
        "department": "Legal",
        "folder_name": "Legal",

        "security_domain": "Privacy",

        "owner": "Privacy Office",

        "classification": "Confidential",

        "risk_level": "Critical",

        "document_prefix": "LEG-PRI",

        "documents_to_generate": 25,

        "actions": PRIVACY_ACTIONS,

        "objects": PRIVACY_OBJECTS,

        "purposes": PRIVACY_PURPOSES,

        "rules": PRIVACY_RULES,

        "keywords": PRIVACY_KEYWORDS

    }

}