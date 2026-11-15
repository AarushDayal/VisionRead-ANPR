from visionread.metrics import normalize


def test_normalize() -> None:
    assert normalize("  kl-34.a 465 ") == "KL34A465"
    assert normalize("b@h!22") == "BH22"
    assert normalize("") == ""
