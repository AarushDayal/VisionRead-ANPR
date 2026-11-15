# Every Python source line explained

Read [FACULTY_EXPLANATION.md](FACULTY_EXPLANATION.md) first for the system and mathematics.

This is a generated syntax companion, not a claim that model weights or third-party library internals are explained line by line. Every physical line of our Python source, including tests and this generator, appears below. Long statements are explained at their first line; following lines identify the statement they continue. Source fingerprints let you detect an outdated guide. Regenerate with `./venv/bin/python -m scripts.explain_code`.

Python basics: indentation groups instructions. `=` stores a value; `==` compares values. A function is a named recipe. A class describes an object. A dictionary holds named values. A list holds ordered values. `None` means missing. `True`/`False` are yes/no. Type hints document expected values; they do not enforce them automatically. An array stores image pixel numbers. `image[y1:y2, x1:x2]` selects rows then columns; the ending coordinates are excluded.

## app/streamlit_app.py

The visible demo: upload, detect, read, show evidence, review, and export a batch.

Source SHA-256: `06a70b395aa0eb63627a5d9c92d747453b6e23190226e3c261953275271e3790`

**Line 1**
```python
"""Offline plate reading demo and transparent experiment dashboard."""
```
Use the fixed value `'offline plate reading demo and transparent experiment dashboard.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import csv
```
Make the named library tools available here: `import csv`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
import hashlib
```
Make the named library tools available here: `import hashlib`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python
import io
```
Make the named library tools available here: `import io`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python
import json
```
Make the named library tools available here: `import json`. Importing a project module makes its reusable functions accessible.

**Line 7**
```python
import sys
```
Make the named library tools available here: `import sys`. Importing a project module makes its reusable functions accessible.

**Line 8**
```python
from datetime import datetime
```
Make the named library tools available here: `from datetime import datetime`. Importing a project module makes its reusable functions accessible.

**Line 9**
```python
from html import escape
```
Make the named library tools available here: `from html import escape`. Importing a project module makes its reusable functions accessible.

**Line 10**
```python
from pathlib import Path
```
Make the named library tools available here: `from pathlib import Path`. Importing a project module makes its reusable functions accessible.

**Line 11**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 12**
```python
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
```
Call `sys.path.insert` with the inputs shown to obtain its result.

**Line 13**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 14**
```python
import cv2
```
Make the named library tools available here: `import cv2`. Importing a project module makes its reusable functions accessible.

**Line 15**
```python
import numpy as np
```
Make the named library tools available here: `import numpy as np`. Importing a project module makes its reusable functions accessible.

**Line 16**
```python
import streamlit as st
```
Make the named library tools available here: `import streamlit as st`. Importing a project module makes its reusable functions accessible.

**Line 17**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 18**
```python
from riskgate import config
```
Make the named library tools available here: `from riskgate import config`. Importing a project module makes its reusable functions accessible.

**Line 19**
```python
from riskgate.calibration import load, predict
```
Make the named library tools available here: `from riskgate.calibration import load, predict`. Importing a project module makes its reusable functions accessible.

**Line 20**
```python
from riskgate.engines.easyocr_engine import EasyOCREngine
```
Make the named library tools available here: `from riskgate.engines.easyocr_engine import EasyOCREngine`. Importing a project module makes its reusable functions accessible.

**Line 21**
```python
from riskgate.engines.fastplate_engine import FastPlateEngine
```
Make the named library tools available here: `from riskgate.engines.fastplate_engine import FastPlateEngine`. Importing a project module makes its reusable functions accessible.

**Line 22**
```python
from riskgate.features import plate_features
```
Make the named library tools available here: `from riskgate.features import plate_features`. Importing a project module makes its reusable functions accessible.

**Line 23**
```python
from riskgate.grammar import classify
```
Make the named library tools available here: `from riskgate.grammar import classify`. Importing a project module makes its reusable functions accessible.

**Line 24**
```python
from riskgate.metrics import normalize
```
Make the named library tools available here: `from riskgate.metrics import normalize`. Importing a project module makes its reusable functions accessible.

**Line 25**
```python
from riskgate.router import route
```
Make the named library tools available here: `from riskgate.router import route`. Importing a project module makes its reusable functions accessible.

**Line 26**
```python
from riskgate.stability import apply_veto, check_stability
```
Make the named library tools available here: `from riskgate.stability import apply_veto, check_stability`. Importing a project module makes its reusable functions accessible.

**Line 27**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 28**
```python
st.set_page_config(page_title="RiskGate • ANPR Lab", page_icon="◈", layout="wide")
```
Call `st.set_page_config` with the inputs shown to obtain its result.

**Line 29**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 30**
```python
CSS = """
```
Store the result in `CSS`: use this fixed text block (presentation content, not model logic).

**Line 31**
```python
<style>
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 32**
```python
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 33**
```python
html, body, [class*="css"], [data-testid="stAppViewContainer"] {font-family:'DM Sans',sans-serif;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 34**
```python
[data-testid="stAppViewContainer"] {background:#07111e;color:#e7f2f5;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 35**
```python
[data-testid="stHeader"] {background:transparent;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 36**
```python
[data-testid="stSidebar"] {background:#0c1b2b;border-right:1px solid #1e3547;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 37**
```python
[data-testid="stSidebar"] * {color:#dceef1;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 38**
```python
.block-container {max-width:1320px;padding-top:1.3rem;padding-bottom:3rem;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 39**
```python
h1,h2,h3 {font-family:'Space Grotesk',sans-serif;letter-spacing:-.04em;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 40**
```python
h2 {color:#ecf8fb!important;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 41**
```python
.hero {position:relative;overflow:hidden;border:1px solid #254c5d;border-radius:26px;padding:36px 42px;background:radial-gradient(circle at 80% 25%,#155f64 0%,transparent 37%),linear-gradient(120deg,#102a3b,#0b1c2b 72%);margin-bottom:25px;box-shadow:0 24px 55px #02070c66;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 42**
```python
.hero:after {content:'◉';position:absolute;right:5%;top:-85px;font-size:300px;line-height:1;color:#59edcf10;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 43**
```python
.eyebrow {color:#5ef0d0;font-size:.76rem;font-weight:700;letter-spacing:.24em;text-transform:uppercase;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 44**
```python
.hero h1 {font-size:clamp(2.5rem,5vw,4.8rem);line-height:1.02;color:white;margin:.4rem 0 .7rem;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 45**
```python
.hero p {max-width:700px;color:#bdd6dc;font-size:1.08rem;line-height:1.55;margin:0;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 46**
```python
.chip {display:inline-block;border:1px solid #3b6d73;background:#1a4148aa;color:#91ffdf;border-radius:999px;padding:6px 12px;font-size:.76rem;font-weight:700;margin-bottom:12px;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 47**
```python
.section-kicker {color:#70e9d1;text-transform:uppercase;letter-spacing:.16em;font-size:.77rem;font-weight:700;margin:8px 0;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 48**
```python
.card {border:1px solid #224154;border-radius:18px;background:#102235;padding:19px 22px;min-height:124px;box-shadow:0 14px 30px #02091255;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 49**
```python
.card .label {font-size:.72rem;color:#94b6c1;letter-spacing:.12em;text-transform:uppercase;font-weight:700;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 50**
```python
.card .value {font-family:'Space Grotesk',sans-serif;color:#f4fcfc;font-size:2rem;font-weight:700;line-height:1.2;margin:8px 0 4px;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 51**
```python
.card .note {font-size:.83rem;color:#98b8c2;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 52**
```python
.stage {display:inline-block;border:1px solid #2c4b59;background:#132b3c;border-radius:999px;padding:8px 13px;margin:0 5px 9px 0;color:#c9edf0;font-size:.82rem;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 53**
```python
.stage strong {color:#6df2d4;margin-right:6px;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 54**
```python
.plate {font-family:'Space Grotesk',sans-serif;letter-spacing:.09em;font-weight:700;font-size:clamp(1.4rem,3vw,2.5rem);color:#10212a;background:linear-gradient(130deg,#f8f9e9,#dce9e5);border:4px solid #d9e3de;box-shadow:0 6px 0 #243c45;border-radius:9px;padding:12px 20px;display:inline-block;margin:12px 0;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 55**
```python
.decision {border-left:4px solid #5fe6ca;background:#12343c;border-radius:8px;padding:16px 19px;margin:10px 0;color:#e9fcf6;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 56**
```python
.decision.review {border-color:#ffba6b;background:#38291f;color:#fff3e4;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 57**
```python
.small-muted {color:#96b6c0;font-size:.9rem;line-height:1.5;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 58**
```python
div[data-testid="stMetric"] {background:#102235;border:1px solid #224154;border-radius:16px;padding:12px 16px;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 59**
```python
div[data-testid="stMetricLabel"] {color:#9bbbc5;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 60**
```python
div[data-testid="stMetricValue"] {color:#f0faf8;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 61**
```python
div[data-testid="stTabs"] button {font-family:'Space Grotesk',sans-serif;font-weight:700;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 62**
```python
div[data-testid="stFileUploader"] {background:#102235;border:1px dashed #3b7079;border-radius:18px;padding:8px 16px;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 63**
```python
div.stButton button[kind="primary"] {background:#5fe6ca;color:#08202a;border:none;font-weight:800;border-radius:10px;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 64**
```python
.foot {border-top:1px solid #264352;margin-top:35px;padding-top:16px;color:#789ba8;font-size:.8rem;}
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 65**
```python
</style>
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 66**
```python
"""
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 67**
```python
st.markdown(CSS, unsafe_allow_html=True)
```
Call `st.markdown` with the inputs shown to obtain its result.

**Line 68**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 69**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 70**
```python
def card(label: str, value: str, note: str) -> None:
```
Define `card`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 71**
```python
    st.markdown(f'<div class="card"><div class="label">{escape(label)}</div><div class="value">{escape(value)}</div><div class="note">{escape(note)}</div></div>', unsafe_allow_html=True)
```
Call `st.markdown` with the inputs shown to obtain its result.

**Line 72**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 73**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 74**
```python
@st.cache_resource
```
Decorator or syntax belonging to the following definition; modifies how that definition is used (for example, caching).

**Line 75**
```python
def reader(name: str):
```
Define `reader`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 76**
```python
    return FastPlateEngine() if name == "FastPlateOCR" else EasyOCREngine(config.READER_UPSCALE, config.READER_ALLOWLIST)
```
Finish this function and choose the first value if `name == 'FastPlateOCR'` is true, otherwise choose the value after `else`; send that result to its caller.

**Line 77**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 78**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 79**
```python
@st.cache_resource
```
Decorator or syntax belonging to the following definition; modifies how that definition is used (for example, caching).

**Line 80**
```python
def detector(path: str):
```
Define `detector`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 81**
```python
    from ultralytics import YOLO
```
Make the named library tools available here: `from ultralytics import YOLO`. Importing a project module makes its reusable functions accessible.

**Line 82**
```python
    return YOLO(path)
```
Finish this function and call `YOLO` with the inputs shown to obtain its result; send that result to its caller.

**Line 83**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 84**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 85**
```python
def demo_examples() -> dict[str, dict]:
```
Define `demo_examples`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 86**
```python
    gallery = config.ROOT / "data/sample_gallery/manifest.csv"
```
Store the result in `gallery`: calculate `config.ROOT / 'data/sample_gallery/manifest.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 87**
```python
    if gallery.exists():
```
Run the indented branch only when `gallery.exists()` is true.

**Line 88**
```python
        with gallery.open(newline="") as source:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 89**
```python
            return {f"{index:02d} · {row['truth']}": row
```
Finish this function and build or iterate values using the inline `for` loop and any `if` filter shown; send that result to its caller.

**Line 90**
```python
                    for index, row in enumerate(csv.DictReader(source), 1)}
```
Continuation of the statement starting at line 89; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 91**
```python
    baseline = config.RESULTS_DIR / "end_to_end_details.csv"
```
Store the result in `baseline`: calculate `config.RESULTS_DIR / 'end_to_end_details.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 92**
```python
    manifest = config.ROOT / "data/indian_manifest.csv"
```
Store the result in `manifest`: calculate `config.ROOT / 'data/indian_manifest.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 93**
```python
    if not baseline.exists() or not manifest.exists():
```
Run the indented branch only when `not baseline.exists() or not manifest.exists()` is true.

**Line 94**
```python
        return {}
```
Finish this function and build a dictionary: each key names the value stored beside it; send that result to its caller.

**Line 95**
```python
    with baseline.open(newline="") as source:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 96**
```python
        rows = list(csv.DictReader(source))
```
Store the result in `rows`: call `list` with the inputs shown to obtain its result.

**Line 97**
```python
    with manifest.open(newline="") as source:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 98**
```python
        original = {r["image_path"]: r for r in csv.DictReader(source)}
```
Store the result in `original`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 99**
```python
    selected = [next((r for r in rows if int(r["ok"]) == outcome and r["route"] == decision
```
Store the result in `selected`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 100**
```python
                      and r["image"] in original), None)
```
Continuation of the statement starting at line 99; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 101**
```python
                for outcome, decision in ((1, "ACCEPT"), (0, "REVIEW"))]
```
Continuation of the statement starting at line 99; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 102**
```python
    result = {}
```
Store the result in `result`: build a dictionary: each key names the value stored beside it.

**Line 103**
```python
    for index, item in enumerate(selected):
```
For each item from `enumerate(selected)`, name it `(index, item)` and run the indented body.

**Line 104**
```python
        if item:
```
Run the indented branch only when `item` is true.

**Line 105**
```python
            result[f"Example {index+1} · {'accepted read' if index == 0 else 'difficult read'}"] = original[item["image"]]
```
Store the result in `result[f"Example {index + 1} · {('accepted read' if index == 0 else 'difficult read')}"]`: look up or slice `original` using the index or range in brackets.

**Line 106**
```python
    return result
```
Finish this function and evaluate `result` using the values currently in memory; send that result to its caller.

**Line 107**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 108**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 109**
```python
def analyze(image: np.ndarray, full_image: bool, model: dict | None,
```
Define `analyze`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 110**
```python
            reader_name: str, target: str = "0.10", stability_enabled: bool = False) -> dict:
```
Continuation of the statement starting at line 109; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 111**
```python
    marked = image.copy()
```
Store the result in `marked`: call `image.copy` with the inputs shown to obtain its result.

**Line 112**
```python
    crop = image
```
Store the result in `crop`: evaluate `image` using the values currently in memory.

**Line 113**
```python
    detection = None
```
Store the result in `detection`: use the fixed value `None`.

**Line 114**
```python
    if full_image:
```
Run the indented branch only when `full_image` is true.

**Line 115**
```python
        weights = config.ROOT / "weights/plate_detector.pt"
```
Store the result in `weights`: calculate `config.ROOT / 'weights/plate_detector.pt'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 116**
```python
        if not weights.exists():
```
Run the indented branch only when `not weights.exists()` is true.

**Line 117**
```python
            return {"error": "Detector weights are not ready. Choose Plate crop mode."}
```
Finish this function and build a dictionary: each key names the value stored beside it; send that result to its caller.

**Line 118**
```python
        result = detector(str(weights)).predict(image, conf=0.25, verbose=False)[0]
```
Store the result in `result`: look up or slice `detector(str(weights)).predict(image, conf=0.25, verbose=False)` using the index or range in brackets.

**Line 119**
```python
        if not len(result.boxes):
```
Run the indented branch only when `not len(result.boxes)` is true.

**Line 120**
```python
            return {"error": "No plate was detected. Send this image for manual review."}
```
Finish this function and build a dictionary: each key names the value stored beside it; send that result to its caller.

**Line 121**
```python
        box = max(result.boxes, key=lambda b: float(b.conf[0]))
```
Store the result in `box`: call `max` with the inputs shown to obtain its result.

**Line 122**
```python
        x1, y1, x2, y2 = [int(v) for v in box.xyxy[0].tolist()]
```
Store the result in `(x1, y1, x2, y2)`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 123**
```python
        x1, y1 = max(0, x1), max(0, y1)
```
Store the result in `(x1, y1)`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 124**
```python
        x2, y2 = min(image.shape[1], x2), min(image.shape[0], y2)
```
Store the result in `(x2, y2)`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 125**
```python
        crop = image[y1:y2, x1:x2]
```
Store the result in `crop`: look up or slice `image` using the index or range in brackets.

**Line 126**
```python
        cv2.rectangle(marked, (x1, y1), (x2, y2), (95, 230, 202), 3)
```
Call `cv2.rectangle` with the inputs shown to obtain its result.

**Line 127**
```python
        detection = float(box.conf[0])
```
Store the result in `detection`: call `float` with the inputs shown to obtain its result.

**Line 128**
```python
    if crop.size == 0:
```
Run the indented branch only when `crop.size == 0` is true.

**Line 129**
```python
        return {"error": "The detected crop was empty. Review the image manually."}
```
Finish this function and build a dictionary: each key names the value stored beside it; send that result to its caller.

**Line 130**
```python
    read = reader(reader_name).read(crop)
```
Store the result in `read`: call `reader(reader_name).read` with the inputs shown to obtain its result.

**Line 131**
```python
    text = normalize(read.text)
```
Store the result in `text`: uppercase the text and keep only letters A–Z and digits 0–9.

**Line 132**
```python
    calibrated = predict(model, plate_features(crop, read)) if model and text else None
```
Store the result in `calibrated`: choose the first value if `model and text` is true, otherwise choose the value after `else`.

**Line 133**
```python
    if calibrated is None:
```
Run the indented branch only when `calibrated is None` is true.

**Line 134**
```python
        decision = "REVIEW"
```
Store the result in `decision`: use the fixed value `'REVIEW'`.

**Line 135**
```python
        reason = "No calibrated confidence is available" if not model else (read.error or "No readable text")
```
Store the result in `reason`: choose the first value if `not model` is true, otherwise choose the value after `else`.

**Line 136**
```python
    else:
```
Run this branch when the associated condition was false.

**Line 137**
```python
        initial = route(text, calibrated, model["thresholds"][target])
```
Store the result in `initial`: apply the format and confidence acceptance rules.

**Line 138**
```python
        decision = "ACCEPT" if initial == "ACCEPT" else "REVIEW"
```
Store the result in `decision`: choose the first value if `initial == 'ACCEPT'` is true, otherwise choose the value after `else`.

**Line 139**
```python
        reason = f"Confidence passed the threshold chosen for the {float(target):.0%} validation target" if initial == "ACCEPT" else (
```
Store the result in `reason`: choose the first value if `initial == 'ACCEPT'` is true, otherwise choose the value after `else`.

**Line 140**
```python
            "Eligible for an optional second opinion; review offline" if initial == "ESCALATE" else "Low confidence or invalid format")
```
Continuation of the statement starting at line 139; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 141**
```python
    base_decision = decision
```
Store the result in `base_decision`: evaluate `decision` using the values currently in memory.

**Line 142**
```python
    stability = check_stability(crop, text, reader(reader_name).read) if stability_enabled else None
```
Store the result in `stability`: choose the first value if `stability_enabled` is true, otherwise choose the value after `else`.

**Line 143**
```python
    if stability:
```
Run the indented branch only when `stability` is true.

**Line 144**
```python
        decision = apply_veto(decision, stability)
```
Store the result in `decision`: change an accepted answer to review if the stability check failed.

**Line 145**
```python
        if decision != base_decision:
```
Run the indented branch only when `decision != base_decision` is true.

**Line 146**
```python
            reason = "Automatic acceptance vetoed: OCR changed under a mild image transformation"
```
Store the result in `reason`: use the fixed value `'Automatic acceptance vetoed: OCR changed under a mild image transformation'`.

**Line 147**
```python
    return {"base_route": base_decision, "stability": stability,
```
Finish this function and build a dictionary: each key names the value stored beside it; send that result to its caller.

**Line 148**
```python
            "marked": marked, "crop": crop, "text": text, "confidence": calibrated,
```
Continuation of the statement starting at line 147; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 149**
```python
            "raw_confidence": read.raw_conf, "route": decision, "reason": reason,
```
Continuation of the statement starting at line 147; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 150**
```python
            "detection": detection, "latency_ms": read.latency_ms,
```
Continuation of the statement starting at line 147; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 151**
```python
            "grammar": classify(text), "error": read.error}
```
Continuation of the statement starting at line 147; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 152**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 153**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 154**
```python
def save_correction(image_bytes: bytes, proposed: str, corrected: str) -> None:
```
Define `save_correction`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 155**
```python
    path = config.RESULTS_DIR / "review_corrections.csv"
```
Store the result in `path`: calculate `config.RESULTS_DIR / 'review_corrections.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 156**
```python
    path.parent.mkdir(exist_ok=True)
```
Call `path.parent.mkdir` with the inputs shown to obtain its result.

**Line 157**
```python
    first = not path.exists()
```
Store the result in `first`: evaluate `not path.exists()` using the values currently in memory.

**Line 158**
```python
    with path.open("a", newline="") as output:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 159**
```python
        writer = csv.DictWriter(output, fieldnames=["time", "image_sha256", "proposed", "corrected"])
```
Store the result in `writer`: call `csv.DictWriter` with the inputs shown to obtain its result.

**Line 160**
```python
        if first:
```
Run the indented branch only when `first` is true.

**Line 161**
```python
            writer.writeheader()
```
Call `writer.writeheader` with the inputs shown to obtain its result.

**Line 162**
```python
        writer.writerow({"time": datetime.now().isoformat(timespec="seconds"),
```
Call `writer.writerow` with the inputs shown to obtain its result.

**Line 163**
```python
                         "image_sha256": hashlib.sha256(image_bytes).hexdigest(),
```
Continuation of the statement starting at line 162; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 164**
```python
                         "proposed": proposed, "corrected": normalize(corrected)})
```
Continuation of the statement starting at line 162; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 165**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 166**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 167**
```python
model_path = config.CALIBRATION_MODEL
```
Store the result in `model_path`: evaluate `config.CALIBRATION_MODEL` using the values currently in memory.

**Line 168**
```python
calibration = load(model_path) if model_path.exists() else None
```
Store the result in `calibration`: choose the first value if `model_path.exists()` is true, otherwise choose the value after `else`.

**Line 169**
```python
selected_path = config.RESULTS_DIR / "selected_reader.json"
```
Store the result in `selected_path`: calculate `config.RESULTS_DIR / 'selected_reader.json'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 170**
```python
reader_name = json.loads(selected_path.read_text())["reader"] if selected_path.exists() else "EasyOCR"
```
Store the result in `reader_name`: choose the first value if `selected_path.exists()` is true, otherwise choose the value after `else`.

**Line 171**
```python
final_path = config.RESULTS_DIR / "final_test.json"
```
Store the result in `final_path`: calculate `config.RESULTS_DIR / 'final_test.json'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 172**
```python
final = json.loads(final_path.read_text()) if final_path.exists() else None
```
Store the result in `final`: choose the first value if `final_path.exists()` is true, otherwise choose the value after `else`.

**Line 173**
```python
detector_path = config.ROOT / "weights/plate_detector.pt"
```
Store the result in `detector_path`: calculate `config.ROOT / 'weights/plate_detector.pt'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 174**
```python
end_path = config.RESULTS_DIR / "end_to_end_extra.json"
```
Store the result in `end_path`: calculate `config.RESULTS_DIR / 'end_to_end_extra.json'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 175**
```python
if not end_path.exists():
```
Run the indented branch only when `not end_path.exists()` is true.

**Line 176**
```python
    end_path = config.RESULTS_DIR / "end_to_end_test.json"
```
Store the result in `end_path`: calculate `config.RESULTS_DIR / 'end_to_end_test.json'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 177**
```python
end = json.loads(end_path.read_text()) if end_path.exists() else None
```
Store the result in `end`: choose the first value if `end_path.exists()` is true, otherwise choose the value after `else`.

**Line 178**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 179**
```python
st.sidebar.markdown("### RISK<span style='color:#5fe6ca'>GATE</span> / Console", unsafe_allow_html=True)
```
Call `st.sidebar.markdown` with the inputs shown to obtain its result.

**Line 180**
```python
st.sidebar.caption("Local inference · No API calls")
```
Call `st.sidebar.caption` with the inputs shown to obtain its result.

**Line 181**
```python
policy_target = st.sidebar.selectbox("Review policy", ["0.10", "0.05", "0.02"],
```
Store the result in `policy_target`: call `st.sidebar.selectbox` with the inputs shown to obtain its result.

**Line 182**
```python
                                     format_func=lambda value: f"{float(value):.0%} validation target")
```
Continuation of the statement starting at line 181; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 183**
```python
st.sidebar.caption("A target guides threshold choice. It does not guarantee that error rate on new images.")
```
Call `st.sidebar.caption` with the inputs shown to obtain its result.

**Line 184**
```python
stability_enabled = st.sidebar.checkbox("Experimental stability check", value=False)
```
Store the result in `stability_enabled`: call `st.sidebar.checkbox` with the inputs shown to obtain its result.

**Line 185**
```python
st.sidebar.caption("Two extra OCR reads. Disagreement forces review; agreement does not prove correctness.")
```
Call `st.sidebar.caption` with the inputs shown to obtain its result.

**Line 186**
```python
st.sidebar.divider()
```
Call `st.sidebar.divider` with the inputs shown to obtain its result.

**Line 187**
```python
st.sidebar.write("**Active components**")
```
Call `st.sidebar.write` with the inputs shown to obtain its result.

**Line 188**
```python
st.sidebar.write(f"Detector: {'ready' if detector_path.exists() else 'unavailable'}")
```
Call `st.sidebar.write` with the inputs shown to obtain its result.

**Line 189**
```python
st.sidebar.write(f"Reader: {reader_name}")
```
Call `st.sidebar.write` with the inputs shown to obtain its result.

**Line 190**
```python
st.sidebar.write(f"Confidence model: {'ready' if calibration else 'unavailable'}")
```
Call `st.sidebar.write` with the inputs shown to obtain its result.

**Line 191**
```python
st.sidebar.caption("Inputs and corrections stay on this machine.")
```
Call `st.sidebar.caption` with the inputs shown to obtain its result.

**Line 192**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 193**
```python
st.markdown("""<div class="hero"><span class="chip">OFFLINE • INDIAN ANPR RESEARCH</span>
```
Call `st.markdown` with the inputs shown to obtain its result.

**Line 194**
```python
<div class="eyebrow">Computer vision / selective prediction</div>
```
Continuation of the statement starting at line 193; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 195**
```python
<h1>RISK<span style="color:#5ff0d2">GATE</span><span style="font-weight:400;color:#92adba"> / ANPR</span></h1>
```
Continuation of the statement starting at line 193; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 196**
```python
<p>Read the plate. Measure uncertainty. Route the difficult cases to a human. Every decision is visible, and every result is tied to a real test.</p></div>""", unsafe_allow_html=True)
```
Continuation of the statement starting at line 193; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 197**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 198**
```python
top = st.columns(4, gap="medium")
```
Store the result in `top`: call `st.columns` with the inputs shown to obtain its result.

**Line 199**
```python
with top[0]: card("OCR labels", "1,695", "paired images and text")
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 200**
```python
with top[1]: card("Detector train", "1,027", "847 core + 180 screened")
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 201**
```python
with top[2]: card("Demo gallery", "12", "real vehicle scenes")
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 202**
```python
with top[3]:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 203**
```python
    card("Auto coverage", f"{end['coverage']:.1%}" if end else "PENDING", "full-image evaluation")
```
Call `card` with the inputs shown to obtain its result.

**Line 204**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 205**
```python
st.markdown("<div class='section-kicker'>System flow</div>", unsafe_allow_html=True)
```
Call `st.markdown` with the inputs shown to obtain its result.

**Line 206**
```python
st.markdown("""<span class="stage"><strong>01</strong> Detect plate</span><span class="stage"><strong>02</strong> Read characters</span><span class="stage"><strong>03</strong> Check format</span><span class="stage"><strong>04</strong> Estimate correctness</span><span class="stage"><strong>05</strong> Accept or review</span>""", unsafe_allow_html=True)
```
Call `st.markdown` with the inputs shown to obtain its result.

**Line 207**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 208**
```python
demo_tab, batch_tab, evidence_tab, method_tab = st.tabs(
```
Store the result in `(demo_tab, batch_tab, evidence_tab, method_tab)`: call `st.tabs` with the inputs shown to obtain its result.

**Line 209**
```python
    ["◈   Live analysis", "▦   Batch review", "▥   Measured evidence", "◎   Method & limits"])
```
Continuation of the statement starting at line 208; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 210**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 211**
```python
with demo_tab:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 212**
```python
    left, right = st.columns([1, 1.25], gap="large")
```
Store the result in `(left, right)`: call `st.columns` with the inputs shown to obtain its result.

**Line 213**
```python
    with left:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 214**
```python
        st.subheader("Analyze an image")
```
Call `st.subheader` with the inputs shown to obtain its result.

**Line 215**
```python
        st.markdown("<div class='small-muted'>Use a vehicle photo for the complete pipeline, or a plate crop to inspect the reader on its own.</div>", unsafe_allow_html=True)
```
Call `st.markdown` with the inputs shown to obtain its result.

**Line 216**
```python
        mode = st.radio("Input type", ["Full vehicle photo", "Plate crop"], horizontal=True,
```
Store the result in `mode`: call `st.radio` with the inputs shown to obtain its result.

**Line 217**
```python
                        index=0 if detector_path.exists() else 1)
```
Continuation of the statement starting at line 216; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 218**
```python
        source = st.radio("Image source", ["Upload", "Demo gallery"], horizontal=True)
```
Store the result in `source`: call `st.radio` with the inputs shown to obtain its result.

**Line 219**
```python
        image_bytes = None
```
Store the result in `image_bytes`: use the fixed value `None`.

**Line 220**
```python
        example_truth = None
```
Store the result in `example_truth`: use the fixed value `None`.

**Line 221**
```python
        if source == "Upload":
```
Run the indented branch only when `source == 'Upload'` is true.

**Line 222**
```python
            uploaded = st.file_uploader("Choose a JPG or PNG", type=["jpg", "jpeg", "png"])
```
Store the result in `uploaded`: call `st.file_uploader` with the inputs shown to obtain its result.

**Line 223**
```python
            if uploaded:
```
Run the indented branch only when `uploaded` is true.

**Line 224**
```python
                image_bytes = uploaded.getvalue()
```
Store the result in `image_bytes`: call `uploaded.getvalue` with the inputs shown to obtain its result.

**Line 225**
```python
        else:
```
Run this branch when the associated condition was false.

**Line 226**
```python
            examples = demo_examples()
```
Store the result in `examples`: call `demo_examples` with the inputs shown to obtain its result.

**Line 227**
```python
            if examples:
```
Run the indented branch only when `examples` is true.

**Line 228**
```python
                label = st.selectbox("Choose an example", list(examples), index=1 if len(examples) > 2 else 0)
```
Store the result in `label`: call `st.selectbox` with the inputs shown to obtain its result.

**Line 229**
```python
                row = examples[label]
```
Store the result in `row`: look up or slice `examples` using the index or range in brackets.

**Line 230**
```python
                path = config.ROOT / row["image_path"]
```
Store the result in `path`: calculate `config.ROOT / row['image_path']`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 231**
```python
                image_bytes = path.read_bytes()
```
Store the result in `image_bytes`: call `path.read_bytes` with the inputs shown to obtain its result.

**Line 232**
```python
                if mode == "Plate crop":
```
Run the indented branch only when `mode == 'Plate crop'` is true.

**Line 233**
```python
                    if row.get("crop_path"):
```
Run the indented branch only when `row.get('crop_path')` is true.

**Line 234**
```python
                        image_bytes = (config.ROOT / row["crop_path"]).read_bytes()
```
Store the result in `image_bytes`: call `(config.ROOT / row['crop_path']).read_bytes` with the inputs shown to obtain its result.

**Line 235**
```python
                    elif all(row.get(key) for key in ("xmin", "ymin", "xmax", "ymax")):
```
Run the indented branch only when `all((row.get(key) for key in ('xmin', 'ymin', 'xmax', 'ymax')))` is true.

**Line 236**
```python
                        image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
```
Store the result in `image`: call `cv2.imdecode` with the inputs shown to obtain its result.

**Line 237**
```python
                        x1, y1, x2, y2 = [int(row[key]) for key in ("xmin", "ymin", "xmax", "ymax")]
```
Store the result in `(x1, y1, x2, y2)`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 238**
```python
                        crop = image[y1:y2, x1:x2]
```
Store the result in `crop`: look up or slice `image` using the index or range in brackets.

**Line 239**
```python
                        image_bytes = cv2.imencode(".jpg", crop)[1].tobytes()
```
Store the result in `image_bytes`: call `cv2.imencode('.jpg', crop)[1].tobytes` with the inputs shown to obtain its result.

**Line 240**
```python
                example_truth = row["truth"]
```
Store the result in `example_truth`: look up or slice `row` using the index or range in brackets.

**Line 241**
```python
                st.image(str(path), caption="Real vehicle scene · visually checked label · demo only", width=360)
```
Call `st.image` with the inputs shown to obtain its result.

**Line 242**
```python
            else:
```
Run this branch when the associated condition was false.

**Line 243**
```python
                st.info("Demo examples are unavailable on this machine.")
```
Call `st.info` with the inputs shown to obtain its result.

**Line 244**
```python
        if st.button("Analyze plate", type="primary", width="stretch", disabled=image_bytes is None):
```
Run the indented branch only when `st.button('Analyze plate', type='primary', width='stretch', disabled=image_bytes is None)` is true.

**Line 245**
```python
            image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
```
Store the result in `image`: call `cv2.imdecode` with the inputs shown to obtain its result.

**Line 246**
```python
            if image is None:
```
Run the indented branch only when `image is None` is true.

**Line 247**
```python
                st.error("Could not decode this image.")
```
Call `st.error` with the inputs shown to obtain its result.

**Line 248**
```python
            else:
```
Run this branch when the associated condition was false.

**Line 249**
```python
                st.session_state["analysis"] = analyze(image, mode == "Full vehicle photo", calibration,
```
Store the result in `st.session_state['analysis']`: call `analyze` with the inputs shown to obtain its result.

**Line 250**
```python
                                                        reader_name, policy_target, stability_enabled)
```
Continuation of the statement starting at line 249; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 251**
```python
                st.session_state["source_bytes"] = image_bytes
```
Store the result in `st.session_state['source_bytes']`: evaluate `image_bytes` using the values currently in memory.

**Line 252**
```python
                st.session_state["example_truth"] = example_truth
```
Store the result in `st.session_state['example_truth']`: evaluate `example_truth` using the values currently in memory.

**Line 253**
```python
        if "analysis" in st.session_state:
```
Run the indented branch only when `'analysis' in st.session_state` is true.

**Line 254**
```python
            result = st.session_state["analysis"]
```
Store the result in `result`: look up or slice `st.session_state` using the index or range in brackets.

**Line 255**
```python
            if result.get("error") and "marked" not in result:
```
Run the indented branch only when `result.get('error') and 'marked' not in result` is true.

**Line 256**
```python
                st.warning(result["error"])
```
Call `st.warning` with the inputs shown to obtain its result.

**Line 257**
```python
            else:
```
Run this branch when the associated condition was false.

**Line 258**
```python
                st.image(cv2.cvtColor(result["marked"], cv2.COLOR_BGR2RGB), caption="Input and detected region", width="stretch")
```
Call `st.image` with the inputs shown to obtain its result.

**Line 259**
```python
    with right:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 260**
```python
        st.subheader("Decision trace")
```
Call `st.subheader` with the inputs shown to obtain its result.

**Line 261**
```python
        if "analysis" not in st.session_state or "marked" not in st.session_state["analysis"]:
```
Run the indented branch only when `'analysis' not in st.session_state or 'marked' not in st.session_state['analysis']` is true.

**Line 262**
```python
            st.markdown("<div class='card'><div class='label'>Awaiting input</div><div class='value'>Ready to analyze</div><div class='note'>Upload a photo or select a built-in example.</div></div>", unsafe_allow_html=True)
```
Call `st.markdown` with the inputs shown to obtain its result.

**Line 263**
```python
        else:
```
Run this branch when the associated condition was false.

**Line 264**
```python
            result = st.session_state["analysis"]
```
Store the result in `result`: look up or slice `st.session_state` using the index or range in brackets.

**Line 265**
```python
            image_col, text_col = st.columns([1, 1.1], gap="medium")
```
Store the result in `(image_col, text_col)`: call `st.columns` with the inputs shown to obtain its result.

**Line 266**
```python
            with image_col:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 267**
```python
                st.image(cv2.cvtColor(result["crop"], cv2.COLOR_BGR2RGB), caption="Plate crop", width="stretch")
```
Call `st.image` with the inputs shown to obtain its result.

**Line 268**
```python
            with text_col:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 269**
```python
                st.markdown("<div class='section-kicker'>Local OCR result</div>", unsafe_allow_html=True)
```
Call `st.markdown` with the inputs shown to obtain its result.

**Line 270**
```python
                st.markdown(f"<div class='plate'>{escape(result['text'] or 'UNREADABLE')}</div>", unsafe_allow_html=True)
```
Call `st.markdown` with the inputs shown to obtain its result.

**Line 271**
```python
                if st.session_state.get("example_truth"):
```
Run the indented branch only when `st.session_state.get('example_truth')` is true.

**Line 272**
```python
                    st.caption(f"Example label: {st.session_state['example_truth']}")
```
Call `st.caption` with the inputs shown to obtain its result.

**Line 273**
```python
            cols = st.columns(3)
