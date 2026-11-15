"""Position-aware OCR correction for AA99A[AA]9999 Indian plates."""

DIGITS = str.maketrans("OIBSZ", "01852")
LETTERS = str.maketrans("01852", "OIBSZ")


def correct_plate(text: str) -> str:
    """Correct only listed confusions in slots determined by lengths 9–11.

    No normalization, state-code lookup, or correction of other characters.
    """
    if len(text) not in (9, 10, 11):
        return text
    return (text[:2].translate(LETTERS) + text[2:4].translate(DIGITS)
            + text[4:-4].translate(LETTERS) + text[-4:].translate(DIGITS))
