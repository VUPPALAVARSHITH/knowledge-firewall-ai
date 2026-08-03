import json
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------
# Paths
# ----------------------------------------------------

RESULTS = Path("src/evaluation/results")
OUTPUT = Path("src/evaluation/graphs/output")

OUTPUT.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------
# Matplotlib Style
# ----------------------------------------------------

plt.rcParams.update({
    "figure.figsize": (8,5),
    "figure.dpi": 300,
    "font.size": 12,
    "axes.titlesize": 16,
    "axes.labelsize": 13,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
})

# ----------------------------------------------------
# Helper
# ----------------------------------------------------

def save_bar(labels, values, title, ylabel, filename):

    plt.figure()

    bars = plt.bar(labels, values)

    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(axis="y", alpha=0.3)

    ymax = max(values)

    for bar, value in zip(bars, values):

        plt.text(
            bar.get_x() + bar.get_width()/2,
            value + ymax*0.02,
            f"{value:.2f}",
            ha="center",
            fontsize=10
        )

    plt.tight_layout()
    plt.savefig(OUTPUT / filename)
    plt.close()


# ----------------------------------------------------
# Helper : Confusion Matrix
# ----------------------------------------------------

def save_confusion(matrix, title, filename):

    labels = list(matrix.keys())

    data = np.array([
        [matrix[r][c] for c in labels]
        for r in labels
    ])

    plt.figure(figsize=(6,5))

    plt.imshow(data)

    plt.xticks(range(len(labels)), labels)
    plt.yticks(range(len(labels)), labels)

    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title(title)

    for i in range(len(labels)):
        for j in range(len(labels)):

            plt.text(
                j,
                i,
                str(data[i][j]),
                ha="center",
                va="center",
                color="white" if data[i,j] > data.max()/2 else "black"
            )

    plt.colorbar()

    plt.tight_layout()
    plt.savefig(OUTPUT / filename)
    plt.close()

# ----------------------------------------------------
# Load JSON
# ----------------------------------------------------

layer1 = json.load(open(
    RESULTS / "layer1_results.json",
    encoding="utf-8"
))

layer2 = json.load(open(
    RESULTS / "layer2_results.json",
    encoding="utf-8"
))

layer3 = json.load(open(
    RESULTS / "layer3_results.json",
    encoding="utf-8"
))

layer4 = json.load(open(
    RESULTS / "layer4_results.json",
    encoding="utf-8"
))

# ====================================================
# Figure 1
# Layer-1 Metrics
# ====================================================

m = layer1["experiments"]["attack_detection"]["metrics"]

save_bar(

    ["Accuracy","Precision","Recall","F1"],

    [
        m["accuracy"]*100,
        m["precision"]*100,
        m["recall"]*100,
        m["f1_score"]*100
    ],

    "Layer-1 Security Detection Metrics",

    "Percentage",

    "figure1_layer1_metrics.png"

)

# ====================================================
# Figure 2
# Layer-2 Metrics
# ====================================================

save_bar(

    [
        "Accuracy",
        "Macro P",
        "Macro R",
        "Macro F1",
        "Weighted P",
        "Weighted R",
        "Weighted F1"
    ],

    [

        layer2["accuracy"]*100,

        layer2["macro_precision"]*100,

        layer2["macro_recall"]*100,

        layer2["macro_f1"]*100,

        layer2["weighted_precision"]*100,

        layer2["weighted_recall"]*100,

        layer2["weighted_f1"]*100

    ],

    "Layer-2 Admission Evaluation Metrics",

    "Percentage",

    "figure2_layer2_metrics.png"

)

# ====================================================
# Figure 3
# Layer-2 Confusion Matrix
# ====================================================

save_confusion(

    layer2["confusion_matrix"],

    "Layer-2 Confusion Matrix",

    "figure3_layer2_confusion.png"

)

# ====================================================
# Figure 4
# Repository Health
# ====================================================

save_bar(

    [

        "Trusted",

        "Review",

        "Rejected",

        "Attack\nFindings",

        "Sensitive\nFindings"

    ],

    [

        layer3["trusted"],

        layer3["review"],

        layer3["rejected"],

        layer3["attack_findings"],

        layer3["sensitive_findings"]

    ],

    "Repository Health Summary",

    "Policies",

    "figure4_repository_health.png"

)

# ====================================================
# Figure 5
# Repository Timing
# ====================================================

save_bar(

    [

        "Repository Scan",

        "Avg Policy"

    ],

    [

        layer3["repository_scan_time_seconds"],

        layer3["average_policy_time_seconds"]

    ],

    "Repository Processing Time",

    "Seconds",

    "figure5_repository_time.png"

)

# ====================================================
# Figure 6
# Repository Throughput
# ====================================================

save_bar(

    ["Policies/sec"],

    [

        layer3["throughput_policies_per_second"]

    ],

    "Repository Throughput",

    "Policies/sec",

    "figure6_repository_throughput.png"

)

# ====================================================
# Figure 7
# Upload Timing
# ====================================================

save_bar(

    [

        "Average",

        "Minimum",

        "Maximum"

    ],

    [

        layer4["average_upload_time_seconds"],

        layer4["minimum_upload_time_seconds"],

        layer4["maximum_upload_time_seconds"]

    ],

    "Upload Processing Time",

    "Seconds",

    "figure7_upload_time.png"

)

# ====================================================
# Figure 8
# Upload Throughput
# ====================================================

save_bar(

    ["Documents/sec"],

    [

        layer4["throughput_documents_per_second"]

    ],

    "Upload Throughput",

    "Documents/sec",

    "figure8_upload_throughput.png"

)

print("="*60)
print("Graphs generated successfully.")
print("Saved to:", OUTPUT)
print("="*60)