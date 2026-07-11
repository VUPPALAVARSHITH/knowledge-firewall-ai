"""
models.py

Knowledge Firewall AI

Benchmark QA data models.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class BenchmarkQuestion:

    question: str

    expected_answer: str

    expected_policy: str

    expected_section: str

    department: str

    category: str

    difficulty: str

    source_statement: str