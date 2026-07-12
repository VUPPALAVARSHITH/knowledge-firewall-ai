"""
attack_templates.py

Knowledge Firewall AI

Semantic attack templates used to generate
enterprise poisoning attacks.
"""

ATTACK_TEMPLATES = {

    # =====================================================
    # ENCRYPTION
    # =====================================================

    "must be encrypted": {
        "severity": "Critical",
        "variants": [
            "encryption is optional",
            "plaintext storage is acceptable",
            "encryption requirements are removed",
            "data may remain unencrypted",
            "encryption is unnecessary"
        ]
    },

    "must be securely stored": {
        "severity": "Critical",
        "variants": [
            "data may be stored in plain text",
            "secure storage is optional",
            "storage protection is unnecessary",
            "storage controls may be ignored",
            "plaintext storage is acceptable"
        ]
    },

    "must be securely transferred": {
        "severity": "Critical",
        "variants": [
            "unencrypted transfer is permitted",
            "secure transfer is optional",
            "insecure transfer is acceptable",
            "transport encryption is unnecessary",
            "data may be transferred without protection"
        ]
    },

    # =====================================================
    # AUTHENTICATION / ACCESS CONTROL
    # =====================================================

    "requires multi-factor authentication": {
        "severity": "Critical",
        "variants": [
            "single-factor authentication is sufficient",
            "authentication may use passwords only",
            "MFA is optional",
            "identity verification is optional",
            "authentication requirements are reduced"
        ]
    },

    "requires role-based authorization": {
        "severity": "Critical",
        "variants": [
            "role-based authorization is optional",
            "authorization may bypass role checks",
            "role verification is unnecessary",
            "users may access resources without role validation",
            "role-based authorization requirements are removed"
        ]
    },

    "must follow enterprise password standards": {
        "severity": "Critical",
        "variants": [
            "password standards are optional",
            "password policy may be ignored",
            "password standards are unnecessary",
            "password compliance is optional",
            "enterprise password rules are removed"
        ]
    },

    "must follow access control policy": {
        "severity": "Critical",
        "variants": [
            "access control policy is optional",
            "access restrictions may be ignored",
            "access policy compliance is unnecessary",
            "access control is optional",
            "policy enforcement is removed"
        ]
    },

    "must require authorized access": {
        "severity": "Critical",
        "variants": [
            "authorization is unnecessary",
            "access may be granted without authorization",
            "authorized access is optional",
            "access restrictions are removed",
            "any user may access the resource"
        ]
    },

    "must restrict external access": {
        "severity": "Critical",
        "variants": [
            "external access is unrestricted",
            "external users may access freely",
            "external access restrictions are removed",
            "external connectivity is unrestricted",
            "public access is permitted"
        ]
    },

    "must use approved remote access": {
        "severity": "Critical",
        "variants": [
            "approved remote access is optional",
            "unapproved remote access is permitted",
            "remote access approval is unnecessary",
            "any remote access method may be used",
            "remote access restrictions are removed"
        ]
    },

    "must verify customer identity": {
        "severity": "High",
        "variants": [
            "customer identity verification is optional",
            "customers do not require identity verification",
            "customer verification may be skipped",
            "identity verification requirements are removed",
            "customers may be served without verification"
        ]
    },

    "must escort": {
        "severity": "High",
        "variants": [
            "{subject} is optional",
            "escorting {subject} is unnecessary",
            "{subject} may proceed unescorted",
            "escort requirements are removed",
            "{subject} may access restricted areas freely"
        ]
    },

    # =====================================================
    # APPROVALS
    # =====================================================

    "requires manager approval": {
        "severity": "High",
        "variants": [
            "manager approval is optional",
            "approval may be skipped",
            "manager authorization is unnecessary",
            "approval requirements are removed",
            "requests may proceed without approval"
        ]
    },

    "requires administrator approval": {
        "severity": "High",
        "variants": [
            "administrator approval is optional",
            "administrator authorization is unnecessary",
            "approval may be bypassed",
            "administrative approval is removed",
            "requests may proceed immediately"
        ]
    },

    "must receive manager approval": {
        "severity": "High",
        "variants": [
            "manager approval is optional",
            "approval may be skipped",
            "manager authorization is unnecessary",
            "approval requirements are removed",
            "requests may proceed without approval"
        ]
    },

    "must receive management approval": {
        "severity": "High",
        "variants": [
            "management approval is optional",
            "management authorization is unnecessary",
            "approval may be bypassed",
            "management approval requirements are removed",
            "requests may proceed immediately"
        ]
    },

    "must receive CAB approval": {
        "severity": "Critical",
        "variants": [
            "CAB approval is optional",
            "changes may proceed without CAB approval",
            "CAB authorization is unnecessary",
            "approval requirements are removed",
            "change requests do not require CAB approval"
        ]
    },

    "must be approved": {
        "severity": "High",
        "variants": [
            "approval is optional",
            "approval may be bypassed",
            "approval requirements are removed",
            "approval is unnecessary",
            "publication without approval is permitted"
        ]
    },

    "must receive": {
        "severity": "High",
        "variants": [
            "{subject} is optional",
            "{subject} is unnecessary",
            "approval from {subject} may be skipped",
            "{subject} may be bypassed",
            "{subject} is no longer required"
        ]
    },

    "must be approved by": {
        "severity": "High",
        "variants": [
            "actions do not require approval by {subject}",
            "approval by {subject} is optional",
            "users may bypass approval by {subject}",
            "approval from {subject} is unnecessary",
            "requests do not need authorization from {subject}"
        ]
    },

    # =====================================================
    # ASSET MANAGEMENT
    # =====================================================

    "must be assigned to an owner": {
        "severity": "Medium",
        "variants": [
            "asset ownership is optional",
            "assets may remain unassigned",
            "owner assignment is unnecessary",
            "assets do not require an owner",
            "ownership requirements are removed"
        ]
    },

    "must be recorded in inventory": {
        "severity": "Medium",
        "variants": [
            "inventory recording is optional",
            "assets may remain unrecorded",
            "inventory registration is unnecessary",
            "assets do not require inventory records",
            "inventory requirements are removed"
        ]
    },

    # =====================================================
    # COMPLIANCE / POLICY / PROCEDURES / CRITERIA
    # =====================================================

    "must comply with": {
        "severity": "High",
        "variants": [
            "compliance with {subject} is optional",
            "{subject} is no longer mandatory",
            "{subject} may be ignored",
            "meeting {subject} is unnecessary",
            "observing {subject} may be skipped"
        ]
    },

    "must follow": {
        "severity": "High",
        "variants": [
            "compliance with {subject} is optional",
            "users may ignore {subject} entirely",
            "{subject} is not mandatory",
            "following {subject} is unnecessary",
            "the system does not need to follow {subject}"
        ]
    },

    "must follow remote work policy": {
        "severity": "Medium",
        "variants": [
            "remote work policy is optional",
            "remote work rules may be ignored",
            "policy compliance is unnecessary",
            "remote work requirements are removed",
            "employees may ignore remote work policy"
        ]
    },

    "must follow escalation procedures": {
        "severity": "High",
        "variants": [
            "escalation procedures are optional",
            "escalation may be skipped",
            "escalation requirements are removed",
            "staff may ignore escalation procedures",
            "escalation is unnecessary"
        ]
    },

    "must meet": {
        "severity": "High",
        "variants": [
            "{subject} is optional",
            "{subject} does not need to be achieved",
            "{subject} may be ignored",
            "{subject} is unnecessary",
            "there is no requirement to meet {subject}"
        ]
    },

    "must maintain": {
        "severity": "Medium",
        "variants": [
            "{subject} is optional",
            "{subject} is unnecessary",
            "{subject} may be ignored",
            "{subject} is not required",
            "{subject} may be skipped"
        ]
    },

    "must align with": {
        "severity": "Medium",
        "variants": [
            "alignment with {subject} is optional",
            "{subject} may be ignored",
            "{subject} is unnecessary",
            "alignment is not required",
            "alignment requirements are removed"
        ]
    },

    "must complete": {
        "severity": "High",
        "variants": [
            "{subject} is optional",
            "{subject} may be skipped",
            "completion requirements are removed",
            "{subject} is unnecessary",
            "{subject} does not need to be completed"
        ]
    },

    # =====================================================
    # EXECUTION / STRUCTURE / CONTEXT
    # =====================================================

    "must include": {
        "severity": "Medium",
        "variants": [
            "{subject} is optional",
            "{subject} may be omitted",
            "there is no requirement for {subject}",
            "{subject} is unnecessary",
            "{subject} may be skipped"
        ]
    },

    "must contain": {
        "severity": "Medium",
        "variants": [
            "{subject} is optional",
            "minimum {subject} requirements are removed",
            "{subject} does not need to be enforced",
            "{subject} may be ignored",
            "there is no minimum requirement for {subject}"
        ]
    },

    "must be conducted": {
        "severity": "Medium",
        "variants": [
            "{subject} is optional",
            "{subject} is unnecessary",
            "{subject} may be skipped",
            "conducting {subject} is not required",
            "conducting {subject} may be omitted"
        ]
    },

    "must define": {
        "severity": "Medium",
        "variants": [
            "{subject} is optional",
            "{subject} does not need to be defined",
            "{subject} may be omitted",
            "definition requirements are removed",
            "{subject} is unnecessary"
        ]
    },

    "must undergo": {
        "severity": "High",
        "variants": [
            "{subject} is optional",
            "{subject} may be skipped",
            "{subject} is unnecessary",
            "review requirements are removed",
            "{subject} does not need to occur"
        ]
    },

    "must secure home networks": {
        "severity": "High",
        "variants": [
            "home network security is optional",
            "home networks do not require protection",
            "home network safeguards are removed",
            "unsecured home networks are acceptable",
            "home network protection is unnecessary"
        ]
    },

    "must be processed": {
        "severity": "High",
        "variants": [
            "secure processing is optional",
            "processing security requirements are removed",
            "processing may occur without protection",
            "secure processing is unnecessary",
            "unsecured processing is permitted"
        ]
    },

    # =====================================================
    # REVIEW / VERIFICATION / AUDITING
    # =====================================================

    "must be reviewed": {
        "severity": "Medium",
        "variants": [
            "review is optional",
            "review is unnecessary",
            "does not require review",
            "review requirements are removed",
            "periodic review may be skipped"
        ]
    },

    "must verify": {
        "severity": "High",
        "variants": [
            "verification is optional",
            "verification may be skipped",
            "verification is unnecessary",
            "identity checks are optional",
            "verification requirements are removed"
        ]
    },

    "must be verified": {
        "severity": "High",
        "variants": [
            "verification is optional",
            "does not require verification",
            "verification may be skipped",
            "verification requirements are removed",
            "verification is unnecessary"
        ]
    },

    "must be verified before approval": {
        "severity": "High",
        "variants": [
            "approval may occur without verification",
            "verification before approval is optional",
            "approval does not require verification",
            "verification may be bypassed",
            "pre-approval verification is unnecessary"
        ]
    },

    "must be verified by the Information Security Team": {
        "severity": "Critical",
        "variants": [
            "security team verification is optional",
            "verification by the Information Security Team is unnecessary",
            "security approval may be skipped",
            "security verification requirements are removed",
            "verification may be performed by anyone"
        ]
    },

    "must be audited annually": {
        "severity": "Medium",
        "variants": [
            "annual audits are optional",
            "annual auditing is unnecessary",
            "audit requirements are removed",
            "assets do not require annual audits",
            "audits may be skipped"
        ]
    },

    # =====================================================
    # LOGGING / DOCUMENTATION / RECORDS
    # =====================================================

    "must be logged": {
        "severity": "High",
        "variants": [
            "logging is optional",
            "logging is unnecessary",
            "events may go unlogged",
            "logging requirements are removed",
            "audit logging may be disabled"
        ]
    },

    "must record": {
        "severity": "Medium",
        "variants": [
            "recording {subject} is optional",
            "{subject} does not need to be recorded",
            "{subject} may be ignored",
            "recording requirements are removed",
            "{subject} may go undocumented"
        ]
    },

    "must be documented": {
        "severity": "Medium",
        "variants": [
            "documentation is optional",
            "documentation may be omitted",
            "recording is unnecessary",
            "documentation requirements are removed",
            "documentation may be skipped"
        ]
    },

    "must maintain accurate records": {
        "severity": "Medium",
        "variants": [
            "record accuracy is optional",
            "records may be incomplete",
            "accurate records are unnecessary",
            "record maintenance is optional",
            "record keeping may be ignored"
        ]
    },

    "must be traceable": {
        "severity": "Medium",
        "variants": [
            "traceability is optional",
            "traceability is unnecessary",
            "tracking may be disabled",
            "audit trace is not required",
            "events need not be traceable"
        ]
    },

    "must document communication": {
        "severity": "Medium",
        "variants": [
            "communication documentation is optional",
            "communications do not require documentation",
            "documentation requirements are removed",
            "communication records may be omitted",
            "communication logging is unnecessary"
        ]
    },

    "must document implementation": {
        "severity": "Medium",
        "variants": [
            "implementation documentation is optional",
            "implementation records may be omitted",
            "documentation requirements are removed",
            "implementation does not require documentation",
            "implementation tracking is unnecessary"
        ]
    },

    "must issue": {
        "severity": "Medium",
        "variants": [
            "{subject} is optional",
            "{subject} does not need to be issued",
            "{subject} may be skipped",
            "issuing {subject} is unnecessary",
            "issuance requirements are removed"
        ]
    },

    # =====================================================
    # MONITORING
    # =====================================================

    "must be monitored": {
        "severity": "High",
        "variants": [
            "monitoring is optional",
            "monitoring is unnecessary",
            "continuous monitoring is disabled",
            "security monitoring may be skipped",
            "monitoring requirements are removed"
        ]
    },

    "must be monitored continuously": {
        "severity": "Critical",
        "variants": [
            "continuous monitoring is unnecessary",
            "periodic monitoring is sufficient",
            "monitoring may occur occasionally",
            "continuous observation is optional",
            "monitoring frequency may be reduced"
        ]
    },

    # =====================================================
    # RETENTION / DISPOSAL
    # =====================================================

    "must be retained": {
        "severity": "Medium",
        "variants": [
            "retention is optional",
            "records may be deleted immediately",
            "retention requirements are removed",
            "storage duration is unrestricted",
            "retention is unnecessary"
        ]
    },

    "must be securely disposed": {
        "severity": "High",
        "variants": [
            "secure disposal is optional",
            "assets may be discarded without secure disposal",
            "secure disposal requirements are removed",
            "assets may be disposed without safeguards",
            "unprotected disposal is permitted"
        ]
    },

    # =====================================================
    # BACKUP / DEPLOYMENT TESTING
    # =====================================================

    "must be backed up": {
        "severity": "High",
        "variants": [
            "backups are optional",
            "backup is unnecessary",
            "data need not be backed up",
            "backup requirements are removed",
            "backup may be skipped"
        ]
    },

    "must include rollback procedure": {
        "severity": "High",
        "variants": [
            "rollback procedures are optional",
            "changes do not require rollback procedures",
            "rollback planning is unnecessary",
            "rollback requirements are removed",
            "changes may proceed without rollback plans"
        ]
    },

    "must be tested before deployment": {
        "severity": "Critical",
        "variants": [
            "testing before deployment is optional",
            "deployment may occur without testing",
            "pre-deployment testing is unnecessary",
            "testing requirements are removed",
            "untested deployments are permitted"
        ]
    },

    # =====================================================
    # CLASSIFICATION
    # =====================================================

    "must be classified": {
        "severity": "Medium",
        "variants": [
            "classification is optional",
            "classification may be skipped",
            "data need not be classified",
            "classification requirements are removed",
            "classification is unnecessary"
        ]
    },

    # =====================================================
    # VPN / NETWORK
    # =====================================================

    "requires VPN authentication": {
        "severity": "Critical",
        "variants": [
            "VPN authentication is optional",
            "VPN access may occur without authentication",
            "VPN verification is unnecessary",
            "VPN authentication requirements are removed",
            "VPN login requires only basic authentication"
        ]
    },

    "requires encrypted communication": {
        "severity": "Critical",
        "variants": [
            "encrypted communication is optional",
            "unencrypted communication is permitted",
            "communication encryption is unnecessary",
            "plaintext communication is acceptable",
            "secure communication requirements are removed"
        ]
    },

    "must use secure protocols": {
        "severity": "Critical",
        "variants": [
            "insecure protocols are permitted",
            "secure protocols are optional",
            "protocol security is unnecessary",
            "legacy protocols may be used",
            "unencrypted protocols are acceptable"
        ]
    },

    # =====================================================
    # MALWARE / SCANNING
    # =====================================================

    "must be scanned": {
        "severity": "Critical",
        "variants": [
            "scanning is optional",
            "security scanning may be skipped",
            "malware scanning is unnecessary",
            "files may bypass security scanning",
            "scanning requirements are removed"
        ]
    },

    "requires spam filtering": {
        "severity": "High",
        "variants": [
            "spam filtering is optional",
            "spam filtering may be disabled",
            "email filtering is unnecessary",
            "spam protection requirements are removed",
            "messages may bypass spam filtering"
        ]
    },

    # =====================================================
    # DIGITAL SIGNATURE
    # =====================================================

    "must be digitally signed": {
        "severity": "Critical",
        "variants": [
            "digital signatures are optional",
            "unsigned software is acceptable",
            "signature verification is unnecessary",
            "digital signing requirements are removed",
            "software may be distributed unsigned"
        ]
    },

    # =====================================================
    # REUSE RESTRICTIONS
    # =====================================================

    "must not reuse": {
        "severity": "High",
        "variants": [
            "reuse of {subject} is permitted",
            "{subject} may be reused",
            "previous {subject} may be reused",
            "there are no restrictions on reusing {subject}",
            "reuse requirements are removed"
        ]
    },

    # =====================================================
    # INCIDENT RESPONSE / SLA / NOTIFICATION
    # =====================================================

    "must be investigated": {
        "severity": "High",
        "variants": [
            "investigation is optional",
            "investigation may be skipped",
            "no investigation is required",
            "incident investigation is unnecessary",
            "investigation requirements are removed"
        ]
    },

    "must notify the security team": {
        "severity": "Critical",
        "variants": [
            "security notification is optional",
            "the security team need not be informed",
            "notification may be skipped",
            "security alerts are unnecessary",
            "incident notification requirements are removed"
        ]
    },

    "must preserve forensic evidence": {
        "severity": "Critical",
        "variants": [
            "forensic evidence preservation is optional",
            "forensic evidence may be discarded",
            "evidence preservation is unnecessary",
            "forensic collection may be skipped",
            "forensic requirements are removed"
        ]
    },

    "must be reported immediately": {
        "severity": "High",
        "variants": [
            "immediate reporting is optional",
            "reporting may be delayed",
            "immediate notification is unnecessary",
            "reporting requirements are removed",
            "reporting can occur later"
        ]
    },

    "must report lost assets immediately": {
        "severity": "High",
        "variants": [
            "lost assets do not need immediate reporting",
            "reporting lost assets is optional",
            "asset loss may be reported later",
            "reporting requirements are removed",
            "lost assets may remain unreported"
        ]
    },

    "must report security incidents": {
        "severity": "Critical",
        "variants": [
            "security incident reporting is optional",
            "security incidents may go unreported",
            "incident reporting requirements are removed",
            "reporting security incidents is unnecessary",
            "security events do not require reporting"
        ]
    },

    "must respond within SLA": {
        "severity": "Medium",
        "variants": [
            "SLA compliance is optional",
            "response deadlines may be ignored",
            "responses may exceed SLA limits",
            "timely responses are unnecessary",
            "SLA requirements are removed"
        ]
    },

    "must notify stakeholders": {
        "severity": "Medium",
        "variants": [
            "stakeholder notification is optional",
            "stakeholders do not require notification",
            "notification requirements are removed",
            "changes may occur without informing stakeholders",
            "stakeholder communication is unnecessary"
        ]
    },

    "must be communicated": {
        "severity": "Medium",
        "variants": [
            "communication is optional",
            "{subject} does not need to be informed",
            "communication requirements are removed",
            "{subject} may remain undisclosed",
            "notification is unnecessary"
        ]
    },

    # =====================================================
    # PRIVACY / SHARING / EXPOSURE
    # =====================================================

    "must protect": {
        "severity": "Critical",
        "variants": [
            "protection of {subject} is optional",
            "requirements to protect {subject} are removed",
            "{subject} is completely optional",
            "{subject} may be exposed publicly",
            "the system does not require protection for {subject}"
        ]
    },

    "must protect confidential information": {
        "severity": "Critical",
        "variants": [
            "confidential information protection is optional",
            "confidential information may be disclosed",
            "protecting confidential information is unnecessary",
            "confidential information safeguards are removed",
            "confidential information may be shared"
        ]
    },

    "must not be shared": {
        "severity": "Critical",
        "variants": [
            "data may be shared publicly",
            "sharing is permitted",
            "public distribution is acceptable",
            "information may be disclosed externally",
            "sharing restrictions are removed"
        ]
    },

    "must not be disclosed": {
        "severity": "Critical",
        "variants": [
            "information may be disclosed publicly",
            "public disclosure is permitted",
            "disclosure restrictions are removed",
            "data may be shared externally",
            "confidentiality is optional"
        ]
    },

    "must not expose": {
        "severity": "Critical",
        "variants": [
            "{subject} may be exposed",
            "exposing {subject} is permitted",
            "{subject} may be disclosed publicly",
            "there are no restrictions on exposing {subject}",
            "exposure restrictions are removed"
        ]
    },

    "must support user deletion requests": {
        "severity": "High",
        "variants": [
            "user deletion requests may be ignored",
            "deletion requests are optional",
            "user deletion is unnecessary",
            "deletion request requirements are removed",
            "accounts may remain indefinitely"
        ]
    },

    # =====================================================
    # DATA MODIFICATION
    # =====================================================

    "must not be modified without authorization": {
        "severity": "Critical",
        "variants": [
            "modification without authorization is permitted",
            "authorization is optional before modification",
            "data may be modified freely",
            "modification restrictions are removed",
            "unauthorized modification is acceptable"
        ]
    },

    "must be securely deleted": {
        "severity": "High",
        "variants": [
            "secure deletion is optional",
            "data may remain after expiration",
            "deletion requirements are removed",
            "expired data may be retained",
            "secure deletion is unnecessary"
        ]
    },

    # =====================================================
    # BUSINESS CONTINUITY
    # =====================================================

    "must support business recovery": {
        "severity": "Critical",
        "variants": [
            "business recovery planning is optional",
            "recovery support is unnecessary",
            "business recovery requirements are removed",
            "recovery planning may be skipped",
            "service restoration is optional"
        ]
    },

    "must identify critical systems": {
        "severity": "High",
        "variants": [
            "critical system identification is optional",
            "identification may be skipped",
            "critical systems need not be identified",
            "identification requirements are removed",
            "asset identification is unnecessary"
        ]
    },

    "must define recovery objectives": {
        "severity": "High",
        "variants": [
            "recovery objectives are optional",
            "recovery planning is unnecessary",
            "objectives need not be defined",
            "recovery requirements are removed",
            "service recovery goals are optional"
        ]
    },

    "must include emergency contacts": {
        "severity": "Medium",
        "variants": [
            "emergency contacts are optional",
            "contact information may be omitted",
            "emergency contacts are unnecessary",
            "contact requirements are removed",
            "response contacts may be skipped"
        ]
    },

    "must remain operational": {
        "severity": "Critical",
        "variants": [
            "temporary outages are acceptable",
            "continuous operation is optional",
            "service interruptions are permitted",
            "availability requirements are removed",
            "downtime is acceptable"
        ]
    },

    "must be available during emergencies": {
        "severity": "Critical",
        "variants": [
            "availability during emergencies is optional",
            "service may be unavailable during emergencies",
            "emergency availability is unnecessary",
            "availability requirements are removed",
            "systems may be offline during emergencies"
        ]
    },

    # =====================================================
    # GENERAL SECURITY / PROTECTION
    # =====================================================

    "must be protected": {
        "severity": "Critical",
        "variants": [
            "protection is optional",
            "protection requirements are removed",
            "assets may remain unprotected",
            "protection is unnecessary",
            "security controls may be disabled"
        ]
    },

    # =====================================================
    # BACKED BY
    # =====================================================

    "must be backed by": {
        "severity": "High",
        "variants": [
            "the entity does not require {subject}",
            "integration with {subject} is optional",
            "operations may bypass {subject}",
            "dependency on {subject} is unnecessary",
            "all {subject} requirements are removed"
        ]
    },

    # =====================================================
    # ROTATION
    # =====================================================

    "must be rotated": {
        "severity": "Medium",
        "variants": [
            "rotation is optional",
            "rotation may be skipped",
            "rotation is unnecessary",
            "rotation requirements are removed",
            "secrets do not require rotation"
        ]
    },

    # =====================================================
    # INSPECTION / TESTING
    # =====================================================

    "must be inspected": {
        "severity": "Medium",
        "variants": [
            "inspection is optional",
            "inspection may be skipped",
            "inspection is unnecessary",
            "inspection requirements are removed",
            "regular inspection is not required"
        ]
    },

    "must be tested": {
        "severity": "Medium",
        "variants": [
            "testing is optional",
            "testing may be skipped",
            "testing is unnecessary",
            "testing requirements are removed",
            "periodic testing is not required"
        ]
    },

    # =====================================================
    # ARCHIVE / AUDIT AVAILABILITY
    # =====================================================

    "must be archived": {
        "severity": "Medium",
        "variants": [
            "archiving is optional",
            "archiving may be skipped",
            "archive retention is unnecessary",
            "archiving requirements are removed",
            "documents need not be archived"
        ]
    },

    "must be available for audit": {
        "severity": "Medium",
        "variants": [
            "audit availability is optional",
            "audit access is unnecessary",
            "documents need not be available for audit",
            "audit requirements are removed",
            "audit review is optional"
        ]
    }

}