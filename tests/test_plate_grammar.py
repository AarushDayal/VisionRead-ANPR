import pytest

from riskgate.plate_grammar import correct_plate


@pytest.mark.parametrize("text", ["RJ27T0530", "RJ27TC0530", "RJ27TCA0530"])
def test_valid_plate_unchanged(text: str) -> None:
    assert correct_plate(text) == text


@pytest.mark.parametrize(("text", "expected"), [
    ("RJZ7TCOS3O", "RJ27TC0530"),
    ("01IB852OIBS", "OI18BSZ0185"),
    ("SZBOSZIBZS", "SZ80SZ1825"),
    ("RJ27TC0530", "RJ27TC0530"),
])
def test_confusions_by_slot(text: str, expected: str) -> None:
    assert correct_plate(text) == expected


@pytest.mark.parametrize("text", ["", "RJZ7OS3O", "INDRJZ7TCOS3O", "rj27tc0530", "RJ?7TC0?30"])
def test_other_characters_and_wrong_lengths_unchanged(text: str) -> None:
    assert correct_plate(text) == text
