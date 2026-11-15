"""Load the saved correctness model and compute its logistic estimate."""

import json
import math
from pathlib import Path


def predict(model: dict, features: dict[str, float]) -> float:
    score = model["intercept"] + sum(
        w * (float(features[name]) - mean) / scale
        for name, w, mean, scale in zip(model["feature_names"], model["coefficients"],
                                        model["mean"], model["scale"]))
    return 1 / (1 + math.exp(-max(-700, min(700, score))))


def load(path: Path) -> dict:
    return json.loads(path.read_text())
