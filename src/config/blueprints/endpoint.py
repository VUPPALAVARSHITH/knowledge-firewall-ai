"""
Endpoint Security Blueprint
"""

ENDPOINT_ACTIONS = [
    "Install",
    "Update",
    "Remove",
    "Verify",
    "Approve",
    "Protect"
]

ENDPOINT_OBJECTS = [
    "Software",
    "Application",
    "Operating System",
    "Security Patch",
    "Enterprise Software"
]

ENDPOINT_PURPOSES = [
    "Protect enterprise endpoints.",
    "Prevent unauthorized software installation.",
    "Maintain endpoint compliance."
]

ENDPOINT_RULES = [
    "requires administrator approval",
    "must be digitally signed",
    "must be verified",
    "must be logged",
    "must comply with software policy",
    "must be scanned before installation"
]

ENDPOINT_KEYWORDS = [
    "software",
    "installation",
    "endpoint",
    "application",
    "patch"
]