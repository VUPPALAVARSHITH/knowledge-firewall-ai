"""
parser.py

Knowledge Firewall AI

Parses enterprise policy documents into structured
Policy objects.
"""

import re
from pathlib import Path

from src.core.preprocessing.models import Policy


class PolicyParser:

    def __init__(self):
        pass

    # -------------------------------------------------------
    # Read file
    # -------------------------------------------------------

    def read(self, filepath: Path):

        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()

    # -------------------------------------------------------
    # Extract simple metadata field
    # -------------------------------------------------------

    def extract_field(self, text, field):

        pattern = rf"{re.escape(field)}\s*:\s*(.*)"

        match = re.search(pattern, text)

        if match:
            return match.group(1).strip()

        return ""

    # -------------------------------------------------------
    # Extract section
    # -------------------------------------------------------

    def extract_section(self, text, start, end=None):

        if end:
            pattern = rf"{re.escape(start)}(.*?){re.escape(end)}"
        else:
            pattern = rf"{re.escape(start)}(.*)"

        match = re.search(pattern, text, re.DOTALL)

        if not match:
            return ""

        return match.group(1).strip()

    # -------------------------------------------------------
    # Extract list
    # -------------------------------------------------------

    def extract_list(self, text):

        items = []

        for line in text.splitlines():

            line = line.strip()

            if line.startswith("-"):

                items.append(line[1:].strip())

        return items

    # -------------------------------------------------------
    # Extract policy statements
    # -------------------------------------------------------

    def extract_policy_statements(self, text):

        statements = []

        for line in text.splitlines():

            line = line.strip()

            if re.match(r"^\d+\.", line):

                statements.append(
                    re.sub(r"^\d+\.\s*", "", line)
                )

        return statements

    # -------------------------------------------------------
    # Parse
    # -------------------------------------------------------

    def parse(self, filepath: Path):

        text = self.read(filepath)

        title = self.extract_section(
            text,
            "TITLE",
            "1. PURPOSE"
        ).strip()

        purpose = self.extract_section(
            text,
            "1. PURPOSE",
            "2. SCOPE"
        ).strip()

        scope = self.extract_section(
            text,
            "2. SCOPE",
            "3. DEFINITIONS"
        ).strip()

        definitions = self.extract_list(
            self.extract_section(
                text,
                "3. DEFINITIONS",
                "4. POLICY STATEMENTS"
            )
        )

        policy_statements = self.extract_policy_statements(
            self.extract_section(
                text,
                "4. POLICY STATEMENTS",
                "5. RESPONSIBILITIES"
            )
        )

        responsibilities = self.extract_list(
            self.extract_section(
                text,
                "5. RESPONSIBILITIES",
                "6. EXCEPTIONS"
            )
        )

        exceptions = self.extract_list(
            self.extract_section(
                text,
                "6. EXCEPTIONS",
                "7. COMPLIANCE"
            )
        )

        compliance = self.extract_list(
            self.extract_section(
                text,
                "7. COMPLIANCE",
                "8. REVIEW CYCLE"
            )
        )

        review = self.extract_section(
            text,
            "8. REVIEW CYCLE",
            "KEYWORDS"
        ).strip()

        keywords = [

            k.strip()

            for k in

            self.extract_section(
                text,
                "KEYWORDS"
            ).split(",")

            if k.strip()
        ]

        return Policy(

            policy_id=self.extract_field(text, "Policy ID"),

            department=self.extract_field(text, "Department"),

            category=self.extract_field(text, "Category"),

            security_domain=self.extract_field(
                text,
                "Security Domain"
            ),

            classification=self.extract_field(
                text,
                "Classification"
            ),

            risk_level=self.extract_field(
                text,
                "Risk Level"
            ),

            version=self.extract_field(
                text,
                "Version"
            ),

            status=self.extract_field(
                text,
                "Status"
            ),

            owner=self.extract_field(
                text,
                "Owner Team"
            ),

            title=title,

            purpose=purpose,

            scope=scope,

            definitions=definitions,

            policy_statements=policy_statements,

            responsibilities=responsibilities,

            exceptions=exceptions,

            compliance=compliance,

            review_cycle=review,

            keywords=keywords,

            source_file=str(filepath)

        )


if __name__ == "__main__":

    parser = PolicyParser()

    file = Path(
        "data/enterprise/Information_Technology/Password_Management/IT-PWD-001.txt"
    )

    policy = parser.parse(file)

    print(policy)