```
Store the result in `cols`: call `st.columns` with the inputs shown to obtain its result.

**Line 274**
```python
            cols[0].metric("Correctness estimate", f"{result['confidence']:.1%}" if result["confidence"] is not None else "—")
```
Call `cols[0].metric` with the inputs shown to obtain its result.

**Line 275**
```python
            cols[1].metric("OCR model score", f"{result['raw_confidence']:.1%}")
```
Call `cols[1].metric` with the inputs shown to obtain its result.

**Line 276**
```python
            cols[2].metric("OCR time", f"{result['latency_ms']:.0f} ms")
```
Call `cols[2].metric` with the inputs shown to obtain its result.

**Line 277**
```python
            style = "" if result["route"] == "ACCEPT" else " review"
```
Store the result in `style`: choose the first value if `result['route'] == 'ACCEPT'` is true, otherwise choose the value after `else`.

**Line 278**
```python
            st.markdown(f"<div class='decision{style}'><strong>{result['route']}</strong> · {escape(result['reason'])}<br><span class='small-muted'>Format: {escape(result['grammar'])}" +
```
Call `st.markdown` with the inputs shown to obtain its result.

**Line 279**
```python
                        (f" · Detector score: {result['detection']:.1%}" if result["detection"] is not None else "") + "</span></div>", unsafe_allow_html=True)
```
Continuation of the statement starting at line 278; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 280**
```python
            if result.get("stability"):
```
Run the indented branch only when `result.get('stability')` is true.

**Line 281**
```python
                evidence = result["stability"]
```
Store the result in `evidence`: look up or slice `result` using the index or range in brackets.

**Line 282**
```python
                st.write(f"Stability: {evidence['matching_variants']}/2 variants agree · base route: {result['base_route']}")
```
Call `st.write` with the inputs shown to obtain its result.

**Line 283**
```python
                st.dataframe(evidence["readings"], hide_index=True)
```
Call `st.dataframe` with the inputs shown to obtain its result.

**Line 284**
```python
                st.caption(f"Extra check time: {evidence['extra_latency_ms']:.0f} ms. These are correlated reads from the same model, not independent votes.")
```
Call `st.caption` with the inputs shown to obtain its result.

**Line 285**
```python
            with st.expander("Human correction"):
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 286**
```python
                with st.form("correction_form"):
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 287**
```python
                    corrected = st.text_input("Correct plate text", value=result["text"])
```
Store the result in `corrected`: call `st.text_input` with the inputs shown to obtain its result.

**Line 288**
```python
                    submitted = st.form_submit_button("Save correction")
```
Store the result in `submitted`: call `st.form_submit_button` with the inputs shown to obtain its result.

**Line 289**
```python
                if submitted and normalize(corrected):
```
Run the indented branch only when `submitted and normalize(corrected)` is true.

**Line 290**
```python
                    save_correction(st.session_state["source_bytes"], result["text"], corrected)
```
Call `save_correction` with the inputs shown to obtain its result.

**Line 291**
```python
                    st.success("Correction saved locally in the review log.")
```
Call `st.success` with the inputs shown to obtain its result.

**Line 292**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 293**
```python
with batch_tab:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 294**
```python
    st.subheader("Review a batch")
```
Call `st.subheader` with the inputs shown to obtain its result.

**Line 295**
```python
    st.caption("Analyze up to 20 images at once. Processing stays local; export the decision list as CSV. Manual review is required for uncertain or failed reads.")
```
Call `st.caption` with the inputs shown to obtain its result.

**Line 296**
```python
    batch_mode = st.radio("Batch input", ["Full vehicle photos", "Plate crops"], horizontal=True)
```
Store the result in `batch_mode`: call `st.radio` with the inputs shown to obtain its result.

**Line 297**
```python
    uploads = st.file_uploader("Choose images", type=["jpg", "jpeg", "png"],
```
Store the result in `uploads`: call `st.file_uploader` with the inputs shown to obtain its result.

**Line 298**
```python
                               accept_multiple_files=True, key="batch_uploads")
```
Continuation of the statement starting at line 297; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 299**
```python
    if len(uploads) > 20:
```
Run the indented branch only when `len(uploads) > 20` is true.

**Line 300**
```python
        st.error("Choose at most 20 images per batch.")
```
Call `st.error` with the inputs shown to obtain its result.

**Line 301**
```python
    if st.button("Analyze batch", type="primary", disabled=not uploads or len(uploads) > 20):
```
Run the indented branch only when `st.button('Analyze batch', type='primary', disabled=not uploads or len(uploads) > 20)` is true.

**Line 302**
```python
        records = []
```
Store the result in `records`: evaluate `[]` using the values currently in memory.

**Line 303**
```python
        progress = st.progress(0)
```
Store the result in `progress`: call `st.progress` with the inputs shown to obtain its result.

**Line 304**
```python
        for index, uploaded in enumerate(uploads, 1):
```
For each item from `enumerate(uploads, 1)`, name it `(index, uploaded)` and run the indented body.

**Line 305**
```python
            image = cv2.imdecode(np.frombuffer(uploaded.getvalue(), np.uint8), cv2.IMREAD_COLOR)
```
Store the result in `image`: call `cv2.imdecode` with the inputs shown to obtain its result.

**Line 306**
```python
            result = analyze(image, batch_mode == "Full vehicle photos", calibration,
```
Store the result in `result`: choose the first value if `image is not None` is true, otherwise choose the value after `else`.

**Line 307**
```python
                             reader_name, policy_target, stability_enabled) if image is not None else {"error": "Invalid image"}
```
Continuation of the statement starting at line 306; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 308**
```python
            records.append({"file": uploaded.name, "plate": result.get("text", ""),
```
Call `records.append` with the inputs shown to obtain its result.

**Line 309**
```python
                            "decision": result.get("route", "REVIEW"),
```
Continuation of the statement starting at line 308; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 310**
```python
                            "base_decision": result.get("base_route", "REVIEW"),
```
Continuation of the statement starting at line 308; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 311**
```python
                            "stable": result["stability"]["stable"] if result.get("stability") else "disabled",
```
Continuation of the statement starting at line 308; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 312**
```python
                            "correctness_estimate": round(result["confidence"], 3) if result.get("confidence") is not None else "",
```
Continuation of the statement starting at line 308; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 313**
```python
                            "reason": result.get("reason", result.get("error", ""))})
```
Continuation of the statement starting at line 308; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 314**
```python
            progress.progress(index / len(uploads))
```
Call `progress.progress` with the inputs shown to obtain its result.

**Line 315**
```python
        st.session_state["batch_results"] = records
```
Store the result in `st.session_state['batch_results']`: evaluate `records` using the values currently in memory.

**Line 316**
```python
    if st.session_state.get("batch_results"):
```
Run the indented branch only when `st.session_state.get('batch_results')` is true.

**Line 317**
```python
        records = st.session_state["batch_results"]
```
Store the result in `records`: look up or slice `st.session_state` using the index or range in brackets.

**Line 318**
```python
        st.dataframe(records, width="stretch", hide_index=True)
```
Call `st.dataframe` with the inputs shown to obtain its result.

**Line 319**
```python
        output = io.StringIO()
```
Store the result in `output`: call `io.StringIO` with the inputs shown to obtain its result.

**Line 320**
```python
        writer = csv.DictWriter(output, fieldnames=list(records[0]))
```
Store the result in `writer`: call `csv.DictWriter` with the inputs shown to obtain its result.

**Line 321**
```python
        writer.writeheader()
```
Call `writer.writeheader` with the inputs shown to obtain its result.

**Line 322**
```python
        writer.writerows(records)
```
Call `writer.writerows` with the inputs shown to obtain its result.

**Line 323**
```python
        st.download_button("Export decisions as CSV", output.getvalue(), "riskgate_decisions.csv", "text/csv")
```
Call `st.download_button` with the inputs shown to obtain its result.

**Line 324**
```python
    correction_path = config.RESULTS_DIR / "review_corrections.csv"
```
Store the result in `correction_path`: calculate `config.RESULTS_DIR / 'review_corrections.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 325**
```python
    if correction_path.exists():
```
Run the indented branch only when `correction_path.exists()` is true.

**Line 326**
```python
        with st.expander("Local correction log"):
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 327**
```python
            st.dataframe(list(csv.DictReader(correction_path.open(newline=""))),
```
Call `st.dataframe` with the inputs shown to obtain its result.

**Line 328**
```python
                         width="stretch", hide_index=True)
```
Continuation of the statement starting at line 327; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 329**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 330**
```python
with evidence_tab:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 331**
```python
    stability_report = config.RESULTS_DIR / "stability_gallery.json"
```
Store the result in `stability_report`: calculate `config.RESULTS_DIR / 'stability_gallery.json'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 332**
```python
    if stability_report.exists():
```
Run the indented branch only when `stability_report.exists()` is true.

**Line 333**
```python
        experiment = json.loads(stability_report.read_text())
```
Store the result in `experiment`: call `json.loads` with the inputs shown to obtain its result.

**Line 334**
```python
        with st.expander("New research experiment: stability veto ablation"):
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 335**
```python
            st.caption(experiment["scope"])
```
Call `st.caption` with the inputs shown to obtain its result.

**Line 336**
```python
            st.dataframe([{"policy": key, **value} for key, value in experiment["policies"].items()], hide_index=True)
```
Call `st.dataframe` with the inputs shown to obtain its result.

**Line 337**
```python
            st.warning("This gallery experiment removed one correct acceptance and retained the wrong acceptance. It did not improve observed error. The check remains optional and is off by default.")
```
Call `st.warning` with the inputs shown to obtain its result.

**Line 338**
```python
            st.caption(f"Mean extra processing time: {experiment['mean_extra_latency_ms']:.1f} ms on this run.")
```
Call `st.caption` with the inputs shown to obtain its result.

**Line 339**
```python
    st.subheader("What the held-out evaluation actually showed")
```
Call `st.subheader` with the inputs shown to obtain its result.

**Line 340**
```python
    st.caption("A 10% target was chosen on validation data. The final-test error can exceed that target; the interval shows uncertainty.")
```
Call `st.caption` with the inputs shown to obtain its result.

**Line 341**
```python
    if final:
```
Run the indented branch only when `final` is true.

**Line 342**
```python
        target = final["targets"]["0.10"]
```
Store the result in `target`: look up or slice `final['targets']` using the index or range in brackets.

**Line 343**
```python
        cols = st.columns(4)
```
Store the result in `cols`: call `st.columns` with the inputs shown to obtain its result.

**Line 344**
```python
        cols[0].metric("Test plates", final["n"])
```
Call `cols[0].metric` with the inputs shown to obtain its result.

**Line 345**
```python
        cols[1].metric("Accepted", target["accepted"])
```
Call `cols[1].metric` with the inputs shown to obtain its result.

**Line 346**
```python
        cols[2].metric("Auto coverage", f"{target['coverage']:.1%}")
```
Call `cols[2].metric` with the inputs shown to obtain its result.

**Line 347**
```python
        cols[3].metric("Error among accepted", f"{target['observed_error']:.1%}" if target["observed_error"] is not None else "—")
```
Call `cols[3].metric` with the inputs shown to obtain its result.

**Line 348**
```python
        st.warning("At the stricter 2% and 5% validation targets, no test plates were accepted automatically. The 10% target accepted 72/254, and 9 of those 72 were wrong. This dataset also contains some non-Indian examples and unverified XML labels.")
```
Call `st.warning` with the inputs shown to obtain its result.

**Line 349**
```python
        if end:
```
Run the indented branch only when `end` is true.

**Line 350**
```python
            st.subheader("Complete vehicle-photo pipeline")
```
Call `st.subheader` with the inputs shown to obtain its result.

**Line 351**
```python
            end_cols = st.columns(4)
```
Store the result in `end_cols`: call `st.columns` with the inputs shown to obtain its result.

**Line 352**
```python
            end_cols[0].metric("Exact plate matches", f"{end['whole_plate_exact']}/{end['n']}")
```
Call `end_cols[0].metric` with the inputs shown to obtain its result.

**Line 353**
```python
            end_cols[1].metric("End-to-end accuracy", f"{end['whole_plate_accuracy']:.1%}")
```
Call `end_cols[1].metric` with the inputs shown to obtain its result.

**Line 354**
```python
            end_cols[2].metric("Accepted automatically", end["accepted"])
```
Call `end_cols[2].metric` with the inputs shown to obtain its result.

**Line 355**
```python
            end_cols[3].metric("Accepted errors", end["accepted_errors"])
```
Call `end_cols[3].metric` with the inputs shown to obtain its result.

**Line 356**
```python
            st.caption(f"Full-image route: {end['accepted']}/{end['n']} accepted, {end['accepted_errors']} wrong ({end['accepted_error']:.1%} observed accepted error). The expanded detector was evaluated after the earlier test results were viewed.")
```
Call `st.caption` with the inputs shown to obtain its result.

**Line 357**
```python
        plot_cols = st.columns(2, gap="large")
```
Store the result in `plot_cols`: call `st.columns` with the inputs shown to obtain its result.

**Line 358**
```python
        for column, name, title in ((plot_cols[0], "risk_coverage.png", "Risk versus coverage"),
```
For each item from `((plot_cols[0], 'risk_coverage.png', 'Risk versus coverage'), (plot_cols[1], 'reliability.png', 'Confidence calibration'))`, name it `(column, name, title)` and run the indented body.

**Line 359**
```python
                                    (plot_cols[1], "reliability.png", "Confidence calibration")):
```
Continuation of the statement starting at line 358; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 360**
```python
            with column:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 361**
```python
                path = config.RESULTS_DIR / name
```
Store the result in `path`: calculate `config.RESULTS_DIR / name`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 362**
```python
                if path.exists():
```
Run the indented branch only when `path.exists()` is true.

**Line 363**
```python
                    st.image(str(path), caption=title, width="stretch")
```
Call `st.image` with the inputs shown to obtain its result.

**Line 364**
```python
        detector_report = config.RESULTS_DIR / "detector_test.json"
```
Store the result in `detector_report`: calculate `config.RESULTS_DIR / 'detector_test.json'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 365**
```python
        if detector_report.exists():
```
Run the indented branch only when `detector_report.exists()` is true.

**Line 366**
```python
            report = json.loads(detector_report.read_text())
```
Store the result in `report`: call `json.loads` with the inputs shown to obtain its result.

**Line 367**
```python
            st.subheader("Full-image detector · expanded training")
```
Call `st.subheader` with the inputs shown to obtain its result.

**Line 368**
```python
            dcols = st.columns(3)
```
Store the result in `dcols`: call `st.columns` with the inputs shown to obtain its result.

**Line 369**
```python
            dcols[0].metric("Test images", report["test_images"])
```
Call `dcols[0].metric` with the inputs shown to obtain its result.

**Line 370**
```python
            dcols[1].metric("Found a plate", report["images_with_detection"])
```
Call `dcols[1].metric` with the inputs shown to obtain its result.

**Line 371**
```python
            dcols[2].metric("Matched box at IoU ≥ 0.5", f"{report['recall_at_iou_05']:.1%}")
```
Call `dcols[2].metric` with the inputs shown to obtain its result.

**Line 372**
```python
            comparison = config.RESULTS_DIR / "detector_comparison.json"
```
Store the result in `comparison`: calculate `config.RESULTS_DIR / 'detector_comparison.json'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 373**
```python
            if comparison.exists():
```
Run the indented branch only when `comparison.exists()` is true.

**Line 374**
```python
                versions = json.loads(comparison.read_text())
```
Store the result in `versions`: call `json.loads` with the inputs shown to obtain its result.

**Line 375**
```python
                st.dataframe([{"version": "Original", "training images": 847,
```
Call `st.dataframe` with the inputs shown to obtain its result.

**Line 376**
```python
                               "matched boxes": versions["original"]["matched_at_iou_05"],
```
Continuation of the statement starting at line 375; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 377**
```python
                               "recall": f"{versions['original']['recall_at_iou_05']:.1%}"},
```
Continuation of the statement starting at line 375; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 378**
```python
                              {"version": "Expanded", "training images": 1027,
```
Continuation of the statement starting at line 375; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 379**
```python
                               "matched boxes": versions["expanded_training"]["matched_at_iou_05"],
```
Continuation of the statement starting at line 375; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 380**
```python
                               "recall": f"{versions['expanded_training']['recall_at_iou_05']:.1%}"}],
```
Continuation of the statement starting at line 375; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 381**
```python
                             width="stretch", hide_index=True)
```
Continuation of the statement starting at line 375; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 382**
```python
        summary = config.RESULTS_DIR / "baseline_v2_summary.txt"
```
Store the result in `summary`: calculate `config.RESULTS_DIR / 'baseline_v2_summary.txt'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 383**
```python
        if summary.exists():
```
Run the indented branch only when `summary.exists()` is true.

**Line 384**
```python
            with st.expander("Complete OCR comparison"):
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 385**
```python
                st.code(summary.read_text(), language="text")
```
Call `st.code` with the inputs shown to obtain its result.

**Line 386**
```python
    else:
```
Run this branch when the associated condition was false.

**Line 387**
```python
        st.info("The evaluation pipeline has not produced final numbers yet.")
```
Call `st.info` with the inputs shown to obtain its result.

**Line 388**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 389**
```python
with method_tab:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 390**
```python
    st.subheader("A readable system, not a black box")
```
Call `st.subheader` with the inputs shown to obtain its result.

**Line 391**
```python
    st.markdown("""
```
Call `st.markdown` with the inputs shown to obtain its result.

**Line 392**
```python
**Detection** finds a rectangle around the plate in a full vehicle image. **OCR** reads letters and digits from that crop. **Calibration** uses labeled examples to estimate whether the whole reading is right. **Routing** accepts only readings above a threshold chosen on validation data; others go to review.
```
Continuation of the statement starting at line 391; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 393**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 394**
```python
The data is split by repeated plate identity and source video. The local reader is selected using the training split; confidence is fitted on calibration data, and thresholds are chosen on validation data. An additional box-only source added 180 screened full vehicle photos to detector training. Its other 1,902 plate crops have no trustworthy text labels and are not used for OCR evaluation. The 12-gallery examples are original full vehicle photos from the first source, with their XML plate text visually checked; they are demo examples, not a benchmark. The source XML labels have only a sampled visual audit so far, and some Google images show foreign plates. The OCR test statistics were viewed before the routing evaluation, and the expanded detector was evaluated on that same test. These results are **held out from fitting but not fully blinded**.
```
Continuation of the statement starting at line 391; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 395**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 396**
```python
This is an academic prototype. Glare, motion blur, tiny crops, uncommon layouts, and new cameras can reduce accuracy. Human correction remains necessary for uncertain cases. No plate image or API key is sent to a cloud service by this demo.
```
Continuation of the statement starting at line 391; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 397**
```python
""")
```
Continuation of the statement starting at line 391; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 398**
```python
    st.markdown("**Research basis:** [BLPR](https://arxiv.org/abs/2604.09927) · [Neural Sentinel](https://arxiv.org/abs/2602.07051) · [Nigerian VLM evaluation](https://arxiv.org/abs/2607.02025) · [VehiclePaliGemma](https://arxiv.org/abs/2412.14197) · [ICPR low-resolution competition](https://arxiv.org/abs/2604.22506) · [Indian LPR dataset](https://arxiv.org/abs/2111.06054)")
```
Call `st.markdown` with the inputs shown to obtain its result.

**Line 399**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 400**
```python
st.markdown("<div class='foot'>RISK<span style='color:#5fe6ca'>GATE</span> / ANPR LAB · Local inference · Measured uncertainty · Human review</div>", unsafe_allow_html=True)
```
Call `st.markdown` with the inputs shown to obtain its result.

## riskgate/__init__.py

Package marker: allows this folder to hold importable modules.

Source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

Empty package marker; there are no executable lines.

## riskgate/calibration.py

Learn and use a small model that estimates whether a complete OCR answer is correct.

Source SHA-256: `8e92c7cdb04ba66d8e87b0d58324916c9ec6ecf947a03c459e4518728b472e97`

**Line 1**
```python
"""Small logistic correctness model, stored as portable JSON."""
```
Use the fixed value `'small logistic correctness model, stored as portable json.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import hashlib
```
Make the named library tools available here: `import hashlib`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
import json
```
Make the named library tools available here: `import json`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python
import math
```
Make the named library tools available here: `import math`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python
from datetime import date
```
Make the named library tools available here: `from datetime import date`. Importing a project module makes its reusable functions accessible.

**Line 7**
```python
from pathlib import Path
```
Make the named library tools available here: `from pathlib import Path`. Importing a project module makes its reusable functions accessible.

**Line 8**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 9**
```python
from sklearn.linear_model import LogisticRegression
```
Make the named library tools available here: `from sklearn.linear_model import LogisticRegression`. Importing a project module makes its reusable functions accessible.

**Line 10**
```python
from sklearn.preprocessing import StandardScaler
```
Make the named library tools available here: `from sklearn.preprocessing import StandardScaler`. Importing a project module makes its reusable functions accessible.

**Line 11**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 12**
```python
from riskgate.features import FEATURE_NAMES
```
Make the named library tools available here: `from riskgate.features import FEATURE_NAMES`. Importing a project module makes its reusable functions accessible.

**Line 13**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 14**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 15**
```python
def data_hash(rows: list[dict]) -> str:
```
Define `data_hash`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 16**
```python
    content = json.dumps(sorted(rows, key=lambda r: (r.get("source", ""), r.get("image", ""))),
```
Store the result in `content`: call `json.dumps(sorted(rows, key=lambda r: (r.get('source', ''), r.get('image', ''))), sort_keys=True).encode` with the inputs shown to obtain its result.

**Line 17**
```python
                         sort_keys=True).encode()
```
Continuation of the statement starting at line 16; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 18**
```python
    return hashlib.sha256(content).hexdigest()
```
Finish this function and call `hashlib.sha256(content).hexdigest` with the inputs shown to obtain its result; send that result to its caller.

**Line 19**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 20**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 21**
```python
def fit(rows: list[dict]) -> dict:
```
Define `fit`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 22**
```python
    if len(rows) < 20 or len({int(r["ok"]) for r in rows}) != 2:
```
Run the indented branch only when `len(rows) < 20 or len({int(r['ok']) for r in rows}) != 2` is true.

**Line 23**
```python
        raise ValueError("Calibration needs at least 20 reviewed reads with both correct and wrong examples")
```
Stop this operation with the shown exception and message, rather than silently continuing.

**Line 24**
```python
    x = [[float(r[name]) for name in FEATURE_NAMES] for r in rows]
```
Store the result in `x`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 25**
```python
    y = [int(r["ok"]) for r in rows]
```
Store the result in `y`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 26**
```python
    scaler = StandardScaler().fit(x)
```
Store the result in `scaler`: call `StandardScaler().fit` with the inputs shown to obtain its result.

**Line 27**
```python
    model = LogisticRegression(C=0.1, max_iter=1000).fit(scaler.transform(x), y)
```
Store the result in `model`: call `LogisticRegression(C=0.1, max_iter=1000).fit` with the inputs shown to obtain its result.

**Line 28**
```python
    return {"feature_names": FEATURE_NAMES, "coefficients": model.coef_[0].tolist(),
```
Finish this function and build a dictionary: each key names the value stored beside it; send that result to its caller.

**Line 29**
```python
            "intercept": float(model.intercept_[0]), "mean": scaler.mean_.tolist(),
```
Continuation of the statement starting at line 28; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 30**
```python
            "scale": scaler.scale_.tolist(), "data_sha256": data_hash(rows),
```
Continuation of the statement starting at line 28; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 31**
```python
            "date": date.today().isoformat()}
```
Continuation of the statement starting at line 28; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 32**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 33**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 34**
```python
def predict(model: dict, features: dict[str, float]) -> float:
```
Define `predict`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 35**
```python
    score = model["intercept"] + sum(
```
Store the result in `score`: calculate `model['intercept'] + sum((w * (float(features[name]) - mean) / scale for name, w, mean, scale in zip(model['feature_names'], model['coefficients'], model['mean'], model['scale'])))`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 36**
```python
        w * (float(features[name]) - mean) / scale
```
Continuation of the statement starting at line 35; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 37**
```python
        for name, w, mean, scale in zip(model["feature_names"], model["coefficients"],
```
Continuation of the statement starting at line 35; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 38**
```python
                                        model["mean"], model["scale"]))
```
Continuation of the statement starting at line 35; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 39**
```python
    return 1 / (1 + math.exp(-max(-700, min(700, score))))
```
Finish this function and calculate `1 / (1 + math.exp(-max(-700, min(700, score))))`; `/` divides, `*` multiplies, and paths use `/` to join folders; send that result to its caller.

**Line 40**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 41**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 42**
```python
def save(model: dict, path: Path) -> None:
```
Define `save`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 43**
```python
    path.write_text(json.dumps(model, indent=2) + "\n")
```
Call `path.write_text` with the inputs shown to obtain its result.

**Line 44**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 45**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 46**
```python
def load(path: Path) -> dict:
```
Define `load`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 47**
```python
    return json.loads(path.read_text())
```
Finish this function and call `json.loads` with the inputs shown to obtain its result; send that result to its caller.

## riskgate/config.py

Keep shared file paths and experiment settings in one place.

Source SHA-256: `b37016f044adfd150f6a56d698ef1d10e4a098e2aed455a04cefecc5ad87f32b`

**Line 1**
```python
ROOT = __import__("pathlib").Path(__file__).resolve().parent.parent
```
Store the result in `ROOT`: evaluate `__import__('pathlib').Path(__file__).resolve().parent.parent` using the values currently in memory.

**Line 2**
```python
DATA_DIR = ROOT / "data/legacy/datacluster"
```
Store the result in `DATA_DIR`: calculate `ROOT / 'data/legacy/datacluster'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 3**
```python
SPLITS_V2 = ROOT / "data/splits_v2.json"
```
Store the result in `SPLITS_V2`: calculate `ROOT / 'data/splits_v2.json'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 4**
```python
CALIBRATION_MODEL = ROOT / "weights/calibration.json"
```
Store the result in `CALIBRATION_MODEL`: calculate `ROOT / 'weights/calibration.json'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 5**
```python
DRAFTS = ROOT / "data/labels/draft_labels.csv"
```
Store the result in `DRAFTS`: calculate `ROOT / 'data/labels/draft_labels.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 6**
```python
YOLO_START = ROOT / "weights/yolo11n.pt"
```
Store the result in `YOLO_START`: calculate `ROOT / 'weights/yolo11n.pt'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 7**
```python
RESULTS_DIR = ROOT / "results"
```
Store the result in `RESULTS_DIR`: calculate `ROOT / 'results'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 8**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 9**
```python
SEED = 0
```
Store the result in `SEED`: use the fixed value `0`.

**Line 10**
```python
MIN_CROP_H = 0
```
Store the result in `MIN_CROP_H`: use the fixed value `0`.

**Line 11**
```python
READER_ALLOWLIST = True
```
Store the result in `READER_ALLOWLIST`: use the fixed value `True`.

**Line 12**
```python
READER_UPSCALE = False
```
Store the result in `READER_UPSCALE`: use the fixed value `False`.

## riskgate/contracts.py

Define the fields in a labelled example and an OCR result.

Source SHA-256: `ed51235a53001883f0a19a45e1a2b408505373796b7715f3f4c806efe2e9f024`

**Line 1**
```python
from dataclasses import dataclass
```
Make the named library tools available here: `from dataclasses import dataclass`. Importing a project module makes its reusable functions accessible.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 4**
```python
@dataclass
```
Decorator or syntax belonging to the following definition; modifies how that definition is used (for example, caching).

**Line 5**
```python
class PlateSample:
```
Define the `PlateSample` object type, grouping its data and methods.

**Line 6**
```python
    """One labelled plate: source image, pixel bbox (x1, y1, x2, y2), ground-truth text."""
```
Use the fixed value `'one labelled plate: source image, pixel bbox (x1, y1, x2, y2), ground-truth text.'`.

**Line 7**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 8**
```python
    image_path: str
```
Declare the expected type of `image_path`.

**Line 9**
```python
    bbox: tuple[int, int, int, int]
```
Declare the expected type of `bbox`.

**Line 10**
```python
    truth: str
```
Declare the expected type of `truth`.

**Line 11**
```python
    source: str = "datacluster"
```
Store the result in `source`: use the fixed value `'datacluster'`.

**Line 12**
```python
    group_id: str = ""
```
Store the result in `group_id`: use the fixed value `''`.

**Line 13**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 14**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 15**
```python
@dataclass
```
Decorator or syntax belonging to the following definition; modifies how that definition is used (for example, caching).

**Line 16**
```python
class EngineResult:
```
Define the `EngineResult` object type, grouping its data and methods.

**Line 17**
```python
    """One engine read. On failure error is set and text stays "" - never raise, never fake."""
```
Use the fixed value `'one engine read. on failure error is set and text stays "" - never raise, never fake.'`.

**Line 18**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 19**
```python
    text: str
```
Declare the expected type of `text`.

**Line 20**
```python
    raw_conf: float
```
Declare the expected type of `raw_conf`.

**Line 21**
```python
    latency_ms: float
```
Declare the expected type of `latency_ms`.

**Line 22**
```python
    error: str | None = None
```
Store the result in `error`: use the fixed value `None`.

**Line 23**
```python
    boxes_found: int = 0
```
Store the result in `boxes_found`: use the fixed value `0`.

## riskgate/data.py

Load labels, keep related images together, and crop plate rectangles.

Source SHA-256: `aea9522f2827e27a7eef189595ff7bf91f210016acd33dce32fe31e09d54fb1a`

**Line 1**
```python
import json
```
Make the named library tools available here: `import json`. Importing a project module makes its reusable functions accessible.

**Line 2**
```python
import csv
```
Make the named library tools available here: `import csv`. Importing a project module makes its reusable functions accessible.

**Line 3**
```python
import random
```
Make the named library tools available here: `import random`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
import xml.etree.ElementTree as ET
```
Make the named library tools available here: `import xml.etree.ElementTree as ET`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python
from pathlib import Path
```
Make the named library tools available here: `from pathlib import Path`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 7**
```python
import cv2
```
Make the named library tools available here: `import cv2`. Importing a project module makes its reusable functions accessible.

**Line 8**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 9**
```python
from riskgate import config
```
Make the named library tools available here: `from riskgate import config`. Importing a project module makes its reusable functions accessible.

**Line 10**
```python
from riskgate.contracts import PlateSample
```
Make the named library tools available here: `from riskgate.contracts import PlateSample`. Importing a project module makes its reusable functions accessible.

**Line 11**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 12**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 13**
```python
def load_samples(data_dir: Path = config.DATA_DIR) -> list[PlateSample]:
```
Define `load_samples`; its indented body runs when called. Parse every XML into PlateSamples: skip objects with no plate text, clip bbox to image.

**Line 14**
```python
    """Parse every XML into PlateSamples: skip objects with no plate text, clip bbox to image."""
```
Use the fixed value `'parse every xml into platesamples: skip objects with no plate text, clip bbox to image.'`.

**Line 15**
```python
    samples = []
```
Store the result in `samples`: evaluate `[]` using the values currently in memory.

**Line 16**
```python
    for xml_path in sorted((data_dir / "Annotations").glob("*.xml")):
```
For each item from `sorted((data_dir / 'Annotations').glob('*.xml'))`, name it `xml_path` and run the indented body.

**Line 17**
```python
        root = ET.parse(xml_path).getroot()
```
Store the result in `root`: call `ET.parse(xml_path).getroot` with the inputs shown to obtain its result.

**Line 18**
```python
        name = root.findtext("filename")
```
Store the result in `name`: call `root.findtext` with the inputs shown to obtain its result.

**Line 19**
```python
        img = cv2.imread(str(data_dir / "images" / name))
```
Store the result in `img`: call `cv2.imread` with the inputs shown to obtain its result.

**Line 20**
```python
        if img is None:
```
Run the indented branch only when `img is None` is true.

**Line 21**
```python
            continue
```
Skip the rest of this loop iteration and move to the next item.

**Line 22**
```python
        H, W = img.shape[:2]
```
Store the result in `(H, W)`: look up or slice `img.shape` using the index or range in brackets.

**Line 23**
```python
        for obj in root.findall("object"):
```
For each item from `root.findall('object')`, name it `obj` and run the indented body.

**Line 24**
```python
            truth = next(
```
Store the result in `truth`: call `next` with the inputs shown to obtain its result.

**Line 25**
```python
                (
```
Continuation of the statement starting at line 24; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 26**
```python
                    a.findtext("value")
```
Continuation of the statement starting at line 24; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 27**
```python
                    for a in obj.iter("attribute")
```
Continuation of the statement starting at line 24; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 28**
```python
                    if a.findtext("name") == "number_plate_text"
```
Continuation of the statement starting at line 24; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 29**
```python
                ),
```
Continuation of the statement starting at line 24; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 30**
```python
                None,
```
Continuation of the statement starting at line 24; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 31**
```python
            )
```
Continuation of the statement starting at line 24; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 32**
```python
            if not truth:
```
Run the indented branch only when `not truth` is true.

**Line 33**
```python
                continue
```
Skip the rest of this loop iteration and move to the next item.

**Line 34**
```python
            bb = obj.find("bndbox")
```
Store the result in `bb`: call `obj.find` with the inputs shown to obtain its result.

**Line 35**
```python
            x1, y1, x2, y2 = (
```
Store the result in `(x1, y1, x2, y2)`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 36**
```python
                int(float(bb.findtext(c))) for c in ("xmin", "ymin", "xmax", "ymax")
```
Continuation of the statement starting at line 35; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 37**
```python
            )
```
Continuation of the statement starting at line 35; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 38**
```python
            samples.append(
```
Call `samples.append` with the inputs shown to obtain its result.

**Line 39**
```python
                PlateSample(
```
Continuation of the statement starting at line 38; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 40**
```python
                    image_path=str(data_dir / "images" / name),
```
Continuation of the statement starting at line 38; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 41**
```python
                    bbox=(max(0, x1), max(0, y1), min(W, x2), min(H, y2)),
```
Continuation of the statement starting at line 38; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 42**
```python
                    truth=truth,
```
Continuation of the statement starting at line 38; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 43**
```python
                    source="datacluster",
```
Continuation of the statement starting at line 38; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 44**
```python
                    group_id=f"datacluster:{Path(name).stem}",
```
Continuation of the statement starting at line 38; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 45**
```python
                )
```
Continuation of the statement starting at line 38; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 46**
```python
            )
```
Continuation of the statement starting at line 38; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 47**
```python
    return samples
```
Finish this function and evaluate `samples` using the values currently in memory; send that result to its caller.

**Line 48**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 49**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 50**
```python
def load_all_samples(data_dir: Path = config.DATA_DIR) -> list[PlateSample]:
```
Define `load_all_samples`; its indented body runs when called. Combine XML labels with any human review overrides, without changing either file.

**Line 51**
```python
    """Combine XML labels with any human review overrides, without changing either file."""
```
Use the fixed value `'combine xml labels with any human review overrides, without changing either file.'`.

**Line 52**
```python
    samples = load_samples(data_dir)
```
Store the result in `samples`: call `load_samples` with the inputs shown to obtain its result.

**Line 53**
```python
    xml_labels = config.ROOT / "data/labels/kaggle_xml_labels.csv"
```
Store the result in `xml_labels`: calculate `config.ROOT / 'data/labels/kaggle_xml_labels.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 54**
```python
    reviewed_labels = config.ROOT / "data/labels/kaggle_labels.csv"
```
Store the result in `reviewed_labels`: calculate `config.ROOT / 'data/labels/kaggle_labels.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 55**
```python
    overrides = {}
```
Store the result in `overrides`: build a dictionary: each key names the value stored beside it.

**Line 56**
```python
    if reviewed_labels.exists():
```
Run the indented branch only when `reviewed_labels.exists()` is true.

**Line 57**
```python
        with reviewed_labels.open(newline="") as source:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 58**
```python
            overrides = {row["crop_path"]: row["truth"] for row in csv.DictReader(source)}
```
Store the result in `overrides`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 59**
```python
    labels = xml_labels if xml_labels.exists() else reviewed_labels
```
Store the result in `labels`: choose the first value if `xml_labels.exists()` is true, otherwise choose the value after `else`.

**Line 60**
```python
    if labels.exists():
```
Run the indented branch only when `labels.exists()` is true.

**Line 61**
```python
        with labels.open(newline="") as source:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 62**
```python
            for row in csv.DictReader(source):
```
For each item from `csv.DictReader(source)`, name it `row` and run the indented body.

**Line 63**
```python
                truth = overrides.get(row["crop_path"], row["truth"])
```
Store the result in `truth`: call `overrides.get` with the inputs shown to obtain its result.

**Line 64**
```python
                if not truth or not row.get("crop_path"):
```
Run the indented branch only when `not truth or not row.get('crop_path')` is true.

**Line 65**
```python
                    continue
```
Skip the rest of this loop iteration and move to the next item.

**Line 66**
```python
                image = config.ROOT / row["crop_path"]
```
Store the result in `image`: calculate `config.ROOT / row['crop_path']`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 67**
```python
                if image.exists():
```
Run the indented branch only when `image.exists()` is true.

**Line 68**
```python
                    samples.append(PlateSample(str(image), (0, 0, 0, 0), truth,
```
Call `samples.append` with the inputs shown to obtain its result.

**Line 69**
```python
                                               "kaggle", f"kaggle:{row['group_id']}"))
```
Continuation of the statement starting at line 68; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 70**
```python
    return samples
```
Finish this function and evaluate `samples` using the values currently in memory; send that result to its caller.

