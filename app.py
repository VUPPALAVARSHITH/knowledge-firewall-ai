"""
app.py

Knowledge Firewall AI

Command Line Interface for Secure RAG.
"""

from __future__ import annotations

from src.core.rag import SecureRAG


def print_banner():

    print()

    print("=" * 75)
    print("Knowledge Firewall AI")
    print("Secure Retrieval-Augmented Generation")
    print("=" * 75)


def print_result(result):

    print()

    print("=" * 75)
    print("ANSWER")
    print("=" * 75)
    print(result.answer)

    print()

    print("=" * 75)
    print("FIREWALL REPORT")
    print("=" * 75)

    stats = result.firewall_result.statistics

    print(f"Retrieved   : {stats['retrieved']}")
    print(f"Trusted     : {stats['trusted']}")
    print(f"Suspicious  : {stats['suspicious']}")
    print(f"Blocked     : {stats['blocked']}")

    print()

    print("=" * 75)
    print("VERIFICATION DETAILS")
    print("=" * 75)

    for report in result.firewall_result.verification_reports:

        print(f"Policy      : {report.policy_id}")
        print(f"Chunk       : {report.chunk_id}")
        print(f"Decision    : {report.decision}")
        print(f"Trust Score : {report.trust_score:.4f}")
        print(f"Reason      : {report.reason}")
        print("-" * 75)


def main():

    rag = SecureRAG()

    print_banner()

    while True:

        print()

        question = input("Ask a question (or type 'exit'): ").strip()

        if question.lower() in {"exit", "quit"}:
            break

        if not question:
            continue

        print("\nGenerating answer...\n")

        result = rag.ask(question)

        print_result(result)

    print("\nGoodbye!")


if __name__ == "__main__":

    main()