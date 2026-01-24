from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)


# Load trained model & scaler

BASE_DIR = os.path.dirname(__file__)

model_path = os.path.join(BASE_DIR, "..", "models", "model.pkl")
scaler_path = os.path.join(BASE_DIR, "..", "models", "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)


# Fields used in the form (UPDATED)

fields = ["Glucose", "BMI", "Age"]


# Routes

@app.route("/")
def home():
    return render_template(
        "index.html",
        fields=fields,
        prediction=None
    )

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract form values in correct order
        glucose = float(request.form["Glucose"])
        bmi = float(request.form["BMI"])
        age = float(request.form["Age"])

        # Arrange input (ORDER MUST MATCH TRAINING)
        X = np.array([[glucose, bmi, age]])

        # Scale input
        X_scaled = scaler.transform(X)

        # Predict
        pred = model.predict(X_scaled)[0]

        result = "High Diabetes Risk" if pred == 1 else "Low Diabetes Risk"

        return render_template(
            "index.html",
            fields=fields,
            prediction=result
        )

    except Exception as e:
        return f"An error occurred: {e}"


# Run App

if __name__ == "__main__":
    print("🚀 Starting Flask App...")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
