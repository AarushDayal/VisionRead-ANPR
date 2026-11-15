# RiskGate ANPR

An offline Indian number plate research prototype. It detects a plate in a vehicle photo, reads the crop with a local OCR model, estimates whether the whole reading is correct, and sends uncertain cases for human review. The [faculty explanation](docs/FACULTY_EXPLANATION.md) explains the data flow, training, code files, industry comparison, and viva questions in simple language. The [evaluation report](docs/EVALUATION_REPORT.md) records the measured results and limitations.

## PBL research extension

The sidebar offers an **experimental stability check**: read a resized and slightly brightened crop, show both readings, and veto acceptance on disagreement. It is off by default because the 12-scene gallery ablation reduced acceptance from 5 to 4 while retaining the same one wrong acceptance (accepted error 20% → 25%). This is a measured negative result, not an accuracy gain. See the evidence panel and `results/stability_gallery.json`.

Read [the complete beginner guide](docs/FACULTY_EXPLANATION.md) for the project pitch, training, maths, research boundaries, new experiment, demo sequence, and viva answers. [Every Python line explained](docs/CODE_WALKTHROUGH.md) includes all first-party source files and tests. Regenerate it after edits with `./venv/bin/python -m scripts.explain_code`. This prototype has no established patentability; existing selective-prediction research is cited in the guide.

## Current measured result

On 254 grouped test images, the expanded detector matched 248 plate boxes at IoU ≥ 0.5, up from 237 before adding 180 screened full vehicle photos. The complete photo-to-text pipeline read 71/254 whole plates exactly (28.0%). At the threshold selected for a 10% validation error target, it accepted 75/254 automatically and 11 accepted readings were wrong (14.7% observed error). The detector comparison reuses a previously viewed test; these are prototype results on XML labels that have only a sampled visual audit. Strict 2% and 5% targets accepted no plates.

## Run the demo

The local environment already has its dependencies and generated model files:

```sh
./venv/bin/streamlit run app/streamlit_app.py
```

Open the local address Streamlit prints. The demo uses local models and makes no API calls. Choose **Full vehicle photo** for the detector-plus-OCR flow, or **Plate crop** to examine OCR separately. The gallery now contains 12 real-world vehicle scenes, not plate-only photos, and works in the portable bundle. Batch review accepts up to 20 uploads and exports CSV. The evidence tab shows the test plots and detector comparison. Human corrections are saved locally in `results/review_corrections.csv`.

The [ten-slide presentation](presentation/RiskGate_Presentation.pdf) is ready to use; [interactive slides](presentation/presentation.html) support arrow-key navigation. The local `weights/` folder contains the detector and OCR files needed for an offline demo on this machine.

`RiskGate_Submission.zip` is a portable copy of the demo, models, charts, report, slides, and 12 original vehicle scenes without the full datasets or API keys. It is generated with `./venv/bin/python -m scripts.package_submission`. The gallery source is credited in its manifest and [data notes](docs/DATA_NOTES.md). On another machine, create a Python virtual environment, install `requirements.txt`, and run the Streamlit command.

## Rebuild the experiment

The source archive is the [Saisirishan Indian vehicle dataset](https://www.kaggle.com/datasets/saisirishan/indian-vehicle-dataset). Place its extracted folders under `data/indian/`, then run:

```sh
./venv/bin/pip install -r requirements.txt
./venv/bin/python -m scripts.prepare_indian
./venv/bin/python -m scripts.detector prepare
./venv/bin/python -m scripts.import_extra_detection  # after extracting the second source to data/extra_detection/
./venv/bin/python -m scripts.prepare_gallery
./venv/bin/python -m scripts.baseline_v2
./venv/bin/python -m scripts.eval_router --fit
./venv/bin/python -m scripts.eval_router --final
./venv/bin/python -m scripts.detector train --epochs 12
./venv/bin/python -m scripts.eval_end_to_end
./venv/bin/python -m scripts.plot_results
make check
```

GPU training and GPU EasyOCR inference require a working CUDA installation. The project was run with an RTX 4060 Laptop GPU; FastPlateOCR uses local ONNX CPU inference. The detector training run was interrupted after three completed epochs; its best available checkpoint was copied to `weights/plate_detector.pt` and evaluated. The one-time test commands refuse to overwrite final results.

The source images, crops, generated weights, and result files are Git-ignored. Do not redistribute the dataset. See the [data notes](docs/DATA_NOTES.md).

## Project layout

| Folder | Contents |
| --- | --- |
| `app/` | Streamlit demo. |
| `riskgate/` | Detection, OCR wrappers, confidence, and routing code. |
| `scripts/` | Data preparation, training, evaluation, and packaging. |
| `tests/` | Automated checks. |
| `docs/` | Project explanation, data notes, and measured evaluation. |
| `presentation/` | Slides and PDF for the faculty presentation. |
| `data/`, `weights/`, `results/` | Local inputs, model files, and generated outputs. |

Run commands from the project root. The generated submission ZIP stays at the root; calibration lives in `weights/`, and the grouped split manifest lives in `data/`.
