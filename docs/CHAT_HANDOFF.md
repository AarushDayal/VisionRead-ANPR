# RiskGate handoff for a new chat

**Updated:** 15 November 2026
**Project:** `/home/aarush/Aarush/Projects/riskgate`  
**Git branch:** `main`; submission freeze records the completed work under tag `submission-final`.
**College PBL submission deadline:** 16 November 2026.

## User's goal and constraints

The user needs a substantial, understandable final college PBL project. The first prototype called Gemini on a few test photos. The final project should show real engineering and evaluation, work without paid API keys, run locally on an RTX 4060 laptop, have a polished frontend, and be easy to explain to faculty. The user also has other subjects to study, so favour focused, high-value changes and clear explanations. They requested a lean file structure and full vehicle or street photos in the demo rather than only plate close-ups.

Do not describe the user's contribution as writing every line unaided. Help them understand and present what was actually built. They especially need to explain the data flow, what was trained, why confidence matters, how this differs from a Gemini image API call, how it compares with commercial systems and research, and honest limitations.

## What exists now

RiskGate is an **offline Indian number plate research prototype**. A Streamlit app accepts a full vehicle photo or plate crop. On a full photo it uses a fine-tuned YOLO11n detector to locate the plate, crops the image, reads text with local FastPlateOCR, checks plate format, estimates whole-string correctness with a logistic model, and displays **ACCEPT** or **REVIEW**. Uncertain results are for human review; the app does not call an LLM API. It shows the photo, box, crop, text, scores, reason, and a correction field. Corrections are logged locally and do not automatically retrain models. There is a 20-image batch view, CSV export, evidence charts, and a 12-photo gallery of real vehicle scenes. Crop mode bypasses the detector for diagnosis.

Read these first in the next chat:

1. [README](../README.md): run commands and folder layout.
2. [FACULTY_EXPLANATION.md](FACULTY_EXPLANATION.md): detailed layperson explanation, training, data flow, retained code files, industry/research comparison, future work, and viva questions.
3. [EVALUATION_REPORT.md](EVALUATION_REPORT.md): actual numbers and caveats.
4. [DATA_NOTES.md](DATA_NOTES.md): dataset origins, label quality, and terms.

The app is [app/streamlit_app.py](../app/streamlit_app.py). Core logic is under `riskgate/`; preparation, training, evaluation, plots, and packaging are under `scripts/`. Slides are in `presentation/`. Large source data, models, and generated results are local and Git-ignored. The portable [submission ZIP](../RiskGate_Submission.zip) contains the demo, model files, selected results, docs, slides, and the 12 gallery photos. The ZIP is also Git-ignored; regenerate it after changes.

## Data, training, and results to state accurately

- Main source: Saisirishan Indian vehicle dataset; 1,697 image/XML pairs, **1,695 usable**. Split by repeated plate identity and source-video group: **847 train, 339 calibration, 255 validation, 254 test**. Some XML labels are wrong; a visual audit of 180 crops found eight clear issues. Numerical results still use source XML text as the answer key.
- Detector: YOLO11n initialized from pretrained weights and fine-tuned on the laptop GPU. The first run was interrupted after three completed epochs. A later stage added **180 screened full vehicle photos** from a second source to detector training (1,027 training images total) and fine-tuned three more epochs from the checkpoint. These extra photos had boxes, not trustworthy plate text.
- OCR: EasyOCR and FastPlateOCR were compared on the same crops. FastPlateOCR was selected. **No OCR network was trained from scratch or fine-tuned.** Awiros was assessed but left out: its reported seed training data overlaps the main source, making the current test non-independent, and its inference setup needs another runtime.
- Confidence: a small logistic correctness model was fitted on 339 calibration predictions; acceptance thresholds were chosen on 255 validation predictions. The 10% figure is a validation **target**, not a guarantee.
- Expanded detector: **248/254** labeled boxes matched at IoU ≥ 0.5 (97.6% recall), versus 237/254 before the extra training. It predicted a box in 250/254; box detection and exact text reading are different measures.
- Complete full-image exact plate reading: **71/254 (28.0%)**. At the 10% validation target, **75/254** were automatically accepted and **11/75** accepted readings were wrong (**14.7% observed accepted error**). Strict 2% and 5% targets accepted none. Do not claim the 10% target was achieved or that this is deployment-ready.
- The detector update reused a test set whose earlier results had been viewed. The test remained separate from fitting, but the comparison was **not fully blinded**. Gallery examples are for demonstration, not a new benchmark.

## Recent work and decisions

- Built the offline Streamlit console, local OCR comparison, detector training/evaluation, confidence routing, batch review, result charts, and nine-slide presentation.
- Replaced the earlier close-up demo gallery with 12 original full vehicle/street images. Gallery crops are created in memory. Fixed a Streamlit stale-cache bug that caused a `FileNotFoundError` for deleted old gallery photos; the manifest reader is now uncached.
- Organized the repo, then removed obsolete prototype scripts, unused Gemini experiment/cascade code, duplicate plans, and old tests tied only to removed code. Retained data, trained weights, measured results, and scripts needed to reproduce or audit the final pipeline. The tracked repo went from 60 to 42 files. The current submission ZIP has 59 files.
- Consolidated the explanation into one file, `docs/FACULTY_EXPLANATION.md` (about 4,500 words). It includes a file map and a simple industry/research comparison. Keep future explanatory additions there rather than creating more overlapping guides.
- Latest completed commit before this file: `3b0c9a8` (`Consolidate faculty explanation into one guide`). This describes the earlier handoff; the submission freeze update is below.

