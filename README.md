# VisionRead ANPR

An offline number plate demo: **vehicle photo → YOLO plate detector → FastPlateOCR → correctness estimate → ACCEPT or REVIEW**.

This branch contains the app and presentation material. The complete training, evaluation, and experiment source is preserved under [`submission-final`](https://github.com/AarushDayal/VisionRead-ANPR/tree/submission-final). The demo loads saved models; it does not retrain them.

## Run

On the prepared project laptop:

```sh
./venv/bin/streamlit run app/streamlit_app.py
```

Open the address Streamlit prints. Choose **Demo gallery**, select a vehicle photo, and click **Analyze plate**. You can also upload a photo, inspect a plate crop, review a batch, and save a human correction locally.

On another machine, extract `VisionRead_ANPR_Submission.zip`, then run:

```sh
python -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/streamlit run app/streamlit_app.py
```

A Git clone alone does not include the models or gallery. The prepared ZIP includes the required assets:

- `weights/plate_detector.pt`: fine-tuned YOLO detector.
- `weights/fastplate/`: local ONNX reader and its configuration.
- `weights/calibration.json`: saved correctness model and thresholds.
- `data/sample_gallery/`: 12 vehicle photos and their manifest.
- `results/`: recorded evidence and charts used by the dashboard.

The demo uses FastPlateOCR only. No API key is required. The experimental stability checkbox remains off by default; grammar substitutions are not used by the app.

## Faculty presentation

- [Measured evaluation](docs/EVALUATION_REPORT.md): results and experimental limitations.
- [Presentation PDF](presentation/VisionRead_ANPR_Presentation.pdf) · [interactive slides](presentation/presentation.html).
- [Data notes](docs/DATA_NOTES.md): sources, label quality, and attribution.

The expanded detector matched **248/254** boxes. The full-image pipeline read **71/254** plates exactly (28.0%); at the 10% validation target it accepted **75**, with **11 errors** (14.7%). These are prototype results on an already-viewed test, not a deployment guarantee.

The separate grammar experiment was **crop-level only**, on the already-viewed test. Exact matches rose 71 → 90/254, but accepted error at the 10% target rose **12.5% → 15.5%**. Clopper–Pearson selected the same cutoffs. Grammar remains outside the app. The optional stability experiment also failed to improve accepted error on the 12 gallery examples.

## Code map

| Path | Purpose |
| --- | --- |
| `app/streamlit_app.py` | Dashboard and full photo-to-decision flow. |
| `visionread/engines/fastplate_engine.py` | Read plate crops with the local ONNX model. |
| `visionread/features.py`, `calibration.py` | Build six input signals and apply the saved correctness model. |
| `visionread/grammar.py`, `metrics.py`, `router.py` | Classify format, normalize text, and apply saved thresholds. |
| `visionread/stability.py` | Optional resize/brightness review veto. |
| `visionread/config.py`, `contracts.py` | Local paths and OCR result structure. |
| `tests/` | Runtime checks and a real gallery-photo smoke test. |
| `scripts/package_submission.py` | Assemble the portable demo ZIP. |

## Check and package

```sh
./venv/bin/pip install -r requirements-dev.txt
make check
./venv/bin/python -m scripts.package_submission
```

Training tools, offline experiments, the alternate reader, and the generated line-by-line walkthrough were removed from this branch for presentation. To inspect how the models were built, browse the archived tag, especially [`scripts/detector.py`](https://github.com/AarushDayal/VisionRead-ANPR/blob/submission-final/scripts/detector.py).

Models, datasets, generated results, and the ZIP remain Git-ignored. Local data and recorded results are preserved. See the data notes before redistributing source imagery.
