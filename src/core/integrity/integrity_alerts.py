"""
integrity_alerts.py

Knowledge Firewall AI

Generates security alerts after repository
integrity verification.
"""

from __future__ import annotations

from dataclasses import dataclass

from src.core.integrity.integrity_models import (
    IntegrityResult,
    TrustDrift,
)


@dataclass(slots=True)
class IntegrityAlert:

    severity: str

    policy_id: str

    title: str

    description: str


class IntegrityAlertEngine:

    """
    Generates repository integrity alerts.
    """

    # -----------------------------------------------------

    def generate(

        self,

        results: list[IntegrityResult],

        drift: list[TrustDrift] | None = None,

    ) -> list[IntegrityAlert]:

        alerts = []

        # ---------------------------------------------
        # Scan Results
        # ---------------------------------------------

        for result in results:

            if result.attack_detected:

                alerts.append(

                    IntegrityAlert(

                        severity="Critical",

                        policy_id=result.policy_id,

                        title="Knowledge Manipulation Detected",

                        description=(
                            "Enterprise attack signature detected."
                        ),

                    )

                )

            if result.sensitive_data_detected:

                alerts.append(

                    IntegrityAlert(

                        severity="High",

                        policy_id=result.policy_id,

                        title="Sensitive Information Detected",

                        description=(
                            "Sensitive enterprise information exists."
                        ),

                    )

                )

            if result.decision == "REVIEW":

                alerts.append(

                    IntegrityAlert(

                        severity="Medium",

                        policy_id=result.policy_id,

                        title="Integrity Review Required",

                        description=(
                            "Policy requires manual verification."
                        ),

                    )

                )

        # ---------------------------------------------
        # Trust Drift
        # ---------------------------------------------

        if drift:

            for item in drift:

                if item.status == "Critical":

                    alerts.append(

                        IntegrityAlert(

                            severity="Critical",

                            policy_id=item.policy_id,

                            title="Critical Trust Drift",

                            description=(
                                f"Trust decreased by "
                                f"{abs(item.drift):.2f} points."
                            ),

                        )

                    )

                elif item.status == "Warning":

                    alerts.append(

                        IntegrityAlert(

                            severity="High",

                            policy_id=item.policy_id,

                            title="Trust Score Declining",

                            description=(
                                f"Trust decreased by "
                                f"{abs(item.drift):.2f} points."
                            ),

                        )

                    )

                elif item.status == "Improved":

                    alerts.append(

                        IntegrityAlert(

                            severity="Info",

                            policy_id=item.policy_id,

                            title="Trust Improved",

                            description=(
                                f"Trust increased by "
                                f"{item.drift:.2f} points."
                            ),

                        )

                    )

        return alerts