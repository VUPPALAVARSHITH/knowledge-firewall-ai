"""
metadata_utils.py

Knowledge Firewall AI

Utility functions for parsing enterprise policy documents
and generating metadata.
"""

import hashlib
import re
from pathlib import Path


# --------------------------------------------------------
# SHA256 Hash
# --------------------------------------------------------

def calculate_sha256(filepath: Path) -> str:
    """
    Compute SHA256 hash of a document.
    """

    with open(filepath, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()


# --------------------------------------------------------
# Read File
# --------------------------------------------------------

def read_document(filepath: Path) -> str:
    """
    Read text document.
    """

    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


# --------------------------------------------------------
# Extract Field
# --------------------------------------------------------

def extract_field(text: str, field: str) -> str:
    """
    Extract single-line metadata field.

    Example:
    Policy ID : IT-PWD-001
    """

    pattern = rf"{field}\s*:\s*(.+)"

    match = re.search(
        pattern,
        text
    )

    if match:
        return match.group(1).strip()

    return ""


# --------------------------------------------------------
# Extract Title
# --------------------------------------------------------

def extract_title(text: str) -> str:
    """
    Extract TITLE section.
    """

    match = re.search(

        r"TITLE\s+(.*?)\s+=+",

        text,

        re.DOTALL

    )

    if match:

        return " ".join(

            match.group(1).split()

        )

    return ""


# --------------------------------------------------------
# Extract Keywords
# --------------------------------------------------------

def extract_keywords(text: str):

    match = re.search(

        r"KEYWORDS\s+(.*?)\s+=+",

        text,

        re.DOTALL

    )

    if not match:

        return []

    keywords = [

        keyword.strip()

        for keyword in

        match.group(1).split(",")

    ]

    keywords = [

        k for k in keywords

        if k

    ]

    return sorted(

        list(

            set(keywords)

        )

    )


# --------------------------------------------------------
# Word Count
# --------------------------------------------------------

def word_count(text: str):

    return len(

        text.split()

    )


# --------------------------------------------------------
# Character Count
# --------------------------------------------------------

def character_count(text: str):

    return len(text)


# --------------------------------------------------------
# Parse Enterprise Document
# --------------------------------------------------------

def parse_document(filepath: Path):

    text = read_document(filepath)

    metadata = {

        "policy_id":

            extract_field(
                text,
                "Policy ID"
            ),

        "department":

            extract_field(
                text,
                "Department"
            ),

        "category":

            extract_field(
                text,
                "Category"
            ),

        "security_domain":

            extract_field(
                text,
                "Security Domain"
            ),

        "classification":

            extract_field(
                text,
                "Classification"
            ),

        "risk_level":

            extract_field(
                text,
                "Risk Level"
            ),

        "effective_date":

            extract_field(
                text,
                "Effective Date"
            ),

        "review_date":

            extract_field(
                text,
                "Review Date"
            ),

        "owner":

            extract_field(
                text,
                "Owner Team"
            ),

        "title":

            extract_title(
                text
            ),

        "keywords":

            extract_keywords(
                text
            ),

        "word_count":

            word_count(
                text
            ),

        "char_count":

            character_count(
                text
            ),

        "sha256":

            calculate_sha256(
                filepath
            ),

        "filepath":

            str(filepath)

    }

    return metadata