"""
question_generator.py

Knowledge Firewall AI

Generates benchmark QA pairs from enterprise policies.
"""

from __future__ import annotations

import random

from src.benchmark.models import BenchmarkQuestion


class QuestionGenerator:

    def __init__(self):

        # Fixed seed for reproducibility
        self.random = random.Random(42)

        self.templates = [

            {
                "difficulty": "Easy",
                "question": "Should {statement}?",
                "answer": "Yes. {statement}."
            },

            {
                "difficulty": "Easy",
                "question": "Is it required to {statement}?",
                "answer": "Yes. {statement}."
            },

            {
                "difficulty": "Easy",
                "question": "What is the policy regarding {subject}?",
                "answer": "{statement}."
            },

            {
                "difficulty": "Medium",
                "question": "According to enterprise policy, what should be done for {subject}?",
                "answer": "{statement}."
            },

            {
                "difficulty": "Medium",
                "question": "Which security requirement applies to {subject}?",
                "answer": "{statement}."
            },

            {
                "difficulty": "Medium",
                "question": "How should employees handle {subject}?",
                "answer": "{statement}."
            },

            {
                "difficulty": "Hard",
                "question": "What enterprise security control governs {subject}?",
                "answer": "{statement}."
            },

            {
                "difficulty": "Hard",
                "question": "Which mandatory enterprise requirement applies to {subject}?",
                "answer": "{statement}."
            }

        ]

    # ------------------------------------------------------

    def subject(self, statement: str):

        words = statement.split()

        if len(words) >= 3:

            return " ".join(words[:3]).lower()

        return statement.lower()

    # ------------------------------------------------------

    def clean(self, statement):

        statement = statement.strip()

        if statement.endswith("."):

            statement = statement[:-1]

        return statement

    # ------------------------------------------------------

    def generate_policy_questions(self, policy):

        questions = []

        for statement in policy.policy_statements:

            statement = self.clean(statement)

            subject = self.subject(statement)

            # Generate 3 random templates
            selected = self.random.sample(

                self.templates,

                k=3

            )

            for template in selected:

                question = template["question"].format(

                    statement=statement.lower(),

                    subject=subject

                )

                answer = template["answer"].format(

                    statement=statement

                )

                questions.append(

                    BenchmarkQuestion(

                        question=question,

                        expected_answer=answer,

                        expected_policy=policy.policy_id,

                        expected_section="POLICY_STATEMENT",

                        department=policy.department,

                        category=policy.category,

                        difficulty=template["difficulty"],

                        source_statement=statement

                    )

                )

        return questions