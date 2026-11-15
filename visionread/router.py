"""Apply the saved validation thresholds without refitting them."""

from visionread.grammar import classify


def route(text: str, confidence: float, thresholds: dict) -> str:
    if classify(text) != "INVALID" and thresholds["accept_at"] is not None and confidence >= thresholds["accept_at"]:
        return "ACCEPT"
    return "REVIEW" if confidence < thresholds["review_below"] else "ESCALATE"
