import math

import pytest

from riskgate.calibration import load, predict
from riskgate.router import route


def test_saved_calibrator(tmp_path) -> None:
    path = tmp_path / "calibration.json"
    path.write_text('{"feature_names": ["raw_conf"], "coefficients": [2], '
                    '"intercept": -1, "mean": [0.5], "scale": [0.25]}')
    model = load(path)
    assert predict(model, {"raw_conf": 0.75}) == pytest.approx(1 / (1 + math.exp(-1)))
    assert predict(model, {"raw_conf": 1e6}) == 1.0
    assert 0 <= predict(model, {"raw_conf": -1e6}) < 1e-300


def test_saved_threshold_routing() -> None:
    policy = {"accept_at": 0.8, "review_below": 0.3}
    assert route("KA01AB1234", 0.8, policy) == "ACCEPT"
    assert route("KA01AB1234", 0.7, policy) == "ESCALATE"
    assert route("KA01AB1234", 0.2, policy) == "REVIEW"
    assert route("junk", 1.0, policy) != "ACCEPT"
    assert route("KA01AB1234", 1.0, {**policy, "accept_at": None}) != "ACCEPT"