**Line 71**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 72**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 73**
```python
def make_splits_v2(samples: list[PlateSample], path: Path = config.SPLITS_V2) -> dict[str, list[str]]:
```
Define `make_splits_v2`; its indented body runs when called. Keep every repeated vehicle/video group in one split.

**Line 74**
```python
    """Keep every repeated vehicle/video group in one split."""
```
Use the fixed value `'keep every repeated vehicle/video group in one split.'`.

**Line 75**
```python
    group_sizes = {}
```
Store the result in `group_sizes`: build a dictionary: each key names the value stored beside it.

**Line 76**
```python
    for sample in samples:
```
For each item from `samples`, name it `sample` and run the indented body.

**Line 77**
```python
        if sample.source == "kaggle":
```
Run the indented branch only when `sample.source == 'kaggle'` is true.

**Line 78**
```python
            key = sample.group_id or f"{sample.source}:{Path(sample.image_path).stem}"
```
Store the result in `key`: evaluate `sample.group_id or f'{sample.source}:{Path(sample.image_path).stem}'` using the values currently in memory.

**Line 79**
```python
            group_sizes[key] = group_sizes.get(key, 0) + 1
```
Store the result in `group_sizes[key]`: calculate `group_sizes.get(key, 0) + 1`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 80**
```python
    if not group_sizes:
```
Run the indented branch only when `not group_sizes` is true.

**Line 81**
```python
        raise ValueError("Reviewed Kaggle labels are required before making splits_v2.json")
```
Stop this operation with the shown exception and message, rather than silently continuing.

**Line 82**
```python
    rng = random.Random(config.SEED)
```
Store the result in `rng`: call `random.Random` with the inputs shown to obtain its result.

**Line 83**
```python
    groups = sorted(group_sizes)
```
Store the result in `groups`: call `sorted` with the inputs shown to obtain its result.

**Line 84**
```python
    rng.shuffle(groups)
```
Call `rng.shuffle` with the inputs shown to obtain its result.

**Line 85**
```python
    groups.sort(key=lambda group: group_sizes[group], reverse=True)
```
Call `groups.sort` with the inputs shown to obtain its result.

**Line 86**
```python
    fractions = {"train": 0.5, "calib": 0.2, "val": 0.15, "test": 0.15}
```
Store the result in `fractions`: build a dictionary: each key names the value stored beside it.

**Line 87**
```python
    splits = {name: [] for name in fractions}
```
Store the result in `splits`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 88**
```python
    counts = dict.fromkeys(fractions, 0)
```
Store the result in `counts`: call `dict.fromkeys` with the inputs shown to obtain its result.

**Line 89**
```python
    for group in groups:
```
For each item from `groups`, name it `group` and run the indented body.

**Line 90**
```python
        split = min(fractions, key=lambda name: counts[name] / fractions[name])
```
Store the result in `split`: call `min` with the inputs shown to obtain its result.

**Line 91**
```python
        splits[split].append(group)
```
Call `splits[split].append` with the inputs shown to obtain its result.

**Line 92**
```python
        counts[split] += group_sizes[group]
```
Update `counts[split]` using the operation shown and the new value.

**Line 93**
```python
    splits["cross_dataset_test"] = sorted({s.group_id for s in samples if s.source == "datacluster"})
```
Store the result in `splits['cross_dataset_test']`: call `sorted` with the inputs shown to obtain its result.

**Line 94**
```python
    path.write_text(json.dumps(splits, indent=2) + "\n")
```
Call `path.write_text` with the inputs shown to obtain its result.

**Line 95**
```python
    return splits
```
Finish this function and evaluate `splits` using the values currently in memory; send that result to its caller.

**Line 96**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 97**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 98**
```python
def crop(img, bbox):
```
Define `crop`; its indented body runs when called. Crop bbox out of image, honouring config.MIN_CROP_H (empty crop -> None).

**Line 99**
```python
    """Crop bbox out of image, honouring config.MIN_CROP_H (empty crop -> None)."""
```
Use the fixed value `'crop bbox out of image, honouring config.min_crop_h (empty crop -> none).'`.

**Line 100**
```python
    x1, y1, x2, y2 = bbox
```
Store the result in `(x1, y1, x2, y2)`: evaluate `bbox` using the values currently in memory.

**Line 101**
```python
    c = img[y1:y2, x1:x2]
```
Store the result in `c`: look up or slice `img` using the index or range in brackets.

**Line 102**
```python
    return None if c.size == 0 or c.shape[0] < config.MIN_CROP_H else c
```
Finish this function and choose the first value if `c.size == 0 or c.shape[0] < config.MIN_CROP_H` is true, otherwise choose the value after `else`; send that result to its caller.

## riskgate/engines/__init__.py

Package marker: allows this folder to hold importable modules.

Source SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

Empty package marker; there are no executable lines.

## riskgate/engines/easyocr_engine.py

Adapt EasyOCR output to the common EngineResult format and order text boxes.

Source SHA-256: `c8c5effb4ba3c73fee0336bc56883f45996d9f139c3e48d816c9555437f9113a`

**Line 1**
```python
import time
```
Make the named library tools available here: `import time`. Importing a project module makes its reusable functions accessible.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import cv2
```
Make the named library tools available here: `import cv2`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
import easyocr
```
Make the named library tools available here: `import easyocr`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python
import torch
```
Make the named library tools available here: `import torch`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 7**
```python
from riskgate import config
```
Make the named library tools available here: `from riskgate import config`. Importing a project module makes its reusable functions accessible.

**Line 8**
```python
from riskgate.contracts import EngineResult
```
Make the named library tools available here: `from riskgate.contracts import EngineResult`. Importing a project module makes its reusable functions accessible.

**Line 9**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 10**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 11**
```python
def order_boxes(boxes: list) -> list:
```
Define `order_boxes`; its indented body runs when called. Return EasyOCR results in reading order, grouping overlapping text rows.

**Line 12**
```python
    """Return EasyOCR results in reading order, grouping overlapping text rows."""
```
Use the fixed value `'return easyocr results in reading order, grouping overlapping text rows.'`.

**Line 13**
```python
    rows = []
```
Store the result in `rows`: evaluate `[]` using the values currently in memory.

**Line 14**
```python
    for box in sorted(boxes, key=lambda item: sum(p[1] for p in item[0]) / 4):
```
For each item from `sorted(boxes, key=lambda item: sum((p[1] for p in item[0])) / 4)`, name it `box` and run the indented body.

**Line 15**
```python
        ys = [p[1] for p in box[0]]
```
Store the result in `ys`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 16**
```python
        top, bottom = min(ys), max(ys)
```
Store the result in `(top, bottom)`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 17**
```python
        for row in rows:
```
For each item from `rows`, name it `row` and run the indented body.

**Line 18**
```python
            if min(bottom, row["bottom"]) - max(top, row["top"]) > 0.5 * min(bottom - top, row["bottom"] - row["top"]):
```
Run the indented branch only when `min(bottom, row['bottom']) - max(top, row['top']) > 0.5 * min(bottom - top, row['bottom'] - row['top'])` is true.

**Line 19**
```python
                row["boxes"].append(box)
```
Call `row['boxes'].append` with the inputs shown to obtain its result.

**Line 20**
```python
                row["top"] = min(top, row["top"])
```
Store the result in `row['top']`: call `min` with the inputs shown to obtain its result.

**Line 21**
```python
                row["bottom"] = max(bottom, row["bottom"])
```
Store the result in `row['bottom']`: call `max` with the inputs shown to obtain its result.

**Line 22**
```python
                break
```
Continue the enclosing Python statement using the syntax shown.

**Line 23**
```python
        else:
```
Run this branch when the associated condition was false.

**Line 24**
```python
            rows.append({"top": top, "bottom": bottom, "boxes": [box]})
```
Call `rows.append` with the inputs shown to obtain its result.

**Line 25**
```python
    return [box for row in sorted(rows, key=lambda r: r["top"])
```
Finish this function and build or iterate values using the inline `for` loop and any `if` filter shown; send that result to its caller.

**Line 26**
```python
            for box in sorted(row["boxes"], key=lambda item: min(p[0] for p in item[0]))]
```
Continuation of the statement starting at line 25; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 27**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 28**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 29**
```python
class EasyOCREngine:
```
Define the `EasyOCREngine` object type, grouping its data and methods.

**Line 30**
```python
    """Wraps easyocr on GPU. Flags are config-level, default off (task 7)."""
```
Use the fixed value `'wraps easyocr on gpu. flags are config-level, default off (task 7).'`.

**Line 31**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 32**
```python
    def __init__(self, upscale: bool = False, allowlist: bool = False):
```
Define `__init__`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 33**
```python
        device = "cuda" if torch.cuda.is_available() else "cpu"
```
Store the result in `device`: choose the first value if `torch.cuda.is_available()` is true, otherwise choose the value after `else`.

**Line 34**
```python
        if device == "cpu":
```
Run the indented branch only when `device == 'cpu'` is true.

**Line 35**
```python
            print("WARNING: expected cuda but got cpu - diagnose, do not silently continue")
```
Call `print` with the inputs shown to obtain its result.

**Line 36**
```python
        print(f"EasyOCREngine device: {device}")
```
Call `print` with the inputs shown to obtain its result.

**Line 37**
```python
        self.gpu_used = device == "cuda"
```
Store the result in `self.gpu_used`: check whether `device == 'cuda'` is true.

**Line 38**
```python
        self.upscale = upscale
```
Store the result in `self.upscale`: evaluate `upscale` using the values currently in memory.

**Line 39**
```python
        self.allowlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" if allowlist else None
```
Store the result in `self.allowlist`: choose the first value if `allowlist` is true, otherwise choose the value after `else`.

**Line 40**
```python
        self.reader = easyocr.Reader(["en"], gpu=self.gpu_used)
```
Store the result in `self.reader`: call `easyocr.Reader` with the inputs shown to obtain its result.

**Line 41**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 42**
```python
    def read(self, image) -> EngineResult:
```
Define `read`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 43**
```python
        try:
```
Try the indented work; matching failures are handled by the later `except` branch.

**Line 44**
```python
            if self.upscale:
```
Run the indented branch only when `self.upscale` is true.

**Line 45**
```python
                image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
```
Store the result in `image`: call `cv2.resize` with the inputs shown to obtain its result.

**Line 46**
```python
            t0 = time.perf_counter()
```
Store the result in `t0`: call `time.perf_counter` with the inputs shown to obtain its result.

**Line 47**
```python
            res = self.reader.readtext(image, allowlist=self.allowlist)
```
Store the result in `res`: call `self.reader.readtext` with the inputs shown to obtain its result.

**Line 48**
```python
            latency_ms = (time.perf_counter() - t0) * 1000
```
Store the result in `latency_ms`: calculate `(time.perf_counter() - t0) * 1000`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 49**
```python
            if not res:
```
Run the indented branch only when `not res` is true.

**Line 50**
```python
                return EngineResult("", 0.0, latency_ms, error="no text detected", boxes_found=0)
```
Finish this function and call `EngineResult` with the inputs shown to obtain its result; send that result to its caller.

**Line 51**
```python
            if config.MIN_CROP_H and image.shape[0] < config.MIN_CROP_H:
```
Run the indented branch only when `config.MIN_CROP_H and image.shape[0] < config.MIN_CROP_H` is true.

**Line 52**
```python
                return EngineResult("", 0.0, latency_ms, error="crop too small")
```
Finish this function and call `EngineResult` with the inputs shown to obtain its result; send that result to its caller.

**Line 53**
```python
            res = order_boxes(res)
```
Store the result in `res`: call `order_boxes` with the inputs shown to obtain its result.

**Line 54**
```python
            return EngineResult(
```
Finish this function and call `EngineResult` with the inputs shown to obtain its result; send that result to its caller.

**Line 55**
```python
                "".join(r[1] for r in res),
```
Continuation of the statement starting at line 54; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 56**
```python
                sum(r[2] for r in res) / len(res),
```
Continuation of the statement starting at line 54; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 57**
```python
                latency_ms,
```
Continuation of the statement starting at line 54; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 58**
```python
                boxes_found=len(res),
```
Continuation of the statement starting at line 54; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 59**
```python
            )
```
Continuation of the statement starting at line 54; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 60**
```python
        except (cv2.error, RuntimeError, ValueError, OSError) as e:
```
Handle the specified exception types using the indented recovery code.

**Line 61**
```python
            return EngineResult("", 0.0, 0.0, error=str(e)[:200])
```
Finish this function and call `EngineResult` with the inputs shown to obtain its result; send that result to its caller.

## riskgate/engines/fastplate_engine.py

Load the local ONNX plate reader and adapt its output.

Source SHA-256: `b610c6c934d3bc42ed1e6b94847100e3f130c9737f00e858f9a7cc24381e490a`

**Line 1**
```python
"""Small local ONNX plate reader used for a fair OCR comparison."""
```
Use the fixed value `'small local onnx plate reader used for a fair ocr comparison.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import time
```
Make the named library tools available here: `import time`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 5**
```python
import numpy as np
```
Make the named library tools available here: `import numpy as np`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python
from fast_plate_ocr import LicensePlateRecognizer
```
Make the named library tools available here: `from fast_plate_ocr import LicensePlateRecognizer`. Importing a project module makes its reusable functions accessible.

**Line 7**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 8**
```python
from riskgate import config
```
Make the named library tools available here: `from riskgate import config`. Importing a project module makes its reusable functions accessible.

**Line 9**
```python
from riskgate.contracts import EngineResult
```
Make the named library tools available here: `from riskgate.contracts import EngineResult`. Importing a project module makes its reusable functions accessible.

**Line 10**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 11**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 12**
```python
class FastPlateEngine:
```
Define the `FastPlateEngine` object type, grouping its data and methods.

**Line 13**
```python
    def __init__(self) -> None:
```
Define `__init__`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 14**
```python
        folder = config.ROOT / "weights/fastplate"
```
Store the result in `folder`: calculate `config.ROOT / 'weights/fastplate'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 15**
```python
        model = folder / "cct_s_v2_global.onnx"
```
Store the result in `model`: calculate `folder / 'cct_s_v2_global.onnx'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 16**
```python
        plate_config = folder / "cct_s_v2_global_plate_config.yaml"
```
Store the result in `plate_config`: calculate `folder / 'cct_s_v2_global_plate_config.yaml'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 17**
```python
        if model.exists() and plate_config.exists():
```
Run the indented branch only when `model.exists() and plate_config.exists()` is true.

**Line 18**
```python
            self.reader = LicensePlateRecognizer(onnx_model_path=model, plate_config_path=plate_config, device="cpu")
```
Store the result in `self.reader`: call `LicensePlateRecognizer` with the inputs shown to obtain its result.

**Line 19**
```python
        else:
```
Run this branch when the associated condition was false.

**Line 20**
```python
            self.reader = LicensePlateRecognizer("cct-s-v2-global-model", device="cpu")
```
Store the result in `self.reader`: call `LicensePlateRecognizer` with the inputs shown to obtain its result.

**Line 21**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 22**
```python
    def read(self, image: np.ndarray) -> EngineResult:
```
Define `read`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 23**
```python
        try:
```
Try the indented work; matching failures are handled by the later `except` branch.

**Line 24**
```python
            start = time.perf_counter()
```
Store the result in `start`: call `time.perf_counter` with the inputs shown to obtain its result.

**Line 25**
```python
            predictions = self.reader.run(image, return_confidence=True)
```
Store the result in `predictions`: call `self.reader.run` with the inputs shown to obtain its result.

**Line 26**
```python
            latency = (time.perf_counter() - start) * 1000
```
Store the result in `latency`: calculate `(time.perf_counter() - start) * 1000`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 27**
```python
            if not predictions:
```
Run the indented branch only when `not predictions` is true.

**Line 28**
```python
                return EngineResult("", 0.0, latency, error="no text detected")
```
Finish this function and call `EngineResult` with the inputs shown to obtain its result; send that result to its caller.

**Line 29**
```python
            prediction = predictions[0]
```
Store the result in `prediction`: look up or slice `predictions` using the index or range in brackets.

**Line 30**
```python
            confidence = float(np.mean(prediction.char_probs)) if len(prediction.char_probs) else 0.0
```
Store the result in `confidence`: choose the first value if `len(prediction.char_probs)` is true, otherwise choose the value after `else`.

**Line 31**
```python
            return EngineResult(prediction.plate, confidence, latency, boxes_found=1)
```
Finish this function and call `EngineResult` with the inputs shown to obtain its result; send that result to its caller.

**Line 32**
```python
        except (RuntimeError, ValueError, OSError) as error:
```
Handle the specified exception types using the indented recovery code.

**Line 33**
```python
            return EngineResult("", 0.0, 0.0, error=str(error)[:200])
```
Finish this function and call `EngineResult` with the inputs shown to obtain its result; send that result to its caller.

## riskgate/features.py

Turn the crop and OCR result into six numbers for calibration.

Source SHA-256: `56f21aac61cc69a50bb4767f945de8e9067b2d4148a4531cdea8b1a81b4e08e6`

**Line 1**
```python
"""Stable numeric signals for the correctness calibrator."""
```
Use the fixed value `'stable numeric signals for the correctness calibrator.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import numpy as np
```
Make the named library tools available here: `import numpy as np`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 5**
```python
from riskgate.contracts import EngineResult
```
Make the named library tools available here: `from riskgate.contracts import EngineResult`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python
from riskgate.grammar import classify
```
Make the named library tools available here: `from riskgate.grammar import classify`. Importing a project module makes its reusable functions accessible.

**Line 7**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 8**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 9**
```python
FEATURE_NAMES = ("raw_conf", "grammar", "text_length", "crop_height", "crop_width", "boxes_found")
```
Store the result in `FEATURE_NAMES`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 10**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 11**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 12**
```python
def plate_features(crop: np.ndarray, result: EngineResult) -> dict[str, float]:
```
Define `plate_features`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 13**
```python
    height, width = crop.shape[:2]
```
Store the result in `(height, width)`: look up or slice `crop.shape` using the index or range in brackets.

**Line 14**
```python
    return {"raw_conf": float(result.raw_conf),
```
Finish this function and build a dictionary: each key names the value stored beside it; send that result to its caller.

**Line 15**
```python
            "grammar": float({"INVALID": 0, "NONSTANDARD": 1, "VALID": 2}[classify(result.text)]),
```
Continuation of the statement starting at line 14; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 16**
```python
            "text_length": float(len(result.text)), "crop_height": float(height),
```
Continuation of the statement starting at line 14; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 17**
```python
            "crop_width": float(width), "boxes_found": float(result.boxes_found)}
```
Continuation of the statement starting at line 14; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

## riskgate/grammar.py

Check whether characters resemble a plate format; this cannot verify a real registration.

Source SHA-256: `241d7cdfecb3c3fa391fd4920f28fd6ecc667a7696ff68349c9b3a15d58eb919`

**Line 1**
```python
import re
```
Make the named library tools available here: `import re`. Importing a project module makes its reusable functions accessible.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
STANDARD = re.compile(r"^[A-Z]{2}\d{1,2}[A-Z]{0,3}\d{4}$")
```
Store the result in `STANDARD`: call `re.compile` with the inputs shown to obtain its result.

**Line 4**
```python
BH = re.compile(r"^\d{2}BH\d{4}[A-Z]{1,2}$")
```
Store the result in `BH`: call `re.compile` with the inputs shown to obtain its result.

**Line 5**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 6**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 7**
```python
def classify(text: str) -> str:
```
Define `classify`; its indented body runs when called. VALID (standard Indian format), NONSTANDARD (plate-like but off-format), INVALID (junk).

**Line 8**
```python
    """VALID (standard Indian format), NONSTANDARD (plate-like but off-format), INVALID (junk).
```
Use this fixed text block (presentation content, not model logic).

**Line 9**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 10**
```python
    # ponytail: NONSTANDARD/INVALID boundary is a heuristic (>=6 alnum with both letters
```
Comment for the reader; Python does not execute it. ponytail: NONSTANDARD/INVALID boundary is a heuristic (>=6 alnum with both letters

**Line 11**
```python
    # and digits); if a real licence plate catalogue shows up, replace with lookup.
```
Comment for the reader; Python does not execute it. and digits); if a real licence plate catalogue shows up, replace with lookup.

**Line 12**
```python
    """
```
Continuation of the statement starting at line 8; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 13**
```python
    t = re.sub(r"[^A-Z0-9]", "", (text or "").upper())
```
Store the result in `t`: call `re.sub` with the inputs shown to obtain its result.

**Line 14**
```python
    if STANDARD.match(t) or BH.match(t):
```
Run the indented branch only when `STANDARD.match(t) or BH.match(t)` is true.

**Line 15**
```python
        return "VALID"
```
Finish this function and use the fixed value `'VALID'`; send that result to its caller.

**Line 16**
```python
    if len(t) >= 6 and t.isalnum() and any(c.isdigit() for c in t) and any(c.isalpha() for c in t):
```
Run the indented branch only when `len(t) >= 6 and t.isalnum() and any((c.isdigit() for c in t)) and any((c.isalpha() for c in t))` is true.

**Line 17**
```python
        return "NONSTANDARD"
```
Finish this function and use the fixed value `'NONSTANDARD'`; send that result to its caller.

**Line 18**
```python
    return "INVALID"
```
Finish this function and use the fixed value `'INVALID'`; send that result to its caller.

## riskgate/metrics.py

Measure exact text matches, character errors, calibration, and error versus coverage.

Source SHA-256: `b4a3a760b2ee476e73841047b44f09fc78cefd7bcbe1cdd5430f6e76edd585ab`

**Line 1**
```python
import re
```
Make the named library tools available here: `import re`. Importing a project module makes its reusable functions accessible.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 4**
```python
def normalize(text: str) -> str:
```
Define `normalize`; its indented body runs when called. Uppercase, keep only A-Z and 0-9.

**Line 5**
```python
    """Uppercase, keep only A-Z and 0-9."""
```
Use the fixed value `'uppercase, keep only a-z and 0-9.'`.

**Line 6**
```python
    return re.sub(r"[^A-Z0-9]", "", (text or "").upper())
```
Finish this function and call `re.sub` with the inputs shown to obtain its result; send that result to its caller.

**Line 7**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 8**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 9**
```python
def exact_match(pred: str, truth: str) -> bool:
```
Define `exact_match`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 10**
```python
    return normalize(pred) == normalize(truth)
```
Finish this function and check whether `normalize(pred) == normalize(truth)` is true; send that result to its caller.

**Line 11**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 12**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 13**
```python
def cer(pred: str, truth: str) -> float:
```
Define `cer`; its indented body runs when called. CER = edit distance / len(truth). Always in [0, inf); sane equals converters -> tiny CER.

**Line 14**
```python
    """CER = edit distance / len(truth). Always in [0, inf); sane equals converters -> tiny CER.
```
Use this fixed text block (presentation content, not model logic).

**Line 15**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 16**
```python
    # ponytail: O(n*m) DP is fine at ~10 chars per plate
```
Comment for the reader; Python does not execute it. ponytail: O(n*m) DP is fine at ~10 chars per plate

**Line 17**
```python
    """
```
Continuation of the statement starting at line 14; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 18**
```python
    p, t = normalize(pred), normalize(truth)
```
Store the result in `(p, t)`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 19**
```python
    if not t:
```
Run the indented branch only when `not t` is true.

**Line 20**
```python
        return 0.0 if not p else 1.0
```
Finish this function and choose the first value if `not p` is true, otherwise choose the value after `else`; send that result to its caller.

**Line 21**
```python
    d = list(range(len(t) + 1))
```
Store the result in `d`: call `list` with the inputs shown to obtain its result.

**Line 22**
```python
    for i, cp in enumerate(p, 1):
```
For each item from `enumerate(p, 1)`, name it `(i, cp)` and run the indented body.

**Line 23**
```python
        prev, d[0] = d[0], i
```
Store the result in `(prev, d[0])`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 24**
```python
        for j, ct in enumerate(t, 1):
```
For each item from `enumerate(t, 1)`, name it `(j, ct)` and run the indented body.

**Line 25**
```python
            next_v = min(d[j] + 1, d[j - 1] + 1, prev + (cp != ct))
```
Store the result in `next_v`: call `min` with the inputs shown to obtain its result.

**Line 26**
```python
            prev, d[j] = d[j], next_v
```
Store the result in `(prev, d[j])`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 27**
```python
    return d[-1] / len(t)
```
Finish this function and calculate `d[-1] / len(t)`; `/` divides, `*` multiplies, and paths use `/` to join folders; send that result to its caller.

**Line 28**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 29**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 30**
```python
def ece(confs: list[float], corrects: list[bool], n_bins: int = 10) -> float:
```
Define `ece`; its indented body runs when called. Expected Calibration Error: sum over bins of weight * |accuracy - mean confidence|.

**Line 31**
```python
    """Expected Calibration Error: sum over bins of weight * |accuracy - mean confidence|."""
```
Use the fixed value `'expected calibration error: sum over bins of weight * |accuracy - mean confidence|.'`.

**Line 32**
```python
    assert len(confs) == len(corrects)
```
Check `len(confs) == len(corrects)`. If false, stop with an assertion error: the tested expectation failed.

**Line 33**
```python
    e = 0.0
```
Store the result in `e`: use the fixed value `0.0`.

**Line 34**
```python
    for b in range(n_bins):
```
For each item from `range(n_bins)`, name it `b` and run the indented body.

**Line 35**
```python
        idx = [i for i, c in enumerate(confs) if min(int(c * n_bins), n_bins - 1) == b]
```
Store the result in `idx`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 36**
```python
        if not idx:
```
Run the indented branch only when `not idx` is true.

**Line 37**
```python
            continue
```
Skip the rest of this loop iteration and move to the next item.

**Line 38**
```python
        acc = sum(corrects[i] for i in idx) / len(idx)
```
Store the result in `acc`: calculate `sum((corrects[i] for i in idx)) / len(idx)`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 39**
```python
        conf = sum(confs[i] for i in idx) / len(idx)
```
Store the result in `conf`: calculate `sum((confs[i] for i in idx)) / len(idx)`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 40**
```python
        e += len(idx) / len(confs) * abs(acc - conf)
```
Update `e` using the operation shown and the new value.

**Line 41**
```python
    return e
```
Finish this function and evaluate `e` using the values currently in memory; send that result to its caller.

**Line 42**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 43**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 44**
```python
def risk_coverage(confs: list[float], corrects: list[bool]) -> list[tuple[float, float]]:
```
Define `risk_coverage`; its indented body runs when called. Sort by confidence desc; after each new plate return (coverage, risk) = (k/N, error rate in top-k).

**Line 45**
```python
    """Sort by confidence desc; after each new plate return (coverage, risk) = (k/N, error rate in top-k)."""
```
Use the fixed value `'sort by confidence desc; after each new plate return (coverage, risk) = (k/n, error rate in top-k).'`.

**Line 46**
```python
    order = sorted(range(len(confs)), key=lambda i: confs[i], reverse=True)
```
Store the result in `order`: call `sorted` with the inputs shown to obtain its result.

**Line 47**
```python
    points, wrong = [], 0
```
Store the result in `(points, wrong)`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 48**
```python
    for k, i in enumerate(order, 1):
```
For each item from `enumerate(order, 1)`, name it `(k, i)` and run the indented body.

**Line 49**
```python
        wrong += not corrects[i]
```
Update `wrong` using the operation shown and the new value.

**Line 50**
```python
        points.append((k / len(confs), wrong / k))
```
Call `points.append` with the inputs shown to obtain its result.

**Line 51**
```python
    return points
```
Finish this function and evaluate `points` using the values currently in memory; send that result to its caller.

## riskgate/router.py

Choose validation thresholds and accept, escalate, or review a reading.

Source SHA-256: `b6aac406a58695eea3ba63f6c93ef581ce5da57b80ffd428374dd5c82991ab04`

**Line 1**
```python
"""Selective routing with a Wilson upper error bound."""
```
Use the fixed value `'selective routing with a wilson upper error bound.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import math
```
Make the named library tools available here: `import math`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 5**
```python
from riskgate.grammar import classify
```
Make the named library tools available here: `from riskgate.grammar import classify`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 7**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 8**
```python
TARGETS = (0.02, 0.05, 0.10)
```
Store the result in `TARGETS`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 9**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 10**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 11**
```python
def wilson_interval(errors: int, total: int, z: float = 1.96) -> tuple[float, float]:
```
Define `wilson_interval`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 12**
```python
    if total == 0:
```
Run the indented branch only when `total == 0` is true.

**Line 13**
```python
        return (0.0, 1.0)
```
Finish this function and collect the values in order (a tuple), which can also be unpacked into separate names; send that result to its caller.

**Line 14**
```python
    p = errors / total
```
Store the result in `p`: calculate `errors / total`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 15**
```python
    denom = 1 + z * z / total
```
Store the result in `denom`: calculate `1 + z * z / total`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 16**
```python
    center = (p + z * z / (2 * total)) / denom
```
Store the result in `center`: calculate `(p + z * z / (2 * total)) / denom`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 17**
```python
    radius = z * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / denom
```
Store the result in `radius`: calculate `z * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / denom`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 18**
```python
    return max(0.0, center - radius), min(1.0, center + radius)
```
Finish this function and collect the values in order (a tuple), which can also be unpacked into separate names; send that result to its caller.

**Line 19**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 20**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 21**
```python
def choose_thresholds(rows: list[dict], review_below: float = 0.3) -> dict[str, dict]:
```
Define `choose_thresholds`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 22**
```python
    eligible = sorted((r for r in rows if classify(r["pred"]) != "INVALID"),
```
Store the result in `eligible`: call `sorted` with the inputs shown to obtain its result.

**Line 23**
```python
                      key=lambda r: float(r["calibrated_conf"]), reverse=True)
```
Continuation of the statement starting at line 22; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 24**
```python
    result = {}
```
Store the result in `result`: build a dictionary: each key names the value stored beside it.

**Line 25**
```python
    for target in TARGETS:
```
For each item from `TARGETS`, name it `target` and run the indented body.

**Line 26**
```python
        chosen = None
```
Store the result in `chosen`: use the fixed value `None`.

**Line 27**
```python
        for i, row in enumerate(eligible):
```
For each item from `enumerate(eligible)`, name it `(i, row)` and run the indented body.

**Line 28**
```python
            conf = float(row["calibrated_conf"])
```
Store the result in `conf`: call `float` with the inputs shown to obtain its result.

**Line 29**
```python
            if i + 1 < len(eligible) and float(eligible[i + 1]["calibrated_conf"]) == conf:
```
Run the indented branch only when `i + 1 < len(eligible) and float(eligible[i + 1]['calibrated_conf']) == conf` is true.

**Line 30**
```python
                continue
```
Skip the rest of this loop iteration and move to the next item.

**Line 31**
```python
            accepted = eligible[:i + 1]
```
Store the result in `accepted`: look up or slice `eligible` using the index or range in brackets.

**Line 32**
```python
            errors = sum(not int(r["ok"]) for r in accepted)
```
Store the result in `errors`: call `sum` with the inputs shown to obtain its result.

**Line 33**
```python
            if wilson_interval(errors, len(accepted))[1] <= target:
```
Run the indented branch only when `wilson_interval(errors, len(accepted))[1] <= target` is true.

**Line 34**
```python
                chosen = conf
```
Store the result in `chosen`: evaluate `conf` using the values currently in memory.

**Line 35**
```python
        result[f"{target:.2f}"] = {"accept_at": chosen, "review_below": review_below}
```
Store the result in `result[f'{target:.2f}']`: build a dictionary: each key names the value stored beside it.

**Line 36**
```python
    return result
```
Finish this function and evaluate `result` using the values currently in memory; send that result to its caller.

**Line 37**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 38**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 39**
```python
def route(text: str, confidence: float, thresholds: dict) -> str:
```
Define `route`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 40**
```python
    if classify(text) != "INVALID" and thresholds["accept_at"] is not None and confidence >= thresholds["accept_at"]:
```
Run the indented branch only when `classify(text) != 'INVALID' and thresholds['accept_at'] is not None and (confidence >= thresholds['accept_at'])` is true.

**Line 41**
```python
        return "ACCEPT"
```
Finish this function and use the fixed value `'ACCEPT'`; send that result to its caller.

**Line 42**
```python
    return "REVIEW" if confidence < thresholds["review_below"] else "ESCALATE"
```
Finish this function and choose the first value if `confidence < thresholds['review_below']` is true, otherwise choose the value after `else`; send that result to its caller.

## riskgate/stability.py

Run two transformed-image reads and veto acceptance when either disagrees.

Source SHA-256: `243094f1943cbfcf994a841cefcc83336676eca76eaa9159e8b8cd0007d0eab8`

**Line 1**
```python
"""An additional review veto; agreement is evidence, never a probability."""
```
Use the fixed value `'an additional review veto; agreement is evidence, never a probability.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
from collections.abc import Callable
```
Make the named library tools available here: `from collections.abc import Callable`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
from time import perf_counter
```
Make the named library tools available here: `from time import perf_counter`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 6**
```python
import cv2
```
Make the named library tools available here: `import cv2`. Importing a project module makes its reusable functions accessible.

**Line 7**
```python
import numpy as np
```
Make the named library tools available here: `import numpy as np`. Importing a project module makes its reusable functions accessible.

**Line 8**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 9**
```python
from riskgate.contracts import EngineResult
```
Make the named library tools available here: `from riskgate.contracts import EngineResult`. Importing a project module makes its reusable functions accessible.

**Line 10**
```python
from riskgate.metrics import normalize
```
Make the named library tools available here: `from riskgate.metrics import normalize`. Importing a project module makes its reusable functions accessible.

**Line 11**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 12**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 13**
```python
def check_stability(crop: np.ndarray, original: str,
```
Define `check_stability`; its indented body runs when called. Read two fixed, mild transformations without changing the original answer.

**Line 14**
```python
                    read: Callable[[np.ndarray], EngineResult]) -> dict:
```
Continuation of the statement starting at line 13; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 15**
```python
    """Read two fixed, mild transformations without changing the original answer."""
```
Use the fixed value `'read two fixed, mild transformations without changing the original answer.'`.

**Line 16**
```python
    if crop.size == 0:
```
Run the indented branch only when `crop.size == 0` is true.

**Line 17**
```python
        raise ValueError("Cannot check an empty crop")
```
Stop this operation with the shown exception and message, rather than silently continuing.

**Line 18**
```python
    start = perf_counter()
```
Store the result in `start`: call `perf_counter` with the inputs shown to obtain its result.

**Line 19**
```python
    # Fixed before evaluation: no searching for a transformation that looks correct.
```
Comment for the reader; Python does not execute it. Fixed before evaluation: no searching for a transformation that looks correct.

**Line 20**
```python
    variants = {
```
Store the result in `variants`: build a dictionary: each key names the value stored beside it.

**Line 21**
```python
        "resize_125": cv2.resize(crop, None, fx=1.25, fy=1.25, interpolation=cv2.INTER_CUBIC),
```
Continuation of the statement starting at line 20; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 22**
```python
        "brightness_110": np.clip(crop.astype(np.float32) * 1.10, 0, 255).astype(np.uint8),
```
Continuation of the statement starting at line 20; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 23**
```python
    }
```
Continuation of the statement starting at line 20; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 24**
```python
    original = normalize(original)
```
Store the result in `original`: uppercase the text and keep only letters A–Z and digits 0–9.

**Line 25**
```python
    readings = []
```
Store the result in `readings`: evaluate `[]` using the values currently in memory.

**Line 26**
```python
    for name, image in variants.items():
```
For each item from `variants.items()`, name it `(name, image)` and run the indented body.

**Line 27**
```python
        result = read(image)
```
Store the result in `result`: call `read` with the inputs shown to obtain its result.

**Line 28**
```python
        text = normalize(result.text)
```
Store the result in `text`: uppercase the text and keep only letters A–Z and digits 0–9.

**Line 29**
```python
        readings.append({"variant": name, "text": text, "error": result.error,
```
Call `readings.append` with the inputs shown to obtain its result.

**Line 30**
```python
                         "matches_original": bool(original and text == original and not result.error)})
```
Continuation of the statement starting at line 29; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 31**
```python
    stable = all(row["matches_original"] for row in readings)
```
Store the result in `stable`: call `all` with the inputs shown to obtain its result.

**Line 32**
```python
    return {"stable": stable, "matching_variants": sum(row["matches_original"] for row in readings),
```
Finish this function and build a dictionary: each key names the value stored beside it; send that result to its caller.

**Line 33**
```python
            "variant_count": len(readings), "readings": readings,
```
Continuation of the statement starting at line 32; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 34**
```python
            "extra_latency_ms": (perf_counter() - start) * 1000}
```
Continuation of the statement starting at line 32; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 35**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 36**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 37**
```python
def apply_veto(decision: str, evidence: dict) -> str:
```
Define `apply_veto`; its indented body runs when called. Only remove acceptance. Never promote a review or replace plate characters.

**Line 38**
```python
    """Only remove acceptance. Never promote a review or replace plate characters."""
```
Use the fixed value `'only remove acceptance. never promote a review or replace plate characters.'`.

**Line 39**
```python
    return "REVIEW" if decision == "ACCEPT" and not evidence["stable"] else decision
```
Finish this function and choose the first value if `decision == 'ACCEPT' and (not evidence['stable'])` is true, otherwise choose the value after `else`; send that result to its caller.

## scripts/baseline_v2.py

Compare readers on labelled crops and record predictions and features.

Source SHA-256: `b36ba62afe6317ff2131e3e0fa80103e4e95e45a65d85f6da5c94a244dd7ddbc`

