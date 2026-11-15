"""Descriptive gallery ablation, not a new held-out accuracy benchmark."""

import csv
import json
from statistics import mean

import cv2
from ultralytics import YOLO

from riskgate import config
from riskgate.calibration import load, predict
from riskgate.engines.fastplate_engine import FastPlateEngine
from riskgate.features import plate_features
from riskgate.metrics import exact_match, normalize
from riskgate.router import route
from riskgate.stability import apply_veto, check_stability


def main() -> None:
    output = config.RESULTS_DIR / "stability_gallery.json"
    if output.exists():
        raise FileExistsError("Keep the first gallery experiment; do not tune on these results")
    selected = json.loads((config.RESULTS_DIR / "selected_reader.json").read_text())["reader"]
    if selected != "FastPlateOCR":
        raise ValueError("This experiment requires the project's selected FastPlateOCR reader")
    reader = FastPlateEngine()
    detector = YOLO(str(config.ROOT / "weights/plate_detector.pt"))
    model = load(config.CALIBRATION_MODEL)
    with (config.ROOT / "data/sample_gallery/manifest.csv").open(newline="") as source:
        gallery = list(csv.DictReader(source))
    rows = []
    for item in gallery:
        image = cv2.imread(str(config.ROOT / item["image_path"]))
        if image is None:
            raise ValueError(f"Unreadable gallery image: {item['image_path']}")
        boxes = detector.predict(image, conf=0.25, verbose=False)[0].boxes
        row = {"image": item["image_path"], "truth": item["truth"], "pred": "",
               "base_route": "REVIEW", "route": "REVIEW", "stability": None, "ok": False}
        if len(boxes):
            box = max(boxes, key=lambda value: float(value.conf[0]))
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            crop = image[max(0, y1):min(image.shape[0], y2), max(0, x1):min(image.shape[1], x2)]
            if crop.size:
                read = reader.read(crop)
                pred = normalize(read.text)
                base = "REVIEW"
                if pred and not read.error:
                    confidence = predict(model, plate_features(crop, read))
                    base = "ACCEPT" if route(pred, confidence, model["thresholds"]["0.10"]) == "ACCEPT" else "REVIEW"
                evidence = check_stability(crop, pred, reader.read)
                row.update(pred=pred, base_route=base, route=apply_veto(base, evidence),
                           stability=evidence, ok=exact_match(pred, item["truth"]))
        rows.append(row)
    report = {"scope": "12 previously selected demo scenes; descriptive only, not held-out",
              "policy": "0.10 validation target; fixed resize 1.25 and brightness 1.10; exact agreement",
              "n": len(rows), "exact_reads": sum(row["ok"] for row in rows), "policies": {}}
    for key in ("base_route", "route"):
        accepted = [row for row in rows if row[key] == "ACCEPT"]
        errors = sum(not row["ok"] for row in accepted)
        report["policies"][key] = {"accepted": len(accepted), "errors": errors,
            "coverage": len(accepted) / len(rows), "accepted_error": errors / len(accepted) if accepted else None}
    timings = [row["stability"]["extra_latency_ms"] for row in rows if row["stability"]]
    report["mean_extra_latency_ms"] = mean(timings) if timings else None
    report["details"] = rows
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: value for key, value in report.items() if key != "details"}, indent=2))


if __name__ == "__main__":
    main()
