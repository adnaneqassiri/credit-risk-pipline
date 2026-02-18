from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"
PRED_DIR = DATA_DIR / "predictions"

MODELS_DIR = BASE_DIR / "models"
REGISTRY_PATH = MODELS_DIR / "registry.json"

DB_URL = "postgresql+psycopg2://mluser:mlpassword@localhost:5432/homecredit"
