# RiskGate: complete faculty explanation in simple words

**A plain-language guide to what we built, how it works, and why.**  
**Project state checked:** 11 November 2026. For the precise experiment conditions, see the [evaluation report](EVALUATION_REPORT.md).

## The whole project in one minute

RiskGate takes a photo of a vehicle and tries to read its number plate. It then decides whether to **accept the reading automatically** or **ask a person to check it**. ANPR stands for *Automatic Number Plate Recognition*. OCR stands for *optical character recognition*: reading letters and numbers from an image.

The key idea is simple: a computer can give a convincing-looking answer that is wrong by just one character. RiskGate therefore shows the evidence behind its answer and sends uncertain cases for review.

```text
Vehicle photo
    ↓
Find the plate's location (detector)
    ↓
Cut out the plate (crop)
    ↓
Read its letters and digits (OCR)
    ↓
Check its format and estimate whether the whole reading is correct
    ↓
ACCEPT, or ask a person to REVIEW and correct it
```

There are **two separate processes** to understand. *Building and evaluating* the system happens beforehand, using labeled images. *Using* the system happens when someone uploads a new photo to the demo. Training does not happen every time a photo is uploaded.

**How to use this file:** Read the photo journey in Part 2 first if you are new to the project. Then read Part 1 to learn how the models were prepared. Before the viva, practise the short spoken explanation and the questions near the end. The [evaluation report](EVALUATION_REPORT.md) holds the exact measurements; this file explains what they mean.

## Part 1: How we built the system

### Step 1 — Get images with answers attached