## Commands and verification

Run from the project root:

```sh
./venv/bin/streamlit run app/streamlit_app.py
make check
./venv/bin/python -m scripts.package_submission
```

At the earlier handoff check, `make check` passed **20 tests**, including a gallery-photo app smoke test. The rebuilt ZIP was extracted to a clean temporary directory and the bundled app analyzed `RJ27TC0530` successfully. Refresh the ZIP after any code or documentation changes that should be submitted. `docs/AGENTS.md` contains local project work rules: test after changes, never commit datasets/crops/keys, and never edit reviewed labels.

## Practical cautions for the next assistant

- Do not rerun protected one-time evaluation commands casually; some refuse overwriting results and the test has already been viewed. Check scripts and report before changing claims.
- Do not delete `data/`, `weights/`, or `results/` wholesale. They are ignored in Git but contain the local source data, trained models, split manifest, and measured outputs needed for the demo and presentation.
- The source gallery photos are copied unmodified from a dataset whose Kaggle metadata says CC BY-NC-ND 4.0. The ZIP is intended for noncommercial academic presentation with attribution; check source terms before wider distribution.
- No paid API key is required. The final app makes no Gemini calls. An optional vision-language second opinion is future work, not a current feature.
- The user's next request should determine the next work. Avoid inventing new features close to the deadline; prioritise reliability, clarity, and truthful presentation.

## Submission freeze: exploratory grammar results

**15 November 2026.** The [Exploratory: grammar + conservative threshold](EVALUATION_REPORT.md#exploratory-grammar--conservative-threshold) experiment is **crop-level only**: it reuses cached FastPlateOCR readings, not the full-photo detector pipeline. **The test set was already viewed**, so this is an exploratory repeated test, not a blinded result. **Grammar correction is NOT enabled in the app by default**; it remains in a separate evaluation script. The app, saved confidence model, thresholds, and earlier measurements are unchanged.

The correction uses positions in strings of length 9–11: two state letters, two district digits, one to three series letters, and four final digits. It substitutes only O/0, I/1, B/8, S/5 and Z/2 according to those positions. It does not cover every Indian format or check whether a state code exists. Two correctness calibrators were fitted on 339 calibration readings, with corrected correctness labels for the grammar variant and unchanged cached features. Thresholds were selected on 255 validation readings and frozen before evaluating the 254 test readings.

| Crop-test variant | Exact plates | Mean CER | 10% target: coverage | 10% target: accepted errors; Wilson 95% interval |
| --- | --- | ---: | --- | --- |
| Baseline, Wilson selection | 71/254 (28.0%) | 0.2210 | 72/254 (28.3%) | 9/72 (12.5%); 6.7–22.1% |
| Grammar, Wilson selection | 90/254 (35.4%) | 0.2148 | 97/254 (38.2%) | 15/97 (15.5%); 9.6–24.0% |
| Baseline, Clopper–Pearson selection | 71/254 (28.0%) | 0.2210 | 72/254 (28.3%) | 9/72 (12.5%); 6.7–22.1% |
| Grammar, Clopper–Pearson selection | 90/254 (35.4%) | 0.2148 | 97/254 (38.2%) | 15/97 (15.5%); 9.6–24.0% |

Grammar improved exact match and mean character error rate, but **10% target accepted error rose 12.5% → 15.5%** as more readings were accepted. At 2%, all four variants accepted nothing. At 5%, both baseline variants accepted nothing, while both grammar variants accepted 42/254 (16.5%) with zero errors; their Wilson interval was 0–8.4%, so this does not establish error below 5%. With no acceptances the error rate is undefined and the recorded interval is the uninformative [0, 1]. Full evidence is in `results/grammar_eval.json`, included in the submission ZIP.

**Viva: Why is grammar not the default?** It improved crop-level text accuracy, but the 10% policy's accepted error worsened from 12.5% to 15.5%. It also assumes a restricted plate layout, and the experiment reused an already-viewed test. We have no fresh full-image evidence supporting a default change, so the app keeps its original readings and policy.

**Viva: Why did Clopper–Pearson change nothing?** We replaced the Wilson threshold-selection bound with the upper endpoint of the two-sided 95% exact Clopper–Pearson interval. On these validation readings, both bounds qualified the same lowest confidence cutoffs at all three targets. The bounds differ numerically, but no cutoff decision changed, so the accepted test sets stayed identical. Exact binomial intervals do not fix OCR errors or provide a guarantee after searching thresholds, especially with correlated video frames.

The submission is frozen after packaging and verification. No new features are planned for this submission.
