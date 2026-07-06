"""
Identity Security Blueprint

Reusable templates for all identity-related policies.
"""

IDENTITY_ACTIONS = [
    "Create",
    "Reset",
    "Update",
    "Recover",
    "Protect",
    "Store",
    "Validate",
    "Rotate",
    "Revoke",
    "Disable"
]

IDENTITY_OBJECTS = [
    "Password",
    "Credentials",
    "Administrator Password",
    "Service Account Password",
    "User Password",
    "Authentication Token",
    "Privileged Account",
    "Identity Profile"
]

IDENTITY_PURPOSES = [
    "Protect enterprise identities.",
    "Prevent unauthorized access.",
    "Strengthen authentication controls.",
    "Reduce identity-related risks.",
    "Ensure compliance with organizational security policies.",
    "Improve credential management.",
    "Support Zero Trust security architecture.",
    "Protect critical enterprise resources."
]

IDENTITY_RULES = [

    "requires manager approval",

    "requires multi-factor authentication",

    "must be encrypted",

    "must be securely stored",

    "must not be shared",

    "must be logged",

    "must follow enterprise password standards",

    "must be reviewed every 90 days",

    "must comply with ISO 27001 requirements",

    "must be verified by the Information Security Team",

    "must be monitored continuously",

    "must be protected against unauthorized disclosure",

    "must be rotated periodically",

    "must be backed by identity verification"

]

IDENTITY_KEYWORDS = [

    "identity",

    "authentication",

    "password",

    "credentials",

    "security",

    "MFA",

    "authorization",

    "access control"

]