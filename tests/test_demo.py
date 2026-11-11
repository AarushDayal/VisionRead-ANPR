"""The packaged demo can analyze a real vehicle scene offline."""

from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest


ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.skipif(
    not (ROOT / "weights/plate_detector.pt").exists()
    or not (ROOT / "data/sample_gallery/manifest.csv").exists(),
    reason="local demo assets are not installed",
)
def test_gallery_photo_runs_without_error() -> None:
    app = AppTest.from_file(str(ROOT / "app/streamlit_app.py"), default_timeout=90).run()
    app.radio[1].set_value("Demo gallery").run()
    app.button[0].click().run()
    assert not app.exception
    assert app.session_state["analysis"]["text"] == "RJ27TC0530"
