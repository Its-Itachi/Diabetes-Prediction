# 🩺 Diabetes Prediction App

👉 **Flask App**:  
https://diabetes-prediction-lnrv.onrender.com  

👉 **Streamlit App**:  
https://diabetes-prediction-ndxju8jqihonmmmgwyybdw.streamlit.app/

This is a machine learning web application that predicts whether a person is diabetic based on health parameters.  
The project is deployed using **both Flask and Streamlit** to demonstrate different deployment approaches.

---

## 📊 Model Overview

- **Algorithm**: XGBoost Classifier (with feature scaling and outlier removal)  
- **Dataset**: Pima Indians Diabetes Dataset  
- **Target**: Predict whether the person is diabetic or not  

---

## 🔍 Features Used

### Original Features 
- Pregnancies  
- Glucose  
- Blood Pressure  
- Skin Thickness  
- Insulin  
- BMI  
- Diabetes Pedigree Function  
- Age  

### Selected Features Used for Training & Inference
- **Glucose**
- **BMI**
- **Age**

---

## ⚙️ Enhancements

- Data cleaning: handled missing/zero values  
- Outlier removal using Z-score method  
- Feature scaling (StandardScaler)  
- Model evaluation: classification report, confusion matrix, cross-validation  
- Explainability: SHAP summary plot for feature importance (used during experimentation)  

---

## 🛠 Tech Stack

| Layer      | Tools Used |
|------------|-----------|
| Backend    | Flask |
| ML         | XGBoost, scikit-learn, NumPy, Pandas |
| Frontend   | HTML, CSS (Jinja Templates) |
| UI App    | Streamlit |
| Deployment | Render, Streamlit Cloud |

---

## 🚀 How to Run Locally

1. **Clone the repository**
    ```bash
    git clone https://github.com/Its-Itachi/Diabetes-Prediction.git
    cd Diabetes-Prediction
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**

    - Windows (PowerShell):
      ```bash
      venv\Scripts\activate
      ```

    - macOS / Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

### ▶ Train the Model (Optional)
```bash
cd notebooks
jupyter notebook training.ipynb
````

This step generates `model.pkl` and `scaler.pkl`.

---

### ▶ Run Flask App

```bash
cd app
python app.py
```

Open:

```
http://localhost:5000
```

---

### ▶ Run Streamlit App

```bash
streamlit run streamlit_app.py
```

---

## 🌐 Deployment

* **Flask (Render)**:
  [https://diabetes-prediction-lnrv.onrender.com](https://diabetes-prediction-lnrv.onrender.com)

* **Streamlit Cloud**:
  [https://diabetes-prediction-ndxju8jqihonmmmgwyybdw.streamlit.app/](https://diabetes-prediction-ndxju8jqihonmmmgwyybdw.streamlit.app/)

---

## 👤 Author

**Jayesh Dethe**
GitHub: [https://github.com/Its-Itachi](https://github.com/Its-Itachi)

---

## 📝 Notes

* This project prioritizes **recall** for diabetes screening use cases

---

Happy coding! 🚀

```
