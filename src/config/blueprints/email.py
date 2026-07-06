"""
Email Security Blueprint
"""

EMAIL_ACTIONS = [
    "Send",
    "Receive",
    "Archive",
    "Monitor",
    "Protect",
    "Scan",
    "Validate"
]

EMAIL_OBJECTS = [
    "Corporate Email",
    "Email Attachment",
    "Business Communication",
    "Outgoing Email",
    "Incoming Email"
]

EMAIL_PURPOSES = [
    "Protect enterprise email communications.",
    "Prevent phishing attacks.",
    "Reduce malware risks.",
    "Secure business communication."
]

EMAIL_RULES = [
    "must be scanned for malware",
    "must be encrypted when confidential",
    "must comply with company communication policy",
    "must be archived",
    "requires spam filtering",
    "must be monitored"
]

EMAIL_KEYWORDS = [
    "email",
    "phishing",
    "spam",
    "attachment",
    "communication"
]