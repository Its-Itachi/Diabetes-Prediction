import streamlit as st
import numpy as np
import pickle
import joblib
from pathlib import Path

# ===============================
# Load model & scaler
# ===============================
BASE_DIR = Path(__file__).resolve().parent

model = pickle.load(open(BASE_DIR / "models" / "model.pkl", "rb"))
scaler = joblib.load(BASE_DIR / "models" / "scaler.pkl")

# ===============================
# Streamlit UI
# ===============================
st.set_page_config(
    page_title="Diabetes Risk Prediction",
    layout="centered"
)

st.title("🩺 Diabetes Risk Prediction")
st.write(
    "This tool estimates diabetes risk using **Glucose, BMI, and Age**. "
    "It is intended for **screening purposes only**."
)

st.divider()

# ===============================
# Input fields (NO FORCED DEFAULTS)
# ===============================
glucose = st.number_input(
    "Fasting Glucose (mg/dL)",
    min_value=50,
    max_value=300,
    value=None,
    placeholder="e.g. 120",
    help="Measured after 8–10 hours of fasting"
)

bmi = st.number_input(
    "Body Mass Index (BMI)",
    min_value=10.0,
    max_value=70.0,
    value=None,
    placeholder="e.g. 25.0"
)

age = st.number_input(
    "Age (years)",
    min_value=10,
    max_value=120,
    value=None,
    placeholder="e.g. 30"
)

st.divider()

# ===============================
# Prediction
# ===============================
if st.button("Predict Diabetes Risk"):

    # 🔴 Validation: ensure user entered all values
    if glucose is None or bmi is None or age is None:
        st.warning("Please enter all values before predicting.")
        st.stop()

    # Order MUST match training: ["Glucose", "BMI", "Age"]
    X = np.array([[glucose, bmi, age]])
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)[0]

    if prediction == 1:
        st.error("⚠️ **High risk of Diabetes detected**")
    else:
        st.success("✅ **Low risk of Diabetes detected**")

    st.caption(
        "⚠️ This prediction is not a medical diagnosis. "
        "Please consult a healthcare professional."
    )