**Line 1**
```python
"""Compare two local readers on identical crops, then freeze one on train data."""
```
Use the fixed value `'compare two local readers on identical crops, then freeze one on train data.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import csv
```
Make the named library tools available here: `import csv`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
import json
```
Make the named library tools available here: `import json`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 6**
```python
import cv2
```
Make the named library tools available here: `import cv2`. Importing a project module makes its reusable functions accessible.

**Line 7**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 8**
```python
from riskgate import config
```
Make the named library tools available here: `from riskgate import config`. Importing a project module makes its reusable functions accessible.

**Line 9**
```python
from riskgate.data import crop, load_all_samples, make_splits_v2
```
Make the named library tools available here: `from riskgate.data import crop, load_all_samples, make_splits_v2`. Importing a project module makes its reusable functions accessible.

**Line 10**
```python
from riskgate.engines.easyocr_engine import EasyOCREngine
```
Make the named library tools available here: `from riskgate.engines.easyocr_engine import EasyOCREngine`. Importing a project module makes its reusable functions accessible.

**Line 11**
```python
from riskgate.engines.fastplate_engine import FastPlateEngine
```
Make the named library tools available here: `from riskgate.engines.fastplate_engine import FastPlateEngine`. Importing a project module makes its reusable functions accessible.

**Line 12**
```python
from riskgate.features import plate_features
```
Make the named library tools available here: `from riskgate.features import plate_features`. Importing a project module makes its reusable functions accessible.

**Line 13**
```python
from riskgate.metrics import cer, exact_match, normalize
```
Make the named library tools available here: `from riskgate.metrics import cer, exact_match, normalize`. Importing a project module makes its reusable functions accessible.

**Line 14**
```python
from riskgate.router import wilson_interval
```
Make the named library tools available here: `from riskgate.router import wilson_interval`. Importing a project module makes its reusable functions accessible.

**Line 15**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 16**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 17**
```python
def write_csv(path, rows: list[dict]) -> None:
```
Define `write_csv`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 18**
```python
    with path.open("w", newline="") as output:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 19**
```python
        writer = csv.DictWriter(output, fieldnames=list(rows[0]))
```
Store the result in `writer`: call `csv.DictWriter` with the inputs shown to obtain its result.

**Line 20**
```python
        writer.writeheader()
```
Call `writer.writeheader` with the inputs shown to obtain its result.

**Line 21**
```python
        writer.writerows(rows)
```
Call `writer.writerows` with the inputs shown to obtain its result.

**Line 22**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 23**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 24**
```python
def main() -> None:
```
Define `main`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 25**
```python
    samples = load_all_samples()
```
Store the result in `samples`: call `load_all_samples` with the inputs shown to obtain its result.

**Line 26**
```python
    splits = make_splits_v2(samples)
```
Store the result in `splits`: call `make_splits_v2` with the inputs shown to obtain its result.

**Line 27**
```python
    owner = {group: split for split, groups in splits.items() for group in groups}
```
Store the result in `owner`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 28**
```python
    config.RESULTS_DIR.mkdir(exist_ok=True)
```
Call `config.results_dir.mkdir` with the inputs shown to obtain its result.

**Line 29**
```python
    readers = {"EasyOCR": EasyOCREngine(config.READER_UPSCALE, config.READER_ALLOWLIST),
```
Store the result in `readers`: build a dictionary: each key names the value stored beside it.

**Line 30**
```python
               "FastPlateOCR": FastPlateEngine()}
```
Continuation of the statement starting at line 29; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 31**
```python
    rows = []
```
Store the result in `rows`: evaluate `[]` using the values currently in memory.

**Line 32**
```python
    for index, sample in enumerate(samples, 1):
```
For each item from `enumerate(samples, 1)`, name it `(index, sample)` and run the indented body.

**Line 33**
```python
        image = cv2.imread(sample.image_path)
```
Store the result in `image`: call `cv2.imread` with the inputs shown to obtain its result.

**Line 34**
```python
        if image is None:
```
Run the indented branch only when `image is None` is true.

**Line 35**
```python
            continue
```
Skip the rest of this loop iteration and move to the next item.

**Line 36**
```python
        plate = image if sample.source == "kaggle" else crop(image, sample.bbox)
```
Store the result in `plate`: choose the first value if `sample.source == 'kaggle'` is true, otherwise choose the value after `else`.

**Line 37**
```python
        if plate is None:
```
Run the indented branch only when `plate is None` is true.

**Line 38**
```python
            continue
```
Skip the rest of this loop iteration and move to the next item.

**Line 39**
```python
        for name, reader in readers.items():
```
For each item from `readers.items()`, name it `(name, reader)` and run the indented body.

**Line 40**
```python
            result = reader.read(plate)
```
Store the result in `result`: call `reader.read` with the inputs shown to obtain its result.

**Line 41**
```python
            pred = normalize(result.text)
```
Store the result in `pred`: uppercase the text and keep only letters A–Z and digits 0–9.

**Line 42**
```python
            rows.append({"image": sample.image_path, "group_id": sample.group_id,
```
Call `rows.append` with the inputs shown to obtain its result.

**Line 43**
```python
                         "source": sample.source, "split": owner[sample.group_id],
```
Continuation of the statement starting at line 42; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 44**
```python
                         "reader": name, "truth": normalize(sample.truth), "pred": pred,
```
Continuation of the statement starting at line 42; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 45**
```python
                         "ok": int(exact_match(pred, sample.truth)), "cer": cer(pred, sample.truth),
```
Continuation of the statement starting at line 42; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 46**
```python
                         "latency_ms": result.latency_ms, **plate_features(plate, result)})
```
Continuation of the statement starting at line 42; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 47**
```python
        if index % 100 == 0:
```
Run the indented branch only when `index % 100 == 0` is true.

**Line 48**
```python
            print(f"Read {index}/{len(samples)} plates", flush=True)
```
Call `print` with the inputs shown to obtain its result.

**Line 49**
```python
    write_csv(config.RESULTS_DIR / "ocr_comparison.csv", rows)
```
Call `write_csv` with the inputs shown to obtain its result.

**Line 50**
```python
    train = [row for row in rows if row["split"] == "train"]
```
Store the result in `train`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 51**
```python
    chosen = min(readers, key=lambda name: (-sum(row["ok"] for row in train if row["reader"] == name),
```
Store the result in `chosen`: call `min` with the inputs shown to obtain its result.

**Line 52**
```python
                                             sum(row["cer"] for row in train if row["reader"] == name)))
```
Continuation of the statement starting at line 51; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 53**
```python
    selected = [row for row in rows if row["reader"] == chosen]
```
Store the result in `selected`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 54**
```python
    write_csv(config.RESULTS_DIR / "baseline_v2.csv", selected)
```
Call `write_csv` with the inputs shown to obtain its result.

**Line 55**
```python
    (config.RESULTS_DIR / "selected_reader.json").write_text(json.dumps({"reader": chosen}, indent=2) + "\n")
```
Call `(config.results_dir / 'selected_reader.json').write_text` with the inputs shown to obtain its result.

**Line 56**
```python
    lines = [f"Chosen on train split: {chosen}",
```
Store the result in `lines`: evaluate `[f'Chosen on train split: {chosen}', 'Reader | Split | Source | n | Exact | 95% Wilson interval | Mean CER | Mean latency ms', '--- | --- | --- | ---: | ---: | --- | ---: | ---:']` using the values currently in memory.

**Line 57**
```python
             "Reader | Split | Source | n | Exact | 95% Wilson interval | Mean CER | Mean latency ms",
```
Continuation of the statement starting at line 56; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 58**
```python
             "--- | --- | --- | ---: | ---: | --- | ---: | ---:"]
```
Continuation of the statement starting at line 56; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 59**
```python
    for name in readers:
```
For each item from `readers`, name it `name` and run the indented body.

**Line 60**
```python
        for split in splits:
```
For each item from `splits`, name it `split` and run the indented body.

**Line 61**
```python
            subset = [row for row in rows if row["reader"] == name and row["split"] == split]
```
Store the result in `subset`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 62**
```python
            if not subset:
```
Run the indented branch only when `not subset` is true.

**Line 63**
```python
                continue
```
Skip the rest of this loop iteration and move to the next item.

**Line 64**
```python
            n, good = len(subset), sum(row["ok"] for row in subset)
```
Store the result in `(n, good)`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 65**
```python
            lo, hi = wilson_interval(n - good, n)
```
Store the result in `(lo, hi)`: call `wilson_interval` with the inputs shown to obtain its result.

**Line 66**
```python
            lines.append(f"{name} | {split} | {subset[0]['source']} | {n} | {good/n:.3f} | "
```
Call `lines.append` with the inputs shown to obtain its result.

**Line 67**
```python
                         f"[{1-hi:.3f}, {1-lo:.3f}] | {sum(row['cer'] for row in subset)/n:.3f} | "
```
Continuation of the statement starting at line 66; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 68**
```python
                         f"{sum(row['latency_ms'] for row in subset)/n:.1f}")
```
Continuation of the statement starting at line 66; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 69**
```python
    (config.RESULTS_DIR / "baseline_v2_summary.txt").write_text("\n".join(lines) + "\n")
```
Call `(config.results_dir / 'baseline_v2_summary.txt').write_text` with the inputs shown to obtain its result.

**Line 70**
```python
    print("\n".join(lines))
```
Call `print` with the inputs shown to obtain its result.

**Line 71**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 72**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 73**
```python
if __name__ == "__main__":
```
Run the indented branch only when `__name__ == '__main__'` is true.

**Line 74**
```python
    main()
```
Call `main` with the inputs shown to obtain its result.

## scripts/detector.py

Prepare YOLO box labels, fine-tune the detector, and measure box overlap.

Source SHA-256: `eb792d6bd2fce45b1f69a163f1cb8584d5839ecf7cf28f83b86cdd1ea3f510c8`

**Line 1**
```python
"""Train and evaluate a small full-image plate detector on the grouped split."""
```
Use the fixed value `'train and evaluate a small full-image plate detector on the grouped split.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import argparse
```
Make the named library tools available here: `import argparse`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
import csv
```
Make the named library tools available here: `import csv`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python
import json
```
Make the named library tools available here: `import json`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python
import shutil
```
Make the named library tools available here: `import shutil`. Importing a project module makes its reusable functions accessible.

**Line 7**
```python
from pathlib import Path
```
Make the named library tools available here: `from pathlib import Path`. Importing a project module makes its reusable functions accessible.

**Line 8**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 9**
```python
import cv2
```
Make the named library tools available here: `import cv2`. Importing a project module makes its reusable functions accessible.

**Line 10**
```python
from ultralytics import YOLO
```
Make the named library tools available here: `from ultralytics import YOLO`. Importing a project module makes its reusable functions accessible.

**Line 11**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 12**
```python
from riskgate import config
```
Make the named library tools available here: `from riskgate import config`. Importing a project module makes its reusable functions accessible.

**Line 13**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 14**
```python
MANIFEST = config.ROOT / "data/indian_manifest.csv"
```
Store the result in `MANIFEST`: calculate `config.ROOT / 'data/indian_manifest.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 15**
```python
DATASET = config.ROOT / "data/yolo"
```
Store the result in `DATASET`: calculate `config.ROOT / 'data/yolo'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 16**
```python
WEIGHTS = config.ROOT / "weights/plate_detector.pt"
```
Store the result in `WEIGHTS`: calculate `config.ROOT / 'weights/plate_detector.pt'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 17**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 18**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 19**
```python
def load_rows() -> list[dict]:
```
Define `load_rows`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 20**
```python
    with MANIFEST.open(newline="") as source:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 21**
```python
        return list(csv.DictReader(source))
```
Finish this function and call `list` with the inputs shown to obtain its result; send that result to its caller.

**Line 22**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 23**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 24**
```python
def box_to_yolo(row: dict, width: int, height: int) -> str:
```
Define `box_to_yolo`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 25**
```python
    x1, y1, x2, y2 = (float(row[key]) for key in ("xmin", "ymin", "xmax", "ymax"))
```
Store the result in `(x1, y1, x2, y2)`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 26**
```python
    return f"0 {(x1+x2)/(2*width):.6f} {(y1+y2)/(2*height):.6f} {(x2-x1)/width:.6f} {(y2-y1)/height:.6f}\n"
```
Finish this function and evaluate `f'0 {(x1 + x2) / (2 * width):.6f} {(y1 + y2) / (2 * height):.6f} {(x2 - x1) / width:.6f} {(y2 - y1) / height:.6f}\n'` using the values currently in memory; send that result to its caller.

**Line 27**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 28**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 29**
```python
def prepare() -> dict:
```
Define `prepare`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 30**
```python
    splits = json.loads(config.SPLITS_V2.read_text())
```
Store the result in `splits`: call `json.loads` with the inputs shown to obtain its result.

**Line 31**
```python
    owner = {group: split for split, groups in splits.items() for group in groups}
```
Store the result in `owner`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 32**
```python
    counts = {split: 0 for split in ("train", "val", "test")}
```
Store the result in `counts`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 33**
```python
    for index, row in enumerate(load_rows()):
```
For each item from `enumerate(load_rows())`, name it `(index, row)` and run the indented body.

**Line 34**
```python
        split = owner["kaggle:" + row["group_id"]]
```
Store the result in `split`: look up or slice `owner` using the index or range in brackets.

**Line 35**
```python
        if split not in counts:
```
Run the indented branch only when `split not in counts` is true.

**Line 36**
```python
            continue
```
Skip the rest of this loop iteration and move to the next item.

**Line 37**
```python
        image_path = config.ROOT / row["image_path"]
```
Store the result in `image_path`: calculate `config.ROOT / row['image_path']`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 38**
```python
        image = cv2.imread(str(image_path))
```
Store the result in `image`: call `cv2.imread` with the inputs shown to obtain its result.

**Line 39**
```python
        if image is None:
```
Run the indented branch only when `image is None` is true.

**Line 40**
```python
            continue
```
Skip the rest of this loop iteration and move to the next item.

**Line 41**
```python
        height, width = image.shape[:2]
```
Store the result in `(height, width)`: look up or slice `image.shape` using the index or range in brackets.

**Line 42**
```python
        image_dir = DATASET / "images" / split
```
Store the result in `image_dir`: calculate `DATASET / 'images' / split`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 43**
```python
        label_dir = DATASET / "labels" / split
```
Store the result in `label_dir`: calculate `DATASET / 'labels' / split`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 44**
```python
        image_dir.mkdir(parents=True, exist_ok=True)
```
Call `image_dir.mkdir` with the inputs shown to obtain its result.

**Line 45**
```python
        label_dir.mkdir(parents=True, exist_ok=True)
```
Call `label_dir.mkdir` with the inputs shown to obtain its result.

**Line 46**
```python
        name = f"plate_{index:04d}"
```
Store the result in `name`: evaluate `f'plate_{index:04d}'` using the values currently in memory.

**Line 47**
```python
        link = image_dir / f"{name}{image_path.suffix.lower()}"
```
Store the result in `link`: calculate `image_dir / f'{name}{image_path.suffix.lower()}'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 48**
```python
        if not link.exists():
```
Run the indented branch only when `not link.exists()` is true.

**Line 49**
```python
            link.symlink_to(image_path)
```
Call `link.symlink_to` with the inputs shown to obtain its result.

**Line 50**
```python
        (label_dir / f"{name}.txt").write_text(box_to_yolo(row, width, height))
```
Call `(label_dir / f'{name}.txt').write_text` with the inputs shown to obtain its result.

**Line 51**
```python
        counts[split] += 1
```
Update `counts[split]` using the operation shown and the new value.

**Line 52**
```python
    (DATASET / "dataset.yaml").write_text(
```
Call `(dataset / 'dataset.yaml').write_text` with the inputs shown to obtain its result.

**Line 53**
```python
        f"path: {DATASET}\ntrain: images/train\nval: images/val\ntest: images/test\nnames:\n  0: license_plate\n"
```
Continuation of the statement starting at line 52; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 54**
```python
    )
```
Continuation of the statement starting at line 52; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 55**
```python
    return counts
```
Finish this function and evaluate `counts` using the values currently in memory; send that result to its caller.

**Line 56**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 57**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 58**
```python
def overlap(a: tuple[float, ...], b: tuple[float, ...]) -> float:
```
Define `overlap`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 59**
```python
    left, top = max(a[0], b[0]), max(a[1], b[1])
```
Store the result in `(left, top)`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 60**
```python
    right, bottom = min(a[2], b[2]), min(a[3], b[3])
```
Store the result in `(right, bottom)`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 61**
```python
    intersection = max(0, right-left) * max(0, bottom-top)
```
Store the result in `intersection`: calculate `max(0, right - left) * max(0, bottom - top)`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 62**
```python
    area_a = max(0, a[2]-a[0]) * max(0, a[3]-a[1])
```
Store the result in `area_a`: calculate `max(0, a[2] - a[0]) * max(0, a[3] - a[1])`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 63**
```python
    area_b = max(0, b[2]-b[0]) * max(0, b[3]-b[1])
```
Store the result in `area_b`: calculate `max(0, b[2] - b[0]) * max(0, b[3] - b[1])`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 64**
```python
    return intersection / (area_a + area_b - intersection) if area_a + area_b > intersection else 0.0
```
Finish this function and choose the first value if `area_a + area_b > intersection` is true, otherwise choose the value after `else`; send that result to its caller.

**Line 65**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 66**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 67**
```python
def evaluate(model: YOLO) -> dict:
```
Define `evaluate`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 68**
```python
    splits = json.loads(config.SPLITS_V2.read_text())
```
Store the result in `splits`: call `json.loads` with the inputs shown to obtain its result.

**Line 69**
```python
    test = set(splits["test"])
```
Store the result in `test`: call `set` with the inputs shown to obtain its result.

**Line 70**
```python
    rows = [row for row in load_rows() if "kaggle:" + row["group_id"] in test]
```
Store the result in `rows`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 71**
```python
    found, correct, predictions = 0, 0, 0
```
Store the result in `(found, correct, predictions)`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 72**
```python
    details = []
```
Store the result in `details`: evaluate `[]` using the values currently in memory.

**Line 73**
```python
    for row in rows:
```
For each item from `rows`, name it `row` and run the indented body.

**Line 74**
```python
        result = model.predict(str(config.ROOT / row["image_path"]), conf=0.25, verbose=False)[0]
```
Store the result in `result`: look up or slice `model.predict(str(config.ROOT / row['image_path']), conf=0.25, verbose=False)` using the index or range in brackets.

**Line 75**
```python
        boxes = [tuple(float(v) for v in box.xyxy[0].tolist()) for box in result.boxes]
```
Store the result in `boxes`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 76**
```python
        predictions += len(boxes)
```
Update `predictions` using the operation shown and the new value.

**Line 77**
```python
        truth = tuple(float(row[key]) for key in ("xmin", "ymin", "xmax", "ymax"))
```
Store the result in `truth`: call `tuple` with the inputs shown to obtain its result.

**Line 78**
```python
        best = max((overlap(box, truth) for box in boxes), default=0.0)
```
Store the result in `best`: call `max` with the inputs shown to obtain its result.

**Line 79**
```python
        found += bool(boxes)
```
Update `found` using the operation shown and the new value.

**Line 80**
```python
        correct += best >= 0.5
```
Update `correct` using the operation shown and the new value.

**Line 81**
```python
        details.append({"image": row["image_path"], "truth": row["truth"],
```
Call `details.append` with the inputs shown to obtain its result.

**Line 82**
```python
                        "found": bool(boxes), "matched_iou_05": best >= 0.5, "best_iou": round(best, 3)})
```
Continuation of the statement starting at line 81; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 83**
```python
    report = {"test_images": len(rows), "boxes_predicted": predictions,
```
Store the result in `report`: build a dictionary: each key names the value stored beside it.

**Line 84**
```python
              "images_with_detection": found, "matched_at_iou_05": correct,
```
Continuation of the statement starting at line 83; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 85**
```python
              "recall_at_iou_05": correct / len(rows),
```
Continuation of the statement starting at line 83; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 86**
```python
              "precision_at_iou_05": correct / predictions if predictions else 0.0}
```
Continuation of the statement starting at line 83; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 87**
```python
    config.RESULTS_DIR.mkdir(exist_ok=True)
```
Call `config.results_dir.mkdir` with the inputs shown to obtain its result.

**Line 88**
```python
    (config.RESULTS_DIR / "detector_test.json").write_text(json.dumps(report, indent=2) + "\n")
```
Call `(config.results_dir / 'detector_test.json').write_text` with the inputs shown to obtain its result.

**Line 89**
```python
    with (config.RESULTS_DIR / "detector_test_details.csv").open("w", newline="") as output:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 90**
```python
        writer = csv.DictWriter(output, fieldnames=list(details[0]))
```
Store the result in `writer`: call `csv.DictWriter` with the inputs shown to obtain its result.

**Line 91**
```python
        writer.writeheader()
```
Call `writer.writeheader` with the inputs shown to obtain its result.

**Line 92**
```python
        writer.writerows(details)
```
Call `writer.writerows` with the inputs shown to obtain its result.

**Line 93**
```python
    return report
```
Finish this function and evaluate `report` using the values currently in memory; send that result to its caller.

**Line 94**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 95**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 96**
```python
def main() -> None:
```
Define `main`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 97**
```python
    parser = argparse.ArgumentParser()
```
Store the result in `parser`: call `argparse.ArgumentParser` with the inputs shown to obtain its result.

**Line 98**
```python
    parser.add_argument("mode", choices=("prepare", "train", "evaluate"))
```
Call `parser.add_argument` with the inputs shown to obtain its result.

**Line 99**
```python
    parser.add_argument("--epochs", type=int, default=15)
```
Call `parser.add_argument` with the inputs shown to obtain its result.

**Line 100**
```python
    parser.add_argument("--start-from", default=str(config.YOLO_START))
```
Call `parser.add_argument` with the inputs shown to obtain its result.

**Line 101**
```python
    parser.add_argument("--name", default="detector_training")
```
Call `parser.add_argument` with the inputs shown to obtain its result.

**Line 102**
```python
    args = parser.parse_args()
```
Store the result in `args`: call `parser.parse_args` with the inputs shown to obtain its result.

**Line 103**
```python
    if args.mode == "prepare":
```
Run the indented branch only when `args.mode == 'prepare'` is true.

**Line 104**
```python
        print(json.dumps(prepare(), indent=2))
```
Call `print` with the inputs shown to obtain its result.

**Line 105**
```python
    elif args.mode == "train":
```
Run the indented branch only when `args.mode == 'train'` is true.

**Line 106**
```python
        if not (DATASET / "dataset.yaml").exists():
```
Run the indented branch only when `not (DATASET / 'dataset.yaml').exists()` is true.

**Line 107**
```python
            prepare()
```
Call `prepare` with the inputs shown to obtain its result.

**Line 108**
```python
        model = YOLO(args.start_from)
```
Store the result in `model`: call `YOLO` with the inputs shown to obtain its result.

**Line 109**
```python
        model.train(data=str(DATASET / "dataset.yaml"), epochs=args.epochs, imgsz=640,
```
Call `model.train` with the inputs shown to obtain its result.

**Line 110**
```python
                    batch=8, device=0, project=str(config.RESULTS_DIR), name=args.name,
```
Continuation of the statement starting at line 109; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 111**
```python
                    exist_ok=True, workers=2, seed=config.SEED)
```
Continuation of the statement starting at line 109; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 112**
```python
        WEIGHTS.parent.mkdir(exist_ok=True)
```
Call `weights.parent.mkdir` with the inputs shown to obtain its result.

**Line 113**
```python
        shutil.copyfile(config.RESULTS_DIR / args.name / "weights/best.pt", WEIGHTS)
```
Call `shutil.copyfile` with the inputs shown to obtain its result.

**Line 114**
```python
        print(json.dumps(evaluate(YOLO(str(WEIGHTS))), indent=2))
```
Call `print` with the inputs shown to obtain its result.

**Line 115**
```python
    else:
```
Run this branch when the associated condition was false.

**Line 116**
```python
        print(json.dumps(evaluate(YOLO(str(WEIGHTS))), indent=2))
```
Call `print` with the inputs shown to obtain its result.

**Line 117**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 118**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 119**
```python
if __name__ == "__main__":
```
Run the indented branch only when `__name__ == '__main__'` is true.

**Line 120**
```python
    main()
```
Call `main` with the inputs shown to obtain its result.

## scripts/eval_end_to_end.py

Evaluate full photos, counting missed plates as failed text readings.

Source SHA-256: `637962fd7ce30bf4e8f0b06a1c37bb023e7ab8905f801b2f4eb510cef9bee248`

**Line 1**
```python
"""One-time full-image evaluation: detector miss counts as an OCR failure."""
```
Use the fixed value `'one-time full-image evaluation: detector miss counts as an ocr failure.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import argparse
```
Make the named library tools available here: `import argparse`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
import csv
```
Make the named library tools available here: `import csv`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python
import json
```
Make the named library tools available here: `import json`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python
from pathlib import Path
```
Make the named library tools available here: `from pathlib import Path`. Importing a project module makes its reusable functions accessible.

**Line 7**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 8**
```python
import cv2
```
Make the named library tools available here: `import cv2`. Importing a project module makes its reusable functions accessible.

**Line 9**
```python
from ultralytics import YOLO
```
Make the named library tools available here: `from ultralytics import YOLO`. Importing a project module makes its reusable functions accessible.

**Line 10**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 11**
```python
from riskgate import config
```
Make the named library tools available here: `from riskgate import config`. Importing a project module makes its reusable functions accessible.

**Line 12**
```python
from riskgate.calibration import load, predict
```
Make the named library tools available here: `from riskgate.calibration import load, predict`. Importing a project module makes its reusable functions accessible.

**Line 13**
```python
from riskgate.engines.easyocr_engine import EasyOCREngine
```
Make the named library tools available here: `from riskgate.engines.easyocr_engine import EasyOCREngine`. Importing a project module makes its reusable functions accessible.

**Line 14**
```python
from riskgate.engines.fastplate_engine import FastPlateEngine
```
Make the named library tools available here: `from riskgate.engines.fastplate_engine import FastPlateEngine`. Importing a project module makes its reusable functions accessible.

**Line 15**
```python
from riskgate.features import plate_features
```
Make the named library tools available here: `from riskgate.features import plate_features`. Importing a project module makes its reusable functions accessible.

**Line 16**
```python
from riskgate.metrics import cer, exact_match, normalize
```
Make the named library tools available here: `from riskgate.metrics import cer, exact_match, normalize`. Importing a project module makes its reusable functions accessible.

**Line 17**
```python
from riskgate.router import route, wilson_interval
```
Make the named library tools available here: `from riskgate.router import route, wilson_interval`. Importing a project module makes its reusable functions accessible.

**Line 18**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 19**
```python
def main() -> None:
```
Define `main`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 20**
```python
    parser = argparse.ArgumentParser()
```
Store the result in `parser`: call `argparse.ArgumentParser` with the inputs shown to obtain its result.

**Line 21**
```python
    parser.add_argument("--output", type=Path, default=config.RESULTS_DIR / "end_to_end_test.json")
```
Call `parser.add_argument` with the inputs shown to obtain its result.

**Line 22**
```python
    parser.add_argument("--weights", type=Path, default=config.ROOT / "weights/plate_detector.pt")
```
Call `parser.add_argument` with the inputs shown to obtain its result.

**Line 23**
```python
    args = parser.parse_args()
```
Store the result in `args`: call `parser.parse_args` with the inputs shown to obtain its result.

**Line 24**
```python
    if args.output.exists():
```
Run the indented branch only when `args.output.exists()` is true.

**Line 25**
```python
        raise FileExistsError(f"{args.output} already exists; keep the first evaluation run")
```
Stop this operation with the shown exception and message, rather than silently continuing.

**Line 26**
```python
    splits = json.loads(config.SPLITS_V2.read_text())
```
Store the result in `splits`: call `json.loads` with the inputs shown to obtain its result.

**Line 27**
```python
    test = set(splits["test"])
```
Store the result in `test`: call `set` with the inputs shown to obtain its result.

**Line 28**
```python
    with (config.ROOT / "data/indian_manifest.csv").open(newline="") as source:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 29**
```python
        samples = [row for row in csv.DictReader(source) if "kaggle:" + row["group_id"] in test]
```
Store the result in `samples`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 30**
```python
    name = json.loads((config.RESULTS_DIR / "selected_reader.json").read_text())["reader"]
```
Store the result in `name`: look up or slice `json.loads((config.RESULTS_DIR / 'selected_reader.json').read_text())` using the index or range in brackets.

**Line 31**
```python
    reader = FastPlateEngine() if name == "FastPlateOCR" else EasyOCREngine(config.READER_UPSCALE, config.READER_ALLOWLIST)
```
Store the result in `reader`: choose the first value if `name == 'FastPlateOCR'` is true, otherwise choose the value after `else`.

**Line 32**
```python
    detector = YOLO(str(args.weights))
```
Store the result in `detector`: call `YOLO` with the inputs shown to obtain its result.

**Line 33**
```python
    calibration = load(config.CALIBRATION_MODEL)
```
Store the result in `calibration`: call `load` with the inputs shown to obtain its result.

**Line 34**
```python
    details = []
```
Store the result in `details`: evaluate `[]` using the values currently in memory.

**Line 35**
```python
    for row in samples:
```
For each item from `samples`, name it `row` and run the indented body.

**Line 36**
```python
        image = cv2.imread(str(config.ROOT / row["image_path"]))
```
Store the result in `image`: call `cv2.imread` with the inputs shown to obtain its result.

**Line 37**
```python
        if image is None:
```
Run the indented branch only when `image is None` is true.

**Line 38**
```python
            continue
```
Skip the rest of this loop iteration and move to the next item.

**Line 39**
```python
        result = detector.predict(image, conf=0.25, verbose=False)[0]
```
Store the result in `result`: look up or slice `detector.predict(image, conf=0.25, verbose=False)` using the index or range in brackets.

**Line 40**
```python
        pred, confidence, decision, read_time = "", 0.0, "REVIEW", 0.0
```
Store the result in `(pred, confidence, decision, read_time)`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 41**
```python
        if len(result.boxes):
```
Run the indented branch only when `len(result.boxes)` is true.

**Line 42**
```python
            box = max(result.boxes, key=lambda item: float(item.conf[0]))
```
Store the result in `box`: call `max` with the inputs shown to obtain its result.

**Line 43**
```python
            x1, y1, x2, y2 = [int(value) for value in box.xyxy[0].tolist()]
```
Store the result in `(x1, y1, x2, y2)`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 44**
```python
            plate = image[max(0, y1):min(image.shape[0], y2), max(0, x1):min(image.shape[1], x2)]
```
Store the result in `plate`: look up or slice `image` using the index or range in brackets.

**Line 45**
```python
            if plate.size:
```
Run the indented branch only when `plate.size` is true.

**Line 46**
```python
                read = reader.read(plate)
```
Store the result in `read`: call `reader.read` with the inputs shown to obtain its result.

**Line 47**
```python
                pred = normalize(read.text)
```
Store the result in `pred`: uppercase the text and keep only letters A–Z and digits 0–9.

**Line 48**
```python
                read_time = read.latency_ms
```
Store the result in `read_time`: evaluate `read.latency_ms` using the values currently in memory.

**Line 49**
```python
                if pred:
```
Run the indented branch only when `pred` is true.

**Line 50**
```python
                    confidence = predict(calibration, plate_features(plate, read))
```
Store the result in `confidence`: calculate the correctness estimate using the saved calibration model.

**Line 51**
```python
                    decision = route(pred, confidence, calibration["thresholds"]["0.10"])
```
Store the result in `decision`: apply the format and confidence acceptance rules.

**Line 52**
```python
        details.append({"image": row["image_path"], "truth": row["truth"], "pred": pred,
```
Call `details.append` with the inputs shown to obtain its result.

**Line 53**
```python
                        "ok": int(exact_match(pred, row["truth"])), "cer": cer(pred, row["truth"]),
```
Continuation of the statement starting at line 52; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 54**
```python
                        "detected": int(bool(len(result.boxes))), "confidence": confidence,
```
Continuation of the statement starting at line 52; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 55**
```python
                        "route": decision, "ocr_latency_ms": read_time})
```
Continuation of the statement starting at line 52; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 56**
```python
    n = len(details)
```
Store the result in `n`: call `len` with the inputs shown to obtain its result.

**Line 57**
```python
    good = sum(row["ok"] for row in details)
```
Store the result in `good`: call `sum` with the inputs shown to obtain its result.

**Line 58**
```python
    accepted = [row for row in details if row["route"] == "ACCEPT"]
```
Store the result in `accepted`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 59**
```python
    errors = sum(1 - row["ok"] for row in accepted)
```
Store the result in `errors`: call `sum` with the inputs shown to obtain its result.

**Line 60**
```python
    report = {"reader": name, "n": n, "detected": sum(row["detected"] for row in details),
```
Store the result in `report`: build a dictionary: each key names the value stored beside it.

**Line 61**
```python
              "whole_plate_exact": good, "whole_plate_accuracy": good/n,
```
Continuation of the statement starting at line 60; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 62**
```python
              "accuracy_95ci": tuple(1-x for x in reversed(wilson_interval(n-good, n))),
```
Continuation of the statement starting at line 60; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 63**
```python
              "mean_cer": sum(row["cer"] for row in details)/n,
```
Continuation of the statement starting at line 60; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 64**
```python
              "accepted": len(accepted), "accepted_errors": errors,
```
Continuation of the statement starting at line 60; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 65**
```python
              "accepted_error": errors/len(accepted) if accepted else None,
```
Continuation of the statement starting at line 60; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 66**
```python
              "coverage": len(accepted)/n}
```
Continuation of the statement starting at line 60; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 67**
```python
    config.RESULTS_DIR.mkdir(exist_ok=True)
```
Call `config.results_dir.mkdir` with the inputs shown to obtain its result.

**Line 68**
```python
    args.output.write_text(json.dumps(report, indent=2) + "\n")
```
Call `args.output.write_text` with the inputs shown to obtain its result.

**Line 69**
```python
    with args.output.with_name(args.output.stem + "_details.csv").open("w", newline="") as output:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 70**
```python
        writer = csv.DictWriter(output, fieldnames=list(details[0]))
```
Store the result in `writer`: call `csv.DictWriter` with the inputs shown to obtain its result.

**Line 71**
```python
        writer.writeheader()
```
Call `writer.writeheader` with the inputs shown to obtain its result.

**Line 72**
```python
        writer.writerows(details)
```
Call `writer.writerows` with the inputs shown to obtain its result.

**Line 73**
```python
    print(json.dumps(report, indent=2))
```
Call `print` with the inputs shown to obtain its result.

**Line 74**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 75**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 76**
```python
if __name__ == "__main__":
```
Run the indented branch only when `__name__ == '__main__'` is true.

**Line 77**
```python
    main()
```
Call `main` with the inputs shown to obtain its result.

## scripts/eval_router.py

Fit calibration, choose validation thresholds, and evaluate the saved policy.

Source SHA-256: `61593ed71f8821e6a5159ec47b33088fe2a9dff2489d551605fd13e2740cb895`

**Line 1**
```python
"""Fit on calib, select on val, and perform a guarded one-time test."""
```
Use the fixed value `'fit on calib, select on val, and perform a guarded one-time test.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import argparse
```
Make the named library tools available here: `import argparse`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
import csv
```
Make the named library tools available here: `import csv`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python
import json
```
Make the named library tools available here: `import json`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python
from pathlib import Path
```
Make the named library tools available here: `from pathlib import Path`. Importing a project module makes its reusable functions accessible.

**Line 7**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 8**
```python
from riskgate import config
```
Make the named library tools available here: `from riskgate import config`. Importing a project module makes its reusable functions accessible.

**Line 9**
```python
from riskgate.calibration import data_hash, fit, load, predict, save
```
Make the named library tools available here: `from riskgate.calibration import data_hash, fit, load, predict, save`. Importing a project module makes its reusable functions accessible.

**Line 10**
```python
from riskgate.metrics import ece, risk_coverage
```
Make the named library tools available here: `from riskgate.metrics import ece, risk_coverage`. Importing a project module makes its reusable functions accessible.

**Line 11**
```python
from riskgate.router import choose_thresholds, route, wilson_interval
```
Make the named library tools available here: `from riskgate.router import choose_thresholds, route, wilson_interval`. Importing a project module makes its reusable functions accessible.

**Line 12**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 13**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 14**
```python
READS = config.RESULTS_DIR / "baseline_v2.csv"
```
Store the result in `READS`: calculate `config.RESULTS_DIR / 'baseline_v2.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 15**
```python
MODEL = config.CALIBRATION_MODEL
```
Store the result in `MODEL`: evaluate `config.CALIBRATION_MODEL` using the values currently in memory.

**Line 16**
```python
FINAL = config.RESULTS_DIR / "final_test.json"
```
Store the result in `FINAL`: calculate `config.RESULTS_DIR / 'final_test.json'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 17**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 18**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 19**
```python
def read_rows() -> list[dict]:
```
Define `read_rows`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 20**
```python
    with READS.open(newline="") as f:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 21**
```python
        return list(csv.DictReader(f))
```
Finish this function and call `list` with the inputs shown to obtain its result; send that result to its caller.

**Line 22**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 23**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 24**
```python
def fit_model(rows: list[dict]) -> None:
```
Define `fit_model`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 25**
```python
    calib = [r for r in rows if r["split"] == "calib"]
```
Store the result in `calib`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 26**
```python
    val = [r for r in rows if r["split"] == "val"]
```
Store the result in `val`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 27**
```python
    if not val:
```
Run the indented branch only when `not val` is true.

