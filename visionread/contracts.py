from dataclasses import dataclass


@dataclass
class EngineResult:
    """One engine read. On failure error is set and text stays "" - never raise, never fake."""

    text: str
    raw_conf: float
    latency_ms: float
    error: str | None = None
    boxes_found: int = 0
