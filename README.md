# 🩺 Diabetes Prediction App

👉 **Live App**: [https://diabetes-prediction-lnrv.onrender.com](https://diabetes-prediction-lnrv.onrender.com)

This is a machine learning web application built with **Flask**, which predicts whether a person is diabetic based on input health parameters.

---

## 📊 Model Overview

- **Algorithm**: Logistic Regression  
- **Dataset**: Pima Indians Diabetes Dataset  
- **Target**: Predict whether the person is diabetic or not

### 🔍 Features Used

- Pregnancies  
- Glucose  
- Blood Pressure  
- Skin Thickness  
- Insulin  
- BMI  
- Diabetes Pedigree Function  
- Age

---

## 🛠 Tech Stack

| Layer      | Tools Used                       |
|------------|----------------------------------|
| Backend    | Flask                            |
| ML         | scikit-learn, NumPy, Pandas      |
| Frontend   | HTML, CSS (Jinja Templates)      |
| Deployment | Render                           |

---

## 🚀 How to Run Locally

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Its-Itachi/Diabetes-Prediction.git
    cd Diabetes-Prediction
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows (PowerShell):
      ```bash
      venv\Scripts\Activate.ps1
      ```
      Or if that doesn’t work:
      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Train the machine learning model:**
    ```bash
    cd notebooks
    python training.py
    ```

6. **Run the Flask app:**
    ```bash
    cd ../app
    python app.py
    ```

7. **Open your browser and visit:**
    ```
    http://localhost:5000
    ```

---

## 🌐 Deployment (Render)

The app is deployed on **Render** and can be accessed live here:  
[https://diabetes-prediction-lnrv.onrender.com](https://diabetes-prediction-lnrv.onrender.com)

---

## 👤 Author

**Name**: Jayesh Dethe  
**GitHub**: [@Its-Itachi](https://github.com/Its-Itachi)

---

## ⭐ Support

If you find this project useful, please:

- ⭐ Star the repository on GitHub  
- 📢 Share with friends and peers  
- 🔔 Follow for more ML + Web projects  

---

## 📝 Notes

- Make sure to activate your virtual environment every time before running the app.  
- The training step creates `model.pkl` which is used by the Flask app for prediction.  
- For any issues, feel free to open an issue on GitHub or reach out to me!

---

Happy coding! 🚀