**Line 28**
```python
        raise ValueError("Validation split is empty")
```
Stop this operation with the shown exception and message, rather than silently continuing.

**Line 29**
```python
    model = fit(calib)
```
Store the result in `model`: learn the calibration parameters.

**Line 30**
```python
    for r in val:
```
For each item from `val`, name it `r` and run the indented body.

**Line 31**
```python
        r["calibrated_conf"] = predict(model, r)
```
Store the result in `r['calibrated_conf']`: calculate the correctness estimate using the saved calibration model.

**Line 32**
```python
    model["thresholds"] = choose_thresholds(val)
```
Store the result in `model['thresholds']`: call `choose_thresholds` with the inputs shown to obtain its result.

**Line 33**
```python
    model["validation_ece"] = {"raw": ece([float(r["raw_conf"]) for r in val],
```
Store the result in `model['validation_ece']`: build a dictionary: each key names the value stored beside it.

**Line 34**
```python
                                           [bool(int(r["ok"])) for r in val]),
```
Continuation of the statement starting at line 33; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 35**
```python
                               "calibrated": ece([r["calibrated_conf"] for r in val],
```
Continuation of the statement starting at line 33; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 36**
```python
                                                 [bool(int(r["ok"])) for r in val])}
```
Continuation of the statement starting at line 33; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 37**
```python
    save(model, MODEL)
```
Call `save` with the inputs shown to obtain its result.

**Line 38**
```python
    print(json.dumps({"thresholds": model["thresholds"], "val_ece": model["validation_ece"]}, indent=2))
```
Call `print` with the inputs shown to obtain its result.

**Line 39**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 40**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 41**
```python
def final_test(rows: list[dict], force: bool) -> None:
```
Define `final_test`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 42**
```python
    if FINAL.exists() and not force:
```
Run the indented branch only when `FINAL.exists() and (not force)` is true.

**Line 43**
```python
        raise FileExistsError(f"{FINAL} exists; use --force only if you explicitly intend to invalidate the one-time test")
```
Stop this operation with the shown exception and message, rather than silently continuing.

**Line 44**
```python
    model = load(MODEL)
```
Store the result in `model`: call `load` with the inputs shown to obtain its result.

**Line 45**
```python
    if data_hash([r for r in rows if r["split"] == "calib"]) != model["data_sha256"]:
```
Run the indented branch only when `data_hash([r for r in rows if r['split'] == 'calib']) != model['data_sha256']` is true.

**Line 46**
```python
        raise ValueError("Calibration data changed since fitting; refusing final test")
```
Stop this operation with the shown exception and message, rather than silently continuing.

**Line 47**
```python
    test = [r for r in rows if r["split"] == "test"]
```
Store the result in `test`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 48**
```python
    if not test:
```
Run the indented branch only when `not test` is true.

**Line 49**
```python
        raise ValueError("Test split is empty")
```
Stop this operation with the shown exception and message, rather than silently continuing.

**Line 50**
```python
    for r in test:
```
For each item from `test`, name it `r` and run the indented body.

**Line 51**
```python
        r["calibrated_conf"] = predict(model, r)
```
Store the result in `r['calibrated_conf']`: calculate the correctness estimate using the saved calibration model.

**Line 52**
```python
    report = {"n": len(test), "model_data_sha256": model["data_sha256"], "targets": {}}
```
Store the result in `report`: build a dictionary: each key names the value stored beside it.

**Line 53**
```python
    for target, thresholds in model["thresholds"].items():
```
For each item from `model['thresholds'].items()`, name it `(target, thresholds)` and run the indented body.

**Line 54**
```python
        counts = {name: [r for r in test if route(r["pred"], r["calibrated_conf"], thresholds) == name]
```
Store the result in `counts`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 55**
```python
                  for name in ("ACCEPT", "ESCALATE", "REVIEW")}
```
Continuation of the statement starting at line 54; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 56**
```python
        accepted = counts["ACCEPT"]
```
Store the result in `accepted`: look up or slice `counts` using the index or range in brackets.

**Line 57**
```python
        errors = sum(not int(r["ok"]) for r in accepted)
```
Store the result in `errors`: call `sum` with the inputs shown to obtain its result.

**Line 58**
```python
        report["targets"][target] = {"accepted": len(accepted), "coverage": len(accepted)/len(test),
```
Store the result in `report['targets'][target]`: build a dictionary: each key names the value stored beside it.

**Line 59**
```python
                                     "observed_error": errors/len(accepted) if accepted else None,
```
Continuation of the statement starting at line 58; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 60**
```python
                                     "error_95ci": wilson_interval(errors, len(accepted)) if accepted else None,
```
Continuation of the statement starting at line 58; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 61**
```python
                                     "escalated": len(counts["ESCALATE"])/len(test),
```
Continuation of the statement starting at line 58; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 62**
```python
                                     "review": len(counts["REVIEW"])/len(test)}
```
Continuation of the statement starting at line 58; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 63**
```python
    FINAL.write_text(json.dumps(report, indent=2) + "\n")
```
Call `final.write_text` with the inputs shown to obtain its result.

**Line 64**
```python
    import matplotlib
```
Make the named library tools available here: `import matplotlib`. Importing a project module makes its reusable functions accessible.

**Line 65**
```python
    matplotlib.use("Agg")
```
Call `matplotlib.use` with the inputs shown to obtain its result.

**Line 66**
```python
    import matplotlib.pyplot as plt
```
Make the named library tools available here: `import matplotlib.pyplot as plt`. Importing a project module makes its reusable functions accessible.

**Line 67**
```python
    correct = [bool(int(r["ok"])) for r in test]
```
Store the result in `correct`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 68**
```python
    conf = [r["calibrated_conf"] for r in test]
```
Store the result in `conf`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 69**
```python
    plt.figure()
```
Call `plt.figure` with the inputs shown to obtain its result.

**Line 70**
```python
    plt.plot([0, 1], [0, 1], "--", label="ideal")
```
Call `plt.plot` with the inputs shown to obtain its result.

**Line 71**
```python
    plt.scatter(conf, correct, alpha=0.35, label="test plates")
```
Call `plt.scatter` with the inputs shown to obtain its result.

**Line 72**
```python
    plt.xlabel("Calibrated confidence")
```
Call `plt.xlabel` with the inputs shown to obtain its result.

**Line 73**
```python
    plt.ylabel("Correct (1) or wrong (0)")
```
Call `plt.ylabel` with the inputs shown to obtain its result.

**Line 74**
```python
    plt.legend()
```
Call `plt.legend` with the inputs shown to obtain its result.

**Line 75**
```python
    plt.savefig(config.RESULTS_DIR / "reliability.png")
```
Call `plt.savefig` with the inputs shown to obtain its result.

**Line 76**
```python
    plt.close()
```
Call `plt.close` with the inputs shown to obtain its result.

**Line 77**
```python
    points = risk_coverage(conf, correct)
```
Store the result in `points`: call `risk_coverage` with the inputs shown to obtain its result.

**Line 78**
```python
    plt.figure()
```
Call `plt.figure` with the inputs shown to obtain its result.

**Line 79**
```python
    plt.plot(*zip(*points))
```
Call `plt.plot` with the inputs shown to obtain its result.

**Line 80**
```python
    plt.xlabel("Coverage")
```
Call `plt.xlabel` with the inputs shown to obtain its result.

**Line 81**
```python
    plt.ylabel("Observed error rate")
```
Call `plt.ylabel` with the inputs shown to obtain its result.

**Line 82**
```python
    plt.savefig(config.RESULTS_DIR / "risk_coverage.png")
```
Call `plt.savefig` with the inputs shown to obtain its result.

**Line 83**
```python
    plt.close()
```
Call `plt.close` with the inputs shown to obtain its result.

**Line 84**
```python
    print(json.dumps(report, indent=2))
```
Call `print` with the inputs shown to obtain its result.

**Line 85**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 86**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 87**
```python
def main() -> None:
```
Define `main`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 88**
```python
    parser = argparse.ArgumentParser()
```
Store the result in `parser`: call `argparse.ArgumentParser` with the inputs shown to obtain its result.

**Line 89**
```python
    mode = parser.add_mutually_exclusive_group(required=True)
```
Store the result in `mode`: call `parser.add_mutually_exclusive_group` with the inputs shown to obtain its result.

**Line 90**
```python
    mode.add_argument("--fit", action="store_true")
```
Call `mode.add_argument` with the inputs shown to obtain its result.

**Line 91**
```python
    mode.add_argument("--final", action="store_true")
```
Call `mode.add_argument` with the inputs shown to obtain its result.

**Line 92**
```python
    parser.add_argument("--force", action="store_true")
```
Call `parser.add_argument` with the inputs shown to obtain its result.

**Line 93**
```python
    args = parser.parse_args()
```
Store the result in `args`: call `parser.parse_args` with the inputs shown to obtain its result.

**Line 94**
```python
    rows = read_rows()
```
Store the result in `rows`: call `read_rows` with the inputs shown to obtain its result.

**Line 95**
```python
    if args.fit:
```
Run the indented branch only when `args.fit` is true.

**Line 96**
```python
        fit_model(rows)
```
Call `fit_model` with the inputs shown to obtain its result.

**Line 97**
```python
    else:
```
Run this branch when the associated condition was false.

**Line 98**
```python
        final_test(rows, args.force)
```
Call `final_test` with the inputs shown to obtain its result.

**Line 99**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 100**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 101**
```python
if __name__ == "__main__":
```
Run the indented branch only when `__name__ == '__main__'` is true.

**Line 102**
```python
    main()
```
Call `main` with the inputs shown to obtain its result.

## scripts/eval_stability.py

Compare the original policy with the optional veto on the existing demo gallery.

Source SHA-256: `2dba64fb3f6dd5e81253ba772eea24fe693d001e7b183d02911030e91c88e949`

**Line 1**
```python
"""Descriptive gallery ablation, not a new held-out accuracy benchmark."""
```
Use the fixed value `'descriptive gallery ablation, not a new held-out accuracy benchmark.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import csv
```
Make the named library tools available here: `import csv`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
import json
```
Make the named library tools available here: `import json`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python
from statistics import mean
```
Make the named library tools available here: `from statistics import mean`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 7**
```python
import cv2
```
Make the named library tools available here: `import cv2`. Importing a project module makes its reusable functions accessible.

**Line 8**
```python
from ultralytics import YOLO
```
Make the named library tools available here: `from ultralytics import YOLO`. Importing a project module makes its reusable functions accessible.

**Line 9**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 10**
```python
from riskgate import config
```
Make the named library tools available here: `from riskgate import config`. Importing a project module makes its reusable functions accessible.

**Line 11**
```python
from riskgate.calibration import load, predict
```
Make the named library tools available here: `from riskgate.calibration import load, predict`. Importing a project module makes its reusable functions accessible.

**Line 12**
```python
from riskgate.engines.fastplate_engine import FastPlateEngine
```
Make the named library tools available here: `from riskgate.engines.fastplate_engine import FastPlateEngine`. Importing a project module makes its reusable functions accessible.

**Line 13**
```python
from riskgate.features import plate_features
```
Make the named library tools available here: `from riskgate.features import plate_features`. Importing a project module makes its reusable functions accessible.

**Line 14**
```python
from riskgate.metrics import exact_match, normalize
```
Make the named library tools available here: `from riskgate.metrics import exact_match, normalize`. Importing a project module makes its reusable functions accessible.

**Line 15**
```python
from riskgate.router import route
```
Make the named library tools available here: `from riskgate.router import route`. Importing a project module makes its reusable functions accessible.

**Line 16**
```python
from riskgate.stability import apply_veto, check_stability
```
Make the named library tools available here: `from riskgate.stability import apply_veto, check_stability`. Importing a project module makes its reusable functions accessible.

**Line 17**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 18**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 19**
```python
def main() -> None:
```
Define `main`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 20**
```python
    output = config.RESULTS_DIR / "stability_gallery.json"
```
Store the result in `output`: calculate `config.RESULTS_DIR / 'stability_gallery.json'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 21**
```python
    if output.exists():
```
Run the indented branch only when `output.exists()` is true.

**Line 22**
```python
        raise FileExistsError("Keep the first gallery experiment; do not tune on these results")
```
Stop this operation with the shown exception and message, rather than silently continuing.

**Line 23**
```python
    selected = json.loads((config.RESULTS_DIR / "selected_reader.json").read_text())["reader"]
```
Store the result in `selected`: look up or slice `json.loads((config.RESULTS_DIR / 'selected_reader.json').read_text())` using the index or range in brackets.

**Line 24**
```python
    if selected != "FastPlateOCR":
```
Run the indented branch only when `selected != 'FastPlateOCR'` is true.

**Line 25**
```python
        raise ValueError("This experiment requires the project's selected FastPlateOCR reader")
```
Stop this operation with the shown exception and message, rather than silently continuing.

**Line 26**
```python
    reader = FastPlateEngine()
```
Store the result in `reader`: call `FastPlateEngine` with the inputs shown to obtain its result.

**Line 27**
```python
    detector = YOLO(str(config.ROOT / "weights/plate_detector.pt"))
```
Store the result in `detector`: call `YOLO` with the inputs shown to obtain its result.

**Line 28**
```python
    model = load(config.CALIBRATION_MODEL)
```
Store the result in `model`: call `load` with the inputs shown to obtain its result.

**Line 29**
```python
    with (config.ROOT / "data/sample_gallery/manifest.csv").open(newline="") as source:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 30**
```python
        gallery = list(csv.DictReader(source))
```
Store the result in `gallery`: call `list` with the inputs shown to obtain its result.

**Line 31**
```python
    rows = []
```
Store the result in `rows`: evaluate `[]` using the values currently in memory.

**Line 32**
```python
    for item in gallery:
```
For each item from `gallery`, name it `item` and run the indented body.

**Line 33**
```python
        image = cv2.imread(str(config.ROOT / item["image_path"]))
```
Store the result in `image`: call `cv2.imread` with the inputs shown to obtain its result.

**Line 34**
```python
        if image is None:
```
Run the indented branch only when `image is None` is true.

**Line 35**
```python
            raise ValueError(f"Unreadable gallery image: {item['image_path']}")
```
Stop this operation with the shown exception and message, rather than silently continuing.

**Line 36**
```python
        boxes = detector.predict(image, conf=0.25, verbose=False)[0].boxes
```
Store the result in `boxes`: evaluate `detector.predict(image, conf=0.25, verbose=False)[0].boxes` using the values currently in memory.

**Line 37**
```python
        row = {"image": item["image_path"], "truth": item["truth"], "pred": "",
```
Store the result in `row`: build a dictionary: each key names the value stored beside it.

**Line 38**
```python
               "base_route": "REVIEW", "route": "REVIEW", "stability": None, "ok": False}
```
Continuation of the statement starting at line 37; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 39**
```python
        if len(boxes):
```
Run the indented branch only when `len(boxes)` is true.

**Line 40**
```python
            box = max(boxes, key=lambda value: float(value.conf[0]))
```
Store the result in `box`: call `max` with the inputs shown to obtain its result.

**Line 41**
```python
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
```
Store the result in `(x1, y1, x2, y2)`: call `map` with the inputs shown to obtain its result.

**Line 42**
```python
            crop = image[max(0, y1):min(image.shape[0], y2), max(0, x1):min(image.shape[1], x2)]
```
Store the result in `crop`: look up or slice `image` using the index or range in brackets.

**Line 43**
```python
            if crop.size:
```
Run the indented branch only when `crop.size` is true.

**Line 44**
```python
                read = reader.read(crop)
```
Store the result in `read`: call `reader.read` with the inputs shown to obtain its result.

**Line 45**
```python
                pred = normalize(read.text)
```
Store the result in `pred`: uppercase the text and keep only letters A–Z and digits 0–9.

**Line 46**
```python
                base = "REVIEW"
```
Store the result in `base`: use the fixed value `'REVIEW'`.

**Line 47**
```python
                if pred and not read.error:
```
Run the indented branch only when `pred and (not read.error)` is true.

**Line 48**
```python
                    confidence = predict(model, plate_features(crop, read))
```
Store the result in `confidence`: calculate the correctness estimate using the saved calibration model.

**Line 49**
```python
                    base = "ACCEPT" if route(pred, confidence, model["thresholds"]["0.10"]) == "ACCEPT" else "REVIEW"
```
Store the result in `base`: choose the first value if `route(pred, confidence, model['thresholds']['0.10']) == 'ACCEPT'` is true, otherwise choose the value after `else`.

**Line 50**
```python
                evidence = check_stability(crop, pred, reader.read)
```
Store the result in `evidence`: read resized and brightened copies and compare with the original text.

**Line 51**
```python
                row.update(pred=pred, base_route=base, route=apply_veto(base, evidence),
```
Call `row.update` with the inputs shown to obtain its result.

**Line 52**
```python
                           stability=evidence, ok=exact_match(pred, item["truth"]))
```
Continuation of the statement starting at line 51; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 53**
```python
        rows.append(row)
```
Call `rows.append` with the inputs shown to obtain its result.

**Line 54**
```python
    report = {"scope": "12 previously selected demo scenes; descriptive only, not held-out",
```
Store the result in `report`: build a dictionary: each key names the value stored beside it.

**Line 55**
```python
              "policy": "0.10 validation target; fixed resize 1.25 and brightness 1.10; exact agreement",
```
Continuation of the statement starting at line 54; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 56**
```python
              "n": len(rows), "exact_reads": sum(row["ok"] for row in rows), "policies": {}}
```
Continuation of the statement starting at line 54; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 57**
```python
    for key in ("base_route", "route"):
```
For each item from `('base_route', 'route')`, name it `key` and run the indented body.

**Line 58**
```python
        accepted = [row for row in rows if row[key] == "ACCEPT"]
```
Store the result in `accepted`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 59**
```python
        errors = sum(not row["ok"] for row in accepted)
```
Store the result in `errors`: call `sum` with the inputs shown to obtain its result.

**Line 60**
```python
        report["policies"][key] = {"accepted": len(accepted), "errors": errors,
```
Store the result in `report['policies'][key]`: build a dictionary: each key names the value stored beside it.

**Line 61**
```python
            "coverage": len(accepted) / len(rows), "accepted_error": errors / len(accepted) if accepted else None}
```
Continuation of the statement starting at line 60; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 62**
```python
    timings = [row["stability"]["extra_latency_ms"] for row in rows if row["stability"]]
```
Store the result in `timings`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 63**
```python
    report["mean_extra_latency_ms"] = mean(timings) if timings else None
```
Store the result in `report['mean_extra_latency_ms']`: choose the first value if `timings` is true, otherwise choose the value after `else`.

**Line 64**
```python
    report["details"] = rows
```
Store the result in `report['details']`: evaluate `rows` using the values currently in memory.

**Line 65**
```python
    output.write_text(json.dumps(report, indent=2) + "\n")
```
Call `output.write_text` with the inputs shown to obtain its result.

**Line 66**
```python
    print(json.dumps({key: value for key, value in report.items() if key != "details"}, indent=2))
```
Call `print` with the inputs shown to obtain its result.

**Line 67**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 68**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 69**
```python
if __name__ == "__main__":
```
Run the indented branch only when `__name__ == '__main__'` is true.

**Line 70**
```python
    main()
```
Call `main` with the inputs shown to obtain its result.

## scripts/explain_code.py

Generate this line reference from the actual source and record source fingerprints.

Source SHA-256: `d9581fadd5ccbd8bfcea3a99e1226e795f4eba3ba6bb4e92d13598233ecbf299`

**Line 1**
```python
"""Regenerate the beginner's source reference using Python's own syntax parser."""
```
Use the fixed value `"regenerate the beginner's source reference using python's own syntax parser."`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import ast
```
Make the named library tools available here: `import ast`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
import hashlib
```
Make the named library tools available here: `import hashlib`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python
from pathlib import Path
```
Make the named library tools available here: `from pathlib import Path`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 7**
```python
ROOT = Path(__file__).resolve().parents[1]
```
Store the result in `ROOT`: look up or slice `Path(__file__).resolve().parents` using the index or range in brackets.

**Line 8**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 9**
```python
PURPOSES = {
```
Store the result in `PURPOSES`: build a dictionary: each key names the value stored beside it.

**Line 10**
```python
    "app/streamlit_app.py": "The visible demo: upload, detect, read, show evidence, review, and export a batch.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 11**
```python
    "riskgate/calibration.py": "Learn and use a small model that estimates whether a complete OCR answer is correct.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 12**
```python
    "riskgate/config.py": "Keep shared file paths and experiment settings in one place.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 13**
```python
    "riskgate/contracts.py": "Define the fields in a labelled example and an OCR result.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 14**
```python
    "riskgate/data.py": "Load labels, keep related images together, and crop plate rectangles.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 15**
```python
    "riskgate/features.py": "Turn the crop and OCR result into six numbers for calibration.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 16**
```python
    "riskgate/grammar.py": "Check whether characters resemble a plate format; this cannot verify a real registration.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 17**
```python
    "riskgate/metrics.py": "Measure exact text matches, character errors, calibration, and error versus coverage.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 18**
```python
    "riskgate/router.py": "Choose validation thresholds and accept, escalate, or review a reading.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 19**
```python
    "riskgate/stability.py": "Run two transformed-image reads and veto acceptance when either disagrees.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 20**
```python
    "riskgate/engines/easyocr_engine.py": "Adapt EasyOCR output to the common EngineResult format and order text boxes.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 21**
```python
    "riskgate/engines/fastplate_engine.py": "Load the local ONNX plate reader and adapt its output.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 22**
```python
    "scripts/baseline_v2.py": "Compare readers on labelled crops and record predictions and features.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 23**
```python
    "scripts/detector.py": "Prepare YOLO box labels, fine-tune the detector, and measure box overlap.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 24**
```python
    "scripts/eval_end_to_end.py": "Evaluate full photos, counting missed plates as failed text readings.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 25**
```python
    "scripts/eval_router.py": "Fit calibration, choose validation thresholds, and evaluate the saved policy.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 26**
```python
    "scripts/eval_stability.py": "Compare the original policy with the optional veto on the existing demo gallery.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 27**
```python
    "scripts/explain_code.py": "Generate this line reference from the actual source and record source fingerprints.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 28**
```python
    "scripts/import_extra_detection.py": "Screen the additional box-only source and add eligible photos to detector training.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 29**
```python
    "scripts/label_tool.py": "Support manual inspection of proposed labels.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 30**
```python
    "scripts/package_submission.py": "Build the portable academic demo ZIP from an explicit list of folders and assets.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 31**
```python
    "scripts/plot_results.py": "Draw charts from saved experiment results.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 32**
```python
    "scripts/prepare_gallery.py": "Copy selected original demo scenes and write their gallery manifest.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 33**
```python
    "scripts/prepare_indian.py": "Read the main dataset, group related examples, and prepare labels and splits.",
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 34**
```python
}
```
Continuation of the statement starting at line 9; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 35**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 36**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 37**
```python
def expression(node: ast.AST) -> str:
```
Define `expression`; its indented body runs when called. Translate common Python expressions into short, concrete reading instructions.

**Line 38**
```python
    """Translate common Python expressions into short, concrete reading instructions."""
```
Use the fixed value `'translate common python expressions into short, concrete reading instructions.'`.

**Line 39**
```python
    if isinstance(node, ast.Call):
```
Run the indented branch only when `isinstance(node, ast.Call)` is true.

**Line 40**
```python
        name = ast.unparse(node.func)
```
Store the result in `name`: call `ast.unparse` with the inputs shown to obtain its result.

**Line 41**
```python
        actions = {"normalize": "uppercase the text and remove characters outside A–Z and 0–9",
```
Store the result in `actions`: build a dictionary: each key names the value stored beside it.

**Line 42**
```python
                   "predict": "calculate the correctness estimate using the saved calibration model",
```
Continuation of the statement starting at line 41; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 43**
```python
                   "plate_features": "extract the six input signals from the crop and OCR result",
```
Continuation of the statement starting at line 41; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 44**
```python
                   "route": "apply the format and confidence acceptance rules",
```
Continuation of the statement starting at line 41; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 45**
```python
                   "check_stability": "read resized and brightened copies and compare with the original text",
```
Continuation of the statement starting at line 41; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 46**
```python
                   "apply_veto": "change an accepted answer to review if the stability check failed",
```
Continuation of the statement starting at line 41; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 47**
```python
                   "classify": "check the plate format", "fit": "learn the calibration parameters",
```
Continuation of the statement starting at line 41; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 48**
```python
                   "normalize": "uppercase the text and keep only letters A–Z and digits 0–9"}
```
Continuation of the statement starting at line 41; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 49**
```python
        if name in actions:
```
Run the indented branch only when `name in actions` is true.

**Line 50**
```python
            return actions[name]
```
Finish this function and look up or slice `actions` using the index or range in brackets; send that result to its caller.

**Line 51**
```python
        return f"call `{name}` with the inputs shown to obtain its result"
```
Finish this function and evaluate `f'call `{name}` with the inputs shown to obtain its result'` using the values currently in memory; send that result to its caller.

**Line 52**
```python
    if isinstance(node, ast.Constant):
```
Run the indented branch only when `isinstance(node, ast.Constant)` is true.

**Line 53**
```python
        return f"use the fixed value `{repr(node.value)}`" if not isinstance(node.value, str) or len(node.value) < 100 else "use this fixed text block (presentation content, not model logic)"
```
Finish this function and choose the first value if `not isinstance(node.value, str) or len(node.value) < 100` is true, otherwise choose the value after `else`; send that result to its caller.

**Line 54**
```python
    if isinstance(node, ast.Dict):
```
Run the indented branch only when `isinstance(node, ast.Dict)` is true.

**Line 55**
```python
        return "build a dictionary: each key names the value stored beside it"
```
Finish this function and use the fixed value `'build a dictionary: each key names the value stored beside it'`; send that result to its caller.

**Line 56**
```python
    if isinstance(node, (ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp)):
```
Run the indented branch only when `isinstance(node, (ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp))` is true.

**Line 57**
```python
        return "build or iterate values using the inline `for` loop and any `if` filter shown"
```
Finish this function and use the fixed value `'build or iterate values using the inline `for` loop and any `if` filter shown'`; send that result to its caller.

**Line 58**
```python
    if isinstance(node, ast.Subscript):
```
Run the indented branch only when `isinstance(node, ast.Subscript)` is true.

**Line 59**
```python
        return f"look up or slice `{ast.unparse(node.value)}` using the index or range in brackets"
```
Finish this function and evaluate `f'look up or slice `{ast.unparse(node.value)}` using the index or range in brackets'` using the values currently in memory; send that result to its caller.

**Line 60**
```python
    if isinstance(node, ast.IfExp):
```
Run the indented branch only when `isinstance(node, ast.IfExp)` is true.

**Line 61**
```python
        return f"choose the first value if `{ast.unparse(node.test)}` is true, otherwise choose the value after `else`"
```
Finish this function and evaluate `f'choose the first value if `{ast.unparse(node.test)}` is true, otherwise choose the value after `else`'` using the values currently in memory; send that result to its caller.

**Line 62**
```python
    if isinstance(node, ast.Compare):
```
Run the indented branch only when `isinstance(node, ast.Compare)` is true.

**Line 63**
```python
        return f"check whether `{ast.unparse(node)}` is true"
```
Finish this function and evaluate `f'check whether `{ast.unparse(node)}` is true'` using the values currently in memory; send that result to its caller.

**Line 64**
```python
    if isinstance(node, ast.BinOp):
```
Run the indented branch only when `isinstance(node, ast.BinOp)` is true.

**Line 65**
```python
        return f"calculate `{ast.unparse(node)}`; `/` divides, `*` multiplies, and paths use `/` to join folders"
```
Finish this function and evaluate `f'calculate `{ast.unparse(node)}`; `/` divides, `*` multiplies, and paths use `/` to join folders'` using the values currently in memory; send that result to its caller.

**Line 66**
```python
    if isinstance(node, ast.Tuple):
```
Run the indented branch only when `isinstance(node, ast.Tuple)` is true.

**Line 67**
```python
        return "collect the values in order (a tuple), which can also be unpacked into separate names"
```
Finish this function and use the fixed value `'collect the values in order (a tuple), which can also be unpacked into separate names'`; send that result to its caller.

**Line 68**
```python
    return f"evaluate `{ast.unparse(node)}` using the values currently in memory"
```
Finish this function and evaluate `f'evaluate `{ast.unparse(node)}` using the values currently in memory'` using the values currently in memory; send that result to its caller.

**Line 69**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 70**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 71**
```python
def explanation(node: ast.AST) -> str:
```
Define `explanation`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 72**
```python
    if isinstance(node, (ast.Import, ast.ImportFrom)):
```
Run the indented branch only when `isinstance(node, (ast.Import, ast.ImportFrom))` is true.

**Line 73**
```python
        return f"Make the named library tools available here: `{ast.unparse(node)}`. Importing a project module makes its reusable functions accessible."
```
Finish this function and evaluate `f'Make the named library tools available here: `{ast.unparse(node)}`. Importing a project module makes its reusable functions accessible.'` using the values currently in memory; send that result to its caller.

**Line 74**
```python
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
```
Run the indented branch only when `isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))` is true.

**Line 75**
```python
        doc = ast.get_docstring(node)
```
Store the result in `doc`: call `ast.get_docstring` with the inputs shown to obtain its result.

**Line 76**
```python
        return f"Define `{node.name}`; its indented body runs when called. " + (doc.splitlines()[0] if doc else "Inputs are in parentheses; the return annotation describes the expected output type.")
```
Finish this function and calculate `f'Define `{node.name}`; its indented body runs when called. ' + (doc.splitlines()[0] if doc else 'Inputs are in parentheses; the return annotation describes the expected output type.')`; `/` divides, `*` multiplies, and paths use `/` to join folders; send that result to its caller.

**Line 77**
```python
    if isinstance(node, ast.ClassDef):
```
Run the indented branch only when `isinstance(node, ast.ClassDef)` is true.

**Line 78**
```python
        return f"Define the `{node.name}` object type, grouping its data and methods."
```
Finish this function and evaluate `f'Define the `{node.name}` object type, grouping its data and methods.'` using the values currently in memory; send that result to its caller.

**Line 79**
```python
    if isinstance(node, (ast.Assign, ast.AnnAssign)):
```
Run the indented branch only when `isinstance(node, (ast.Assign, ast.AnnAssign))` is true.

**Line 80**
```python
        targets = ', '.join(ast.unparse(t) for t in node.targets) if isinstance(node, ast.Assign) else ast.unparse(node.target)
```
Store the result in `targets`: choose the first value if `isinstance(node, ast.Assign)` is true, otherwise choose the value after `else`.

**Line 81**
```python
        return f"Store the result in `{targets}`: {expression(node.value)}." if node.value else f"Declare the expected type of `{targets}`."
```
Finish this function and choose the first value if `node.value` is true, otherwise choose the value after `else`; send that result to its caller.

**Line 82**
```python
    if isinstance(node, ast.AugAssign):
```
Run the indented branch only when `isinstance(node, ast.AugAssign)` is true.

**Line 83**
```python
        return f"Update `{ast.unparse(node.target)}` using the operation shown and the new value."
```
Finish this function and evaluate `f'Update `{ast.unparse(node.target)}` using the operation shown and the new value.'` using the values currently in memory; send that result to its caller.

**Line 84**
```python
    if isinstance(node, ast.Return):
```
Run the indented branch only when `isinstance(node, ast.Return)` is true.

**Line 85**
```python
        return "Finish this function and " + (expression(node.value) + "; send that result to its caller." if node.value else "send back no value (`None`).")
```
Finish this function and calculate `'Finish this function and ' + (expression(node.value) + '; send that result to its caller.' if node.value else 'send back no value (`None`).')`; `/` divides, `*` multiplies, and paths use `/` to join folders; send that result to its caller.

**Line 86**
```python
    if isinstance(node, ast.If):
```
Run the indented branch only when `isinstance(node, ast.If)` is true.

**Line 87**
```python
        return f"Run the indented branch only when `{ast.unparse(node.test)}` is true."
```
Finish this function and evaluate `f'Run the indented branch only when `{ast.unparse(node.test)}` is true.'` using the values currently in memory; send that result to its caller.

**Line 88**
```python
    if isinstance(node, ast.For):
```
Run the indented branch only when `isinstance(node, ast.For)` is true.

**Line 89**
```python
        return f"For each item from `{ast.unparse(node.iter)}`, name it `{ast.unparse(node.target)}` and run the indented body."
```
Finish this function and evaluate `f'For each item from `{ast.unparse(node.iter)}`, name it `{ast.unparse(node.target)}` and run the indented body.'` using the values currently in memory; send that result to its caller.

**Line 90**
```python
    if isinstance(node, ast.With):
```
Run the indented branch only when `isinstance(node, ast.With)` is true.

**Line 91**
```python
        return "Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel."
```
Finish this function and use this fixed text block (presentation content, not model logic); send that result to its caller.

**Line 92**
```python
    if isinstance(node, ast.Assert):
```
Run the indented branch only when `isinstance(node, ast.Assert)` is true.

**Line 93**
```python
        return f"Check `{ast.unparse(node.test)}`. If false, stop with an assertion error: the tested expectation failed."
```
Finish this function and evaluate `f'Check `{ast.unparse(node.test)}`. If false, stop with an assertion error: the tested expectation failed.'` using the values currently in memory; send that result to its caller.

**Line 94**
```python
    if isinstance(node, ast.Raise):
```
Run the indented branch only when `isinstance(node, ast.Raise)` is true.

**Line 95**
```python
        return "Stop this operation with the shown exception and message, rather than silently continuing."
```
Finish this function and use the fixed value `'Stop this operation with the shown exception and message, rather than silently continuing.'`; send that result to its caller.

**Line 96**
```python
    if isinstance(node, ast.Try):
```
Run the indented branch only when `isinstance(node, ast.Try)` is true.

**Line 97**
```python
        return "Try the indented work; matching failures are handled by the later `except` branch."
```
Finish this function and use the fixed value `'Try the indented work; matching failures are handled by the later `except` branch.'`; send that result to its caller.

**Line 98**
```python
    if isinstance(node, ast.ExceptHandler):
```
Run the indented branch only when `isinstance(node, ast.ExceptHandler)` is true.

**Line 99**
```python
        return "Handle the specified exception types using the indented recovery code."
```
Finish this function and use the fixed value `'Handle the specified exception types using the indented recovery code.'`; send that result to its caller.

**Line 100**
```python
    if isinstance(node, ast.Continue):
```
Run the indented branch only when `isinstance(node, ast.Continue)` is true.

**Line 101**
```python
        return "Skip the rest of this loop iteration and move to the next item."
```
Finish this function and use the fixed value `'Skip the rest of this loop iteration and move to the next item.'`; send that result to its caller.

**Line 102**
```python
    if isinstance(node, ast.Expr):
```
Run the indented branch only when `isinstance(node, ast.Expr)` is true.

**Line 103**
```python
        return expression(node.value).capitalize() + "."
```
Finish this function and calculate `expression(node.value).capitalize() + '.'`; `/` divides, `*` multiplies, and paths use `/` to join folders; send that result to its caller.

**Line 104**
```python
    return "Continue the enclosing Python statement using the syntax shown."
```
Finish this function and use the fixed value `'Continue the enclosing Python statement using the syntax shown.'`; send that result to its caller.

**Line 105**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 106**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 107**
```python
def main() -> None:
```
Define `main`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 108**
```python
    paths = sorted(path for folder in ("riskgate", "app", "scripts", "tests")
```
Store the result in `paths`: call `sorted` with the inputs shown to obtain its result.

**Line 109**
```python
                   for path in (ROOT / folder).rglob("*.py"))
```
Continuation of the statement starting at line 108; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 110**
```python
    output = ["# Every Python source line explained", "",
```
Store the result in `output`: evaluate `['# Every Python source line explained', '', 'Read [FACULTY_EXPLANATION.md](FACULTY_EXPLANATION.md) first for the system and mathematics.', '', 'This is a generated syntax companion, not a claim that model weights or third-party library internals are explained line by line. Every physical line of our Python source, including tests and this generator, appears below. Long statements are explained at their first line; following lines identify the statement they continue. Source fingerprints let you detect an outdated guide. Regenerate with `./venv/bin/python -m scripts.explain_code`.', '', 'Python basics: indentation groups instructions. `=` stores a value; `==` compares values. A function is a named recipe. A class describes an object. A dictionary holds named values. A list holds ordered values. `None` means missing. `True`/`False` are yes/no. Type hints document expected values; they do not enforce them automatically. An array stores image pixel numbers. `image[y1:y2, x1:x2]` selects rows then columns; the ending coordinates are excluded.', '']` using the values currently in memory.

**Line 111**
```python
              "Read [FACULTY_EXPLANATION.md](FACULTY_EXPLANATION.md) first for the system and mathematics.", "",
```
Continuation of the statement starting at line 110; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 112**
```python
              "This is a generated syntax companion, not a claim that model weights or third-party library internals are explained line by line. Every physical line of our Python source, including tests and this generator, appears below. Long statements are explained at their first line; following lines identify the statement they continue. Source fingerprints let you detect an outdated guide. Regenerate with `./venv/bin/python -m scripts.explain_code`.", "",
```
Continuation of the statement starting at line 110; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 113**
```python
              "Python basics: indentation groups instructions. `=` stores a value; `==` compares values. A function is a named recipe. A class describes an object. A dictionary holds named values. A list holds ordered values. `None` means missing. `True`/`False` are yes/no. Type hints document expected values; they do not enforce them automatically. An array stores image pixel numbers. `image[y1:y2, x1:x2]` selects rows then columns; the ending coordinates are excluded.", ""]
