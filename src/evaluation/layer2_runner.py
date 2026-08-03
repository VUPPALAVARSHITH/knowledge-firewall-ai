"""
layer2_runner.py

Knowledge Firewall AI

Layer-2 Benchmark Evaluation

Evaluates the complete Knowledge Admission Firewall
using benchmark enterprise documents.
"""

from pathlib import Path
import json
from src.enterprise.managers.upload_manager import UploadManager


# ==========================================================
# Paths
# ==========================================================

BENCHMARK = Path("src/evaluation/benchmark")

RESULTS = Path("src/evaluation/results")

RESULTS.mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================================
# Expected Decisions
# ==========================================================

DATASETS = {

    "clean":"ACCEPT",

    "duplicates":"REJECT",

    "near_duplicates":"REVIEW",

    "poisoned":"REJECT",

    "sensitive":"MIXED",

    "combined":"REJECT",

}


# ==========================================================
# Benchmark Runner
# ==========================================================

def main():

    print()

    print("=" * 60)
    print("KNOWLEDGE FIREWALL AI")
    print("LAYER-2 BENCHMARK")
    print("=" * 60)

    manager = UploadManager()

    results = []

    labels = ["ACCEPT", "REVIEW", "REJECT"]

    confusion = {
        actual: {
            predicted: 0
            for predicted in labels
        }
        for actual in labels
    }

    # ------------------------------------------------------

    for folder, expected in DATASETS.items():

        directory = BENCHMARK / folder

        if not directory.exists():

            print(f"Skipping missing folder: {folder}")

            continue

        files = sorted(directory.glob("*.txt"))

        print(f"\nEvaluating {folder} ({len(files)} files)...")

        for file in files:

            # Determine expected label
            if folder == "sensitive":

                number = int(file.stem.split("-")[-1])

                if number <= 20:
                    expected = "REVIEW"
                else:
                    expected = "REJECT"

            else:

                expected = DATASETS[folder]

            report = manager.analyze(file)

            results.append(
                {
                    "file": file.name,
                    "dataset": folder,
                    "expected": expected,
                    "predicted": report.decision,
                    "trust_score": report.trust_score,
                    "correct": expected == report.decision,
                }
            )

            confusion[expected][report.decision] += 1



    # ------------------------------------------------------
    # Metrics
    # ------------------------------------------------------

    total = len(results)

    correct = sum(
        r["correct"]
        for r in results
    )

    incorrect = total - correct

    accuracy = correct / total if total else 0.0

    per_class = {}

    macro_precision = 0
    macro_recall = 0
    macro_f1 = 0

    weighted_precision = 0
    weighted_recall = 0
    weighted_f1 = 0

    for label in labels:

        tp = confusion[label][label]

        fp = sum(
            confusion[a][label]
            for a in labels
            if a != label
        )

        fn = sum(
            confusion[label][p]
            for p in labels
            if p != label
        )

        support = sum(
            confusion[label].values()
        )

        precision = (
            tp / (tp + fp)
            if tp + fp
            else 0
        )

        recall = (
            tp / (tp + fn)
            if tp + fn
            else 0
        )

        f1 = (
            2 * precision * recall
            / (precision + recall)
            if precision + recall
            else 0
        )

        per_class[label] = {

            "precision": round(precision,4),

            "recall": round(recall,4),

            "f1": round(f1,4),

            "support": support,

        }

        macro_precision += precision
        macro_recall += recall
        macro_f1 += f1

        weighted_precision += precision * support
        weighted_recall += recall * support
        weighted_f1 += f1 * support

    classes = len(labels)

    macro_precision /= classes
    macro_recall /= classes
    macro_f1 /= classes

    weighted_precision /= total
    weighted_recall /= total
    weighted_f1 /= total

    summary = {

        "samples": total,

        "correct": correct,

        "incorrect": incorrect,

        "accuracy": round(
            accuracy,
            4,
        ),

        "macro_precision": round(
            macro_precision,
            4,
        ),

        "macro_recall": round(
            macro_recall,
            4,
        ),

        "macro_f1": round(
            macro_f1,
            4,
        ),

        "weighted_precision": round(
            weighted_precision,
            4,
        ),

        "weighted_recall": round(
            weighted_recall,
            4,
        ),

        "weighted_f1": round(
            weighted_f1,
            4,
        ),

        "confusion_matrix": confusion,

        "per_class_metrics": per_class,

        "results": results,

    }

    # ------------------------------------------------------
    # Save Results
    # ------------------------------------------------------

    output_file = RESULTS / "layer2_results.json"

    with open(

        output_file,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            summary,

            f,

            indent=4

        )

    # ------------------------------------------------------
    # Report
    # ------------------------------------------------------

    print()

    print("=" * 60)
    print("LAYER-2 EVALUATION COMPLETED")
    print("=" * 60)

    print(f"Samples    : {total}")
    print(f"Correct    : {correct}")
    print(f"Incorrect  : {incorrect}")
    print(f"Accuracy            : {accuracy:.4f}")
    print(f"Macro Precision     : {macro_precision:.4f}")
    print(f"Macro Recall        : {macro_recall:.4f}")
    print(f"Macro F1            : {macro_f1:.4f}")
    print(f"Weighted Precision  : {weighted_precision:.4f}")
    print(f"Weighted Recall     : {weighted_recall:.4f}")
    print(f"Weighted F1         : {weighted_f1:.4f}")

    print()

    print(f"Results : {output_file}")

    print("=" * 60)


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    main()