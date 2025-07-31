from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load trained model
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')
model = joblib.load(model_path)

fields = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
          'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

@app.route('/')
def home():
    return render_template('index.html', fields=fields, prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        values = [float(request.form[f]) for f in fields]
        input_data = np.array(values).reshape(1, -1)
        pred = model.predict(input_data)[0]
        result = "Diabetic" if pred == 1 else "Not Diabetic"
        return render_template('index.html', fields=fields, prediction=result)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    print("🚀 Starting Flask App...")
    app.run(debug=True)
