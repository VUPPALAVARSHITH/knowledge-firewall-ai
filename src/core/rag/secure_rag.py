"""
secure_rag.py

Knowledge Firewall AI

Secure Retrieval-Augmented Generation Pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass

from src.core.firewall.knowledge_firewall import KnowledgeFirewall
from src.rag.prompt_builder import PromptBuilder
from src.rag.llm import EnterpriseLLM


# ==========================================================
# Result
# ==========================================================

@dataclass(slots=True)
class SecureRAGResult:

    question: str

    answer: str

    trusted_context: str

    firewall_result: object


# ==========================================================
# Secure RAG
# ==========================================================

class SecureRAG:

    def __init__(

        self,

        model: str = "qwen2.5:3b"

    ):

        self.firewall = KnowledgeFirewall()

        self.prompt_builder = PromptBuilder()

        self.llm = EnterpriseLLM(model=model)

    # ------------------------------------------------------

    def ask(

        self,

        question: str,

        top_k: int = 5,

        include_suspicious: bool = False

    ) -> SecureRAGResult:

        firewall_result = self.firewall.verify_query(

            query=question,

            top_k=top_k,

            include_suspicious=include_suspicious

        )

        # ---------------------------------------------
        # No trusted context
        # ---------------------------------------------

        if firewall_result.context.strip() == "":

            return SecureRAGResult(

                question=question,

                answer=(
                    "I could not find this information in the "
                    "trusted enterprise knowledge base."
                ),

                trusted_context="",

                firewall_result=firewall_result

            )

        # ---------------------------------------------
        # Prompt
        # ---------------------------------------------

        prompt = self.prompt_builder.build(

            question=question,

            context=firewall_result.context

        )

        # ---------------------------------------------
        # Generate
        # ---------------------------------------------

        answer = self.llm.generate(

            prompt.prompt

        )

        return SecureRAGResult(

            question=question,

            answer=answer,

            trusted_context=firewall_result.context,

            firewall_result=firewall_result

        )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    rag = SecureRAG()

    result = rag.ask(

        "Does VPN require authentication?"

    )

    print()

    print("=" * 70)

    print("QUESTION")

    print("=" * 70)

    print(result.question)

    print()

    print("=" * 70)

    print("TRUSTED CONTEXT")

    print("=" * 70)

    print(result.trusted_context)

    print()

    print("=" * 70)

    print("ANSWER")

    print("=" * 70)

    print(result.answer)

    print()

    print("=" * 70)

    print("FIREWALL")

    print("=" * 70)

    print(result.firewall_result.statistics)