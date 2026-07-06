"""
IT Department Policy Catalog

Knowledge Firewall AI

Defines all IT-related enterprise policy categories.
"""

from src.config.blueprints.identity import (
    IDENTITY_ACTIONS,
    IDENTITY_OBJECTS,
    IDENTITY_PURPOSES,
    IDENTITY_RULES,
    IDENTITY_KEYWORDS
)

from src.config.blueprints.network import (
    NETWORK_ACTIONS,
    NETWORK_OBJECTS,
    NETWORK_PURPOSES,
    NETWORK_RULES,
    NETWORK_KEYWORDS
)

from src.config.blueprints.email import (
    EMAIL_ACTIONS,
    EMAIL_OBJECTS,
    EMAIL_PURPOSES,
    EMAIL_RULES,
    EMAIL_KEYWORDS
)

from src.config.blueprints.endpoint import (
    ENDPOINT_ACTIONS,
    ENDPOINT_OBJECTS,
    ENDPOINT_PURPOSES,
    ENDPOINT_RULES,
    ENDPOINT_KEYWORDS
)

from src.config.title_templates.it_titles import (
    PASSWORD_MANAGEMENT_TITLES,
    IDENTITY_AUTHENTICATION_TITLES,
    ACCESS_CONTROL_TITLES,
    REMOTE_ACCESS_TITLES,
    EMAIL_SECURITY_TITLES,
    SOFTWARE_INSTALLATION_TITLES,
)



IT_POLICIES = {

    ###########################################################################
    # PASSWORD MANAGEMENT
    ###########################################################################

    "Password_Management": {

        "title_templates": PASSWORD_MANAGEMENT_TITLES,
        "department": "Information Technology",
        "folder_name": "Information_Technology",
        "security_domain": "Identity Security",
        "owner": "Information Security Team",
        "classification": "Internal",
        "risk_level": "High",
        "document_prefix": "IT-PWD",
        "documents_to_generate": 25,

        "actions": IDENTITY_ACTIONS,

        "objects": IDENTITY_OBJECTS + [
            "Password",
            "Administrator Password",
            "Service Account Password"
        ],

        "purposes": IDENTITY_PURPOSES,

        "rules": IDENTITY_RULES + [
            "must not reuse previous passwords",
            "must contain at least 12 characters"
        ],

        "keywords": IDENTITY_KEYWORDS,
        
    },

    ###########################################################################
    # IDENTITY AUTHENTICATION
    ###########################################################################

    "Identity_Authentication": {

        "title_templates": IDENTITY_AUTHENTICATION_TITLES,
        "department": "Information Technology",
        "folder_name": "Information_Technology",
        "security_domain": "Identity Security",
        "owner": "Identity Management Team",
        "classification": "Internal",
        "risk_level": "High",
        "document_prefix": "IT-IDA",
        "documents_to_generate": 25,

        "actions": IDENTITY_ACTIONS,

        "objects": IDENTITY_OBJECTS + [
            "Authentication Token",
            "Single Sign-On",
            "Biometric Authentication",
            "Identity Provider"
        ],

        "purposes": IDENTITY_PURPOSES,

        "rules": IDENTITY_RULES + [
            "must verify user identity before access",
            "requires multi-factor authentication"
        ],

        "keywords": IDENTITY_KEYWORDS + [
            "SSO",
            "biometric",
            "identity provider"
        ],

        },

    ###########################################################################
    # ACCESS CONTROL
    ###########################################################################

    "Access_Control": {

        "title_templates": ACCESS_CONTROL_TITLES,
        "department": "Information Technology",
        "folder_name": "Information_Technology",
        "security_domain": "Access Management",
        "owner": "Access Management Team",
        "classification": "Confidential",
        "risk_level": "Critical",
        "document_prefix": "IT-ACC",
        "documents_to_generate": 25,

        "actions": IDENTITY_ACTIONS,

        "objects": IDENTITY_OBJECTS + [
            "Role",
            "Permission",
            "Access Privilege",
            "Security Group",
            "Administrative Access"
        ],

        "purposes": IDENTITY_PURPOSES + [
            "Ensure least-privilege access."
        ],

        "rules": IDENTITY_RULES + [
            "must follow least privilege principle",
            "must be reviewed quarterly",
            "requires role-based authorization"
        ],

        "keywords": IDENTITY_KEYWORDS + [
            "RBAC",
            "privilege",
            "authorization"
        ],

        
    },

    ###########################################################################
    # VPN
    ###########################################################################

    "Remote_Access": {

        "title_templates": REMOTE_ACCESS_TITLES,
        "department": "Information Technology",
        "folder_name": "Information_Technology",
        "security_domain": "Network Security",
        "owner": "Network Operations Team",
        "classification": "Internal",
        "risk_level": "High",
        "document_prefix": "IT-VPN",
        "documents_to_generate": 25,

        "actions": NETWORK_ACTIONS,
        "objects": NETWORK_OBJECTS,
        "purposes": NETWORK_PURPOSES,
        "rules": NETWORK_RULES,
        "keywords": NETWORK_KEYWORDS,
       
    },

    ###########################################################################
    # EMAIL SECURITY
    ###########################################################################

    "Email_Security": {

        "title_templates": EMAIL_SECURITY_TITLES,
        "department": "Information Technology",
        "folder_name": "Information_Technology",
        "security_domain": "Communication Security",
        "owner": "Messaging Team",
        "classification": "Internal",
        "risk_level": "High",
        "document_prefix": "IT-EML",
        "documents_to_generate": 25,

        "actions": EMAIL_ACTIONS,
        "objects": EMAIL_OBJECTS,
        "purposes": EMAIL_PURPOSES,
        "rules": EMAIL_RULES,
        "keywords": EMAIL_KEYWORDS,

       
    },

    ###########################################################################
    # SOFTWARE INSTALLATION
    ###########################################################################

    "Software_Installation": {

        "title_templates": SOFTWARE_INSTALLATION_TITLES,
        "department": "Information Technology",
        "folder_name": "Information_Technology",
        "security_domain": "Endpoint Security",
        "owner": "Desktop Support Team",
        "classification": "Internal",
        "risk_level": "Medium",
        "document_prefix": "IT-SFT",
        "documents_to_generate": 25,

        "actions": ENDPOINT_ACTIONS,
        "objects": ENDPOINT_OBJECTS,
        "purposes": ENDPOINT_PURPOSES,
        "rules": ENDPOINT_RULES,
        "keywords": ENDPOINT_KEYWORDS,
       
    }

}