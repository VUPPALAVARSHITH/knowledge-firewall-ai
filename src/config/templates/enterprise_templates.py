"""
Enterprise Template Configuration

Knowledge Firewall AI

Defines the available document templates used by the
Enterprise Policy Generator.
"""

ENTERPRISE_TEMPLATES = {

    "standard": {
        "name": "Standard Enterprise Policy",

        "sections": [
            "summary",
            "purpose",
            "scope",
            "definitions",
            "policy",
            "responsibilities",
            "implementation",
            "exceptions",
            "compliance",
            "audit",
            "related_policies",
            "revision_history"
        ]
    },

    "governance": {
        "name": "Governance Policy",

        "sections": [
            "executive_summary",
            "objectives",
            "scope",
            "governance",
            "controls",
            "exceptions",
            "compliance",
            "review"
        ]
    },

    "operational": {
        "name": "Operational Guideline",

        "sections": [
            "overview",
            "procedure",
            "roles",
            "implementation",
            "monitoring",
            "review"
        ]
    },

    "security_standard": {
        "name": "Security Standard",

        "sections": [
            "introduction",
            "security_controls",
            "implementation",
            "monitoring",
            "audit",
            "references"
        ]
    }

}