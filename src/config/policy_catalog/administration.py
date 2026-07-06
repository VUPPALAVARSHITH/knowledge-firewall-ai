"""
Administration Department Policy Catalog

Knowledge Firewall AI
"""

from src.config.blueprints.physical_security import *
from src.config.title_templates.administration_titles import (
    VISITOR_MANAGEMENT_TITLES,
    PHYSICAL_SECURITY_TITLES,
    ASSET_MANAGEMENT_TITLES
)

ADMINISTRATION_POLICIES = {

    ###########################################################################
    # VISITOR MANAGEMENT
    ###########################################################################

    "Visitor_Management": {

        "title_templates": VISITOR_MANAGEMENT_TITLES,
        "department": "Administration",

        "folder_name": "Administration",

        "security_domain": "Visitor Management",

        "owner": "Facilities Team",

        "classification": "Internal",

        "risk_level": "Medium",

        "document_prefix": "ADM-VIS",

        "documents_to_generate": 25,

        "actions": PHYSICAL_ACTIONS,

        "objects": PHYSICAL_OBJECTS + [

            "Visitor Pass",
            "Guest",
            "Reception Area"

        ],

        "purposes": PHYSICAL_PURPOSES,

        "rules": PHYSICAL_RULES + [

            "must verify visitor identity",
            "must issue temporary visitor badge",
            "must escort visitors in restricted areas"

        ],

        "keywords": PHYSICAL_KEYWORDS + [

            "visitor",
            "guest",
            "reception"

        ]

    },

    ###########################################################################
    # PHYSICAL SECURITY
    ###########################################################################

    "Physical_Security": {

        "title_templates": PHYSICAL_SECURITY_TITLES,
        "department": "Administration",

        "folder_name": "Administration",

        "security_domain": "Facility Security",

        "owner": "Corporate Security",

        "classification": "Confidential",

        "risk_level": "High",

        "document_prefix": "ADM-PSC",

        "documents_to_generate": 25,

        "actions": PHYSICAL_ACTIONS,

        "objects": PHYSICAL_OBJECTS,

        "purposes": PHYSICAL_PURPOSES,

        "rules": PHYSICAL_RULES,

        "keywords": PHYSICAL_KEYWORDS

    },

    ###########################################################################
    # ASSET MANAGEMENT
    ###########################################################################

    "Asset_Management": {

        "title_templates": ASSET_MANAGEMENT_TITLES,

        "department": "Administration",

        "folder_name": "Administration",

        "security_domain": "Asset Management",

        "owner": "Asset Management Team",

        "classification": "Internal",

        "risk_level": "Medium",

        "document_prefix": "ADM-AST",

        "documents_to_generate": 25,

        "actions": [

            "Assign",
            "Track",
            "Recover",
            "Maintain",
            "Audit",
            "Register",
            "Replace",
            "Inspect",
            "Transfer",
            "Retire"

        ],

        "objects": [

            "Laptop",
            "Desktop",
            "Mobile Device",
            "Printer",
            "Monitor",
            "Hardware Asset",
            "Software License",
            "Office Equipment"

        ],

        "purposes": [

            "Protect enterprise assets.",

            "Maintain accurate inventory.",

            "Reduce asset loss.",

            "Support lifecycle management."

        ],

        "rules": [

            "must be assigned to an owner",

            "must be recorded in inventory",

            "must be audited annually",

            "must be securely disposed",

            "must report lost assets immediately"

        ],

        "keywords": [

            "asset",

            "inventory",

            "hardware",

            "device",

            "lifecycle"

        ]

    }

}