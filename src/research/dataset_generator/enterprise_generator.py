"""
enterprise_generator.py

Knowledge Firewall AI
Enterprise Knowledge Generator

Generates realistic enterprise policy documents
for the enterprise knowledge base.
"""

from datetime import datetime, timedelta
import random
from src.config.document_template import DOCUMENT_TEMPLATE
from src.config.company_config import COMPANY
from src.config.policy_catalog import POLICY_CATALOG
from src.config.path_config import ENTERPRISE_DIR


class EnterprisePolicyGenerator:
    def __init__(self):
        self.company = COMPANY
        self.catalog = POLICY_CATALOG

        # Fixed seed for reproducible dataset generation
        self.random = random.Random(42)

    # ---------------------------------------------------
    # Generate Policy ID
    # ---------------------------------------------------

    def generate_policy_id(self, prefix, number):
        return f"{prefix}-{number:03d}"

    # ---------------------------------------------------
    # Generate Dates
    # ---------------------------------------------------

    def generate_dates(self):
        effective = datetime(2026, 1, 1) + timedelta(
            days=self.random.randint(0, 180)
        )

        review = effective + timedelta(days=365)

        return (
            effective.strftime("%Y-%m-%d"),
            review.strftime("%Y-%m-%d")
        )

    # ---------------------------------------------------
    # Build Structured Policy Object
    # ---------------------------------------------------

    def build_policy(self, category_name, config, number):

        action = self.random.choice(config["actions"])
        obj = self.random.choice(config["objects"])
        purpose = self.random.choice(config["purposes"])

        rules = self.random.sample(
            config["rules"],
            k=min(3, len(config["rules"]))
        )

        effective, review = self.generate_dates()

        policy_id = self.generate_policy_id(
            config["document_prefix"],
            number
        )

        return {
            "policy_id": policy_id,
            "department": config["department"],
            "security_domain": config["security_domain"],
            "category": category_name,
            "title": self.random.choice(
                config["title_templates"]
            ),
            "purpose": purpose,
            "rules": [
                f"{action} {obj} {rule}."
                for rule in rules
            ],
            "owner": config["owner"],
            "classification": config["classification"],
            "risk_level": config["risk_level"],
            "effective_date": effective,
            "review_date": review,
            "keywords": config["keywords"]
        }

    # ---------------------------------------------------
    # Convert Policy Object into Enterprise Document
    # ---------------------------------------------------

    def render_document(self, policy):

        rules = "\n".join(
            [
                f"{i + 1}. {rule}"
                for i, rule in enumerate(policy["rules"])
            ]
        )

        definitions = "\n".join(
            [
                f"- {item}"
                for item in DOCUMENT_TEMPLATE["definitions"]
            ]
        )

        responsibilities = "\n".join(
            [
                f"- {item}"
                for item in DOCUMENT_TEMPLATE["responsibilities"]
            ]
        )

        exceptions = "\n".join(
            [
                f"- {item}"
                for item in DOCUMENT_TEMPLATE["exceptions"]
            ]
        )

        compliance = "\n".join(
            [
                f"- {item}"
                for item in DOCUMENT_TEMPLATE["compliance"]
            ]
        )

        keywords = ", ".join(
            sorted(set(policy["keywords"]))
        )

        return f"""
================================================================

{self.company["name"]}

ENTERPRISE SECURITY POLICY

================================================================

Policy ID          : {policy["policy_id"]}
Department         : {policy["department"]}
Category           : {policy["category"]}
Security Domain    : {policy["security_domain"]}
Classification     : {policy["classification"]}
Risk Level         : {policy["risk_level"]}
Version            : 1.0
Status             : Active

Effective Date     : {policy["effective_date"]}
Review Date        : {policy["review_date"]}

Owner Team         : {policy["owner"]}

================================================================

TITLE

{policy["title"]}

================================================================

1. PURPOSE

{policy["purpose"]}

{DOCUMENT_TEMPLATE["purpose"]}

================================================================

2. SCOPE

{DOCUMENT_TEMPLATE["scope"]}

================================================================

3. DEFINITIONS

{definitions}

================================================================

4. POLICY STATEMENTS

{rules}

================================================================

5. RESPONSIBILITIES

{responsibilities}

================================================================

6. EXCEPTIONS

{exceptions}

================================================================

7. COMPLIANCE

{compliance}

================================================================

8. REVIEW CYCLE

{DOCUMENT_TEMPLATE["review_cycle"]}

================================================================

KEYWORDS

{keywords}

================================================================
"""
    # ---------------------------------------------------
    # Save Document
    # ---------------------------------------------------

    def save_policy(self, folder, filename, content):

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        print(f"Saving: {folder / filename}")

        with open(
            folder / filename,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(content)

    # ---------------------------------------------------
    # Generate One Category
    # ---------------------------------------------------

    def generate_category(self, category_name, config):

        folder = (
            ENTERPRISE_DIR
            / config["folder_name"]
            / category_name
        )

        print(f"\nGenerating {category_name}...")

        for i in range(
            1,
            config["documents_to_generate"] + 1
        ):

            policy = self.build_policy(
                category_name,
                config,
                i
            )

            document = self.render_document(policy)

            self.save_policy(
                folder,
                f"{policy['policy_id']}.txt",
                document
            )

    # ---------------------------------------------------
    # Generate Complete Enterprise Knowledge Base
    # ---------------------------------------------------

    def generate(self):

        print("\n========================================")
        print("Generating Enterprise Knowledge Base")
        print("========================================\n")

        generated = 0

        for category, config in self.catalog.items():

            if "actions" not in config:
                print(f"Skipping {category} (Blueprint incomplete)")
                continue

            self.generate_category(
                category,
                config
            )

            generated += config["documents_to_generate"]

        print("\n========================================")
        print("Generation Completed")
        print("========================================")
        print(f"Total Documents Generated : {generated}")
        print(f"Output Directory : {ENTERPRISE_DIR}")
        print("========================================\n")


# ---------------------------------------------------
# Main
# ---------------------------------------------------

if __name__ == "__main__":
    generator = EnterprisePolicyGenerator()
    generator.generate()