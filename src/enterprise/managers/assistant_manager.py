"""
assistant_manager.py

Knowledge Firewall AI

Enterprise Assistant Manager.

Wraps the SecureRAG backend for the enterprise UI.
"""

from src.core.rag.secure_rag import SecureRAG


class AssistantManager:

    def __init__(self):
        self.rag = SecureRAG()

    # -----------------------------------------------------

    def ask(
        self,
        question,
        top_k=5,
        include_suspicious=False
    ):
        return self.rag.ask(
            question,
            top_k=top_k,
            include_suspicious=include_suspicious
        )