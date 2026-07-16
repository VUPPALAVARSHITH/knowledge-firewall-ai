"""
prompt_builder.py

Knowledge Firewall AI

Builds secure prompts for the Enterprise LLM.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Prompt:

    prompt: str


class PromptBuilder:

    def build(
        self,
        question: str,
        context: str
    ) -> Prompt:

        prompt = f"""
You are Knowledge Firewall AI.

You MUST answer ONLY using the trusted enterprise knowledge provided below.

If the answer is not contained in the trusted context,
reply:

"I could not find this information in the trusted enterprise knowledge base."

-------------------------
TRUSTED CONTEXT
-------------------------

{context}

-------------------------
QUESTION
-------------------------

{question}

-------------------------
ANSWER
-------------------------
"""

        return Prompt(prompt=prompt)