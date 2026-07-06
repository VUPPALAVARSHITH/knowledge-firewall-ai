"""
Research Department Policy Catalog

Knowledge Firewall AI
"""

from src.config.blueprints.data_management import *
from src.config.title_templates.research_titles import (
    RESEARCH_DATA_PROTECTION_TITLES
)

RESEARCH_POLICIES = {

    ###########################################################################
    # RESEARCH DATA PROTECTION
    ###########################################################################

    "Research_Data_Protection": {

        "title_templates": RESEARCH_DATA_PROTECTION_TITLES,

        "department": "Research",

        "folder_name": "Research",

        "security_domain": "Research Data Protection",

        "owner": "Research Governance Team",

        "classification": "Confidential",

        "risk_level": "Critical",

        "document_prefix": "RES-DAT",

        "documents_to_generate": 25,

        "actions": DATA_ACTIONS,

        "objects": DATA_OBJECTS + [

            "Research Dataset",

            "Research Paper",

            "Prototype",

            "Experimental Result",

            "Research Repository",

            "Innovation Record"

        ],

        "purposes": DATA_PURPOSES + [

            "Protect intellectual property."

        ],

        "rules": DATA_RULES + [

            "must not be shared externally without approval",

            "must protect confidential research",

            "must maintain research integrity"

        ],

        "keywords": DATA_KEYWORDS + [

            "research",

            "innovation",

            "prototype",

            "intellectual property"

        ]

    }

}