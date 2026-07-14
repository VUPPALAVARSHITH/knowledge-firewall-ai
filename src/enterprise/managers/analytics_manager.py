"""
analytics_manager.py

Knowledge Firewall AI

Enterprise Analytics Manager.
"""

from src.enterprise.managers.repository_manager import RepositoryManager


class AnalyticsManager:

    def __init__(self):

        self.repository = RepositoryManager()

    # -----------------------------------------------------

    def get_summary(self):

        return {

            "policies": self.repository.total_policies(),

            "chunks": self.repository.total_chunks(),

            "trusted": self.repository.trusted_chunks(),

            "suspicious": self.repository.suspicious_chunks(),

            "blocked": self.repository.blocked_chunks(),

            "average_trust": self.repository.average_trust(),

        }

    # -----------------------------------------------------

    def trust_distribution(self):

        return self.repository.trust_distribution()

    # -----------------------------------------------------

    def department_distribution(self):

        return self.repository.department_statistics()

    # -----------------------------------------------------

    def category_distribution(self):

        policies = self.repository.list_policies()

        if policies.empty:

            return policies

        return (

            policies

            .groupby("category")

            .size()

            .reset_index(name="Policies")

        )

    # -----------------------------------------------------

    def risk_distribution(self):

        policies = self.repository.list_policies()

        if policies.empty:

            return policies

        return (

            policies

            .groupby("risk_level")

            .size()

            .reset_index(name="Policies")

        )

    # -----------------------------------------------------

    def classification_distribution(self):

        policies = self.repository.list_policies()

        if policies.empty:

            return policies

        return (

            policies

            .groupby("classification")

            .size()

            .reset_index(name="Policies")

        )