The main [vehicle dataset](https://www.kaggle.com/datasets/saisirishan/indian-vehicle-dataset) contains photos and XML annotation files. Think of an XML file as a small answer sheet for a photo. It gives the plate's rectangle and the text that the plate is supposed to contain. We found **1,695 usable image/XML pairs**; two more annotations pointed to missing photos.

The labels are helpful, but they are not perfect. We visually inspected 180 plate crops and found eight clear annotation problems, including foreign plates, incomplete text, and one vehicle badge labeled as a plate. The numerical results still use the source XML text as their answer key. That limits how strongly we can claim accuracy. The [data notes](DATA_NOTES.md) explain the sources and label status.

### Step 2 — Keep similar photos together when splitting the data

We divided the 1,695 images into four groups:

| Group | Images | What it is for |
| --- | ---: | --- |
| Training | 847 | Teach the detector and select the local OCR reader. |
| Calibration | 339 | Learn what correct and incorrect OCR results tend to look like. |
| Validation | 255 | Choose the rule for automatic acceptance. |
| Test | 254 | Measure the resulting system on images not used for fitting. |

Many photos came from video. Ten adjacent frames might show the same car and plate. If some frames were used for training and others for testing, the test would be too easy. We therefore grouped frames from the same source video and repeated plate identities before splitting.

This reduces a common problem called **data leakage**: accidentally letting the system see nearly the same example while it learns and while it is being tested. It does not rule out every possible duplicate. Also, some test results were viewed before later detector improvements, so the final comparison is *held out from fitting but not fully blinded*.

### Step 3 — Train a model to find the plate

The detector's only job is to answer: **“Where in this full photo is the number plate?”** It draws a rectangle around the most likely plate. We started with a small, already-pretrained YOLO11n model and fine-tuned it on plate rectangles. This is much more practical on a laptop RTX 4060 than training a vision model from nothing.

We also screened a second dataset and added **180 full vehicle photos with plate boxes** to detector training. The detector then had **1,027 training images** in total. Those extra images did not have trustworthy plate text, so we did not treat them as OCR answers.

On the 254-image test, the expanded detector produced a matching box for **248 images**, using a minimum box overlap of 0.5. It found some sort of plate box in 250 images, but two of those boxes did not match the labeled location closely enough. A *correct box* tells us where the plate is; it does **not** tell us that every character will be read correctly.

### Step 4 — Choose a model to read the cropped plate

Once the plate is located, the app cuts out just that part of the photo. This smaller image is the **crop**. We compared two local OCR readers, EasyOCR and FastPlateOCR, on the same labeled plate crops. FastPlateOCR was chosen because it read more complete plates correctly in the development comparison. The final demo uses its local model; it does not call Gemini.

We did **not** train a new OCR network from scratch. We integrated an existing reader and measured its behavior on this data. That distinction matters when explaining what work was actually done.

### Step 5 — Learn whether a whole reading is likely to be right

An OCR model supplies a score, but a high OCR score does not automatically mean “this entire plate is correct.” For example, `KA03MN1234` and `KA03MN1284` differ by one digit, yet both look believable.

We used the 339 calibration images to train a small **logistic regression** model. For each OCR result, it looks at the OCR score, whether the text resembles a plate format, text length, crop width and height, and OCR detection information. It learns how those signals relate to a **completely correct plate reading**. The resulting number is called the *correctness estimate*.

This is called **calibration**. If many similar readings receive an estimate near 80%, roughly 80% of those readings should be correct for the estimate to be well calibrated. It is still an estimate, not proof that any particular plate is right. The format check is only one clue: a wrong plate can have a perfectly plausible format.

### Step 6 — Choose when to accept and when to review

We used the separate 255-image validation group to choose confidence thresholds for three intended error targets: 2%, 5%, and 10%. The rule accepts a reading only when its format is eligible and its correctness estimate reaches the chosen threshold. Otherwise, the app marks it **REVIEW**. In the offline demo, a possible “get another opinion” state also ends in human review; it does not make an API call.

The tradeoff is:

- **Coverage:** How many images the computer handles automatically? If it accepts 30 of 100 images, coverage is 30%.
- **Accepted error:** Of the accepted readings, how many are wrong? If 3 of those 30 are wrong, accepted error is 3/30 = 10%.

Increasing caution generally reduces the number accepted. A “10% target” describes how a threshold was **selected on validation data**. It is not a guarantee of 10% error on new photos.

### Step 7 — Measure the complete system

Finally, we ran full vehicle photos through **detection → crop → OCR → confidence → decision**. If the detector misses the plate, that photo counts as an end-to-end failure, even if the OCR reader might have succeeded on a manually supplied crop. This is the result that matters when someone uploads a whole vehicle photo.

The 12 photos in the demo gallery are full vehicle or street scenes for showing how the app works. They are **presentation examples**, not a new benchmark or extra evidence of accuracy.

### Exactly what was trained, and what was reused

| Component | What happened |
| --- | --- |
| YOLO11n plate detector | Started with free pretrained weights and fine-tuned it on our plate boxes. The first run stopped after three completed epochs. We saved its best checkpoint, then ran three more epochs after adding 180 screened training photos. This is the component trained on the laptop GPU. |
| EasyOCR and FastPlateOCR | Used existing pretrained readers. We compared them on the same crops and selected FastPlateOCR; we did **not** fine-tune either OCR network. FastPlateOCR runs locally through ONNX. |
| Correctness model | Fitted a small logistic regression on 339 calibration predictions, using whether each complete plate string matched its label as the answer. This is training, but much smaller than training a vision network. |
| Acceptance thresholds | Chosen on 255 separate validation predictions. A threshold is a decision rule, not another neural network. |
| 254-image test | Used to report the results. Later detector changes were checked against this already-viewed test, so the updated comparison is exploratory. |

To reproduce the steps, follow the commands in the [README](../README.md). The main scripts are `prepare_indian → detector prepare/train → baseline_v2 → eval_router → eval_end_to_end → plot_results`. The second detector source is imported before the extra training stage. The demo simply **loads** the saved detector, OCR reader, and correctness model; it does not train them when you click Analyze.

## Part 2: What happens to one photo in the demo

Imagine you upload a photo of a car whose true plate reads `KA03MN1234`. These characters are just an example; they are not a claimed test result.

1. **The app receives the photo.** You can upload a JPG/PNG or select a gallery scene. The main demo processes it on this machine.
2. **The detector proposes a rectangle.** The app shows that box on the original image. If it finds no plate, it reports that the image needs manual review.
3. **The app cuts out the rectangle.** You see the crop beside the result. A poor crop can already make the next step fail.
4. **OCR reads the crop.** It might return `KA03MN1234`, or make a subtle error such as `KA03MN1284`.
5. **The app checks and scores the result.** It checks the plate's format and estimates the chance that the *entire string* is correct. Both example strings could pass a simple format check, so format alone cannot settle the case.
6. **The app routes the result.** A result that meets the selected acceptance rule is shown as **ACCEPT**. Other results are shown as **REVIEW** so a person can inspect the photo and correct the text.

The **Plate crop** input mode skips detection and sends a supplied crop straight to OCR. This helps demonstrate whether a failure comes from *finding* the plate or *reading* it. It is a diagnostic mode, not the complete vehicle-photo pipeline.

The app also offers a batch view for up to 20 uploads and a CSV export of its decisions. A human correction is saved in a local log. **Saving a correction does not automatically retrain the models**; it records information that could be reviewed and used in a future training cycle.

### What happens when you start the program?

Run the Streamlit command shown in the [README](../README.md). Streamlit opens the local dashboard. The app loads the saved plate detector, chosen OCR reader, and correctness model from files on the laptop. When you select a photo and press **Analyze plate**, the image is decoded into pixels; the detector and reader process those pixels; the decision is calculated; and the dashboard displays the evidence. No cloud API receives the image. Changing the review-policy setting changes the acceptance rule, not the detector or OCR weights.

The dashboard shows several numbers that sound similar but answer different questions:

| Number or check | Everyday meaning | What it cannot prove |
| --- | --- | --- |
| **Detector score** | How strongly the detector believes its chosen rectangle contains a plate. | It cannot tell whether the characters were read correctly. |
| **OCR model score** | How strongly the OCR reader supports the text it produced. | It is not automatically the chance that the complete plate string is right. |
| **Format result** | Whether the text resembles a familiar Indian plate pattern. | A one-character mistake can still look valid. |
| **Correctness estimate** | The small trained model's estimate that the *whole* text is right, based on the signals above and crop details. | It is a measured estimate for similar images, not a guarantee for this photo. |
| **ACCEPT / REVIEW** | The chosen policy's action after applying the estimate and format rule. | ACCEPT is not a certificate of truth; the test still found accepted mistakes. |

## Why this architecture instead of only calling an LLM API?

Your original prototype sent a photo to Gemini and displayed its answer. That was useful as a first demonstration: it proved that an AI system could sometimes read a plate. It did not establish how often the answer was exactly right, whether a plausible answer could be trusted, or how the demo would work without an API key or internet connection.

RiskGate separates the task into visible jobs. We can measure **plate location**, **character reading**, and **accept/review behavior** independently. The complete pipeline runs locally, so the main demo does not depend on paid API access or sending a vehicle photo to an external service.

An image-capable LLM could be added as an **optional second opinion** for difficult cases. That would produce another possible reading; it would not automatically tell us which reading is correct. If two readers disagree, a person still needs to check. An API could also add network delay, quota or cost limits, and data-sharing considerations. RiskGate currently uses **human review**, not an LLM API, for uncertain cases.

We also examined the Awiros Indian OCR model. Its published material describes use of our main dataset as seed training data, so testing it on that same dataset would not be an independent comparison. Its inference setup also needs another runtime. We therefore did not add it to the headline result or the offline demo.

## What the numbers actually mean

These are the current measured results on the grouped **254-image test**. The detector improvement was evaluated on the same test after earlier results had been viewed, so treat the comparison as exploratory.

| Question | Result | Plain meaning |
| --- | --- | --- |
| Did the expanded detector place a matching box? | **248/254** (97.6%) | Finding the plate usually works on this test. |
| Did the complete photo-to-text system read every character correctly? | **71/254** (28.0%) | Exact reading is much harder than finding the plate. |
| How many were accepted automatically at the 10% validation target? | **75/254** (29.5% coverage) | The other 179 were not automatically accepted. |
| How many accepted readings were wrong? | **11/75** (14.7% observed error) | The validation target was **not achieved** on this test. |
| What happened with the stricter 2% and 5% targets? | **0/254** accepted automatically | The available evidence did not justify any automatic accepts under those rules. |

Do not describe 97.6% detector box matching as “97.6% plate reading accuracy.” Also, an accepted result can still be wrong. The 10% setting is a *threshold-selection target*, and its actual observed error here was 14.7%.

The dataset has some inaccurate XML labels, repeated video frames, foreign plates, and limited coverage of difficult conditions. The results describe this academic experiment; they are not a claim of reliable performance at every camera, road, or time of day. **OCR is the main current bottleneck.** The appropriate next research step is to curate better Indian plate labels, improve or train the reader, and evaluate again without using the test repeatedly to guide changes.

## How this compares with real products and research

**Commercial systems:** The basic detector-and-reader idea is already used in industry. For example, [AXIS License Plate Verifier](https://www.axis.com/en-ph/products/axis-license-plate-verifier) runs recognition on compatible cameras and supports vehicle access, free-flow traffic, search, and event logs. Some systems also identify vehicle type, color, make, and model. [Rekor Edge Pro documentation](https://docs.rekor.ai/edge-pro/configuring/overview) describes configuring camera exposure and infrared settings for day and night conditions. These examples show why camera choice and image capture matter as much as software. Commercial products may connect to gates, lists of allowed vehicles, databases, and continuous video streams. RiskGate currently analyzes uploaded still images or small batches on a laptop; it has no live camera, gate, traffic-scale storage, or deployment accuracy claim.

**Research:** Researchers are still tackling low resolution, blur, different layouts, and confidence. The [ICPR 2026 low-resolution competition](https://arxiv.org/abs/2604.22506) used real low-quality plate tracks and showed that multiple views and difficult image conditions remain important. [BLPR](https://arxiv.org/abs/2604.09927) studies confidence-driven use of a vision-language model as a fallback. [Neural Sentinel](https://arxiv.org/abs/2602.07051) studies calibration and human involvement. These are examples of related ideas, **not features we invented or experiments we completed**. RiskGate's contribution is a small, transparent Indian-plate prototype that connects local detection, local OCR, calibrated whole-string confidence, and a measurable accept/review rule. Its measured accuracy is below what a dependable field system would need.

**Why our result cannot be compared directly with a product's advertised accuracy:** Products may use purpose-built cameras, controlled installation angles, infrared lighting, repeated video frames, and different datasets or definitions of a “correct” read. We used a mixed public-image dataset and required the *entire plate string* to match. A fair comparison would run both systems on the same independently labeled images under the same conditions.

Here are the research papers in one sentence each. Their reported results use different countries, datasets, and evaluation rules, so do not compare their percentages directly with RiskGate's 28% exact-match figure.

| Research | Main idea | Relationship to RiskGate |
| --- | --- | --- |
| [Indian Licence Plate Dataset in the Wild](https://arxiv.org/abs/2111.06054) | Indian plates in everyday scenes vary in appearance and conditions. | Motivates using Indian vehicle photos instead of only neat plate crops. |
| [VehiclePaliGemma](https://arxiv.org/abs/2412.14197) | Fine-tunes a vision-language model for difficult plate reading. | A possible stronger reader to study later; RiskGate did not train one. |
| [Neural Sentinel](https://arxiv.org/abs/2602.07051) | Combines a vision-language model with confidence calibration and human corrections. | Related motivation for measuring confidence and showing corrections; our corrections are logged, not automatically used for continual learning. |
| [BLPR](https://arxiv.org/abs/2604.09927) | Uses a second vision-language reader only when the first reading is uncertain. | A possible future fallback; our current uncertain cases go to a person. |
| [ICPR 2026 low-resolution LPR competition](https://arxiv.org/abs/2604.22506) | Studies recognition on difficult low-resolution plate tracks. | Motivates testing small plates and combining multiple video frames later. |
| [Nigerian VLM comparison](https://arxiv.org/abs/2607.02025) | Compares five vision-language models on 88 challenging Nigerian images. | Shows another approach worth benchmarking, but it is a different country and a small test. |

### Future work, in a sensible order

1. **Fix the answer key.** Review more XML labels, remove foreign or incomplete examples, and gather permission-cleared Indian plates from the cameras intended for use.
2. **Improve reading.** Train or fine-tune a specialist OCR model on corrected Indian crops; evaluate small, blurry, two-row, night, and angled plates separately.
3. **Use more than one frame.** A vehicle in video can give several views of the same plate; combine them only after measuring whether this reduces errors.
4. **Re-test without peeking.** Freeze the new model and policy, then use a fresh grouped test from a different camera or location. Report whole-string accuracy, accepted error, coverage, and processing time.
5. **Only then consider deployment.** Add camera integration, secure event storage, access rules, monitoring, privacy controls, and a human review workflow. An optional VLM second opinion should be compared on the same held-out images, including latency, cost, and wrong-but-confident answers.

## Which remaining files do what?

Start with the **live path**: `app/streamlit_app.py` calls the reader and detector, then `riskgate/features.py`, `calibration.py`, `grammar.py`, and `router.py`. Read the training and evaluation scripts afterward. Files with `__init__.py` simply mark Python packages.

| File or group | Why it remains |
| --- | --- |
| `app/streamlit_app.py` | The whole user interface: upload/gallery, analysis, decision display, correction, batch export, and evidence tabs. Its `analyze()` function is the live photo-to-decision path. |
| `riskgate/config.py`, `contracts.py` | Project paths and small data shapes: a labeled plate sample and an OCR result. |
| `riskgate/data.py` | Load annotated samples, apply any separately reviewed text overrides, group samples for splitting, and crop images. |
| `riskgate/engines/easyocr_engine.py`, `fastplate_engine.py` | Wrap the two existing OCR libraries so each returns text, model score, timing, and error information in the same form. |
| `riskgate/grammar.py`, `metrics.py` | Plate-format categories and measurement helpers such as exact match, character error rate, calibration error, and coverage. |
| `riskgate/features.py`, `calibration.py`, `router.py` | Convert an OCR result into numeric signals, fit/load the correctness model, choose thresholds, and return ACCEPT or REVIEW/ESCALATE. The offline app displays non-accepted cases for review. |
| `scripts/prepare_indian.py`, `import_extra_detection.py` | Read source annotations and prepare the original and extra detector data. |
| `scripts/detector.py` | Prepare YOLO labels, train/fine-tune the detector, and measure box matching. |
| `scripts/baseline_v2.py`, `eval_router.py`, `eval_end_to_end.py` | Compare OCR readers, fit confidence and select thresholds, then evaluate the full image pipeline. |
| `scripts/prepare_gallery.py`, `label_tool.py` | Copy the real-scene demo gallery and review draft text labels without silently overwriting source XML labels. |
| `scripts/plot_results.py`, `package_submission.py` | Draw the report charts and assemble the portable submission ZIP. |
| `tests/` | Check grouping, labels, box math, OCR ordering, confidence, routing, metrics, and the live gallery path. |
| `docs/`, `presentation/` | This explanation, data provenance, measured report, and slides. |
| `data/`, `weights/`, `results/` | Local source/generated data, saved models, and experiment outputs. Large files are intentionally outside Git. |
| `README.md`, `requirements.txt`, `Makefile`, `.streamlit/config.toml` | Starting instructions, Python dependencies, test command, and the demo's visual settings. |

If asked about a line of code, identify **its input, output, and which step above it serves**. For example, `analyze()` receives image pixels and a mode, detects/crops when needed, calls OCR, estimates correctness, and returns a result dictionary to the screen. This is more useful than memorizing syntax without knowing what it does.

## What you can show in the faculty demo

1. Start with a **full vehicle photo** in the gallery. Point to the original photo, detected box, crop, and proposed text.
2. Point to **OCR model score** and **correctness estimate**. Explain that they answer different questions.
3. Point to **ACCEPT** or **REVIEW** and read the stated reason. Show how a person can correct an uncertain result.
4. Open the **Measured evidence** tab. State the 71/254 exact reading result and the 75 accepted / 11 wrong result honestly.
5. If asked where errors come from, compare full-photo mode with **Plate crop** mode on the same example. Show that a correct box can still lead to wrong characters.

Choose one example that works and one that fails before the presentation. A failure is useful evidence if you can explain which stage caused it. Do not imply that a gallery example is a separate test result.

## A short explanation you can say aloud

> “I started with a prototype that asked Gemini to read a number plate. For this project I built a local pipeline and measured each stage. First, a YOLO detector finds the plate in a full vehicle photo. Then FastPlateOCR reads the cropped plate. A small confidence model uses the OCR result and image information to estimate whether the whole plate is right. The app accepts only readings that pass a threshold chosen on separate validation data; the rest go to human review.
>
> On our grouped 254-image test, the expanded detector placed a matching box for 248 images, but the complete system read only 71 plate strings exactly. At the 10% validation target, it accepted 75 automatically, and 11 of those were wrong. So I would not deploy it unattended. The project shows a working offline system, measured limitations, and a clear direction for improving OCR.”

## Questions you may get

**“What is your contribution if YOLO and OCR already exist?”**  
“I put the parts together for vehicle photos, trained the detector on this data, compared readers, built a correctness estimate and review rule, and measured the full system. I am not claiming to have invented YOLO or a new OCR network.”

**“Why do you need two confidence numbers?”**  
“The OCR score comes from the reader. The correctness estimate is trained to predict whether *every character* in the plate is right. A strong OCR score can still accompany a one-character mistake.”

**“Does REVIEW mean the system failed completely?”**  
“No. It may have a useful proposed reading, but it is not confident enough to trust automatically. A person can inspect and correct it. If detection misses entirely, that is a full-image reading failure and also needs review.”

**“Could Gemini replace the whole pipeline?”**  
“It could provide a reading or a second opinion, but I would still need labeled tests and a rule for handling errors. The local pipeline makes each stage visible and works without an API key.”

**“Can you claim the system meets a 10% error limit?”**  
“No. The threshold was selected with that target on validation data, but the test showed 11 errors among 75 accepted readings, or 14.7%. I report the observed result.”

**“Does saving a correction improve tomorrow's predictions?”**  
“Not by itself. The correction is logged locally. It would need to be checked and included in a later, controlled training run.”

**“What would you improve next?”**  
“I would first audit and correct more labels, then improve OCR for small, blurry, and unusual Indian plates. I would use a fresh evaluation set to measure whether it actually helps.”

## Tiny glossary

| Word | Simple meaning |
| --- | --- |
| **Annotation / label** | The answer attached to an image: plate location and/or text. |
| **Detector** | The model that finds the plate's location. |
| **Crop** | The smaller image cut out around the plate. |
| **OCR** | The reader that turns plate pixels into letters and digits. |
| **Fine-tuning** | Adapting a pretrained model to our labeled examples. |
| **Calibration** | Checking and improving what a confidence number means. |
| **Threshold** | The minimum estimate required for automatic acceptance. |
| **Coverage** | The share of images accepted automatically. |
| **Accepted error** | The share of automatically accepted readings that are wrong. |
| **Test set** | Images reserved to measure the system after training and threshold choice. |

**If you only remember three things:** finding a plate is different from reading it; a high model score is not proof that the whole text is right; and uncertain readings must go to a person. For exact results and caveats, keep the [evaluation report](EVALUATION_REPORT.md) beside this guide.

## Part 8: PBL research extension — checking whether a reading stays the same

**Added 12 November 2026.** Use the [every-line source companion](CODE_WALKTHROUGH.md) alongside this guide. It contains the actual source and an explanation for every physical Python line, including tests. It explains our code; it does not pretend to explain millions of numbers inside downloaded neural networks.

### A project title you can defend

**RiskGate: An Offline, Uncertainty-Aware Number Plate Recognition System with Explainable Human Review and Image-Stability Testing.**

A useful research question is: *Can simple consistency checks identify unreliable plate readings beyond a calibrated confidence threshold, and what automation do we lose in exchange?* That is specific enough to implement, measure, and discuss. “An AI that reads plates” is a much less precise contribution.

The completed extension adds a fixed image-stability check, an optional veto in live and batch analysis, a visible table of transformed readings, an experiment comparing the policy with and without the veto, and reproducible source documentation. It uses existing installed libraries and the existing OCR model. It does not train another neural network.

### The simplest analogy

Imagine reading a number from a paper. You move the paper slightly closer and turn up the light. If you suddenly read a different number, you should check the paper again. If you read the same number three times, you might still be consistently misreading a damaged digit. That distinction is the entire point of this experiment.

For one detected plate crop, the code keeps the original answer and creates two copies:

1. A copy enlarged to 125% of its width and height using cubic interpolation. Interpolation estimates new pixel values between existing ones; it cannot recover details that were never photographed.
2. A copy with pixel values multiplied by 1.10. Values above 255 are clipped to 255. This slightly brightens an ordinary 8-bit image. It can also saturate a bright area, so disagreement can be caused by the transformation itself.

The same OCR reader processes both copies. Their text is normalized in exactly the same way as the original answer. Both must produce nonempty, error-free text that exactly matches the original. Matching 9 of 10 characters is still disagreement, because one wrong character can identify another vehicle.

`matching_variants` is a count between zero and two. It is **not a correctness probability**. These are correlated outputs from one model looking at nearly the same pixels. Three identical wrong answers remain possible. We deliberately do not multiply confidence scores or treat these reads as three independent witnesses.

### How acceptance changes

The original policy uses plate format and calibrated confidence. The experiment adds a second condition:

```text
Final ACCEPT = original policy ACCEPT AND stability check passes
Otherwise REVIEW
```

A failure never rewrites the original characters, selects a more attractive answer, or promotes a review into acceptance. The trace retains `base_route`, the route before the veto, and `route`, the route after it. This is an ablation: comparing one system with one component switched off against the same system with that component switched on.

“Only removes acceptance” is a guarantee about program behaviour, not a guarantee about the percentage of accepted answers that are wrong. If the veto removes correct answers and leaves wrong ones, that percentage gets worse. This is why both accepted error and coverage must be measured.

### What the experiment actually found

We ran the fixed check on the existing 12 full-vehicle gallery scenes. The images were already selected for demonstration, so this is a descriptive experiment on known examples. It is not independent validation, a new held-out benchmark, or proof of generalization.

| Measurement | Original policy | With stability veto |
| --- | --- | --- |
| Images | 12 | 12 |
| Exactly correct original OCR readings | 4 | 4 |
| Automatically accepted | 5 | 4 |
| Wrong accepted readings | 1 | 1 |
| Coverage | 41.7% | 33.3% |
| Error among accepted | 20.0% | 25.0% |

The extra reads took about **21.2 milliseconds per detected crop on this run**. This is added checking time, including constructing variants; it is not the complete detection-plus-OCR latency and is not a hardware-independent speed claim.

The veto removed one correct acceptance and retained the incorrect acceptance. Therefore it **did not improve the observed error rate**. The prototype leaves this experimental feature off by default. The sidebar lets you enable it for demonstration. This is a negative research result with an engineering consequence: a plausible extra check was measured, and the default policy was preserved because the evidence did not support enabling it.

The full record, including every variant reading, is `results/stability_gallery.json`. Run `./venv/bin/python -m scripts.eval_stability` only when this record is absent; the script refuses to replace the first run. No original evaluation results or reviewed labels were overwritten. Future work should freeze a policy using calibration/validation images and test once on newly collected, independently labelled images. Choosing new transformations repeatedly to improve this 12-image result would overfit the gallery.

### How the confidence mathematics works, slowly

The OCR reader produces its own score. FastPlateOCR provides character scores, which our wrapper averages. A high average can hide one bad character. For illustration, even if ten characters each had a genuinely independent 95% chance of being right, the chance all ten were right would be `0.95^10`, about 60%. Real character errors are not independent, and the raw scores are not necessarily probabilities. This calculation explains the distinction; it is not our confidence formula.

Our small correctness model takes six numbers: raw OCR score, format category, text length, crop height, crop width, and number of text boxes. Each feature is standardized: subtract its calibration-set mean and divide by its calibration-set standard deviation. This lets quantities measured on different scales, such as pixels and a 0–1 score, enter the model sensibly.

For each standardized feature, multiply by its learned weight. Add those products and a learned intercept. This total is called a score, `s`. Convert it to a value between zero and one with `1 / (1 + exp(-s))`. This is logistic regression. Positive weights push the estimate up as that feature grows; negative weights push it down, holding the others fixed. The model learns the weights from examples labelled “whole reading correct” or “whole reading wrong.” A format match is evidence, not proof.

The code clips `s` to the interval −700 to 700 before computing the exponential to avoid numerical overflow. The JSON file stores weights, means, scales, feature order, date, and a fingerprint of fitting data. Inference uses this saved recipe rather than learning again for each upload. Logistic regression can still be poorly calibrated on a new camera or different kinds of plates.

Threshold selection then sorts validation readings by estimated correctness. It considers complete groups of tied scores, counts errors in the accepted prefix, and checks a Wilson upper confidence bound against each error target. A Wilson interval accounts for sampling uncertainty better than simply assuming zero observed mistakes means zero risk. For example, zero wrong answers in only five trials is weak evidence. Zero wrong answers in many trials is stronger evidence.

The 1.96 constant gives the usual approximate 95% two-sided Wilson interval for a fixed binomial sample. Searching many thresholds on the same validation set does **not** turn that interval into a simultaneous or distribution-free guarantee. The original script uses it as a threshold-selection heuristic. The full-photo inference crops also differ from the labelled crops used to fit confidence, which can change calibration. Adding a stability veto changes the accepted subset again; the old confidence estimate is not a recalibrated estimate conditional on passing that veto.

### What is ours, what is reused, and what you can say about originality

Existing components include YOLO, EasyOCR, FastPlateOCR, logistic regression, format checks, and the broader idea of selective prediction. Existing research already studies rejecting uncertain predictions: see [Selective Classification for Deep Neural Networks, 2017](https://proceedings.neurips.cc/paper_files/paper/2017/hash/4a8423d5e91fda00bb7e46540e2b0cf1-Abstract.html) and [SelectiveNet, 2019](https://proceedings.mlr.press/v97/geifman19a.html). RiskGate does not implement SelectiveNet's jointly trained architecture. Image transformations for scene-text recognition also predate this project; [STRAug, 2021](https://openaccess.thecvf.com/content/ICCV2021W/ILDAV/html/Atienza_Data_Augmentation_for_Scene_Text_Recognition_ICCVW_2021_paper.html) is a training augmentation paper, not evidence that our particular inference veto works.

The concrete student-project contribution is integrating an offline full-photo pipeline, grouped data preparation, detector adaptation, reader comparison, whole-string correctness estimation, explicit review routing, visible evidence, local corrections, and a measured optional stability extension. That is substantial engineering and an experimental study. It does not establish a new algorithm or patentability. No patent search or legal novelty assessment has been completed. Do not put “patented,” “patent pending,” “first ever,” or “guaranteed safe” on the submission.

If asked for an invention direction, describe it as a **proposal for further investigation**: camera-specific acceptance control combining measured correctness, reading stability, and human review evidence. To make that direction credible, you would need fresh camera data, comparisons against confidence-only baselines, careful investigation of existing work, and evidence that a specific technical change helps. Those are future tasks, not completed results.

### A two-minute faculty pitch

“My project is RiskGate, an offline number plate recognition and review system. It finds a plate in a vehicle image, reads the characters, and estimates whether the complete answer is correct. The important problem is that a readable-looking plate can still contain one wrong character. So I measure both how many cases the system automates and how many automated readings are wrong.

“I adapted a YOLO detector, compared local OCR readers, fitted a small correctness model, and selected review thresholds on separate validation data. The detector matches 248 out of 254 labelled boxes, but the complete pipeline reads only 71 plates exactly. The bottleneck is reading, and I show that limitation explicitly.

“I also implemented an image-stability experiment: enlarge and brighten the crop slightly, read again, and send disagreements to review. On 12 existing demo scenes it removed a correct acceptance while retaining a wrong one. So it remains optional. This showed why extra AI checks need measurement rather than an assumption that more checks must improve accuracy.

“The result is a reproducible prototype with visible evidence and human correction. The next research step is curated Indian-only labels and stronger OCR, followed by evaluation on a fresh camera dataset.”

### Viva questions about this extension

**Why did you keep an experiment that did not help?** It answers a concrete question, has a reproducible result, and shows why the default was left unchanged. An unsuccessful hypothesis is still a useful result when the method and conclusion are accurate.

**Is this three different AI models voting?** No. One model reads three related images. The outputs are correlated.

**Does agreement increase confidence to 100%?** No. The stability count is separate from the saved correctness estimate. A stable wrong reading is possible and occurred in the gallery.

**Why not just correct O to 0?** Changing characters can invent a plausible but wrong registration. The app normalizes case and removes separators; it does not silently substitute ambiguous characters. The separate crop-level grammar experiment below tests position-aware substitutions without enabling them in the app.

**Can your system verify that the plate belongs to that car?** No. There is no registration-database lookup or identity verification. Recognition is different from authorization.

**Does saving a correction teach the AI immediately?** No. It writes a local CSV record containing a timestamp, image fingerprint, original suggestion, and correction. Retraining requires a separate, reviewed procedure. Hashing an image identifies identical bytes; it is not encryption or a guarantee of anonymity.

**Why not promise a 2% error rate?** The strict policy currently accepts nothing, and the 10% validation-target policy misses that target on the recorded full-photo test. A target is a selection setting, not a deployment guarantee.

### Demonstration order and remaining non-Python files

Start with `./venv/bin/streamlit run app/streamlit_app.py`. Choose a gallery photo in full-photo mode, click Analyze, and identify the box, crop, text, correctness estimate, and decision. Explain the distinction between detector score and whole-answer confidence. Enable the experimental sidebar checkbox and click Analyze again; changing the checkbox alone does not recompute a previously displayed result. Show the original and transformed readings. Open Measured evidence and the ablation panel. Finally demonstrate a correction and batch CSV export. Show difficult examples as well as easy ones.

`README.md` is the entry point and command reference. `requirements.txt` lists Python packages; it currently has no version pins, so installing later can produce a different environment. `Makefile` gives `make check` its test command. `.gitignore` excludes local environments, bulky/private data, generated results, model weights, and the submission ZIP from ordinary Git tracking. `.streamlit/config.toml` chooses demo colors and a 12 MB per-file upload limit. `presentation/presentation.html` contains slide content, CSS appearance, and a small JavaScript arrow-key navigator; the PDF is its printable export. `docs/DATA_NOTES.md` describes dataset provenance. `docs/EVALUATION_REPORT.md` contains the original measurements and this extension's summary. `docs/CHAT_HANDOFF.md` preserves earlier project context and is historical. `docs/AGENTS.md` gives editing instructions to coding assistants, not instructions executed by the app.

`data/` holds source images, labels, split manifests, and gallery assets. `weights/` holds the detector, OCR network, and calibration parameters. These binary weights are learned numerical arrays, not handwritten Python source. `results/` contains CSV predictions, JSON measurements, plots, and the local correction log. `RiskGate_Submission.zip` is a generated portable snapshot, not an additional implementation. The every-line companion covers all first-party Python files and tests; external dependencies, data rows, model tensors, and generated binary artifacts are explained by role rather than pretending that each byte is a source-code line.

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
