from src.enterprise.managers.repository_manager import RepositoryManager
from src.enterprise.models import (
    Activity,
    Alert,
    DashboardSummary,
)


class DashboardManager:

    def __init__(self):

        self.repository = RepositoryManager()

    # ---------------------------------------------------------

    def get_summary(self):

        return DashboardSummary(

            total_policies=self.repository.total_policies(),

            total_chunks=self.repository.total_chunks(),

            trusted_chunks=self.repository.trusted_chunks(),

            suspicious_chunks=self.repository.suspicious_chunks(),

            blocked_chunks=self.repository.blocked_chunks(),

            average_trust=self.repository.average_trust(),

            repository_health=self._repository_health(),

            last_scan="Today"

        )

    # ---------------------------------------------------------

    def get_department_statistics(self):

        return self.repository.department_statistics()

    # ---------------------------------------------------------

    def get_trust_distribution(self):

        return self.repository.trust_distribution()

    # ---------------------------------------------------------

    def get_recent_policies(self):

        return self.repository.get_policy_table().head(10)

    # ---------------------------------------------------------

    def get_recent_activity(self):

        return [

            Activity(

                "Today",

                f"{self.repository.total_policies()} enterprise policies indexed",

                "Success"

            ),

            Activity(

                "Today",

                f"{self.repository.total_chunks()} semantic chunks verified",

                "Success"

            ),

            Activity(

                "Today",

                "Fingerprint database synchronized",

                "Success"

            ),

        ]

    # ---------------------------------------------------------

    def get_alerts(self):

        alerts = []

        blocked = self.repository.blocked_chunks()

        suspicious = self.repository.suspicious_chunks()

        trust = self.repository.average_trust()

        # -----------------------------------------
        # Blocked Knowledge
        # -----------------------------------------

        if blocked > 0:

            alerts.append(

                Alert(

                    severity="High",

                    title="Blocked Knowledge Detected",

                    description=(
                        f"{blocked} blocked chunks require "
                        "administrator attention."
                    )

                )

            )

        # -----------------------------------------
        # Suspicious Knowledge
        # -----------------------------------------

        if suspicious > 0:

            alerts.append(

                Alert(

                    severity="Medium",

                    title="Suspicious Knowledge Found",

                    description=(
                        f"{suspicious} suspicious chunks "
                        "should be reviewed."
                    )

                )

            )

        # -----------------------------------------
        # Repository Trust
        # -----------------------------------------

        if trust < 90:

            alerts.append(

                Alert(

                    severity="High",

                    title="Repository Trust Degraded",

                    description=(
                        f"Average trust has dropped to "
                        f"{trust:.2f}%."
                    )

                )

            )

        elif trust < 95:

            alerts.append(

                Alert(

                    severity="Medium",

                    title="Repository Trust Warning",

                    description=(
                        f"Average trust is "
                        f"{trust:.2f}%."
                    )

                )

            )

        else:

            alerts.append(

                Alert(

                    severity="Low",

                    title="Repository Healthy",

                    description=(
                        "Knowledge repository is operating "
                        "normally."
                    )

                )

            )

        return alerts

    # ---------------------------------------------------------

    def _repository_health(self):

        trust = self.repository.average_trust()

        if trust >= 98:

            return "Excellent"

        elif trust >= 95:

            return "Healthy"

        elif trust >= 90:

            return "Warning"

        return "Critical"