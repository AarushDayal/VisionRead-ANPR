import pytest

from riskgate.router import route
from scripts.eval_grammar import clopper_pearson_upper, choose_upper_thresholds, prepare_rows


def test_exact_upper_bound_edges() -> None:
    assert clopper_pearson_upper(0, 0) == 1.0
    assert clopper_pearson_upper(10, 10) == 1.0
    assert clopper_pearson_upper(0, 100) == pytest.approx(1 - 0.025 ** (1 / 100))
    assert clopper_pearson_upper(1, 100) > clopper_pearson_upper(0, 100)


def test_threshold_selection_keeps_ties_and_excludes_invalid() -> None:
    rows = [{"pred": "RJ27TC0530", "calibrated_conf": 0.9, "ok": 1} for _ in range(100)]
    rows += [{"pred": "RJ27TC0530", "calibrated_conf": 0.8, "ok": 0} for _ in range(20)]
    rows += [{"pred": "junk", "calibrated_conf": 0.99, "ok": 0}]
    thresholds = choose_upper_thresholds(rows)
    assert thresholds["0.02"]["accept_at"] is None
    assert thresholds["0.05"]["accept_at"] == 0.9
    assert thresholds["0.10"]["accept_at"] == 0.9
    for target, policy in thresholds.items():
        accepted = [r for r in rows if route(r["pred"], r["calibrated_conf"], policy) == "ACCEPT"]
        if accepted:
            assert clopper_pearson_upper(sum(1 - r["ok"] for r in accepted), len(accepted)) <= float(target)


def test_threshold_uses_lowest_qualifying_cutoff() -> None:
    rows = [{"pred": "RJ27TC0530", "calibrated_conf": i / 200, "ok": 1}
            for i in range(200)]
    assert all(policy["accept_at"] == 0.0 for policy in choose_upper_thresholds(rows).values())
    assert all(policy["accept_at"] is None for policy in choose_upper_thresholds([]).values())


def test_grammar_relabels_without_mutating_cached_features() -> None:
    original = {"pred": "RJZ7TCOS3O", "truth": "RJ27TC0530", "ok": "0", "grammar": "1.0"}
    corrected = prepare_rows([original], True)[0]
    assert corrected["pred"] == original["truth"]
    assert corrected["ok"] == 1 and corrected["cer"] == 0.0
    assert corrected["grammar"] == original["grammar"]
    assert original["pred"] == "RJZ7TCOS3O" and original["ok"] == "0"
    assert prepare_rows([original], False)[0]["ok"] == 0
