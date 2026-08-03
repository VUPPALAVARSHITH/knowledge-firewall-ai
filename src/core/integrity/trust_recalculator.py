"""
trust_recalculator.py

Knowledge Firewall AI

Compares integrity scans and detects trust drift.
"""

from __future__ import annotations

from src.core.integrity.integrity_models import (
    IntegrityScanReport,
    TrustDrift,
)


class TrustRecalculator:

    """
    Detects trust score changes between scans.
    """

    # ---------------------------------------------------------

    def compare(

        self,

        previous: IntegrityScanReport,

        current: IntegrityScanReport,

    ) -> list[TrustDrift]:

        previous_map = {

            result.policy_id: result

            for result in previous.results

        }

        drift_results = []

        # -----------------------------------------------------

        for current_result in current.results:

            old = previous_map.get(

                current_result.policy_id

            )

            if old is None:
                continue

            change = round(

                current_result.trust_score
                - old.trust_score,

                2

            )

            if abs(change) < 1:

                status = "Stable"

            elif change > 0:

                status = "Improved"

            else:

                if change <= -25:

                    status = "Critical"

                elif change <= -10:

                    status = "Warning"

                else:

                    status = "Minor"

            drift_results.append(

                TrustDrift(

                    policy_id=current_result.policy_id,

                    previous_trust=old.trust_score,

                    current_trust=current_result.trust_score,

                    drift=change,

                    status=status,

                )

            )

        return drift_results