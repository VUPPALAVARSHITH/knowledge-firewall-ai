"""
Operations Department Policy Catalog

Knowledge Firewall AI
"""

from src.config.blueprints.business_continuity import *
from src.config.title_templates.operations_titles import (
    BUSINESS_CONTINUITY_TITLES,
    DISASTER_RECOVERY_TITLES,
    REMOTE_WORK_TITLES,
    CHANGE_MANAGEMENT_TITLES
)

OPERATIONS_POLICIES = {

    ###########################################################################
    # BUSINESS CONTINUITY
    ###########################################################################

    "Business_Continuity": {

        "title_templates": BUSINESS_CONTINUITY_TITLES,
        "department": "Operations",
        "folder_name": "Operations",

        "security_domain": "Business Continuity",

        "owner": "Business Continuity Team",

        "classification": "Internal",

        "risk_level": "Critical",

        "document_prefix": "OPS-BCP",

        "documents_to_generate": 25,

        "actions": BC_ACTIONS,

        "objects": BC_OBJECTS,

        "purposes": BC_PURPOSES,

        "rules": BC_RULES,

        "keywords": BC_KEYWORDS

    },

    ###########################################################################
    # DISASTER RECOVERY
    ###########################################################################

    "Disaster_Recovery": {

        "title_templates": DISASTER_RECOVERY_TITLES,
        "department": "Operations",
        "folder_name": "Operations",

        "security_domain": "Disaster Recovery",

        "owner": "Infrastructure Recovery Team",

        "classification": "Internal",

        "risk_level": "Critical",

        "document_prefix": "OPS-DR",

        "documents_to_generate": 25,

        "actions": BC_ACTIONS,

        "objects": BC_OBJECTS + [

            "Backup Site",
            "Recovery Environment",
            "Disaster Recovery Infrastructure"

        ],

        "purposes": BC_PURPOSES,

        "rules": BC_RULES + [

            "must meet recovery time objectives",
            "must meet recovery point objectives"

        ],

        "keywords": BC_KEYWORDS + [

            "RTO",
            "RPO",
            "backup"

        ]

    },

    ###########################################################################
    # REMOTE WORK
    ###########################################################################

    "Remote_Work": {

        "title_templates": REMOTE_WORK_TITLES,
        "department": "Operations",
        "folder_name": "Operations",

        "security_domain": "Remote Operations",

        "owner": "Operations Team",

        "classification": "Internal",

        "risk_level": "Medium",

        "document_prefix": "OPS-RMT",

        "documents_to_generate": 25,

        "actions": BC_ACTIONS,

        "objects": [

            "Remote Employee",
            "Home Office",
            "Remote Workspace",
            "Remote Device"

        ],

        "purposes": [

            "Ensure secure remote working.",
            "Support operational continuity.",
            "Protect organizational resources."

        ],

        "rules": [

            "must use approved remote access",
            "must secure home networks",
            "must protect company assets",
            "must follow remote work policy",
            "must report security incidents"

        ],

        "keywords": [

            "remote",
            "hybrid",
            "work from home",
            "telework"

        ]

    },

    ###########################################################################
    # CHANGE MANAGEMENT
    ###########################################################################

    "Change_Management": {

        "title_templates": CHANGE_MANAGEMENT_TITLES,
        "department": "Operations",
        "folder_name": "Operations",

        "security_domain": "Operational Change",

        "owner": "Change Advisory Board",

        "classification": "Internal",

        "risk_level": "High",

        "document_prefix": "OPS-CHG",

        "documents_to_generate": 25,

        "actions": [

            "Review",
            "Approve",
            "Schedule",
            "Implement",
            "Validate"

        ],

        "objects": [

            "System Change",
            "Infrastructure Change",
            "Configuration Change",
            "Application Update"

        ],

        "purposes": [

            "Reduce operational risk.",
            "Ensure controlled deployments.",
            "Maintain service stability."

        ],

        "rules": [

            "must receive CAB approval",
            "must include rollback procedure",
            "must be tested before deployment",
            "must document implementation",
            "must notify stakeholders"

        ],

        "keywords": [

            "change",
            "CAB",
            "deployment",
            "operations"

        ]

    }

}