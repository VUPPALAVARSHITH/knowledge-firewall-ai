"""
metrics.py

Knowledge Firewall AI

Evaluation metrics for poison detection.
"""

from dataclasses import dataclass, asdict


@dataclass(slots=True)
class Metrics:

    tp: int = 0
    tn: int = 0
    fp: int = 0
    fn: int = 0

    accuracy: float = 0.0
    precision: float = 0.0
    recall: float = 0.0
    f1_score: float = 0.0

    false_positive_rate: float = 0.0
    false_negative_rate: float = 0.0

    detection_rate: float = 0.0

    # -----------------------------------------

    def compute(self):

        total = self.tp + self.tn + self.fp + self.fn

        self.accuracy = (
            (self.tp + self.tn) / total
            if total else 0
        )

        self.precision = (
            self.tp / (self.tp + self.fp)
            if (self.tp + self.fp) else 0
        )

        self.recall = (
            self.tp / (self.tp + self.fn)
            if (self.tp + self.fn) else 0
        )

        if self.precision + self.recall:

            self.f1_score = (

                2

                * self.precision

                * self.recall

            ) / (

                self.precision

                + self.recall

            )

        self.false_positive_rate = (

            self.fp

            / (self.fp + self.tn)

            if (self.fp + self.tn)

            else 0

        )

        self.false_negative_rate = (

            self.fn

            / (self.fn + self.tp)

            if (self.fn + self.tp)

            else 0

        )

        self.detection_rate = self.recall

        return self

    # -----------------------------------------

    def to_dict(self):

        return asdict(self)