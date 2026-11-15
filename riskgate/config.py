from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CALIBRATION_MODEL = ROOT / "weights/calibration.json"
RESULTS_DIR = ROOT / "results"
