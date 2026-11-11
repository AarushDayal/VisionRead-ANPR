ROOT = __import__("pathlib").Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data/legacy/datacluster"
SPLITS_V2 = ROOT / "data/splits_v2.json"
CALIBRATION_MODEL = ROOT / "weights/calibration.json"
DRAFTS = ROOT / "data/labels/draft_labels.csv"
YOLO_START = ROOT / "weights/yolo11n.pt"
RESULTS_DIR = ROOT / "results"

SEED = 0
MIN_CROP_H = 0
READER_ALLOWLIST = True
READER_UPSCALE = False
