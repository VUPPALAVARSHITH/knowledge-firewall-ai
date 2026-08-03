"""
layer4_runner.py

Knowledge Firewall AI

Layer-4 Performance & Scalability Evaluation
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import psutil

from src.config.path_config import ENTERPRISE_DIR
from src.enterprise.managers.upload_manager import UploadManager
from src.core.integrity.integrity_verifier import IntegrityVerifier


RESULT_DIR = Path(
    "src/evaluation/results"
)

RESULT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


class Layer4Runner:

    def __init__(self):

        self.manager = UploadManager()

        self.verifier = IntegrityVerifier()

        self.process = psutil.Process()

        self.upload_times = []

        self.upload_trust = []

    # -----------------------------------------------------

    def benchmark_uploads(self):

        print()

        print("Benchmarking Upload Pipeline...")

        files = sorted(
            ENTERPRISE_DIR.rglob("*.txt")
        )

        successful = 0

        start = time.perf_counter()

        for file in files:

            t1 = time.perf_counter()

            report = self.manager.analyze(file)

            elapsed = (
                time.perf_counter()
                - t1
            )

            self.upload_times.append(
                elapsed
            )

            self.upload_trust.append(
                report.trust_score
            )

            successful += 1

        total = (
            time.perf_counter()
            - start
        )

        return {

            "documents": len(files),

            "successful": successful,

            "total_time": total,

        }

    # -----------------------------------------------------

    def benchmark_repository(self):

        print()

        print("Benchmarking Repository Scan...")

        start = time.perf_counter()

        report = self.verifier.verify_repository()

        elapsed = (
            time.perf_counter()
            - start
        )

        return report, elapsed

        # -----------------------------------------------------

    def generate_report(

        self,

        upload,

        repository,

        repository_time,

    ):

        cpu = psutil.cpu_percent(interval=1)

        memory = (
            self.process.memory_info().rss
            / 1024
            / 1024
        )

        average_upload = (

            sum(self.upload_times)

            / len(self.upload_times)

            if self.upload_times

            else 0

        )

        minimum_upload = (

            min(self.upload_times)

            if self.upload_times

            else 0

        )

        maximum_upload = (

            max(self.upload_times)

            if self.upload_times

            else 0

        )

        average_trust = (

            sum(self.upload_trust)

            / len(self.upload_trust)

            if self.upload_trust

            else 0

        )

        throughput = (

            upload["documents"]

            / upload["total_time"]

            if upload["total_time"]

            else 0

        )

        output = {

            "evaluation_layer": 4,

            "documents": upload["documents"],

            "successful_uploads": upload["successful"],

            "upload_total_time_seconds": round(
                upload["total_time"],
                4,
            ),

            "average_upload_time_seconds": round(
                average_upload,
                4,
            ),

            "minimum_upload_time_seconds": round(
                minimum_upload,
                4,
            ),

            "maximum_upload_time_seconds": round(
                maximum_upload,
                4,
            ),

            "repository_scan_time_seconds": round(
                repository_time,
                4,
            ),

            "repository_health": repository.repository_health,

            "repository_average_trust": repository.average_trust,

            "throughput_documents_per_second": round(
                throughput,
                2,
            ),

            "cpu_percent": cpu,

            "memory_mb": round(
                memory,
                2,
            ),

            "average_upload_trust": round(
                average_trust,
                2,
            ),

        }

        output_file = (
            RESULT_DIR /
            "layer4_results.json"
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
        print("LAYER-4 PERFORMANCE COMPLETED")
        print("=" * 60)

        print(f"Documents              : {upload['documents']}")
        print(f"Successful Uploads     : {upload['successful']}")
        print(f"Upload Time            : {upload['total_time']:.2f} sec")
        print(f"Average Upload         : {average_upload:.4f} sec")
        print(f"Minimum Upload         : {minimum_upload:.4f} sec")
        print(f"Maximum Upload         : {maximum_upload:.4f} sec")
        print(f"Repository Scan        : {repository_time:.2f} sec")
        print(f"Repository Health      : {repository.repository_health}")
        print(f"Average Trust          : {repository.average_trust:.2f}")
        print(f"Throughput             : {throughput:.2f} docs/sec")
        print(f"CPU Usage              : {cpu:.2f}%")
        print(f"Memory Usage           : {memory:.2f} MB")

        print()
        print(f"Results : {output_file}")
        print("=" * 60)

    # -----------------------------------------------------

    def run(self):

        print()
        print("=" * 60)
        print("KNOWLEDGE FIREWALL AI")
        print("LAYER-4 PERFORMANCE & SCALABILITY")
        print("=" * 60)

        upload = self.benchmark_uploads()

        repository, repository_time = (
            self.benchmark_repository()
        )

        self.generate_report(

            upload,

            repository,

            repository_time,

        )


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    Layer4Runner().run()