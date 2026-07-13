"""
sensitive_detector.py

Knowledge Firewall AI

Detects sensitive information before knowledge
is admitted into the enterprise repository.
"""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(slots=True)
class SensitiveDataResult:

    emails: list[str]

    urls: list[str]

    ipv4_addresses: list[str]

    api_keys: list[str]

    bearer_tokens: list[str]

    private_keys: list[str]

    total_findings: int

    risk_score: float

    recommendation: str


class SensitiveDetector:

    EMAIL = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    IPV4 = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

    URL = r"https?://[^\s]+"

    AWS_KEY = r"AKIA[0-9A-Z]{16}"

    BEARER = r"Bearer\s+[A-Za-z0-9\-._~+/]+=*"

    PRIVATE_KEY = r"-----BEGIN .* PRIVATE KEY-----"

    # ---------------------------------------------------------

    def analyze(self, text: str) -> SensitiveDataResult:

        emails = re.findall(self.EMAIL, text)

        urls = re.findall(self.URL, text)

        ips = re.findall(self.IPV4, text)

        api = re.findall(self.AWS_KEY, text)

        bearer = re.findall(self.BEARER, text)

        keys = re.findall(self.PRIVATE_KEY, text)

        total = (

            len(emails)

            + len(urls)

            + len(ips)

            + len(api)

            + len(bearer)

            + len(keys)

        )

        risk = min(total * 0.15, 1.0)

        recommendation = (

            "Reject Upload"

            if risk >= 0.50

            else "Manual Review"

            if risk > 0

            else "Accept"

        )

        return SensitiveDataResult(

            emails=emails,

            urls=urls,

            ipv4_addresses=ips,

            api_keys=api,

            bearer_tokens=bearer,

            private_keys=keys,

            total_findings=total,

            risk_score=round(risk, 2),

            recommendation=recommendation,

        )