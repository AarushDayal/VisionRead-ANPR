import numpy as np

from visionread.contracts import EngineResult
from visionread.stability import apply_veto, check_stability


def test_stability_veto_and_failure():
    crop = np.full((20, 80, 3), 100, dtype=np.uint8)
    seen = []
    def read(image):
        seen.append(image.copy())
        return EngineResult("KA01AB1234", 0.99, 1)
    evidence = check_stability(crop, "KA01AB1234", read)
    assert evidence["stable"]
    assert seen[0].shape[:2] == (25, 100)
    assert seen[1][0, 0, 0] == 110
    assert np.all(crop == 100)
    assert apply_veto("ACCEPT", evidence) == "ACCEPT"
    assert apply_veto("REVIEW", evidence) == "REVIEW"
    for result in (EngineResult("KA01AB1235", .99, 1),
                   EngineResult("", 0, 1, error="failed"),
                   EngineResult("KA01AB1234", .99, 1, error="failed")):
        evidence = check_stability(crop, "KA01AB1234", lambda image: result)
        assert not evidence["stable"]
        assert apply_veto("ACCEPT", evidence) == "REVIEW"
    assert not check_stability(crop, "", lambda image: EngineResult("", 0, 1))["stable"]
