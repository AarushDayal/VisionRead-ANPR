"""An additional review veto; agreement is evidence, never a probability."""

from collections.abc import Callable
from time import perf_counter

import cv2
import numpy as np

from riskgate.contracts import EngineResult
from riskgate.metrics import normalize


def check_stability(crop: np.ndarray, original: str,
                    read: Callable[[np.ndarray], EngineResult]) -> dict:
    """Read two fixed, mild transformations without changing the original answer."""
    if crop.size == 0:
        raise ValueError("Cannot check an empty crop")
    start = perf_counter()
    # Fixed before evaluation: no searching for a transformation that looks correct.
    variants = {
        "resize_125": cv2.resize(crop, None, fx=1.25, fy=1.25, interpolation=cv2.INTER_CUBIC),
        "brightness_110": np.clip(crop.astype(np.float32) * 1.10, 0, 255).astype(np.uint8),
    }
    original = normalize(original)
    readings = []
    for name, image in variants.items():
        result = read(image)
        text = normalize(result.text)
        readings.append({"variant": name, "text": text, "error": result.error,
                         "matches_original": bool(original and text == original and not result.error)})
    stable = all(row["matches_original"] for row in readings)
    return {"stable": stable, "matching_variants": sum(row["matches_original"] for row in readings),
            "variant_count": len(readings), "readings": readings,
            "extra_latency_ms": (perf_counter() - start) * 1000}


def apply_veto(decision: str, evidence: dict) -> str:
    """Only remove acceptance. Never promote a review or replace plate characters."""
    return "REVIEW" if decision == "ACCEPT" and not evidence["stable"] else decision
