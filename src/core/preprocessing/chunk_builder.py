"""
chunk_builder.py

Knowledge Firewall AI

Builds enriched semantic chunks from Policy objects.
"""

from src.core.preprocessing.models import Chunk
from src.config.constants import (
    SECTION_PRIORITY,
    DOCUMENT_TYPE_ENTERPRISE
)


class ChunkBuilder:

    def __init__(self):
        pass

    # ---------------------------------------------------
    # Build Enriched Text
    # ---------------------------------------------------

    def build_enriched_text(
        self,
        policy,
        section,
        text
    ):

        keyword_text = ", ".join(policy.keywords)

        return (
            f"Department: {policy.department}\n"
            f"Category: {policy.category}\n"
            f"Security Domain: {policy.security_domain}\n"
            f"Risk Level: {policy.risk_level}\n"
            f"Classification: {policy.classification}\n"
            f"Section: {section}\n\n"
            f"{text}\n\n"
            f"Keywords: {keyword_text}"
        )

    # ---------------------------------------------------
    # Generic Chunk Creator
    # ---------------------------------------------------

    def create_chunk(
        self,
        policy,
        section,
        suffix,
        order,
        text,
        statement_number=None
    ):

        enriched = self.build_enriched_text(
            policy,
            section,
            text
        )

        return Chunk(

            chunk_id=f"{policy.policy_id}_{suffix}",

            policy_id=policy.policy_id,

            department=policy.department,

            category=policy.category,

            security_domain=policy.security_domain,

            classification=policy.classification,

            risk_level=policy.risk_level,

            version=policy.version,

            status=policy.status,

            owner=policy.owner,

            section=section,

            priority=SECTION_PRIORITY[section],

            chunk_order=order,

            statement_number=statement_number,

            text=text,

            enriched_text=enriched,

            keywords=policy.keywords,

            word_count=len(text.split()),

            character_count=len(text),

            source_file=policy.source_file,

            document_type=DOCUMENT_TYPE_ENTERPRISE,

            is_poisoned=False,

            created_from="Dataset-1"

        )

    # ---------------------------------------------------
    # Build Chunks
    # ---------------------------------------------------

    def build(self, policy):

        chunks = []

        order = 1

        metadata = (
            f"Policy ID: {policy.policy_id}\n"
            f"Department: {policy.department}\n"
            f"Category: {policy.category}\n"
            f"Security Domain: {policy.security_domain}\n"
            f"Classification: {policy.classification}\n"
            f"Risk Level: {policy.risk_level}\n"
            f"Version: {policy.version}\n"
            f"Status: {policy.status}\n"
            f"Owner: {policy.owner}"
        )

        sections = [

            ("METADATA", metadata, "META"),

            ("TITLE", policy.title, "TITLE"),

            ("PURPOSE", policy.purpose, "PURPOSE"),

            ("SCOPE", policy.scope, "SCOPE"),

            ("DEFINITIONS",
             "\n".join(policy.definitions),
             "DEF")

        ]

        for section, text, suffix in sections:

            chunks.append(

                self.create_chunk(
                    policy,
                    section,
                    suffix,
                    order,
                    text
                )

            )

            order += 1

        # -----------------------------------------
        # Policy Statements
        # -----------------------------------------

        for i, statement in enumerate(
            policy.policy_statements,
            start=1
        ):

            chunks.append(

                self.create_chunk(
                    policy,
                    "POLICY_STATEMENT",
                    f"PS{i}",
                    order,
                    statement,
                    statement_number=i
                )

            )

            order += 1

        remaining = [

            (
                "RESPONSIBILITIES",
                "\n".join(policy.responsibilities),
                "RESP"
            ),

            (
                "EXCEPTIONS",
                "\n".join(policy.exceptions),
                "EXC"
            ),

            (
                "COMPLIANCE",
                "\n".join(policy.compliance),
                "COMP"
            ),

            (
                "REVIEW_CYCLE",
                policy.review_cycle,
                "REVIEW"
            ),

            (
                "KEYWORDS",
                ", ".join(policy.keywords),
                "KEYWORDS"
            )

        ]

        for section, text, suffix in remaining:

            chunks.append(

                self.create_chunk(
                    policy,
                    section,
                    suffix,
                    order,
                    text
                )

            )

            order += 1

        return chunks