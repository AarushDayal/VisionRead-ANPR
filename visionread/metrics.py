import re


def normalize(text: str) -> str:
    """Uppercase, keep only A-Z and 0-9."""
    return re.sub(r"[^A-Z0-9]", "", (text or "").upper())