```
Continuation of the statement starting at line 110; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 114**
```python
    for path in paths:
```
For each item from `paths`, name it `path` and run the indented body.

**Line 115**
```python
        source = path.read_text()
```
Store the result in `source`: call `path.read_text` with the inputs shown to obtain its result.

**Line 116**
```python
        relative = path.relative_to(ROOT).as_posix()
```
Store the result in `relative`: call `path.relative_to(ROOT).as_posix` with the inputs shown to obtain its result.

**Line 117**
```python
        tree = ast.parse(source)
```
Store the result in `tree`: call `ast.parse` with the inputs shown to obtain its result.

**Line 118**
```python
        statements = [node for node in ast.walk(tree) if isinstance(node, (ast.stmt, ast.ExceptHandler))]
```
Store the result in `statements`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 119**
```python
        output += [f"## {relative}", "", PURPOSES.get(relative, "Automated checks for the named component." if relative.startswith("tests/") else "Package marker: allows this folder to hold importable modules."), "",
```
Update `output` using the operation shown and the new value.

**Line 120**
```python
                   f"Source SHA-256: `{hashlib.sha256(source.encode()).hexdigest()}`", ""]
```
Continuation of the statement starting at line 119; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 121**
```python
        for number, line in enumerate(source.splitlines(), 1):
```
For each item from `enumerate(source.splitlines(), 1)`, name it `(number, line)` and run the indented body.

**Line 122**
```python
            containing = [node for node in statements if node.lineno <= number <= getattr(node, "end_lineno", node.lineno)]
```
Store the result in `containing`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 123**
```python
            containing.sort(key=lambda node: (getattr(node, "end_lineno", node.lineno) - node.lineno, -node.lineno))
```
Call `containing.sort` with the inputs shown to obtain its result.

**Line 124**
```python
            node = containing[0] if containing else None
```
Store the result in `node`: choose the first value if `containing` is true, otherwise choose the value after `else`.

**Line 125**
```python
            stripped = line.strip()
```
Store the result in `stripped`: call `line.strip` with the inputs shown to obtain its result.

**Line 126**
```python
            if not stripped:
```
Run the indented branch only when `not stripped` is true.

**Line 127**
```python
                note = "Blank line: separates ideas for readability; performs no action."
```
Store the result in `note`: use the fixed value `'Blank line: separates ideas for readability; performs no action.'`.

**Line 128**
```python
            elif stripped.startswith("#"):
```
Run the indented branch only when `stripped.startswith('#')` is true.

**Line 129**
```python
                note = "Comment for the reader; Python does not execute it. " + stripped[1:].strip()
```
Store the result in `note`: calculate `'Comment for the reader; Python does not execute it. ' + stripped[1:].strip()`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 130**
```python
            elif node is not None and node.lineno == number:
```
Run the indented branch only when `node is not None and node.lineno == number` is true.

**Line 131**
```python
                note = explanation(node)
```
Store the result in `note`: call `explanation` with the inputs shown to obtain its result.

**Line 132**
```python
            elif stripped.startswith("else:"):
```
Run the indented branch only when `stripped.startswith('else:')` is true.

**Line 133**
```python
                note = "Run this branch when the associated condition was false."
```
Store the result in `note`: use the fixed value `'Run this branch when the associated condition was false.'`.

**Line 134**
```python
            elif node is not None:
```
Run the indented branch only when `node is not None` is true.

**Line 135**
```python
                note = f"Continuation of the statement starting at line {node.lineno}; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation."
```
Store the result in `note`: evaluate `f"Continuation of the statement starting at line {node.lineno}; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation."` using the values currently in memory.

**Line 136**
```python
            else:
```
Run this branch when the associated condition was false.

**Line 137**
```python
                note = "Decorator or syntax belonging to the following definition; modifies how that definition is used (for example, caching)."
```
Store the result in `note`: use this fixed text block (presentation content, not model logic).

**Line 138**
```python
            output += [f"**Line {number}**", "```python", line, "```", note, ""]
```
Update `output` using the operation shown and the new value.

**Line 139**
```python
        if not source:
```
Run the indented branch only when `not source` is true.

**Line 140**
```python
            output += ["Empty package marker; there are no executable lines.", ""]
```
Update `output` using the operation shown and the new value.

**Line 141**
```python
    for filename in ("requirements.txt", "Makefile", ".gitignore", ".streamlit/config.toml", "presentation/presentation.html"):
```
For each item from `('requirements.txt', 'Makefile', '.gitignore', '.streamlit/config.toml', 'presentation/presentation.html')`, name it `filename` and run the indented body.

**Line 142**
```python
        output += [f"## {filename}", "", "Supporting configuration or presentation source; not part of neural inference.", ""]
```
Update `output` using the operation shown and the new value.

**Line 143**
```python
        for number, line in enumerate((ROOT / filename).read_text().splitlines(), 1):
```
For each item from `enumerate((ROOT / filename).read_text().splitlines(), 1)`, name it `(number, line)` and run the indented body.

**Line 144**
```python
            stripped = line.strip()
```
Store the result in `stripped`: call `line.strip` with the inputs shown to obtain its result.

**Line 145**
```python
            if not stripped:
```
Run the indented branch only when `not stripped` is true.

**Line 146**
```python
                note = "Blank line for readability."
```
Store the result in `note`: use the fixed value `'Blank line for readability.'`.

**Line 147**
```python
            elif filename == "requirements.txt":
```
Run the indented branch only when `filename == 'requirements.txt'` is true.

**Line 148**
```python
                note = f"Install the Python package `{stripped}`. Brackets request optional extras; no version is pinned."
```
Store the result in `note`: evaluate `f'Install the Python package `{stripped}`. Brackets request optional extras; no version is pinned.'` using the values currently in memory.

**Line 149**
```python
            elif filename == ".gitignore":
```
Run the indented branch only when `filename == '.gitignore'` is true.

**Line 150**
```python
                note = f"Exclude paths matching `{stripped}` from ordinary Git tracking; this does not delete existing files."
```
Store the result in `note`: evaluate `f'Exclude paths matching `{stripped}` from ordinary Git tracking; this does not delete existing files.'` using the values currently in memory.

**Line 151**
```python
            elif filename == "Makefile":
```
Run the indented branch only when `filename == 'Makefile'` is true.

**Line 152**
```python
                note = "Declare a command target (or run its indented shell recipe). `check` runs the tests through the project's virtual environment. `.PHONY` ensures a same-named file cannot suppress the command."
```
Store the result in `note`: use this fixed text block (presentation content, not model logic).

**Line 153**
```python
            elif filename.endswith("toml"):
```
Run the indented branch only when `filename.endswith('toml')` is true.

**Line 154**
```python
                note = "Start a settings section with brackets, or assign the shown setting. Theme settings control appearance; maxUploadSize sets Streamlit's per-file upload limit in MB."
```
Store the result in `note`: use this fixed text block (presentation content, not model logic).

**Line 155**
```python
            elif "<section" in line:
```
Run the indented branch only when `'<section' in line` is true.

**Line 156**
```python
                note = "Define one presentation slide. The visible headings, paragraphs, numbers, links, and image references on this line make up its content. Class names select the appearance rules in the style block."
```
Store the result in `note`: use this fixed text block (presentation content, not model logic).

**Line 157**
```python
            elif "<script>" in line:
```
Run the indented branch only when `'<script>' in line` is true.

**Line 158**
```python
                note = "Keep the current slide index; collect slides; move within valid bounds, toggle the active class, update the counter, and listen for left/right/space keys. preventDefault stops space from scrolling."
```
Store the result in `note`: use this fixed text block (presentation content, not model logic).

**Line 159**
```python
            elif "{" in line and "}" in line:
```
Run the indented branch only when `'{' in line and '}' in line` is true.

**Line 160**
```python
                note = "CSS appearance rules: selectors before braces choose elements; name:value declarations set their layout, size, colors, spacing, or print behaviour. They do not process plate images."
```
Store the result in `note`: use this fixed text block (presentation content, not model logic).

**Line 161**
```python
            elif "<div class=" in line:
```
Run the indented branch only when `'<div class=' in line` is true.

**Line 162**
```python
                note = "Render navigation controls and the slide counter; the arrow buttons call move with minus or plus one."
```
Store the result in `note`: use this fixed text block (presentation content, not model logic).

**Line 163**
```python
            else:
```
Run this branch when the associated condition was false.

**Line 164**
```python
                note = "HTML document structure or metadata: opening tags begin an element, closing tags end it; meta tags configure text encoding and viewport; style holds appearance rules."
```
Store the result in `note`: use this fixed text block (presentation content, not model logic).

**Line 165**
```python
            output += [f"**Line {number}**", "```text", line, "```", note, ""]
```
Update `output` using the operation shown and the new value.

**Line 166**
```python
    (ROOT / "docs/CODE_WALKTHROUGH.md").write_text('\n'.join(output))
```
Call `(root / 'docs/code_walkthrough.md').write_text` with the inputs shown to obtain its result.

**Line 167**
```python
    print(f"Explained {len(paths)} Python files")
```
Call `print` with the inputs shown to obtain its result.

**Line 168**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 169**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 170**
```python
if __name__ == "__main__":
```
Run the indented branch only when `__name__ == '__main__'` is true.

**Line 171**
```python
    main()
```
Call `main` with the inputs shown to obtain its result.

## scripts/import_extra_detection.py

Screen the additional box-only source and add eligible photos to detector training.

Source SHA-256: `b83f6459241f959077f845e5fea91d3d709e657d947d72b4b95de48839f259cc`

**Line 1**
```python
"""Add public box-only images to detector training while protecting existing holdouts."""
```
Use the fixed value `'add public box-only images to detector training while protecting existing holdouts.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import csv
```
Make the named library tools available here: `import csv`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
import json
```
Make the named library tools available here: `import json`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python
from pathlib import Path
```
Make the named library tools available here: `from pathlib import Path`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 7**
```python
import cv2
```
Make the named library tools available here: `import cv2`. Importing a project module makes its reusable functions accessible.

**Line 8**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 9**
```python
from riskgate import config
```
Make the named library tools available here: `from riskgate import config`. Importing a project module makes its reusable functions accessible.

**Line 10**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 11**
```python
SOURCE = config.ROOT / "data/extra_detection"
```
Store the result in `SOURCE`: calculate `config.ROOT / 'data/extra_detection'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 12**
```python
OUTPUT = config.ROOT / "data/extra_detection_import.csv"
```
Store the result in `OUTPUT`: calculate `config.ROOT / 'data/extra_detection_import.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 13**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 14**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 15**
```python
def dhash(path: Path) -> int:
```
Define `dhash`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 16**
```python
    image = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
```
Store the result in `image`: call `cv2.imread` with the inputs shown to obtain its result.

**Line 17**
```python
    if image is None:
```
Run the indented branch only when `image is None` is true.

**Line 18**
```python
        raise ValueError(f"Unreadable image: {path}")
```
Stop this operation with the shown exception and message, rather than silently continuing.

**Line 19**
```python
    small = cv2.resize(image, (9, 8))
```
Store the result in `small`: call `cv2.resize` with the inputs shown to obtain its result.

**Line 20**
```python
    bits = (small[:, 1:] > small[:, :-1]).flatten()
```
Store the result in `bits`: call `(small[:, 1:] > small[:, :-1]).flatten` with the inputs shown to obtain its result.

**Line 21**
```python
    value = 0
```
Store the result in `value`: use the fixed value `0`.

**Line 22**
```python
    for bit in bits:
```
For each item from `bits`, name it `bit` and run the indented body.

**Line 23**
```python
        value = (value << 1) | int(bit)
```
Store the result in `value`: calculate `value << 1 | int(bit)`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 24**
```python
    return value
```
Finish this function and evaluate `value` using the values currently in memory; send that result to its caller.

**Line 25**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 26**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 27**
```python
def valid_labels(path: Path) -> bool:
```
Define `valid_labels`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 28**
```python
    try:
```
Try the indented work; matching failures are handled by the later `except` branch.

**Line 29**
```python
        lines = [line.split() for line in path.read_text().splitlines() if line.strip()]
