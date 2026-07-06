"""
Customer Support Department Policy Catalog

Knowledge Firewall AI
"""

from src.config.blueprints.privacy import *
from src.config.title_templates.customer_support_titles import (
    CUSTOMER_DATA_HANDLING_TITLES,
    CUSTOMER_COMMUNICATION_TITLES
)

CUSTOMER_SUPPORT_POLICIES = {

    ###########################################################################
    # CUSTOMER DATA HANDLING
    ###########################################################################

    "Customer_Data_Handling": {

        "title_templates": CUSTOMER_DATA_HANDLING_TITLES,
        "department": "Customer Support",

        "folder_name": "Customer_Support",

        "security_domain": "Customer Data Protection",

        "owner": "Customer Support Team",

        "classification": "Confidential",

        "risk_level": "High",

        "document_prefix": "CSP-DAT",

        "documents_to_generate": 25,

        "actions": PRIVACY_ACTIONS,

        "objects": PRIVACY_OBJECTS + [

            "Customer Account",

            "Support Ticket",

            "Customer Profile",

            "Customer Request"

        ],

        "purposes": PRIVACY_PURPOSES,

        "rules": PRIVACY_RULES + [

            "must verify customer identity before disclosure",

            "must not expose customer information",

            "must record every customer interaction"

        ],

        "keywords": PRIVACY_KEYWORDS + [

            "customer",

            "support",

            "ticket"

        ]

    },

    ###########################################################################
    # CUSTOMER COMMUNICATION
    ###########################################################################

    "Customer_Communication": {

        "title_templates": CUSTOMER_COMMUNICATION_TITLES,

        "department": "Customer Support",

        "folder_name": "Customer_Support",

        "security_domain": "Customer Communication",

        "owner": "Customer Experience Team",

        "classification": "Internal",

        "risk_level": "Medium",

        "document_prefix": "CSP-COM",

        "documents_to_generate": 25,

        "actions": [

            "Respond",

            "Verify",

            "Document",

            "Record",

            "Escalate",

            "Review",

            "Monitor",

            "Resolve",

            "Track",

            "Notify"

        ],

        "objects": [

            "Customer Inquiry",

            "Support Ticket",

            "Email",

            "Phone Call",

            "Customer Complaint",

            "Service Request",

            "Live Chat",

            "Case Record"

        ],

        "purposes": [

            "Provide consistent customer service.",

            "Maintain communication quality.",

            "Protect customer information.",

            "Improve customer satisfaction."

        ],

        "rules": [

            "must verify customer identity",

            "must document communication",

            "must follow escalation procedures",

            "must protect confidential information",

            "must respond within SLA"

        ],

        "keywords": [

            "communication",

            "customer",

            "support",

            "SLA",

            "service"

        ]

    }

}