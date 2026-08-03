"""
sensitive_detector.py

Knowledge Firewall AI

Detects sensitive information before knowledge
is admitted into the enterprise repository.
"""

from __future__ import annotations

import re

from src.core.security.models import SensitiveDataResult


class SensitiveDetector:

    # ---------------------------------------------------------
    # Detection Patterns
    # ---------------------------------------------------------

    EMAIL = (
        r"\b[A-Za-z0-9._%+-]+@"
        r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    )

    IPV4 = (
        r"\b(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})"
        r"(?:\.(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})){3}\b"
    )

    URL = r"https?://[^\s]+"

    AWS_KEY = r"\bAKIA[0-9A-Z]{16}\b"

    BEARER = r"\bBearer\s+[A-Za-z0-9\-._~+/]+=*"

    PRIVATE_KEY = (
        r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?"
        r"PRIVATE KEY-----"
    )

    SSN = r"\b\d{3}-\d{2}-\d{4}\b"

    CREDIT_CARD = r"\b(?:\d[ -]*?){13,19}\b"

    PASSWORD = (
        r"(?i)\b(?:password|passwd|pwd)"
        r"\s*(?:=|:)\s*"
        r"[^\s,;]+"
    )

    # ---------------------------------------------------------

    def analyze(self, text: str) -> SensitiveDataResult:

        text = getattr(
            text,
            "content",
            str(text)
        )

        emails = re.findall(self.EMAIL, text)
        urls = re.findall(self.URL, text)
        ips = re.findall(self.IPV4, text)
        api_keys = re.findall(self.AWS_KEY, text)
        bearer_tokens = re.findall(self.BEARER, text)
        private_keys = re.findall(self.PRIVATE_KEY, text)
        ssns = re.findall(self.SSN, text)
        credit_cards = re.findall(self.CREDIT_CARD, text)
        passwords = re.findall(self.PASSWORD, text)

        total = (
            len(emails)
            + len(urls)
            + len(ips)
            + len(api_keys)
            + len(bearer_tokens)
            + len(private_keys)
            + len(ssns)
            + len(credit_cards)
            + len(passwords)
        )

        # -----------------------------------------------------
        # Risk calculation
        # -----------------------------------------------------

        risk = (
            len(emails) * 0.30
            + len(urls) * 0.20
            + len(ips) * 0.30
            + len(api_keys) * 0.50
            + len(bearer_tokens) * 0.60
            + len(private_keys) * 0.80
            + len(ssns) * 0.50
            + len(credit_cards) * 0.60
            + len(passwords) * 0.60
        )

        risk = min(risk, 1.0)

        if risk >= 0.50:
            recommendation = "Reject Upload"

        elif risk > 0:
            recommendation = "Manual Review"

        else:
            recommendation = "Accept"

        return SensitiveDataResult(
            emails=emails,
            urls=urls,
            ipv4_addresses=ips,
            api_keys=api_keys,
            bearer_tokens=bearer_tokens,
            private_keys=private_keys,
            ssns=ssns,
            credit_cards=credit_cards,
            passwords=passwords,
            total_findings=total,
            risk_score=round(risk, 2),
            recommendation=recommendation,
        )