```
Store the result in `lines`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 30**
```python
        return bool(lines) and all(len(line) == 5 and line[0] == "0" and
```
Finish this function and evaluate `bool(lines) and all((len(line) == 5 and line[0] == '0' and all((0 <= float(value) <= 1 for value in line[1:])) and (float(line[3]) > 0) and (float(line[4]) > 0) for line in lines))` using the values currently in memory; send that result to its caller.

**Line 31**
```python
                                   all(0 <= float(value) <= 1 for value in line[1:]) and
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 32**
```python
                                   float(line[3]) > 0 and float(line[4]) > 0 for line in lines)
```
Continuation of the statement starting at line 30; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 33**
```python
    except (OSError, ValueError):
```
Handle the specified exception types using the indented recovery code.

**Line 34**
```python
        return False
```
Finish this function and use the fixed value `False`; send that result to its caller.

**Line 35**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 36**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 37**
```python
def main() -> None:
```
Define `main`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 38**
```python
    splits = json.loads(config.SPLITS_V2.read_text())
```
Store the result in `splits`: call `json.loads` with the inputs shown to obtain its result.

**Line 39**
```python
    protected = set().union(*(set(splits[name]) for name in ("calib", "val", "test")))
```
Store the result in `protected`: call `set().union` with the inputs shown to obtain its result.

**Line 40**
```python
    with (config.ROOT / "data/indian_manifest.csv").open(newline="") as source:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 41**
```python
        holdout_paths = {config.ROOT / row["image_path"] for row in csv.DictReader(source)
```
Store the result in `holdout_paths`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 42**
```python
                         if "kaggle:" + row["group_id"] in protected}
```
Continuation of the statement starting at line 41; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 43**
```python
    holdout_hashes = [dhash(path) for path in sorted(holdout_paths)]
```
Store the result in `holdout_hashes`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 44**
```python
    images = sorted((SOURCE / "images").glob("*.jpg"))
```
Store the result in `images`: call `sorted` with the inputs shown to obtain its result.

**Line 45**
```python
    image_dir = config.ROOT / "data/yolo/images/train"
```
Store the result in `image_dir`: calculate `config.ROOT / 'data/yolo/images/train'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 46**
```python
    label_dir = config.ROOT / "data/yolo/labels/train"
```
Store the result in `label_dir`: calculate `config.ROOT / 'data/yolo/labels/train'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 47**
```python
    image_dir.mkdir(parents=True, exist_ok=True)
```
Call `image_dir.mkdir` with the inputs shown to obtain its result.

**Line 48**
```python
    label_dir.mkdir(parents=True, exist_ok=True)
```
Call `label_dir.mkdir` with the inputs shown to obtain its result.

**Line 49**
```python
    rows = []
```
Store the result in `rows`: evaluate `[]` using the values currently in memory.

**Line 50**
```python
    for path in images:
```
For each item from `images`, name it `path` and run the indented body.

**Line 51**
```python
        label = SOURCE / "labels" / f"{path.stem}.txt"
```
Store the result in `label`: calculate `SOURCE / 'labels' / f'{path.stem}.txt'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 52**
```python
        status = "included"
```
Store the result in `status`: use the fixed value `'included'`.

**Line 53**
```python
        if not valid_labels(label):
```
Run the indented branch only when `not valid_labels(label)` is true.

**Line 54**
```python
            status = "missing_or_invalid_label"
```
Store the result in `status`: use the fixed value `'missing_or_invalid_label'`.

**Line 55**
```python
        else:
```
Run this branch when the associated condition was false.

**Line 56**
```python
            fingerprint = dhash(path)
```
Store the result in `fingerprint`: call `dhash` with the inputs shown to obtain its result.

**Line 57**
```python
            if any((fingerprint ^ other).bit_count() <= 3 for other in holdout_hashes):
```
Run the indented branch only when `any(((fingerprint ^ other).bit_count() <= 3 for other in holdout_hashes))` is true.

**Line 58**
```python
                status = "possible_holdout_duplicate"
```
Store the result in `status`: use the fixed value `'possible_holdout_duplicate'`.

**Line 59**
```python
        if status == "included":
```
Run the indented branch only when `status == 'included'` is true.

**Line 60**
```python
            link = image_dir / f"extra_{path.stem}.jpg"
```
Store the result in `link`: calculate `image_dir / f'extra_{path.stem}.jpg'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 61**
```python
            if not link.exists():
```
Run the indented branch only when `not link.exists()` is true.

**Line 62**
```python
                link.symlink_to(path)
```
Call `link.symlink_to` with the inputs shown to obtain its result.

**Line 63**
```python
            (label_dir / f"extra_{path.stem}.txt").write_text(label.read_text())
```
Call `(label_dir / f'extra_{path.stem}.txt').write_text` with the inputs shown to obtain its result.

**Line 64**
```python
        rows.append({"image_path": str(path.relative_to(config.ROOT)), "status": status})
```
Call `rows.append` with the inputs shown to obtain its result.

**Line 65**
```python
    with OUTPUT.open("w", newline="") as target:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 66**
```python
        writer = csv.DictWriter(target, fieldnames=["image_path", "status"])
```
Store the result in `writer`: call `csv.DictWriter` with the inputs shown to obtain its result.

**Line 67**
```python
        writer.writeheader()
```
Call `writer.writeheader` with the inputs shown to obtain its result.

**Line 68**
```python
        writer.writerows(rows)
```
Call `writer.writerows` with the inputs shown to obtain its result.

**Line 69**
```python
    counts = {status: sum(row["status"] == status for row in rows) for status in sorted({row["status"] for row in rows})}
```
Store the result in `counts`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 70**
```python
    print(json.dumps({"total_full_images": len(images), "status": counts,
```
Call `print` with the inputs shown to obtain its result.

**Line 71**
```python
                      "unlabeled_plate_crops": len(list((SOURCE / "images").glob("*.png")))}, indent=2))
```
Continuation of the statement starting at line 70; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 72**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 73**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 74**
```python
if __name__ == "__main__":
```
Run the indented branch only when `__name__ == '__main__'` is true.

**Line 75**
```python
    main()
```
Call `main` with the inputs shown to obtain its result.

## scripts/label_tool.py

Support manual inspection of proposed labels.

Source SHA-256: `9fbd2a29f668b02c3c4b93589b7543ef530cb16514684c6dc191cd9f157acf12`

**Line 1**
```python
"""Review OCR drafts one crop at a time with Streamlit."""
```
Use the fixed value `'review ocr drafts one crop at a time with streamlit.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import csv
```
Make the named library tools available here: `import csv`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
from pathlib import Path
```
Make the named library tools available here: `from pathlib import Path`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 6**
```python
import streamlit as st
```
Make the named library tools available here: `import streamlit as st`. Importing a project module makes its reusable functions accessible.

**Line 7**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 8**
```python
ROOT = Path(__file__).resolve().parents[1]
```
Store the result in `ROOT`: look up or slice `Path(__file__).resolve().parents` using the index or range in brackets.

**Line 9**
```python
DRAFTS = ROOT / "data/labels/draft_labels.csv"
```
Store the result in `DRAFTS`: calculate `ROOT / 'data/labels/draft_labels.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 10**
```python
LABELS = ROOT / "data/labels/kaggle_labels.csv"
```
Store the result in `LABELS`: calculate `ROOT / 'data/labels/kaggle_labels.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 11**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 12**
```python
st.title("RiskGate plate labeling")
```
Call `st.title` with the inputs shown to obtain its result.

**Line 13**
```python
if not DRAFTS.exists():
```
Run the indented branch only when `not DRAFTS.exists()` is true.

**Line 14**
```python
    st.info("Place draft_labels.csv in data/labels/ with crop_path, group_id, draft columns.")
```
Call `st.info` with the inputs shown to obtain its result.

**Line 15**
```python
    st.stop()
```
Call `st.stop` with the inputs shown to obtain its result.

**Line 16**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 17**
```python
with DRAFTS.open(newline="") as f:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 18**
```python
    drafts = list(csv.DictReader(f))
```
Store the result in `drafts`: call `list` with the inputs shown to obtain its result.

**Line 19**
```python
if not {"crop_path", "group_id", "draft"}.issubset(drafts[0] if drafts else {}):
```
Run the indented branch only when `not {'crop_path', 'group_id', 'draft'}.issubset(drafts[0] if drafts else {})` is true.

**Line 20**
```python
    st.error("draft_labels.csv needs crop_path, group_id, draft columns")
```
Call `st.error` with the inputs shown to obtain its result.

**Line 21**
```python
    st.stop()
```
Call `st.stop` with the inputs shown to obtain its result.

**Line 22**
```python
done = set()
```
Store the result in `done`: call `set` with the inputs shown to obtain its result.

**Line 23**
```python
if LABELS.exists():
```
Run the indented branch only when `LABELS.exists()` is true.

**Line 24**
```python
    with LABELS.open(newline="") as f:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 25**
```python
        done = {r["crop_path"] for r in csv.DictReader(f)}
```
Store the result in `done`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 26**
```python
pending = [r for r in drafts if r["crop_path"] not in done]
```
Store the result in `pending`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 27**
```python
st.write(f"Reviewed: {len(done)} / {len(drafts)}")
```
Call `st.write` with the inputs shown to obtain its result.

**Line 28**
```python
if not pending:
```
Run the indented branch only when `not pending` is true.

**Line 29**
```python
    st.success("All drafts reviewed")
```
Call `st.success` with the inputs shown to obtain its result.

**Line 30**
```python
    st.stop()
```
Call `st.stop` with the inputs shown to obtain its result.

**Line 31**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 32**
```python
row = pending[0]
```
Store the result in `row`: look up or slice `pending` using the index or range in brackets.

**Line 33**
```python
path = ROOT / row["crop_path"]
```
Store the result in `path`: calculate `ROOT / row['crop_path']`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 34**
```python
if not path.exists():
```
Run the indented branch only when `not path.exists()` is true.

**Line 35**
```python
    st.error(f"Missing crop: {path}")
```
Call `st.error` with the inputs shown to obtain its result.

**Line 36**
```python
    st.stop()
```
Call `st.stop` with the inputs shown to obtain its result.

**Line 37**
```python
st.image(str(path), caption=row["crop_path"], width=500)
```
Call `st.image` with the inputs shown to obtain its result.

**Line 38**
```python
with st.form("label"):
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 39**
```python
    correction = st.text_input("Plate text (leave blank to accept draft)", placeholder=row["draft"])
```
Store the result in `correction`: call `st.text_input` with the inputs shown to obtain its result.

**Line 40**
```python
    accept = st.form_submit_button("Save and next")
```
Store the result in `accept`: call `st.form_submit_button` with the inputs shown to obtain its result.

**Line 41**
```python
    skip = st.form_submit_button("Skip unreadable")
```
Store the result in `skip`: call `st.form_submit_button` with the inputs shown to obtain its result.

**Line 42**
```python
if accept or skip:
```
Run the indented branch only when `accept or skip` is true.

**Line 43**
```python
    truth = "" if skip else (correction.strip() or row["draft"].strip())
```
Store the result in `truth`: choose the first value if `skip` is true, otherwise choose the value after `else`.

**Line 44**
```python
    LABELS.parent.mkdir(parents=True, exist_ok=True)
```
Call `labels.parent.mkdir` with the inputs shown to obtain its result.

**Line 45**
```python
    new_file = not LABELS.exists()
```
Store the result in `new_file`: evaluate `not LABELS.exists()` using the values currently in memory.

**Line 46**
```python
    with LABELS.open("a", newline="") as f:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 47**
```python
        writer = csv.DictWriter(f, fieldnames=["crop_path", "group_id", "truth"])
```
Store the result in `writer`: call `csv.DictWriter` with the inputs shown to obtain its result.

**Line 48**
```python
        if new_file:
```
Run the indented branch only when `new_file` is true.

**Line 49**
```python
            writer.writeheader()
```
Call `writer.writeheader` with the inputs shown to obtain its result.

**Line 50**
```python
        writer.writerow({"crop_path": row["crop_path"], "group_id": row["group_id"], "truth": truth})
```
Call `writer.writerow` with the inputs shown to obtain its result.

**Line 51**
```python
    st.rerun()
```
Call `st.rerun` with the inputs shown to obtain its result.

## scripts/package_submission.py

Build the portable academic demo ZIP from an explicit list of folders and assets.

Source SHA-256: `68352e2a64b97ff805030ce49c816864816962ab933966852ca0412d7ed395b5`

**Line 1**
```python
"""Make a portable demo bundle with gallery photos but no bulk dataset or API keys."""
```
Use the fixed value `'make a portable demo bundle with gallery photos but no bulk dataset or api keys.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
from pathlib import Path
```
Make the named library tools available here: `from pathlib import Path`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
from zipfile import ZIP_DEFLATED, ZipFile
```
Make the named library tools available here: `from zipfile import ZIP_DEFLATED, ZipFile`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 6**
```python
from riskgate import config
```
Make the named library tools available here: `from riskgate import config`. Importing a project module makes its reusable functions accessible.

**Line 7**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 8**
```python
ROOT = config.ROOT
```
Store the result in `ROOT`: evaluate `config.ROOT` using the values currently in memory.

**Line 9**
```python
OUTPUT = ROOT / "RiskGate_Submission.zip"
```
Store the result in `OUTPUT`: calculate `ROOT / 'RiskGate_Submission.zip'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 10**
```python
SINGLE = ["README.md", "requirements.txt", "Makefile", "weights/calibration.json", ".streamlit/config.toml"]
```
Store the result in `SINGLE`: evaluate `['README.md', 'requirements.txt', 'Makefile', 'weights/calibration.json', '.streamlit/config.toml']` using the values currently in memory.

**Line 11**
```python
FOLDERS = ["app", "riskgate", "scripts", "docs", "presentation", "weights/fastplate", "data/sample_gallery", "tests"]
```
Store the result in `FOLDERS`: evaluate `['app', 'riskgate', 'scripts', 'docs', 'presentation', 'weights/fastplate', 'data/sample_gallery', 'tests']` using the values currently in memory.

**Line 12**
```python
RESULTS = ["stability_gallery.json", "selected_reader.json", "final_test.json", "end_to_end_test.json",
```
Store the result in `RESULTS`: evaluate `['stability_gallery.json', 'selected_reader.json', 'final_test.json', 'end_to_end_test.json', 'end_to_end_extra.json', 'detector_test.json', 'detector_comparison.json', 'baseline_v2_summary.txt', 'risk_coverage.png', 'reliability.png', 'audit_issues.csv']` using the values currently in memory.

**Line 13**
```python
           "end_to_end_extra.json", "detector_test.json", "detector_comparison.json",
```
Continuation of the statement starting at line 12; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 14**
```python
           "baseline_v2_summary.txt", "risk_coverage.png", "reliability.png", "audit_issues.csv"]
```
Continuation of the statement starting at line 12; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 15**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 16**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 17**
```python
def main() -> None:
```
Define `main`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 18**
```python
    files = [ROOT / name for name in SINGLE]
```
Store the result in `files`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 19**
```python
    for folder in FOLDERS:
```
For each item from `FOLDERS`, name it `folder` and run the indented body.

**Line 20**
```python
        files += [path for path in (ROOT / folder).rglob("*")
```
Update `files` using the operation shown and the new value.

**Line 21**
```python
                  if path.is_file() and "__pycache__" not in path.parts and path.name != "AGENTS.md"]
```
Continuation of the statement starting at line 20; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 22**
```python
    files += [ROOT / "weights/plate_detector.pt"]
```
Update `files` using the operation shown and the new value.

**Line 23**
```python
    files += [ROOT / "results" / name for name in RESULTS]
```
Update `files` using the operation shown and the new value.

**Line 24**
```python
    missing = [str(path.relative_to(ROOT)) for path in files if not path.exists()]
```
Store the result in `missing`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 25**
```python
    if missing:
```
Run the indented branch only when `missing` is true.

**Line 26**
```python
        raise FileNotFoundError(f"Missing required bundle files: {missing}")
```
Stop this operation with the shown exception and message, rather than silently continuing.

**Line 27**
```python
    with ZipFile(OUTPUT, "w", ZIP_DEFLATED, compresslevel=6) as archive:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 28**
```python
        for path in files:
```
For each item from `files`, name it `path` and run the indented body.

**Line 29**
```python
            archive.write(path, path.relative_to(ROOT))
```
Call `archive.write` with the inputs shown to obtain its result.

**Line 30**
```python
    print(f"Created {OUTPUT} ({OUTPUT.stat().st_size / 1024 / 1024:.1f} MiB, {len(files)} files)")
```
Call `print` with the inputs shown to obtain its result.

**Line 31**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 32**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 33**
```python
if __name__ == "__main__":
```
Run the indented branch only when `__name__ == '__main__'` is true.

**Line 34**
```python
    main()
```
Call `main` with the inputs shown to obtain its result.

## scripts/plot_results.py

Draw charts from saved experiment results.

Source SHA-256: `2b6e553003e30e3308ab61b7438c7debc808d37644fb65fe81e6a70ddb90b857`

**Line 1**
```python
"""Make presentation plots without changing the frozen evaluation JSON files."""
```
Use the fixed value `'make presentation plots without changing the frozen evaluation json files.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import csv
```
Make the named library tools available here: `import csv`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 5**
```python
import matplotlib
```
Make the named library tools available here: `import matplotlib`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python
matplotlib.use("Agg")
```
Call `matplotlib.use` with the inputs shown to obtain its result.

**Line 7**
```python
import matplotlib.pyplot as plt
```
Make the named library tools available here: `import matplotlib.pyplot as plt`. Importing a project module makes its reusable functions accessible.

**Line 8**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 9**
```python
from riskgate import config
```
Make the named library tools available here: `from riskgate import config`. Importing a project module makes its reusable functions accessible.

**Line 10**
```python
from riskgate.calibration import load, predict
```
Make the named library tools available here: `from riskgate.calibration import load, predict`. Importing a project module makes its reusable functions accessible.

**Line 11**
```python
from riskgate.metrics import risk_coverage
```
Make the named library tools available here: `from riskgate.metrics import risk_coverage`. Importing a project module makes its reusable functions accessible.

**Line 12**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 13**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 14**
```python
def rows(path):
```
Define `rows`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 15**
```python
    with path.open(newline="") as source:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 16**
```python
        return list(csv.DictReader(source))
```
Finish this function and call `list` with the inputs shown to obtain its result; send that result to its caller.

**Line 17**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 18**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 19**
```python
def style() -> None:
```
Define `style`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 20**
```python
    plt.rcParams.update({"figure.facecolor": "#0c1c2c", "axes.facecolor": "#10283b",
```
Call `plt.rcparams.update` with the inputs shown to obtain its result.

**Line 21**
```python
                         "axes.edgecolor": "#42616f", "axes.labelcolor": "#d8edf0",
```
Continuation of the statement starting at line 20; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 22**
```python
                         "text.color": "#e8f7f5", "xtick.color": "#a9cbd1", "ytick.color": "#a9cbd1",
```
Continuation of the statement starting at line 20; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 23**
```python
                         "grid.color": "#27485a", "font.size": 11})
```
Continuation of the statement starting at line 20; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 24**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 25**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 26**
```python
def main() -> None:
```
Define `main`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 27**
```python
    style()
```
Call `style` with the inputs shown to obtain its result.

**Line 28**
```python
    model = load(config.CALIBRATION_MODEL)
```
Store the result in `model`: call `load` with the inputs shown to obtain its result.

**Line 29**
```python
    cropped = [row for row in rows(config.RESULTS_DIR / "baseline_v2.csv") if row["split"] == "test"]
```
Store the result in `cropped`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 30**
```python
    extra = config.RESULTS_DIR / "end_to_end_extra_details.csv"
```
Store the result in `extra`: calculate `config.RESULTS_DIR / 'end_to_end_extra_details.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 31**
```python
    full = rows(extra if extra.exists() else config.RESULTS_DIR / "end_to_end_details.csv")
```
Store the result in `full`: call `rows` with the inputs shown to obtain its result.

**Line 32**
```python
    crop_conf = [predict(model, row) for row in cropped]
```
Store the result in `crop_conf`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 33**
```python
    crop_ok = [bool(int(row["ok"])) for row in cropped]
```
Store the result in `crop_ok`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 34**
```python
    full_conf = [float(row["confidence"]) for row in full]
```
Store the result in `full_conf`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 35**
```python
    full_ok = [bool(int(row["ok"])) for row in full]
```
Store the result in `full_ok`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 36**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 37**
```python
    fig, ax = plt.subplots(figsize=(7, 4.3))
```
Store the result in `(fig, ax)`: call `plt.subplots` with the inputs shown to obtain its result.

**Line 38**
```python
    for confidence, correct, title, color in ((crop_conf, crop_ok, "Labeled crop", "#5fe6ca"),
```
For each item from `((crop_conf, crop_ok, 'Labeled crop', '#5fe6ca'), (full_conf, full_ok, 'Full vehicle image', '#ffba6b'))`, name it `(confidence, correct, title, color)` and run the indented body.

**Line 39**
```python
                                               (full_conf, full_ok, "Full vehicle image", "#ffba6b")):
```
Continuation of the statement starting at line 38; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 40**
```python
        points = risk_coverage(confidence, correct)
```
Store the result in `points`: call `risk_coverage` with the inputs shown to obtain its result.

**Line 41**
```python
        ax.plot([x for x, _ in points], [y for _, y in points], color=color, linewidth=2.5, label=title)
```
Call `ax.plot` with the inputs shown to obtain its result.

**Line 42**
```python
    ax.set(xlabel="Fraction handled automatically (coverage)", ylabel="Wrong among accepted (risk)",
```
Call `ax.set` with the inputs shown to obtain its result.

**Line 43**
```python
           title="More automation can mean more mistakes", xlim=(0, 1), ylim=(0, 1))
```
Continuation of the statement starting at line 42; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 44**
```python
    ax.grid(alpha=.4)
```
Call `ax.grid` with the inputs shown to obtain its result.

**Line 45**
```python
    ax.legend(facecolor="#173449", edgecolor="#42616f", labelcolor="#e8f7f5")
```
Call `ax.legend` with the inputs shown to obtain its result.

**Line 46**
```python
    fig.tight_layout()
```
Call `fig.tight_layout` with the inputs shown to obtain its result.

**Line 47**
```python
    fig.savefig(config.RESULTS_DIR / "risk_coverage.png", dpi=160)
```
Call `fig.savefig` with the inputs shown to obtain its result.

**Line 48**
```python
    plt.close(fig)
```
Call `plt.close` with the inputs shown to obtain its result.

**Line 49**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 50**
```python
    bins = [i / 8 for i in range(9)]
```
Store the result in `bins`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 51**
```python
    means, accuracy, count = [], [], []
```
Store the result in `(means, accuracy, count)`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 52**
```python
    for left, right in zip(bins[:-1], bins[1:]):
```
For each item from `zip(bins[:-1], bins[1:])`, name it `(left, right)` and run the indented body.

**Line 53**
```python
        indexes = [i for i, value in enumerate(crop_conf) if left <= value < right or right == 1 and value == 1]
```
Store the result in `indexes`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 54**
```python
        if indexes:
```
Run the indented branch only when `indexes` is true.

**Line 55**
```python
            means.append(sum(crop_conf[i] for i in indexes) / len(indexes))
```
Call `means.append` with the inputs shown to obtain its result.

**Line 56**
```python
            accuracy.append(sum(crop_ok[i] for i in indexes) / len(indexes))
```
Call `accuracy.append` with the inputs shown to obtain its result.

**Line 57**
```python
            count.append(len(indexes))
```
Call `count.append` with the inputs shown to obtain its result.

**Line 58**
```python
    fig, ax = plt.subplots(figsize=(7, 4.3))
```
Store the result in `(fig, ax)`: call `plt.subplots` with the inputs shown to obtain its result.

**Line 59**
```python
    ax.plot([0, 1], [0, 1], "--", color="#9db7c0", label="Perfect calibration")
```
Call `ax.plot` with the inputs shown to obtain its result.

**Line 60**
```python
    ax.scatter(means, accuracy, s=[max(40, n*4) for n in count], color="#5fe6ca", alpha=.85,
```
Call `ax.scatter` with the inputs shown to obtain its result.

**Line 61**
```python
               edgecolor="#d8fff5", label="Test bins; size = sample count")
```
Continuation of the statement starting at line 60; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 62**
```python
    ax.set(xlabel="Estimated chance of exact plate", ylabel="Observed exact-match frequency",
```
Call `ax.set` with the inputs shown to obtain its result.

**Line 63**
```python
           title="Does stated confidence match reality?", xlim=(0, 1), ylim=(0, 1))
```
Continuation of the statement starting at line 62; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 64**
```python
    ax.grid(alpha=.4)
```
Call `ax.grid` with the inputs shown to obtain its result.

**Line 65**
```python
    ax.legend(facecolor="#173449", edgecolor="#42616f", labelcolor="#e8f7f5")
```
Call `ax.legend` with the inputs shown to obtain its result.

**Line 66**
```python
    fig.tight_layout()
```
Call `fig.tight_layout` with the inputs shown to obtain its result.

**Line 67**
```python
    fig.savefig(config.RESULTS_DIR / "reliability.png", dpi=160)
```
Call `fig.savefig` with the inputs shown to obtain its result.

**Line 68**
```python
    plt.close(fig)
```
Call `plt.close` with the inputs shown to obtain its result.

**Line 69**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 70**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 71**
```python
if __name__ == "__main__":
```
Run the indented branch only when `__name__ == '__main__'` is true.

**Line 72**
```python
    main()
```
Call `main` with the inputs shown to obtain its result.

## scripts/prepare_gallery.py

Copy selected original demo scenes and write their gallery manifest.

Source SHA-256: `c998c70a4c93be55e29c930e802bf56ad527a7a7cb618c1f109de5fe6969939c`

**Line 1**
```python
"""Copy visually checked full vehicle photos for the noncommercial demo gallery."""
```
Use the fixed value `'copy visually checked full vehicle photos for the noncommercial demo gallery.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import csv
```
Make the named library tools available here: `import csv`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
import shutil
```
Make the named library tools available here: `import shutil`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python
from pathlib import Path
```
Make the named library tools available here: `from pathlib import Path`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 7**
```python
from riskgate import config
```
Make the named library tools available here: `from riskgate import config`. Importing a project module makes its reusable functions accessible.

**Line 8**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 9**
```python
GALLERY = config.ROOT / "data/sample_gallery"
```
Store the result in `GALLERY`: calculate `config.ROOT / 'data/sample_gallery'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 10**
```python
SOURCE = "saisirishan/indian-vehicle-dataset"
```
Store the result in `SOURCE`: use the fixed value `'saisirishan/indian-vehicle-dataset'`.

**Line 11**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 12**
```python
# Every source file is copied unmodified. Crops are made in memory by the app.
```
Comment for the reader; Python does not execute it. Every source file is copied unmodified. Crops are made in memory by the app.

**Line 13**
```python
SCENES = (
```
Store the result in `SCENES`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 14**
```python
    "google_images/0b24d6ed-d32f-420d-bc18-03deece29073___2015-Maruti-Ciaz-Test-Drive-Review.jpg.jpeg",
```
Continuation of the statement starting at line 13; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 15**
```python
    "google_images/2c9306ab-3454-4ca0-89fd-db3f51dabcef___3e7fd381-0ae5-4421-8a70-279ee0ec1c61_Nissan-Terrano-front-three-quarters-on-plain-ground.jpg",
```
Continuation of the statement starting at line 13; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 16**
```python
    "google_images/car-wbs-MH14EH7958_00000.jpeg",
```
Continuation of the statement starting at line 13; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 17**
```python
    "google_images/car-wbs-HR26CT6702_00000.jpeg",
```
Continuation of the statement starting at line 13; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 18**
```python
    "google_images/car-wbs-KA03NA8385_00000.png",
```
Continuation of the statement starting at line 13; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 19**
```python
    "google_images/car-wbs-MH03BS7778_00001.jpeg",
```
Continuation of the statement starting at line 13; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 20**
```python
    "google_images/2424211e-e6ba-4478-8ed1-6a04e25499c7___main-qimg-7673aeac86d0ef987deb837552c5dd4c-1.png",
```
Continuation of the statement starting at line 13; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 21**
```python
    "video_images/video9_360.jpg",
```
Continuation of the statement starting at line 13; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 22**
```python
    "video_images/video11_1150.jpg",
```
Continuation of the statement starting at line 13; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 23**
```python
    "video_images/video10_870.jpg",
```
Continuation of the statement starting at line 13; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 24**
```python
    "video_images/car-wbs-MH01DE2780_00000.png",
```
Continuation of the statement starting at line 13; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 25**
```python
    "google_images/e354039f-d73c-4f12-9df5-f0129345fa79___scorpio.JPG.jpeg",
```
Continuation of the statement starting at line 13; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 26**
```python
)
```
Continuation of the statement starting at line 13; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 27**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 28**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 29**
```python
def main() -> None:
```
Define `main`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 30**
```python
    with (config.ROOT / "data/indian_manifest.csv").open(newline="") as source:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 31**
```python
        labels = {row["image_path"]: row for row in csv.DictReader(source)}
```
Store the result in `labels`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 32**
```python
    GALLERY.mkdir(parents=True, exist_ok=True)
```
Call `gallery.mkdir` with the inputs shown to obtain its result.

**Line 33**
```python
    rows = []
```
Store the result in `rows`: evaluate `[]` using the values currently in memory.

**Line 34**
```python
    for index, relative in enumerate(SCENES, 1):
```
For each item from `enumerate(SCENES, 1)`, name it `(index, relative)` and run the indented body.

**Line 35**
```python
        source_path = config.ROOT / "data/indian" / relative
```
Store the result in `source_path`: calculate `config.ROOT / 'data/indian' / relative`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 36**
```python
        row = labels[str(source_path.relative_to(config.ROOT))]
```
Store the result in `row`: look up or slice `labels` using the index or range in brackets.

**Line 37**
```python
        target = GALLERY / f"scene_{index:02d}{source_path.suffix.lower()}"
```
Store the result in `target`: calculate `GALLERY / f'scene_{index:02d}{source_path.suffix.lower()}'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 38**
```python
        shutil.copy2(source_path, target)
```
Call `shutil.copy2` with the inputs shown to obtain its result.

**Line 39**
```python
        rows.append({"image_path": str(target.relative_to(config.ROOT)), "truth": row["truth"],
```
Call `rows.append` with the inputs shown to obtain its result.

**Line 40**
```python
                     "xmin": row["xmin"], "ymin": row["ymin"],
```
Continuation of the statement starting at line 39; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 41**
```python
                     "xmax": row["xmax"], "ymax": row["ymax"],
```
Continuation of the statement starting at line 39; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 42**
```python
                     "label_source": "xml_text_visually_checked", "source": SOURCE,
```
Continuation of the statement starting at line 39; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 43**
```python
                     "license": "CC BY-NC-ND 4.0"})
```
Continuation of the statement starting at line 39; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 44**
```python
    with (GALLERY / "manifest.csv").open("w", newline="") as target:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 45**
```python
        writer = csv.DictWriter(target, fieldnames=list(rows[0]))
```
Store the result in `writer`: call `csv.DictWriter` with the inputs shown to obtain its result.

**Line 46**
```python
        writer.writeheader()
```
Call `writer.writeheader` with the inputs shown to obtain its result.

**Line 47**
```python
        writer.writerows(rows)
```
Call `writer.writerows` with the inputs shown to obtain its result.

**Line 48**
```python
    print(f"Prepared {len(rows)} full vehicle scenes in {GALLERY}")
```
Call `print` with the inputs shown to obtain its result.

**Line 49**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 50**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 51**
```python
if __name__ == "__main__":
```
Run the indented branch only when `__name__ == '__main__'` is true.

**Line 52**
```python
    main()
```
Call `main` with the inputs shown to obtain its result.

## scripts/prepare_indian.py

Read the main dataset, group related examples, and prepare labels and splits.

Source SHA-256: `cf09f1719705b2223271631c7be7a0999260fbb505f6760e5cae7b29e14e0c99`

**Line 1**
```python
"""Create crops and a reproducible manifest from the downloaded image/XML pairs."""
```
Use the fixed value `'create crops and a reproducible manifest from the downloaded image/xml pairs.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
import csv
```
Make the named library tools available here: `import csv`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
import json
```
Make the named library tools available here: `import json`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python
import re
```
Make the named library tools available here: `import re`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python
import xml.etree.ElementTree as ET
```
Make the named library tools available here: `import xml.etree.ElementTree as ET`. Importing a project module makes its reusable functions accessible.

**Line 7**
```python
from pathlib import Path
```
Make the named library tools available here: `from pathlib import Path`. Importing a project module makes its reusable functions accessible.

**Line 8**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 9**
```python
import cv2
```
Make the named library tools available here: `import cv2`. Importing a project module makes its reusable functions accessible.

**Line 10**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 11**
```python
from riskgate import config
```
Make the named library tools available here: `from riskgate import config`. Importing a project module makes its reusable functions accessible.

**Line 12**
```python
from riskgate.metrics import normalize
```
Make the named library tools available here: `from riskgate.metrics import normalize`. Importing a project module makes its reusable functions accessible.

**Line 13**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 14**
```python
SOURCE = config.ROOT / "data/indian"
```
Store the result in `SOURCE`: calculate `config.ROOT / 'data/indian'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 15**
```python
XML_LABELS = config.ROOT / "data/labels/kaggle_xml_labels.csv"
```
Store the result in `XML_LABELS`: calculate `config.ROOT / 'data/labels/kaggle_xml_labels.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 16**
```python
DRAFTS = config.DRAFTS
```
Store the result in `DRAFTS`: evaluate `config.DRAFTS` using the values currently in memory.

**Line 17**
```python
MANIFEST = config.ROOT / "data/indian_manifest.csv"
```
Store the result in `MANIFEST`: calculate `config.ROOT / 'data/indian_manifest.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 18**
```python
CROPS = config.ROOT / "data/crops/indian"
```
Store the result in `CROPS`: calculate `config.ROOT / 'data/crops/indian'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 19**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 20**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 21**
```python
def video_key(path: Path) -> str | None:
```
Define `video_key`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 22**
```python
    if path.parts[0] != "video_images":
```
Run the indented branch only when `path.parts[0] != 'video_images'` is true.

**Line 23**
```python
        return None
```
Finish this function and use the fixed value `None`; send that result to its caller.

**Line 24**
```python
    stem = path.stem
```
Store the result in `stem`: evaluate `path.stem` using the values currently in memory.

**Line 25**
```python
    if re.match(r"video\d+_\d+$", stem):
```
Run the indented branch only when `re.match('video\\d+_\\d+$', stem)` is true.

**Line 26**
```python
        return stem.split("_")[0]
```
Finish this function and look up or slice `stem.split('_')` using the index or range in brackets; send that result to its caller.

**Line 27**
```python
    if re.search(r"_\d{5}$", stem):
```
Run the indented branch only when `re.search('_\\d{5}$', stem)` is true.

**Line 28**
```python
        return stem.rsplit("_", 1)[0]
```
Finish this function and look up or slice `stem.rsplit('_', 1)` using the index or range in brackets; send that result to its caller.

**Line 29**
```python
    return stem
```
Finish this function and evaluate `stem` using the values currently in memory; send that result to its caller.

**Line 30**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 31**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 32**
```python
def records() -> list[dict]:
```
Define `records`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 33**
```python
    rows = []
```
Store the result in `rows`: evaluate `[]` using the values currently in memory.

**Line 34**
```python
    for xml_path in sorted(SOURCE.rglob("*.xml")):
```
For each item from `sorted(SOURCE.rglob('*.xml'))`, name it `xml_path` and run the indented body.

**Line 35**
```python
        rel = xml_path.relative_to(SOURCE)
```
Store the result in `rel`: call `xml_path.relative_to` with the inputs shown to obtain its result.

**Line 36**
```python
        root = ET.parse(xml_path).getroot()
```
Store the result in `root`: call `ET.parse(xml_path).getroot` with the inputs shown to obtain its result.

**Line 37**
```python
        image_path = xml_path.parent / (root.findtext("filename") or "")
```
Store the result in `image_path`: calculate `xml_path.parent / (root.findtext('filename') or '')`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 38**
```python
        if not image_path.is_file():
```
Run the indented branch only when `not image_path.is_file()` is true.

**Line 39**
```python
            print(f"Skipping missing image for {rel}")
```
Call `print` with the inputs shown to obtain its result.

**Line 40**
```python
            continue
```
Skip the rest of this loop iteration and move to the next item.

**Line 41**
```python
        image = cv2.imread(str(image_path))
```
Store the result in `image`: call `cv2.imread` with the inputs shown to obtain its result.

**Line 42**
```python
        if image is None:
```
Run the indented branch only when `image is None` is true.

**Line 43**
```python
            continue
```
Skip the rest of this loop iteration and move to the next item.

**Line 44**
```python
        height, width = image.shape[:2]
```
Store the result in `(height, width)`: look up or slice `image.shape` using the index or range in brackets.

**Line 45**
```python
        for index, obj in enumerate(root.findall("object")):
```
For each item from `enumerate(root.findall('object'))`, name it `(index, obj)` and run the indented body.

**Line 46**
```python
            truth = normalize(obj.findtext("name") or "")
```
Store the result in `truth`: uppercase the text and keep only letters A–Z and digits 0–9.

**Line 47**
```python
            box = obj.find("bndbox")
```
Store the result in `box`: call `obj.find` with the inputs shown to obtain its result.

**Line 48**
```python
            if not truth or box is None:
```
Run the indented branch only when `not truth or box is None` is true.

**Line 49**
```python
                continue
```
Skip the rest of this loop iteration and move to the next item.

**Line 50**
```python
            x1, y1, x2, y2 = [int(float(box.findtext(key) or 0)) for key in ("xmin", "ymin", "xmax", "ymax")]
```
Store the result in `(x1, y1, x2, y2)`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 51**
```python
            x1, x2 = max(0, x1), min(width, x2)
```
Store the result in `(x1, x2)`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 52**
```python
            y1, y2 = max(0, y1), min(height, y2)
```
Store the result in `(y1, y2)`: collect the values in order (a tuple), which can also be unpacked into separate names.

**Line 53**
```python
            if x2 <= x1 or y2 <= y1:
```
Run the indented branch only when `x2 <= x1 or y2 <= y1` is true.

**Line 54**
```python
                continue
```
Skip the rest of this loop iteration and move to the next item.

**Line 55**
```python
            crop_path = CROPS / f"{rel.with_suffix('').as_posix().replace('/', '__')}_{index}.jpg"
```
Store the result in `crop_path`: calculate `CROPS / f"{rel.with_suffix('').as_posix().replace('/', '__')}_{index}.jpg"`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 56**
```python
            crop_path.parent.mkdir(parents=True, exist_ok=True)
```
Call `crop_path.parent.mkdir` with the inputs shown to obtain its result.

**Line 57**
```python
            cv2.imwrite(str(crop_path), image[y1:y2, x1:x2])
```
Call `cv2.imwrite` with the inputs shown to obtain its result.

**Line 58**
```python
            rows.append({"image_path": str(image_path.relative_to(config.ROOT)),
```
Call `rows.append` with the inputs shown to obtain its result.

**Line 59**
```python
                         "crop_path": str(crop_path.relative_to(config.ROOT)),
```
Continuation of the statement starting at line 58; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 60**
```python
                         "truth": truth, "source_detail": rel.parts[0],
```
Continuation of the statement starting at line 58; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 61**
```python
                         "video_key": video_key(rel), "xmin": x1, "ymin": y1,
```
Continuation of the statement starting at line 58; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 62**
```python
                         "xmax": x2, "ymax": y2})
```
Continuation of the statement starting at line 58; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 63**
```python
    return rows
```
Finish this function and evaluate `rows` using the values currently in memory; send that result to its caller.

**Line 64**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 65**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 66**
```python
def assign_groups(rows: list[dict]) -> None:
```
Define `assign_groups`; its indented body runs when called. Connect samples sharing a plate text or a source video.

**Line 67**
```python
    """Connect samples sharing a plate text or a source video."""
```
Use the fixed value `'connect samples sharing a plate text or a source video.'`.

**Line 68**
```python
    parent = list(range(len(rows)))
```
Store the result in `parent`: call `list` with the inputs shown to obtain its result.

**Line 69**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 70**
```python
    def root(i: int) -> int:
```
Define `root`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 71**
```python
        while parent[i] != i:
```
Continue the enclosing Python statement using the syntax shown.

**Line 72**
```python
            parent[i] = parent[parent[i]]
```
Store the result in `parent[i]`: look up or slice `parent` using the index or range in brackets.

**Line 73**
```python
            i = parent[i]
```
Store the result in `i`: look up or slice `parent` using the index or range in brackets.

**Line 74**
```python
        return i
```
Finish this function and evaluate `i` using the values currently in memory; send that result to its caller.

**Line 75**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 76**
```python
    seen = {}
```
Store the result in `seen`: build a dictionary: each key names the value stored beside it.

**Line 77**
```python
    for i, row in enumerate(rows):
```
For each item from `enumerate(rows)`, name it `(i, row)` and run the indented body.

**Line 78**
```python
        keys = ["plate:" + row["truth"]]
```
Store the result in `keys`: evaluate `['plate:' + row['truth']]` using the values currently in memory.

**Line 79**
```python
        if row["video_key"]:
```
Run the indented branch only when `row['video_key']` is true.

**Line 80**
```python
            keys.append("video:" + row["video_key"])
```
Call `keys.append` with the inputs shown to obtain its result.

**Line 81**
```python
        for key in keys:
```
For each item from `keys`, name it `key` and run the indented body.

**Line 82**
```python
            if key in seen:
```
Run the indented branch only when `key in seen` is true.

**Line 83**
```python
                parent[root(i)] = root(seen[key])
```
Store the result in `parent[root(i)]`: call `root` with the inputs shown to obtain its result.

**Line 84**
```python
            seen[key] = i
```
Store the result in `seen[key]`: evaluate `i` using the values currently in memory.

**Line 85**
```python
    for i, row in enumerate(rows):
```
For each item from `enumerate(rows)`, name it `(i, row)` and run the indented body.

**Line 86**
```python
        row["group_id"] = f"g{root(i):04d}"
```
Store the result in `row['group_id']`: evaluate `f'g{root(i):04d}'` using the values currently in memory.

**Line 87**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 88**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 89**
```python
def write_csv(path: Path, rows: list[dict], columns: list[str]) -> None:
```
Define `write_csv`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 90**
```python
    path.parent.mkdir(parents=True, exist_ok=True)
```
Call `path.parent.mkdir` with the inputs shown to obtain its result.

**Line 91**
```python
    with path.open("w", newline="") as output:
```
Enter the shown context: an open file is closed afterwards; a Streamlit context places widgets inside that panel.

**Line 92**
```python
        writer = csv.DictWriter(output, fieldnames=columns)
```
Store the result in `writer`: call `csv.DictWriter` with the inputs shown to obtain its result.

**Line 93**
```python
        writer.writeheader()
```
Call `writer.writeheader` with the inputs shown to obtain its result.

**Line 94**
```python
        writer.writerows({key: row.get(key, "") for key in columns} for row in rows)
```
Call `writer.writerows` with the inputs shown to obtain its result.

**Line 95**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 96**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 97**
```python
def main() -> None:
```
Define `main`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 98**
```python
    rows = records()
```
Store the result in `rows`: call `records` with the inputs shown to obtain its result.

**Line 99**
```python
    if not rows:
```
Run the indented branch only when `not rows` is true.

**Line 100**
```python
        raise ValueError(f"No usable image/XML pairs found in {SOURCE}")
```
Stop this operation with the shown exception and message, rather than silently continuing.

**Line 101**
```python
    assign_groups(rows)
```
Call `assign_groups` with the inputs shown to obtain its result.

**Line 102**
```python
    write_csv(MANIFEST, rows, list(rows[0]))
```
Call `write_csv` with the inputs shown to obtain its result.

**Line 103**
```python
    write_csv(XML_LABELS, rows, ["crop_path", "group_id", "truth"])
```
Call `write_csv` with the inputs shown to obtain its result.

**Line 104**
```python
    write_csv(DRAFTS, [{**row, "draft": row["truth"]} for row in rows],
```
Call `write_csv` with the inputs shown to obtain its result.

**Line 105**
```python
              ["crop_path", "group_id", "draft"])
```
Continuation of the statement starting at line 104; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 106**
```python
    print(json.dumps({"images": len({row['image_path'] for row in rows}),
```
Call `print` with the inputs shown to obtain its result.

**Line 107**
```python
                      "plates": len(rows), "groups": len({row['group_id'] for row in rows}),
```
Continuation of the statement starting at line 106; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 108**
```python
                      "source_counts": {source: sum(row["source_detail"] == source for row in rows)
```
Continuation of the statement starting at line 106; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 109**
```python
                                        for source in sorted({row["source_detail"] for row in rows})}}, indent=2))
```
Continuation of the statement starting at line 106; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 110**
```python
    print("Labels came from XML annotations and still need visual auditing.")
```
Call `print` with the inputs shown to obtain its result.

**Line 111**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 112**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 113**
```python
if __name__ == "__main__":
```
Run the indented branch only when `__name__ == '__main__'` is true.

**Line 114**
```python
    main()
```
Call `main` with the inputs shown to obtain its result.

## tests/test_calibration_router.py

Automated checks for the named component.

Source SHA-256: `eb88d7dd2990e0a080ea39ce32c68dc667ed12ff316f51bf6f01a357cba5b392`

**Line 1**
```python
from riskgate.calibration import fit, predict
```
Make the named library tools available here: `from riskgate.calibration import fit, predict`. Importing a project module makes its reusable functions accessible.

**Line 2**
```python
from riskgate.features import FEATURE_NAMES
```
Make the named library tools available here: `from riskgate.features import FEATURE_NAMES`. Importing a project module makes its reusable functions accessible.

**Line 3**
```python
from riskgate.router import choose_thresholds, route, wilson_interval
```
Make the named library tools available here: `from riskgate.router import choose_thresholds, route, wilson_interval`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 5**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 6**
```python
def test_calibrator_roundtrip():
```
Define `test_calibrator_roundtrip`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 7**
```python
    rows = [{**dict.fromkeys(FEATURE_NAMES, float(i % 5)), "ok": int(i % 2), "image": str(i)}
```
Store the result in `rows`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 8**
```python
            for i in range(30)]
```
Continuation of the statement starting at line 7; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 9**
```python
    model = fit(rows)
```
Store the result in `model`: learn the calibration parameters.

**Line 10**
```python
    assert set(model["feature_names"]) == set(FEATURE_NAMES)
```
Check `set(model['feature_names']) == set(FEATURE_NAMES)`. If false, stop with an assertion error: the tested expectation failed.

**Line 11**
```python
    assert 0 <= predict(model, rows[0]) <= 1
```
Check `0 <= predict(model, rows[0]) <= 1`. If false, stop with an assertion error: the tested expectation failed.

**Line 12**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 13**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 14**
```python
def test_wilson_and_invalid_rule():
```
Define `test_wilson_and_invalid_rule`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 15**
```python
    assert wilson_interval(0, 100)[1] < 0.05
```
Check `wilson_interval(0, 100)[1] < 0.05`. If false, stop with an assertion error: the tested expectation failed.

**Line 16**
```python
    rows = [{"pred": "KA01AB1234", "calibrated_conf": i / 100, "ok": 1}
```
Store the result in `rows`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 17**
```python
            for i in range(100)]
```
Continuation of the statement starting at line 16; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 18**
```python
    thresholds = choose_thresholds(rows)
```
Store the result in `thresholds`: call `choose_thresholds` with the inputs shown to obtain its result.

**Line 19**
```python
    assert thresholds["0.05"]["accept_at"] is not None
```
Check `thresholds['0.05']['accept_at'] is not None`. If false, stop with an assertion error: the tested expectation failed.

**Line 20**
```python
    assert route("junk", 1.0, thresholds["0.05"]) != "ACCEPT"
```
Check `route('junk', 1.0, thresholds['0.05']) != 'ACCEPT'`. If false, stop with an assertion error: the tested expectation failed.

## tests/test_demo.py

Automated checks for the named component.

Source SHA-256: `5f6d312d51713f477d7409b02a8af952f192f075f31f803285ce87aa3c3cf491`

**Line 1**
```python
"""The packaged demo can analyze a real vehicle scene offline."""
```
Use the fixed value `'the packaged demo can analyze a real vehicle scene offline.'`.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
from pathlib import Path
```
Make the named library tools available here: `from pathlib import Path`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 5**
```python
import pytest
```
Make the named library tools available here: `import pytest`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python
from streamlit.testing.v1 import AppTest
```
Make the named library tools available here: `from streamlit.testing.v1 import AppTest`. Importing a project module makes its reusable functions accessible.

**Line 7**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 8**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 9**
```python
ROOT = Path(__file__).resolve().parents[1]
```
Store the result in `ROOT`: look up or slice `Path(__file__).resolve().parents` using the index or range in brackets.

**Line 10**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 11**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 12**
```python
@pytest.mark.skipif(
```
Decorator or syntax belonging to the following definition; modifies how that definition is used (for example, caching).

**Line 13**
```python
    not (ROOT / "weights/plate_detector.pt").exists()
```
Decorator or syntax belonging to the following definition; modifies how that definition is used (for example, caching).

**Line 14**
```python
    or not (ROOT / "data/sample_gallery/manifest.csv").exists(),
```
Decorator or syntax belonging to the following definition; modifies how that definition is used (for example, caching).

**Line 15**
```python
    reason="local demo assets are not installed",
```
Decorator or syntax belonging to the following definition; modifies how that definition is used (for example, caching).

**Line 16**
```python
)
```
Decorator or syntax belonging to the following definition; modifies how that definition is used (for example, caching).

**Line 17**
```python
def test_gallery_photo_runs_without_error() -> None:
```
Define `test_gallery_photo_runs_without_error`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 18**
```python
    app = AppTest.from_file(str(ROOT / "app/streamlit_app.py"), default_timeout=90).run()
```
Store the result in `app`: call `AppTest.from_file(str(ROOT / 'app/streamlit_app.py'), default_timeout=90).run` with the inputs shown to obtain its result.

**Line 19**
```python
    app.radio[1].set_value("Demo gallery").run()
```
Call `app.radio[1].set_value('demo gallery').run` with the inputs shown to obtain its result.

**Line 20**
```python
    app.button[0].click().run()
```
Call `app.button[0].click().run` with the inputs shown to obtain its result.

**Line 21**
```python
    assert not app.exception
```
Check `not app.exception`. If false, stop with an assertion error: the tested expectation failed.

**Line 22**
```python
    assert app.session_state["analysis"]["text"] == "RJ27TC0530"
```
Check `app.session_state['analysis']['text'] == 'RJ27TC0530'`. If false, stop with an assertion error: the tested expectation failed.

**Line 23**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 24**
```python
    assert app.session_state["analysis"]["stability"] is None
```
Check `app.session_state['analysis']['stability'] is None`. If false, stop with an assertion error: the tested expectation failed.

**Line 25**
```python
    app.checkbox[0].check().run()
```
Call `app.checkbox[0].check().run` with the inputs shown to obtain its result.

**Line 26**
```python
    app.button[0].click().run()
```
Call `app.button[0].click().run` with the inputs shown to obtain its result.

**Line 27**
```python
    assert not app.exception
```
Check `not app.exception`. If false, stop with an assertion error: the tested expectation failed.

**Line 28**
```python
    result = app.session_state["analysis"]
```
Store the result in `result`: look up or slice `app.session_state` using the index or range in brackets.

**Line 29**
```python
    assert result["stability"]["variant_count"] == 2
```
Check `result['stability']['variant_count'] == 2`. If false, stop with an assertion error: the tested expectation failed.

**Line 30**
```python
    assert len(result["stability"]["readings"]) == 2
```
Check `len(result['stability']['readings']) == 2`. If false, stop with an assertion error: the tested expectation failed.

**Line 31**
```python
    assert result["route"] in (result["base_route"], "REVIEW")
```
Check `result['route'] in (result['base_route'], 'REVIEW')`. If false, stop with an assertion error: the tested expectation failed.

## tests/test_features.py

Automated checks for the named component.

Source SHA-256: `cfb1d09e8b085728da6b39fb89e739118e9384944c88dea7ce48960efbbdb1f2`

**Line 1**
```python
import numpy as np
```
Make the named library tools available here: `import numpy as np`. Importing a project module makes its reusable functions accessible.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
from riskgate.contracts import EngineResult
```
Make the named library tools available here: `from riskgate.contracts import EngineResult`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
from riskgate.features import plate_features
```
Make the named library tools available here: `from riskgate.features import plate_features`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 6**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 7**
```python
def test_features():
```
Define `test_features`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 8**
```python
    f = plate_features(np.zeros((20, 60, 3), dtype=np.uint8),
```
Store the result in `f`: extract the six input signals from the crop and OCR result.

**Line 9**
```python
                       EngineResult("KA01AB1234", 0.8, 1.0, boxes_found=2))
```
Continuation of the statement starting at line 8; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 10**
```python
    assert f == {"raw_conf": 0.8, "grammar": 2.0, "text_length": 10.0,
```
Check `f == {'raw_conf': 0.8, 'grammar': 2.0, 'text_length': 10.0, 'crop_height': 20.0, 'crop_width': 60.0, 'boxes_found': 2.0}`. If false, stop with an assertion error: the tested expectation failed.

**Line 11**
```python
                 "crop_height": 20.0, "crop_width": 60.0, "boxes_found": 2.0}
```
Continuation of the statement starting at line 10; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

## tests/test_grammar.py

Automated checks for the named component.

Source SHA-256: `78658e12657924e061642bc3dcc7fc3b134a678e46ac1ab574ce0068326e8e92`

**Line 1**
```python
from riskgate.grammar import classify
```
Make the named library tools available here: `from riskgate.grammar import classify`. Importing a project module makes its reusable functions accessible.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
# 10 valid (hand-checked against the two formats)
```
Comment for the reader; Python does not execute it. 10 valid (hand-checked against the two formats)

**Line 4**
```python
VALID = [
```
Store the result in `VALID`: evaluate `['KL34A4651', 'MH12DE1234', 'DL3CD1210', 'RJ14AB1234', 'KA01AJ7533', 'TN58D5353', 'MP07L7524', 'KL35F4337', '22BH1234A', '22BH1234AB']` using the values currently in memory.

**Line 5**
```python
    "KL34A4651",
```
Continuation of the statement starting at line 4; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 6**
```python
    "MH12DE1234",
```
Continuation of the statement starting at line 4; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 7**
```python
    "DL3CD1210",
```
Continuation of the statement starting at line 4; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 8**
```python
    "RJ14AB1234",
```
Continuation of the statement starting at line 4; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 9**
```python
    "KA01AJ7533",
```
Continuation of the statement starting at line 4; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 10**
```python
    "TN58D5353",
```
Continuation of the statement starting at line 4; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 11**
```python
    "MP07L7524",
```
Continuation of the statement starting at line 4; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 12**
```python
    "KL35F4337",
```
Continuation of the statement starting at line 4; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 13**
```python
    "22BH1234A",
```
Continuation of the statement starting at line 4; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 14**
```python
    "22BH1234AB",
```
Continuation of the statement starting at line 4; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 15**
```python
]
```
Continuation of the statement starting at line 4; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 16**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 17**
```python
# 10 invalid (not plate-like: empty, too short, digits only, letters only, garbage)
```
Comment for the reader; Python does not execute it. 10 invalid (not plate-like: empty, too short, digits only, letters only, garbage)

**Line 18**
```python
INVALID = ["", "  ", "1234", "12345", "A", "AB", "1A", "ABCDEFGH", "@#$%", "246802"]
```
Store the result in `INVALID`: evaluate `['', '  ', '1234', '12345', 'A', 'AB', '1A', 'ABCDEFGH', '@#$%', '246802']` using the values currently in memory.

**Line 19**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 20**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 21**
```python
def test_valid():
```
Define `test_valid`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 22**
```python
    for s in VALID:
```
For each item from `VALID`, name it `s` and run the indented body.

**Line 23**
```python
        assert classify(s) == "VALID", s
```
Check `classify(s) == 'VALID'`. If false, stop with an assertion error: the tested expectation failed.

**Line 24**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 25**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 26**
```python
def test_nonstandard():
```
Define `test_nonstandard`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 27**
```python
    # plate-like (>=6 alnum, both letters+digits) but off-format
```
Comment for the reader; Python does not execute it. plate-like (>=6 alnum, both letters+digits) but off-format

**Line 28**
```python
    assert classify("KL41L7OOT") == "NONSTANDARD"
```
Check `classify('KL41L7OOT') == 'NONSTANDARD'`. If false, stop with an assertion error: the tested expectation failed.

**Line 29**
```python
    assert classify("INDKL07BX7197") == "NONSTANDARD"
```
Check `classify('INDKL07BX7197') == 'NONSTANDARD'`. If false, stop with an assertion error: the tested expectation failed.

**Line 30**
```python
    assert classify("409C2768") == "NONSTANDARD"
```
Check `classify('409C2768') == 'NONSTANDARD'`. If false, stop with an assertion error: the tested expectation failed.

**Line 31**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 32**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 33**
```python
def test_invalid():
```
Define `test_invalid`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 34**
```python
    for s in INVALID:
```
For each item from `INVALID`, name it `s` and run the indented body.

**Line 35**
```python
        assert classify(s) == "INVALID", s
```
Check `classify(s) == 'INVALID'`. If false, stop with an assertion error: the tested expectation failed.

**Line 36**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 37**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 38**
```python
def test_no_correction():
```
Define `test_no_correction`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 39**
```python
    # classify must never "fix" text - close-but-wrong stays NONSTANDARD, not VALID
```
Comment for the reader; Python does not execute it. classify must never "fix" text - close-but-wrong stays NONSTANDARD, not VALID

**Line 40**
```python
    assert classify("KL34A46") != "VALID"
```
Check `classify('KL34A46') != 'VALID'`. If false, stop with an assertion error: the tested expectation failed.

## tests/test_leakage.py

Automated checks for the named component.

Source SHA-256: `b19b161a4133bd7f0d3c2900d512a6ec0cc45acf1ef3b9d52c17af5ded790b7b`

**Line 1**
```python
from pathlib import Path
```
Make the named library tools available here: `from pathlib import Path`. Importing a project module makes its reusable functions accessible.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
from riskgate.contracts import PlateSample
```
Make the named library tools available here: `from riskgate.contracts import PlateSample`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
from riskgate.data import make_splits_v2
```
Make the named library tools available here: `from riskgate.data import make_splits_v2`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 6**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 7**
```python
def test_group_split_keeps_sources_and_images_apart(tmp_path: Path):
```
Define `test_group_split_keeps_sources_and_images_apart`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 8**
```python
    samples = [PlateSample(f"{i}_{j}.jpg", (0, 0, 1, 1), "AB12", "kaggle", f"kaggle:{i}")
```
Store the result in `samples`: build or iterate values using the inline `for` loop and any `if` filter shown.

**Line 9**
```python
               for i in range(10) for j in range(2)]
```
Continuation of the statement starting at line 8; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 10**
```python
    samples.append(PlateSample("d.jpg", (0, 0, 1, 1), "AB12", "datacluster", "datacluster:d"))
```
Call `samples.append` with the inputs shown to obtain its result.

**Line 11**
```python
    splits = make_splits_v2(samples, tmp_path / "splits_v2.json")
```
Store the result in `splits`: call `make_splits_v2` with the inputs shown to obtain its result.

**Line 12**
```python
    assert len(set().union(*(set(v) for v in splits.values()))) == sum(map(len, splits.values()))
```
Check `len(set().union(*(set(v) for v in splits.values()))) == sum(map(len, splits.values()))`. If false, stop with an assertion error: the tested expectation failed.

**Line 13**
```python
    assert all(splits[name] for name in ("train", "calib", "val", "test"))
```
Check `all((splits[name] for name in ('train', 'calib', 'val', 'test')))`. If false, stop with an assertion error: the tested expectation failed.

**Line 14**
```python
    assert splits["cross_dataset_test"] == ["datacluster:d"]
```
Check `splits['cross_dataset_test'] == ['datacluster:d']`. If false, stop with an assertion error: the tested expectation failed.

## tests/test_metrics.py

Automated checks for the named component.

Source SHA-256: `37ae6aa4a37674b65931844ecdd88a0b4430e071bb2e2379bcc350a2f2e0a5ad`

**Line 1**
```python
from riskgate.metrics import cer, ece, exact_match, normalize, risk_coverage
```
Make the named library tools available here: `from riskgate.metrics import cer, ece, exact_match, normalize, risk_coverage`. Importing a project module makes its reusable functions accessible.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 4**
```python
def test_normalize():
```
Define `test_normalize`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 5**
```python
    assert normalize("  kl-34.a 465 ") == "KL34A465"
```
Check `normalize('  kl-34.a 465 ') == 'KL34A465'`. If false, stop with an assertion error: the tested expectation failed.

**Line 6**
```python
    assert normalize("b@h!22") == "BH22"
```
Check `normalize('b@h!22') == 'BH22'`. If false, stop with an assertion error: the tested expectation failed.

**Line 7**
```python
    assert normalize("") == ""
```
Check `normalize('') == ''`. If false, stop with an assertion error: the tested expectation failed.

**Line 8**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 9**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 10**
```python
def test_exact_match():
```
Define `test_exact_match`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 11**
```python
    assert exact_match("Kl34-A465", "KL34A465") is True
```
Check `exact_match('Kl34-A465', 'KL34A465') is True`. If false, stop with an assertion error: the tested expectation failed.

**Line 12**
```python
    assert exact_match("KL34A465", "KL34A466") is False
```
Check `exact_match('KL34A465', 'KL34A466') is False`. If false, stop with an assertion error: the tested expectation failed.

**Line 13**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 14**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 15**
```python
def test_cer():
```
Define `test_cer`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 16**
```python
    # hand check: truth KL498262 (8 chars), pred KLA98262 -> 1 substitution -> 1/8
```
Comment for the reader; Python does not execute it. hand check: truth KL498262 (8 chars), pred KLA98262 -> 1 substitution -> 1/8

**Line 17**
```python
    assert cer("KLA98262", "KL498262") == 0.125
```
Check `cer('KLA98262', 'KL498262') == 0.125`. If false, stop with an assertion error: the tested expectation failed.

**Line 18**
```python
    # lengthening only: truth AB12, pred AB1234 -> 2 inserts -> 0.5
```
Comment for the reader; Python does not execute it. lengthening only: truth AB12, pred AB1234 -> 2 inserts -> 0.5

**Line 19**
```python
    assert cer("AB1234", "AB12") == 0.5
```
Check `cer('AB1234', 'AB12') == 0.5`. If false, stop with an assertion error: the tested expectation failed.

**Line 20**
```python
    # legit >1 case: pred much longer than truth -> distance 6, len(truth)=4 -> 1.5
```
Comment for the reader; Python does not execute it. legit >1 case: pred much longer than truth -> distance 6, len(truth)=4 -> 1.5

**Line 21**
```python
    assert cer("AB12CD34EF", "AB12") == 1.5
```
Check `cer('AB12CD34EF', 'AB12') == 1.5`. If false, stop with an assertion error: the tested expectation failed.

**Line 22**
```python
    # empty truth with non-empty pred -> 1.0
```
Comment for the reader; Python does not execute it. empty truth with non-empty pred -> 1.0

**Line 23**
```python
    assert cer("ABC", "") == 1.0
```
Check `cer('ABC', '') == 1.0`. If false, stop with an assertion error: the tested expectation failed.

**Line 24**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 25**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 26**
```python
def test_ece():
```
Define `test_ece`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 27**
```python
    # hand: bin5 [conf .5 wrong]: 0.5*|0-.5|=.25 ; bin9 [conf .9 right]: 0.5*|1-.9|=.05 -> .30
```
Comment for the reader; Python does not execute it. hand: bin5 [conf .5 wrong]: 0.5*|0-.5|=.25 ; bin9 [conf .9 right]: 0.5*|1-.9|=.05 -> .30

**Line 28**
```python
    assert ece([0.5, 0.9], [False, True]) == 0.3
```
Check `ece([0.5, 0.9], [False, True]) == 0.3`. If false, stop with an assertion error: the tested expectation failed.

**Line 29**
```python
    # hand: bin5 acc .5 == conf .5, bin9 (conf 1.0) acc 1.0 == conf 1.0 -> 0.0
```
Comment for the reader; Python does not execute it. hand: bin5 acc .5 == conf .5, bin9 (conf 1.0) acc 1.0 == conf 1.0 -> 0.0

**Line 30**
```python
    assert ece([0.5, 0.5, 1.0, 1.0], [True, False, True, True]) == 0.0
```
Check `ece([0.5, 0.5, 1.0, 1.0], [True, False, True, True]) == 0.0`. If false, stop with an assertion error: the tested expectation failed.

**Line 31**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 32**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 33**
```python
def test_risk_coverage():
```
Define `test_risk_coverage`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 34**
```python
    # hand: confs [0.9,0.5,0.8], corrects [T,F,F] -> order .9(ok), .8(ok), .5(wrong)
```
Comment for the reader; Python does not execute it. hand: confs [0.9,0.5,0.8], corrects [T,F,F] -> order .9(ok), .8(ok), .5(wrong)

**Line 35**
```python
    assert risk_coverage([0.9, 0.5, 0.8], [True, False, False]) == [
```
Check `risk_coverage([0.9, 0.5, 0.8], [True, False, False]) == [(1 / 3, 0.0), (2 / 3, 0.5), (1.0, 2 / 3)]`. If false, stop with an assertion error: the tested expectation failed.

**Line 36**
```python
        (1 / 3, 0.0),
```
Continuation of the statement starting at line 35; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 37**
```python
        (2 / 3, 0.5),
```
Continuation of the statement starting at line 35; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 38**
```python
        (1.0, 2 / 3),
```
Continuation of the statement starting at line 35; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 39**
```python
    ]
```
Continuation of the statement starting at line 35; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

## tests/test_pipeline.py

Automated checks for the named component.

Source SHA-256: `fe8057a2f0d88b9e13cae2132a2f6508b358edaf4b1dc8cbc70a0491dfc272ef`

**Line 1**
```python
from pathlib import Path
```
Make the named library tools available here: `from pathlib import Path`. Importing a project module makes its reusable functions accessible.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
from riskgate import config
```
Make the named library tools available here: `from riskgate import config`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
from riskgate.data import load_all_samples
```
Make the named library tools available here: `from riskgate.data import load_all_samples`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python
from scripts.detector import box_to_yolo, overlap
```
Make the named library tools available here: `from scripts.detector import box_to_yolo, overlap`. Importing a project module makes its reusable functions accessible.

**Line 6**
```python
from scripts.import_extra_detection import valid_labels
```
Make the named library tools available here: `from scripts.import_extra_detection import valid_labels`. Importing a project module makes its reusable functions accessible.

**Line 7**
```python
from scripts.prepare_indian import assign_groups, video_key
```
Make the named library tools available here: `from scripts.prepare_indian import assign_groups, video_key`. Importing a project module makes its reusable functions accessible.

**Line 8**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 9**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 10**
```python
def test_video_and_plate_groups_stay_together():
```
Define `test_video_and_plate_groups_stay_together`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 11**
```python
    assert video_key(Path("video_images/video11_1050.jpg")) == "video11"
```
Check `video_key(Path('video_images/video11_1050.jpg')) == 'video11'`. If false, stop with an assertion error: the tested expectation failed.

**Line 12**
```python
    assert video_key(Path("video_images/car-wbs-MH01DE2780_00001.jpg")) == "car-wbs-MH01DE2780"
```
Check `video_key(Path('video_images/car-wbs-MH01DE2780_00001.jpg')) == 'car-wbs-MH01DE2780'`. If false, stop with an assertion error: the tested expectation failed.

**Line 13**
```python
    assert video_key(Path("State-wise_OLX/MH/MH1.jpg")) is None
```
Check `video_key(Path('State-wise_OLX/MH/MH1.jpg')) is None`. If false, stop with an assertion error: the tested expectation failed.

**Line 14**
```python
    rows = [{"truth": "AA1", "video_key": "video11"},
```
Store the result in `rows`: evaluate `[{'truth': 'AA1', 'video_key': 'video11'}, {'truth': 'BB2', 'video_key': 'video11'}, {'truth': 'BB2', 'video_key': None}, {'truth': 'CC3', 'video_key': None}]` using the values currently in memory.

**Line 15**
```python
            {"truth": "BB2", "video_key": "video11"},
```
Continuation of the statement starting at line 14; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 16**
```python
            {"truth": "BB2", "video_key": None},
```
Continuation of the statement starting at line 14; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 17**
```python
            {"truth": "CC3", "video_key": None}]
```
Continuation of the statement starting at line 14; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 18**
```python
    assign_groups(rows)
```
Call `assign_groups` with the inputs shown to obtain its result.

**Line 19**
```python
    assert rows[0]["group_id"] == rows[1]["group_id"] == rows[2]["group_id"]
```
Check `rows[0]['group_id'] == rows[1]['group_id'] == rows[2]['group_id']`. If false, stop with an assertion error: the tested expectation failed.

**Line 20**
```python
    assert rows[3]["group_id"] != rows[0]["group_id"]
```
Check `rows[3]['group_id'] != rows[0]['group_id']`. If false, stop with an assertion error: the tested expectation failed.

**Line 21**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 22**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 23**
```python
def test_detector_box_coordinates_and_overlap():
```
Define `test_detector_box_coordinates_and_overlap`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 24**
```python
    row = {"xmin": 20, "ymin": 10, "xmax": 60, "ymax": 30}
```
Store the result in `row`: build a dictionary: each key names the value stored beside it.

**Line 25**
```python
    assert box_to_yolo(row, 100, 50) == "0 0.400000 0.400000 0.400000 0.400000\n"
```
Check `box_to_yolo(row, 100, 50) == '0 0.400000 0.400000 0.400000 0.400000\n'`. If false, stop with an assertion error: the tested expectation failed.

**Line 26**
```python
    assert overlap((20, 10, 60, 30), (20, 10, 60, 30)) == 1
```
Check `overlap((20, 10, 60, 30), (20, 10, 60, 30)) == 1`. If false, stop with an assertion error: the tested expectation failed.

**Line 27**
```python
    assert overlap((0, 0, 10, 10), (20, 20, 30, 30)) == 0
```
Check `overlap((0, 0, 10, 10), (20, 20, 30, 30)) == 0`. If false, stop with an assertion error: the tested expectation failed.

**Line 28**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 29**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 30**
```python
def test_human_review_overrides_xml_without_editing_it(tmp_path, monkeypatch):
```
Define `test_human_review_overrides_xml_without_editing_it`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 31**
```python
    monkeypatch.setattr(config, "ROOT", tmp_path)
```
Call `monkeypatch.setattr` with the inputs shown to obtain its result.

**Line 32**
```python
    labels = tmp_path / "data/labels"
```
Store the result in `labels`: calculate `tmp_path / 'data/labels'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 33**
```python
    labels.mkdir(parents=True)
```
Call `labels.mkdir` with the inputs shown to obtain its result.

**Line 34**
```python
    (tmp_path / "crop.jpg").write_bytes(b"x")
```
Call `(tmp_path / 'crop.jpg').write_bytes` with the inputs shown to obtain its result.

**Line 35**
```python
    xml = labels / "kaggle_xml_labels.csv"
```
Store the result in `xml`: calculate `labels / 'kaggle_xml_labels.csv'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 36**
```python
    xml.write_text("crop_path,group_id,truth\ncrop.jpg,g1,AB12\n")
```
Call `xml.write_text` with the inputs shown to obtain its result.

**Line 37**
```python
    (labels / "kaggle_labels.csv").write_text("crop_path,group_id,truth\ncrop.jpg,g1,AB13\n")
```
Call `(labels / 'kaggle_labels.csv').write_text` with the inputs shown to obtain its result.

**Line 38**
```python
    samples = load_all_samples(tmp_path / "empty")
```
Store the result in `samples`: call `load_all_samples` with the inputs shown to obtain its result.

**Line 39**
```python
    assert len(samples) == 1 and samples[0].truth == "AB13"
```
Check `len(samples) == 1 and samples[0].truth == 'AB13'`. If false, stop with an assertion error: the tested expectation failed.

**Line 40**
```python
    assert "AB12" in xml.read_text()
```
Check `'AB12' in xml.read_text()`. If false, stop with an assertion error: the tested expectation failed.

**Line 41**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 42**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 43**
```python
def test_extra_detector_labels_reject_invalid_boxes(tmp_path):
```
Define `test_extra_detector_labels_reject_invalid_boxes`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 44**
```python
    label = tmp_path / "plate.txt"
```
Store the result in `label`: calculate `tmp_path / 'plate.txt'`; `/` divides, `*` multiplies, and paths use `/` to join folders.

**Line 45**
```python
    label.write_text("0 0.5 0.5 0.4 0.2\n")
```
Call `label.write_text` with the inputs shown to obtain its result.

**Line 46**
```python
    assert valid_labels(label)
```
Check `valid_labels(label)`. If false, stop with an assertion error: the tested expectation failed.

**Line 47**
```python
    label.write_text("0 0.5 0.5 1.4 0.2\n")
```
Call `label.write_text` with the inputs shown to obtain its result.

**Line 48**
```python
    assert not valid_labels(label)
```
Check `not valid_labels(label)`. If false, stop with an assertion error: the tested expectation failed.

## tests/test_read_order.py

Automated checks for the named component.

Source SHA-256: `7d93eb8aa45a292a4ad2c16889d412f1a093480c225db416f15c48f5ff0ed29a`

**Line 1**
```python
from riskgate.engines.easyocr_engine import order_boxes
```
Make the named library tools available here: `from riskgate.engines.easyocr_engine import order_boxes`. Importing a project module makes its reusable functions accessible.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 4**
```python
def box(x: int, y: int, text: str):
```
Define `box`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 5**
```python
    return ([[x, y], [x + 10, y], [x + 10, y + 8], [x, y + 8]], text, 0.9)
```
Finish this function and collect the values in order (a tuple), which can also be unpacked into separate names; send that result to its caller.

**Line 6**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 7**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 8**
```python
def test_one_line():
```
Define `test_one_line`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 9**
```python
    assert [b[1] for b in order_boxes([box(20, 1, "B"), box(0, 0, "A")])] == ["A", "B"]
```
Check `[b[1] for b in order_boxes([box(20, 1, 'B'), box(0, 0, 'A')])] == ['A', 'B']`. If false, stop with an assertion error: the tested expectation failed.

**Line 10**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 11**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 12**
```python
def test_two_lines():
```
Define `test_two_lines`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 13**
```python
    assert [b[1] for b in order_boxes([box(20, 20, "D"), box(20, 0, "B"),
```
Check `[b[1] for b in order_boxes([box(20, 20, 'D'), box(20, 0, 'B'), box(0, 21, 'C'), box(0, 1, 'A')])] == ['A', 'B', 'C', 'D']`. If false, stop with an assertion error: the tested expectation failed.

**Line 14**
```python
                                       box(0, 21, "C"), box(0, 1, "A")])] == ["A", "B", "C", "D"]
```
Continuation of the statement starting at line 13; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

## tests/test_stability.py

Automated checks for the named component.

Source SHA-256: `e66cd9559af93159b2896ded62a81cfd482d7f4defba906eb1c8a63409f4624d`

**Line 1**
```python
import numpy as np
```
Make the named library tools available here: `import numpy as np`. Importing a project module makes its reusable functions accessible.

**Line 2**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 3**
```python
from riskgate.contracts import EngineResult
```
Make the named library tools available here: `from riskgate.contracts import EngineResult`. Importing a project module makes its reusable functions accessible.

**Line 4**
```python
from riskgate.stability import apply_veto, check_stability
```
Make the named library tools available here: `from riskgate.stability import apply_veto, check_stability`. Importing a project module makes its reusable functions accessible.

**Line 5**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 6**
```python

```
Blank line: separates ideas for readability; performs no action.

**Line 7**
```python
def test_stability_veto_and_failure():
```
Define `test_stability_veto_and_failure`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 8**
```python
    crop = np.full((20, 80, 3), 100, dtype=np.uint8)
```
Store the result in `crop`: call `np.full` with the inputs shown to obtain its result.

**Line 9**
```python
    seen = []
```
Store the result in `seen`: evaluate `[]` using the values currently in memory.

**Line 10**
```python
    def read(image):
```
Define `read`; its indented body runs when called. Inputs are in parentheses; the return annotation describes the expected output type.

**Line 11**
```python
        seen.append(image.copy())
```
Call `seen.append` with the inputs shown to obtain its result.

**Line 12**
```python
        return EngineResult("KA01AB1234", 0.99, 1)
```
Finish this function and call `EngineResult` with the inputs shown to obtain its result; send that result to its caller.

**Line 13**
```python
    evidence = check_stability(crop, "KA01AB1234", read)
```
Store the result in `evidence`: read resized and brightened copies and compare with the original text.

**Line 14**
```python
    assert evidence["stable"]
```
Check `evidence['stable']`. If false, stop with an assertion error: the tested expectation failed.

**Line 15**
```python
    assert seen[0].shape[:2] == (25, 100)
```
Check `seen[0].shape[:2] == (25, 100)`. If false, stop with an assertion error: the tested expectation failed.

**Line 16**
```python
    assert seen[1][0, 0, 0] == 110
```
Check `seen[1][0, 0, 0] == 110`. If false, stop with an assertion error: the tested expectation failed.

**Line 17**
```python
    assert np.all(crop == 100)
```
Check `np.all(crop == 100)`. If false, stop with an assertion error: the tested expectation failed.

**Line 18**
```python
    assert apply_veto("ACCEPT", evidence) == "ACCEPT"
```
Check `apply_veto('ACCEPT', evidence) == 'ACCEPT'`. If false, stop with an assertion error: the tested expectation failed.

**Line 19**
```python
    assert apply_veto("REVIEW", evidence) == "REVIEW"
```
Check `apply_veto('REVIEW', evidence) == 'REVIEW'`. If false, stop with an assertion error: the tested expectation failed.

**Line 20**
```python
    for result in (EngineResult("KA01AB1235", .99, 1),
```
For each item from `(EngineResult('KA01AB1235', 0.99, 1), EngineResult('', 0, 1, error='failed'), EngineResult('KA01AB1234', 0.99, 1, error='failed'))`, name it `result` and run the indented body.

**Line 21**
```python
                   EngineResult("", 0, 1, error="failed"),
```
Continuation of the statement starting at line 20; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 22**
```python
                   EngineResult("KA01AB1234", .99, 1, error="failed")):
```
Continuation of the statement starting at line 20; supplies the remaining text, arguments, values, or closing brackets. Read it together with that statement's explanation.

**Line 23**
```python
        evidence = check_stability(crop, "KA01AB1234", lambda image: result)
```
Store the result in `evidence`: read resized and brightened copies and compare with the original text.

**Line 24**
```python
        assert not evidence["stable"]
```
Check `not evidence['stable']`. If false, stop with an assertion error: the tested expectation failed.

**Line 25**
```python
        assert apply_veto("ACCEPT", evidence) == "REVIEW"
```
Check `apply_veto('ACCEPT', evidence) == 'REVIEW'`. If false, stop with an assertion error: the tested expectation failed.

**Line 26**
```python
    assert not check_stability(crop, "", lambda image: EngineResult("", 0, 1))["stable"]
```
Check `not check_stability(crop, '', lambda image: EngineResult('', 0, 1))['stable']`. If false, stop with an assertion error: the tested expectation failed.

## requirements.txt

Supporting configuration or presentation source; not part of neural inference.

**Line 1**
```text
opencv-python
```
Install the Python package `opencv-python`. Brackets request optional extras; no version is pinned.

**Line 2**
```text
easyocr
```
Install the Python package `easyocr`. Brackets request optional extras; no version is pinned.

**Line 3**
```text
torch
```
Install the Python package `torch`. Brackets request optional extras; no version is pinned.

**Line 4**
```text
pytest
```
Install the Python package `pytest`. Brackets request optional extras; no version is pinned.

**Line 5**
```text
scikit-learn
```
Install the Python package `scikit-learn`. Brackets request optional extras; no version is pinned.

**Line 6**
```text
matplotlib
```
Install the Python package `matplotlib`. Brackets request optional extras; no version is pinned.

**Line 7**
```text
streamlit
```
Install the Python package `streamlit`. Brackets request optional extras; no version is pinned.

**Line 8**
```text
ultralytics
```
Install the Python package `ultralytics`. Brackets request optional extras; no version is pinned.

**Line 9**
```text
fast-plate-ocr[onnx]
```
Install the Python package `fast-plate-ocr[onnx]`. Brackets request optional extras; no version is pinned.

## Makefile

Supporting configuration or presentation source; not part of neural inference.

**Line 1**
```text
.PHONY: check
```
Declare a command target (or run its indented shell recipe). `check` runs the tests through the project's virtual environment. `.PHONY` ensures a same-named file cannot suppress the command.

**Line 2**
```text

```
Blank line for readability.

**Line 3**
```text
check:
```
Declare a command target (or run its indented shell recipe). `check` runs the tests through the project's virtual environment. `.PHONY` ensures a same-named file cannot suppress the command.

**Line 4**
```text
	./venv/bin/python -m pytest tests -q
```
Declare a command target (or run its indented shell recipe). `check` runs the tests through the project's virtual environment. `.PHONY` ensures a same-named file cannot suppress the command.

## .gitignore

Supporting configuration or presentation source; not part of neural inference.

**Line 1**
```text
venv/
```
Exclude paths matching `venv/` from ordinary Git tracking; this does not delete existing files.

**Line 2**
```text
.pytest_cache/
```
Exclude paths matching `.pytest_cache/` from ordinary Git tracking; this does not delete existing files.

**Line 3**
```text
__pycache__/
```
Exclude paths matching `__pycache__/` from ordinary Git tracking; this does not delete existing files.

**Line 4**
```text
*.pyc
```
Exclude paths matching `*.pyc` from ordinary Git tracking; this does not delete existing files.

**Line 5**
```text
data/
```
Exclude paths matching `data/` from ordinary Git tracking; this does not delete existing files.

**Line 6**
```text
weights/
```
Exclude paths matching `weights/` from ordinary Git tracking; this does not delete existing files.

**Line 7**
```text
results/
```
Exclude paths matching `results/` from ordinary Git tracking; this does not delete existing files.

**Line 8**
```text
RiskGate_Submission.zip
```
Exclude paths matching `RiskGate_Submission.zip` from ordinary Git tracking; this does not delete existing files.

## .streamlit/config.toml

Supporting configuration or presentation source; not part of neural inference.

**Line 1**
```text
[theme]
```
Start a settings section with brackets, or assign the shown setting. Theme settings control appearance; maxUploadSize sets Streamlit's per-file upload limit in MB.

**Line 2**
```text
base = "dark"
```
Start a settings section with brackets, or assign the shown setting. Theme settings control appearance; maxUploadSize sets Streamlit's per-file upload limit in MB.

**Line 3**
```text
primaryColor = "#5fe6ca"
```
Start a settings section with brackets, or assign the shown setting. Theme settings control appearance; maxUploadSize sets Streamlit's per-file upload limit in MB.

**Line 4**
```text
backgroundColor = "#07111e"
```
Start a settings section with brackets, or assign the shown setting. Theme settings control appearance; maxUploadSize sets Streamlit's per-file upload limit in MB.

**Line 5**
```text
secondaryBackgroundColor = "#102235"
```
Start a settings section with brackets, or assign the shown setting. Theme settings control appearance; maxUploadSize sets Streamlit's per-file upload limit in MB.

**Line 6**
```text
textColor = "#e7f2f5"
```
Start a settings section with brackets, or assign the shown setting. Theme settings control appearance; maxUploadSize sets Streamlit's per-file upload limit in MB.

**Line 7**
```text
font = "sans serif"
```
Start a settings section with brackets, or assign the shown setting. Theme settings control appearance; maxUploadSize sets Streamlit's per-file upload limit in MB.

**Line 8**
```text

```
Blank line for readability.

**Line 9**
```text
[server]
```
Start a settings section with brackets, or assign the shown setting. Theme settings control appearance; maxUploadSize sets Streamlit's per-file upload limit in MB.

**Line 10**
```text
maxUploadSize = 12
```
Start a settings section with brackets, or assign the shown setting. Theme settings control appearance; maxUploadSize sets Streamlit's per-file upload limit in MB.

## presentation/presentation.html

Supporting configuration or presentation source; not part of neural inference.

**Line 1**
```text
<!doctype html>
```
HTML document structure or metadata: opening tags begin an element, closing tags end it; meta tags configure text encoding and viewport; style holds appearance rules.

**Line 2**
```text
<html lang="en">
```
HTML document structure or metadata: opening tags begin an element, closing tags end it; meta tags configure text encoding and viewport; style holds appearance rules.

**Line 3**
```text
<head>
```
HTML document structure or metadata: opening tags begin an element, closing tags end it; meta tags configure text encoding and viewport; style holds appearance rules.

**Line 4**
```text
<meta charset="utf-8">
```
HTML document structure or metadata: opening tags begin an element, closing tags end it; meta tags configure text encoding and viewport; style holds appearance rules.

**Line 5**
```text
<meta name="viewport" content="width=device-width,initial-scale=1">
```
HTML document structure or metadata: opening tags begin an element, closing tags end it; meta tags configure text encoding and viewport; style holds appearance rules.

**Line 6**
```text
<title>RiskGate ANPR · PBL presentation</title>
```
HTML document structure or metadata: opening tags begin an element, closing tags end it; meta tags configure text encoding and viewport; style holds appearance rules.

**Line 7**
```text
<style>
```
HTML document structure or metadata: opening tags begin an element, closing tags end it; meta tags configure text encoding and viewport; style holds appearance rules.

**Line 8**
```text
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Space+Grotesk:wght@400;600;700&display=swap');
```
HTML document structure or metadata: opening tags begin an element, closing tags end it; meta tags configure text encoding and viewport; style holds appearance rules.

**Line 9**
```text
:root{color-scheme:dark;--bg:#07111e;--panel:#10283b;--mint:#5fe6ca;--warm:#ffba6b;--text:#e8f7f5;--muted:#9ebbc5}
```
CSS appearance rules: selectors before braces choose elements; name:value declarations set their layout, size, colors, spacing, or print behaviour. They do not process plate images.

**Line 10**
```text
*{box-sizing:border-box}body{margin:0;background:#030912;color:var(--text);font-family:'DM Sans',sans-serif}
```
CSS appearance rules: selectors before braces choose elements; name:value declarations set their layout, size, colors, spacing, or print behaviour. They do not process plate images.

**Line 11**
```text
.slide{width:min(100vw,1500px);min-height:100vh;margin:auto;padding:6vh 7vw;display:none;position:relative;overflow:hidden;background:radial-gradient(circle at 87% 8%,#12494b 0,transparent 35%),var(--bg)}
```
CSS appearance rules: selectors before braces choose elements; name:value declarations set their layout, size, colors, spacing, or print behaviour. They do not process plate images.

**Line 12**
```text
.slide.active{display:flex;flex-direction:column;justify-content:center}.slide:after{content:'RISK / GATE';position:absolute;right:6vw;bottom:3vh;color:#567482;font-size:.75rem;letter-spacing:.2em}
```
CSS appearance rules: selectors before braces choose elements; name:value declarations set their layout, size, colors, spacing, or print behaviour. They do not process plate images.

**Line 13**
```text
.kicker{color:var(--mint);font-size:.8rem;letter-spacing:.22em;font-weight:700;text-transform:uppercase}h1,h2,h3,.number{font-family:'Space Grotesk',sans-serif;letter-spacing:-.045em}h1{font-size:clamp(3.5rem,8vw,8rem);line-height:1;margin:.2em 0}h2{font-size:clamp(2.5rem,5vw,5rem);line-height:1.07;margin:.3em 0 .6em}h3{font-size:1.5rem;margin:.25em 0}p,li{font-size:clamp(1.05rem,1.55vw,1.45rem);line-height:1.45;color:#d4e7e9}p.lead{font-size:clamp(1.4rem,2.2vw,2rem);max-width:900px;color:#d8e9eb}.muted{color:var(--muted)}.mint{color:var(--mint)}.warm{color:var(--warm)}
```
CSS appearance rules: selectors before braces choose elements; name:value declarations set their layout, size, colors, spacing, or print behaviour. They do not process plate images.

**Line 14**
```text
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.grid.two{grid-template-columns:repeat(2,1fr)}.card{border:1px solid #2b4c5b;border-radius:20px;background:linear-gradient(135deg,#123145,#102235);padding:25px;min-height:170px}.card p{font-size:1.1rem;margin:.4em 0;color:var(--muted)}.number{font-size:clamp(2.4rem,4vw,4rem);font-weight:700;color:var(--mint)}.pill{display:inline-block;border:1px solid #44736f;border-radius:99px;padding:10px 18px;margin:8px 6px 8px 0;background:#16363c;font-size:1.15rem}.arrow{color:var(--mint);padding:0 5px}.statline{display:flex;gap:16px;flex-wrap:wrap;margin-top:12px}.statline .card{flex:1;min-width:220px}.chart{max-width:100%;max-height:50vh;border:1px solid #345266;border-radius:18px}.side{display:grid;grid-template-columns:1.1fr 1fr;gap:36px;align-items:center}.cite{font-size:.86rem;color:#87a9b3}.cite a{color:#8eeed7}.footer{position:fixed;bottom:16px;left:20px;color:#8ba8b2;font-size:.8rem;z-index:4}.controls{position:fixed;bottom:14px;right:20px;display:flex;gap:8px;z-index:4}.controls button{background:#173244;color:#e6f6f1;border:1px solid #426574;border-radius:9px;padding:7px 14px;cursor:pointer}.controls button:hover{background:#245468}
```
CSS appearance rules: selectors before braces choose elements; name:value declarations set their layout, size, colors, spacing, or print behaviour. They do not process plate images.

**Line 15**
```text
@media(max-width:750px){.slide{padding:70px 25px}.grid,.grid.two,.side{grid-template-columns:1fr}.slide{overflow:auto}.card{min-height:110px}h1{font-size:3.3rem}h2{font-size:2.5rem}}
```
CSS appearance rules: selectors before braces choose elements; name:value declarations set their layout, size, colors, spacing, or print behaviour. They do not process plate images.

**Line 16**
```text
@media print{body{background:white}.slide,.slide.active{display:flex;break-after:page;page-break-after:always;width:100%;height:100vh;min-height:0}.controls,.footer{display:none}@page{size:landscape;margin:0}}
```
CSS appearance rules: selectors before braces choose elements; name:value declarations set their layout, size, colors, spacing, or print behaviour. They do not process plate images.

**Line 17**
```text
</style>
```
HTML document structure or metadata: opening tags begin an element, closing tags end it; meta tags configure text encoding and viewport; style holds appearance rules.

**Line 18**
```text
</head>
```
HTML document structure or metadata: opening tags begin an element, closing tags end it; meta tags configure text encoding and viewport; style holds appearance rules.

**Line 19**
```text
<body>
```
HTML document structure or metadata: opening tags begin an element, closing tags end it; meta tags configure text encoding and viewport; style holds appearance rules.

**Line 20**
```text
<section class="slide active"><div class="kicker">PBL project · Indian number plate recognition</div><h1>RISK<span class="mint">GATE</span><br>ANPR</h1><p class="lead">A local number plate reader that knows when to ask for review.</p><p class="muted">Detect → Read → Estimate correctness → Accept or review</p></section>
```
Define one presentation slide. The visible headings, paragraphs, numbers, links, and image references on this line make up its content. Class names select the appearance rules in the style block.

**Line 21**
```text
<section class="slide"><div class="kicker">01 / Problem</div><h2>A plausible answer can still be wrong.</h2><div class="grid two"><div class="card"><h3>First prototype</h3><p>Send a test photo to Gemini and display its answer.</p></div><div class="card"><h3>Final question</h3><p>Can a local system tell when its plate reading is safe enough to use?</p></div></div><p class="lead">A one-character mistake can make a different vehicle's plate. Format checks alone cannot catch it.</p></section>
```
Define one presentation slide. The visible headings, paragraphs, numbers, links, and image references on this line make up its content. Class names select the appearance rules in the style block.

**Line 22**
```text
<section class="slide"><div class="kicker">02 / System</div><h2>Five understandable steps.</h2><div><span class="pill">1 Detect the plate</span><span class="arrow">→</span><span class="pill">2 Read the crop</span><span class="arrow">→</span><span class="pill">3 Check format</span><span class="arrow">→</span><span class="pill">4 Estimate correctness</span><span class="arrow">→</span><span class="pill">5 Accept / review</span></div><p class="lead">Everything runs locally. The demo shows the photo, box, crop, text, confidence, decision, and a correction input.</p></section>
```
Define one presentation slide. The visible headings, paragraphs, numbers, links, and image references on this line make up its content. Class names select the appearance rules in the style block.

**Line 23**
```text
<section class="slide"><div class="kicker">03 / Data and method</div><h2>Real images, grouped evaluation.</h2><div class="statline"><div class="card"><div class="number">1,695</div><p>usable image / XML text pairs</p></div><div class="card"><div class="number">1,027</div><p>detector training images after expansion</p></div><div class="card"><div class="number">12</div><p>full vehicle scenes in the demo gallery</p></div></div><p class="lead">The original 254-image test stays separate from training. Repeated plates and source-video frames are grouped; a second box-only source added 180 screened full images for detector training.</p><p class="cite">Sources: <a href="https://www.kaggle.com/datasets/saisirishan/indian-vehicle-dataset">Saisirishan</a> and <a href="https://www.kaggle.com/datasets/kedarsai/indian-license-plates-with-labels">Kedarsai</a> Kaggle datasets. XML labels have only a sampled audit.</p></section>
```
Define one presentation slide. The visible headings, paragraphs, numbers, links, and image references on this line make up its content. Class names select the appearance rules in the style block.

**Line 24**
```text
<section class="slide"><div class="kicker">04 / Model stack</div><h2>Small models, clear roles.</h2><div class="grid"><div class="card"><h3>YOLO11n</h3><p>Fine-tuned to find the plate rectangle in a vehicle image.</p></div><div class="card"><h3>FastPlateOCR</h3><p>Selected against EasyOCR on the same training crops; reads the plate locally.</p></div><div class="card"><h3>Logistic model</h3><p>Uses OCR and image signals to estimate whole-plate correctness.</p></div></div><p class="lead">The system does not depend on a paid API or internet connection.</p></section>
```
Define one presentation slide. The visible headings, paragraphs, numbers, links, and image references on this line make up its content. Class names select the appearance rules in the style block.

**Line 25**
```text
<section class="slide"><div class="kicker">05 / Measured result</div><h2>Finding works better than reading.</h2><div class="statline"><div class="card"><div class="number">248 / 254</div><p>expanded detector matches at IoU ≥ 0.5; original 237</p></div><div class="card"><div class="number">71 / 254</div><p>full-image plates read exactly</p></div><div class="card"><div class="number">28.0%</div><p>end-to-end exact match</p></div></div><p class="lead">Extra detector data improved localization on a repeated test, while exact OCR stayed the bottleneck. The second comparison is exploratory, not blinded.</p></section>
```
Define one presentation slide. The visible headings, paragraphs, numbers, links, and image references on this line make up its content. Class names select the appearance rules in the style block.

**Line 26**
```text
<section class="slide"><div class="kicker">06 / Selective prediction</div><div class="side"><div><h2>Automation has a cost.</h2><p class="lead">At the threshold chosen for a 10% validation target, the full pipeline accepted <span class="mint">75 / 254</span> images automatically. <span class="warm">11 / 75</span> accepted answers were wrong.</p><p>Observed accepted error: <strong>14.7%</strong>. The target was not met on test. Strict 2% and 5% targets accepted none.</p></div><img class="chart" src="../results/risk_coverage.png" alt="Risk coverage curve"></div></section>
```
Define one presentation slide. The visible headings, paragraphs, numbers, links, and image references on this line make up its content. Class names select the appearance rules in the style block.

**Line 27**
```text
<section class="slide"><div class="kicker">07 / Confidence</div><div class="side"><div><h2>Confidence is tested, not assumed.</h2><p class="lead">A raw OCR score of 90% does not prove a 90% chance that the entire plate is right.</p><p>On the crop test, calibration ECE changed from <span class="warm">0.559</span> (raw OCR score) to <span class="mint">0.075</span> (correctness estimate). The plot checks whether confidence matches observed frequency.</p></div><img class="chart" src="../results/reliability.png" alt="Reliability diagram"></div></section>
```
Define one presentation slide. The visible headings, paragraphs, numbers, links, and image references on this line make up its content. Class names select the appearance rules in the style block.

**Line 28**
```text
<section class="slide"><div class="kicker">08 / Limits and next step</div><h2>What this prototype proves.</h2><div class="grid two"><div class="card"><h3 class="mint">Done</h3><p>Offline full-image pipeline, detector training, two-reader comparison, calibrated routing, human correction, real test charts.</p></div><div class="card"><h3 class="warm">Limits</h3><p>Exact OCR is 28%. A 180-crop audit found 8 clear data issues. Some Google images show foreign plates. Human review is still necessary.</p></div></div><p class="lead">Next: curate Indian-only labels and train a stronger OCR model. Keep the same grouped evaluation to measure whether it really helps.</p><p class="cite">Research basis: <a href="https://arxiv.org/abs/2604.09927">BLPR</a>, <a href="https://arxiv.org/abs/2602.07051">Neural Sentinel</a>, <a href="https://arxiv.org/abs/2604.22506">ICPR low-resolution LPR</a>, and the other sources in ../docs/EVALUATION_REPORT.md.</p></section>
```
Define one presentation slide. The visible headings, paragraphs, numbers, links, and image references on this line make up its content. Class names select the appearance rules in the style block.

**Line 29**
```text
<section class="slide"><div class="kicker">09 / New research experiment</div><h2>Does reading stability help?</h2><p class="lead">Re-read 125% resized and 10% brighter plate crops. Disagreement can veto automatic acceptance.</p><div class="grid two"><div class="card"><h3>Original policy</h3><div class="number">5 accepted</div><p>1 wrong · 20% accepted error</p></div><div class="card"><h3>With stability veto</h3><div class="number">4 accepted</div><p>1 wrong · 25% accepted error</p></div></div><p>The veto removed a correct acceptance. It remains optional and off by default. Added check time: about 21 ms per crop on this run.</p><p class="cite">12 previously selected demo scenes; descriptive ablation, not a fresh benchmark. Same OCR model, correlated readings. No correctness guarantee or established patentability. Details: results/stability_gallery.json.</p></section>
```
Define one presentation slide. The visible headings, paragraphs, numbers, links, and image references on this line make up its content. Class names select the appearance rules in the style block.

**Line 30**
```text
<div class="footer">Use ← and → to navigate · Print from Chromium to export a PDF</div><div class="controls"><button onclick="move(-1)">←</button><span id="counter" style="padding:8px;color:#9ebbc5">1 / 10</span><button onclick="move(1)">→</button></div>
```
Render navigation controls and the slide counter; the arrow buttons call move with minus or plus one.

**Line 31**
```text
<script>let current=0;const slides=[...document.querySelectorAll('.slide')];function move(step){slides[current].classList.remove('active');current=Math.max(0,Math.min(slides.length-1,current+step));slides[current].classList.add('active');document.getElementById('counter').textContent=`${current+1} / ${slides.length}`};addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key===' '){e.preventDefault();move(1)}if(e.key==='ArrowLeft'){e.preventDefault();move(-1)}})</script>
```
Keep the current slide index; collect slides; move within valid bounds, toggle the active class, update the counter, and listen for left/right/space keys. preventDefault stops space from scrolling.

**Line 32**
```text
</body>
```
HTML document structure or metadata: opening tags begin an element, closing tags end it; meta tags configure text encoding and viewport; style holds appearance rules.

**Line 33**
```text
</html>
```
HTML document structure or metadata: opening tags begin an element, closing tags end it; meta tags configure text encoding and viewport; style holds appearance rules.
