"""
repository_scanner.py

Knowledge Firewall AI

Repository Integrity Scanner

Scans every enterprise policy stored inside the
trusted repository.
"""

from pathlib import Path

from src.config.path_config import ENTERPRISE_DIR


class RepositoryScanner:

    """
    Scans the trusted enterprise repository.
    """

    def __init__(self):

        self.repository = ENTERPRISE_DIR

    # -----------------------------------------------------

    def scan(self) -> list[Path]:

        """
        Returns every enterprise policy.
        """

        return sorted(

            self.repository.rglob("*.txt")

        )

    # -----------------------------------------------------

    def count(self) -> int:

        """
        Number of policies.
        """

        return len(

            self.scan()

        )

    # -----------------------------------------------------

    def departments(self) -> list[str]:

        """
        Available departments.
        """

        departments = {

            path.parent.parent.name

            for path in self.scan()

        }

        return sorted(

            departments

        )

    # -----------------------------------------------------

    def categories(self) -> list[str]:

        """
        Available categories.
        """

        categories = {

            path.parent.name

            for path in self.scan()

        }

        return sorted(

            categories

        )

    # -----------------------------------------------------

    def by_department(

        self,

        department: str

    ) -> list[Path]:

        return [

            path

            for path in self.scan()

            if path.parent.parent.name == department

        ]

    # -----------------------------------------------------

    def by_category(

        self,

        category: str

    ) -> list[Path]:

        return [

            path

            for path in self.scan()

            if path.parent.name == category

        ]