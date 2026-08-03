"""
layer3_runner.py

Knowledge Firewall AI

Layer-3 Repository Integrity Assessment

Evaluates the health of the complete enterprise repository.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from src.core.integrity.integrity_verifier import (
    IntegrityVerifier,
)

RESULT_DIR = Path(
    "src/evaluation/results"
)

RESULT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


class Layer3Runner:

    def __init__(self):

        self.verifier = IntegrityVerifier()

    # -----------------------------------------------------

    def run(self):

        print()
        print("=" * 60)
        print("KNOWLEDGE FIREWALL AI")
        print("LAYER-3 REPOSITORY INTEGRITY")
        print("=" * 60)

        start = time.perf_counter()

        report = self.verifier.verify_repository()

        elapsed = (
            time.perf_counter()
            - start
        )

        trusted = 0
        review = 0
        rejected = 0

        attacks = 0
        sensitive = 0

        results = []

        for item in report.results:

            if item.decision == "ACCEPT":
                trusted += 1

            elif item.decision == "REVIEW":
                review += 1

            else:
                rejected += 1

            if item.attack_detected:
                attacks += 1

            if item.sensitive_data_detected:
                sensitive += 1

            results.append({

                "policy_id": item.policy_id,

                "department": item.department,

                "category": item.category,

                "trust_score": item.trust_score,

                "decision": item.decision,

                "attack_detected": item.attack_detected,

                "sensitive_detected": item.sensitive_data_detected,

            })

        average_time = (
            elapsed / report.total_policies
            if report.total_policies
            else 0
        )

        throughput = (
            report.total_policies / elapsed
            if elapsed
            else 0
        )

        output = {

            "evaluation_layer": 3,

            "total_policies": report.total_policies,

            "average_trust": report.average_trust,

            "repository_health": report.repository_health,

            "trusted": trusted,

            "review": review,

            "rejected": rejected,

            "attack_findings": attacks,

            "sensitive_findings": sensitive,

            "repository_scan_time_seconds": round(
                elapsed,
                4,
            ),

            "average_policy_time_seconds": round(
                average_time,
                4,
            ),

            "throughput_policies_per_second": round(
                throughput,
                2,
            ),

            "results": results,

        }

        output_file = (
            RESULT_DIR /
            "layer3_results.json"
        )

        with open(

            output_file,

            "w",

            encoding="utf-8",

        ) as f:

            json.dump(

                output,

                f,

                indent=4,

            )

        print()

        print("=" * 60)
        print("LAYER-3 COMPLETED")
        print("=" * 60)

        print(
            f"Policies           : {report.total_policies}"
        )

        print(
            f"Average Trust      : {report.average_trust:.2f}"
        )

        print(
            f"Repository Health  : {report.repository_health}"
        )

        print()

        print(
            f"Trusted            : {trusted}"
        )

        print(
            f"Review             : {review}"
        )

        print(
            f"Rejected           : {rejected}"
        )

        print()

        print(
            f"Attack Findings    : {attacks}"
        )

        print(
            f"Sensitive Findings : {sensitive}"
        )

        print()

        print(
            f"Repository Scan    : {elapsed:.2f} sec"
        )

        print(
            f"Average Policy     : {average_time:.4f} sec"
        )

        print(
            f"Throughput         : {throughput:.2f} policies/sec"
        )

        print()

        print(
            f"Results : {output_file}"
        )

        print("=" * 60)


if __name__ == "__main__":

    Layer3Runner().run()