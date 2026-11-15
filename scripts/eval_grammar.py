"""Exploratory cached-crop ablation; never changes the app or fitted defaults."""

import csv
import hashlib
import json

from scipy.stats import beta

from riskgate import config
from riskgate.calibration import fit, predict
from riskgate.grammar import classify
from riskgate.metrics import cer, exact_match
from riskgate.plate_grammar import correct_plate
from riskgate.router import TARGETS, choose_thresholds, route, wilson_interval


def clopper_pearson_upper(errors: int, total: int) -> float:
    """Upper endpoint of the two-sided 95% exact binomial interval."""
    if total == 0 or errors == total:
        return 1.0
    return float(beta.ppf(0.975, errors + 1, total - errors))


def choose_upper_thresholds(rows: list[dict]) -> dict[str, dict]:
    """Lowest confidence cutoff meeting the bound; ties accepted together."""
    eligible = sorted((r for r in rows if classify(r["pred"]) != "INVALID"),
                      key=lambda r: r["calibrated_conf"], reverse=True)
    chosen = dict.fromkeys(TARGETS)
    errors = 0
    for i, row in enumerate(eligible):
        errors += 1 - int(row["ok"])
        confidence = row["calibrated_conf"]
        if i + 1 < len(eligible) and eligible[i + 1]["calibrated_conf"] == confidence:
            continue
        upper = clopper_pearson_upper(errors, i + 1)
        for target in TARGETS:
            if upper <= target:
                chosen[target] = confidence
    return {f"{target:.2f}": {"accept_at": threshold, "review_below": 0.3}
            for target, threshold in chosen.items()}


def prepare_rows(rows: list[dict], grammar: bool) -> list[dict]:
    """Keep cached OCR features fixed; recompute text-dependent outcomes."""
    prepared = []
    for row in rows:
        text = correct_plate(row["pred"]) if grammar else row["pred"]
        prepared.append({**row, "pred": text, "ok": int(exact_match(text, row["truth"])),
                         "cer": cer(text, row["truth"])})
    return prepared


def summarize(rows: list[dict], thresholds: dict[str, dict]) -> dict:
    n = len(rows)
    targets = {}
    for target, policy in thresholds.items():
        accepted = [r for r in rows if route(r["pred"], r["calibrated_conf"], policy) == "ACCEPT"]
        errors = sum(1 - r["ok"] for r in accepted)
        targets[target] = {"accepted": len(accepted), "coverage": len(accepted) / n,
                           "accepted_errors": errors,
                           "accepted_error": errors / len(accepted) if accepted else None,
                           "accepted_error_wilson_95ci": wilson_interval(errors, len(accepted)),
                           "accepted_error_cp_upper_95": clopper_pearson_upper(errors, len(accepted))}
    exact = sum(r["ok"] for r in rows)
    return {"n": n, "exact_matches": exact, "exact_match": exact / n,
            "mean_cer": sum(r["cer"] for r in rows) / n, "targets": targets}


def main() -> None:
    output = config.RESULTS_DIR / "grammar_eval.json"
    if output.exists():
        raise FileExistsError(f"{output} exists; preserve the first exploratory test record")
    reads = config.RESULTS_DIR / "baseline_v2.csv"
    with reads.open(newline="") as source:
        rows = list(csv.DictReader(source))
    reader = json.loads((config.RESULTS_DIR / "selected_reader.json").read_text())["reader"]
    manifest = json.loads(config.SPLITS_V2.read_text())
    splits = {name: [r for r in rows if r["split"] == name]
              for name in ("calib", "val", "test")}
    for name, expected in (("calib", 339), ("val", 255), ("test", 254)):
        subset = splits[name]
        if (len(subset) != expected or len({r["image"] for r in subset}) != expected
                or any(r["reader"] != reader or r["group_id"] not in manifest[name] for r in subset)):
            raise ValueError(f"Unexpected reader, duplicates, size or membership in {name}")
    groups = [set(manifest[name]) for name in splits]
    if any(groups[i] & groups[j] for i in range(3) for j in range(i)):
        raise ValueError("Calibration, validation and test groups overlap")

    # All fitting and threshold selection finish before test outcomes are computed.
    frozen = {}
    for grammar in (False, True):
        calibration = prepare_rows(splits["calib"], grammar)
        validation = prepare_rows(splits["val"], grammar)
        model = fit(calibration)
        for row in validation:
            row["calibrated_conf"] = predict(model, row)
        frozen[grammar] = (model, choose_thresholds(validation),
                           choose_upper_thresholds(validation), validation)

    report = {"exploratory_repeated_test": True,
              "protocol": "Test was viewed earlier; this is not a blinded evaluation. Cached crop OCR only.",
              "reader": reader, "split_sizes": {name: len(part) for name, part in splits.items()},
              "input_sha256": hashlib.sha256(reads.read_bytes()).hexdigest(),
              "cp_convention": "Upper endpoint of two-sided 95% interval: Beta.ppf(0.975, errors+1, n-errors).",
              "selection": "Lowest confidence cutoff meeting validation bound; accept ties together; no solution accepts none.",
              "features": "Original cached features unchanged; grammar changes text and correctness labels only.",
              "variants": {}}
    for grammar, (model, wilson, upper, validation) in frozen.items():
        test = prepare_rows(splits["test"], grammar)
        for row in test:
            row["calibrated_conf"] = predict(model, row)
        for conservative, thresholds in ((False, wilson), (True, upper)):
            name = "grammar" if grammar else "baseline"
            if conservative:
                name += "_upper_bound"
            report["variants"][name] = {"calibrator": model, "thresholds": thresholds,
                                        "validation": summarize(validation, thresholds),
                                        "test": summarize(test, thresholds)}
    # Exclusive creation also prevents accidental overwrites by concurrent runs.
    with output.open("x") as destination:
        destination.write(json.dumps(report, indent=2) + "\n")
    print(json.dumps({name: variant["test"] for name, variant in report["variants"].items()}, indent=2))


if __name__ == "__main__":
    main()
