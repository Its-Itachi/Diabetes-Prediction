import pickle
import joblib
from pathlib import Path

# =====================================
# Resolve project root directory
# =====================================
BASE_DIR = Path(__file__).resolve().parent.parent

# =====================================
# Correct file paths (MATCH YOUR FILES)
# =====================================
MODEL_PATH = BASE_DIR / "models" / "model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"

# =====================================
# Load trained model (pickle)
# =====================================
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# =====================================
# Load scaler (joblib – IMPORTANT)
# =====================================
scaler = joblib.load(SCALER_PATH)
