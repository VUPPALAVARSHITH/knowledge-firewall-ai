"""
enterprise_llm.py

Knowledge Firewall AI

Enterprise LLM Wrapper

Uses Ollama as the backend LLM.
"""

from __future__ import annotations

import ollama


class EnterpriseLLM:

    def __init__(

        self,

        model: str = "qwen2.5:3b"

    ):

        self.model = model

    # -----------------------------------------------------

    def generate(

        self,

        prompt: str

    ) -> str:

        response = ollama.chat(

            model=self.model,

            messages=[

                {

                    "role": "user",

                    "content": prompt

                }

            ]

        )

        return response["message"]["content"].strip()

    # -----------------------------------------------------

    def available(self):

        try:

            ollama.list()

            return True

        except Exception:

            return False