# 🧬 Breast Cancer Prediction App

A **Streamlit-based** web app for predicting **Breast Cancer** (Malignant or Benign) using diagnostic features of cell nuclei. This app utilizes a machine learning model trained on the Breast Cancer Wisconsin Diagnostic Dataset.

<p align="center">
  <img src="https://img.shields.io/github/languages/top/CARLOX62/Breast-Cancer-predict" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/CARLOX62/Breast-Cancer-predict" alt="Last Commit">
  <img src="https://img.shields.io/github/repo-size/CARLOX62/Breast-Cancer-predict" alt="Repo Size">
</p>

---

## 🚀 Live Demo

🔗 **Live App**: (http://localhost:8501/)  

---

## 📂 Repository Contents

```
.
├── app.py                         # Streamlit frontend
├── Breast Cancer.ipynb           # Model training, EDA, and evaluation
├── breast_cancer_dataFrame.csv   # Processed dataset
├── breast_cancer_detector.pickle # Trained model
├── README.md                     # Project documentation
```

---

## 🧠 Project Overview

This project helps identify the likelihood of breast cancer based on patient-specific cell features. The machine learning model is trained to classify tumors as:

- **0 → Benign**
- **1 → Malignant**

Built using:
- 🐍 Python
- 🧪 scikit-learn
- 🌐 Streamlit

It enables real-time predictions from a simple web interface.

---

## 📊 Dataset Details

- **Name**: Breast Cancer Wisconsin (Diagnostic) Dataset  
- **Source**: [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))  
- **Features**: 30 numeric values (e.g., mean radius, texture, smoothness, symmetry)  
- **Samples**: 569  
- **Target Classes**:
  - `M` = Malignant
  - `B` = Benign (converted to 1 and 0)

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/CARLOX62/Breast-Cancer-predict.git
cd Breast-Cancer-predict
```

### 2️⃣ Install Requirements

Install required packages:

```bash
pip install streamlit pandas numpy scikit-learn matplotlib seaborn
```

Or use a `requirements.txt`:

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

### 3️⃣ Run the Web App

```bash
streamlit run app.py
```

Then open your browser and go to:  
`http://localhost:8501/`

---

## 🧪 How It Works

- The model was trained and evaluated inside the `Breast Cancer.ipynb` notebook.
- Final model saved as `breast_cancer_detector.pickle`.
- The app (`app.py`) loads the model and accepts 30 features as user input.
- Based on the prediction, it displays:
  - ✅ **No Breast Cancer (Benign)**
  - ⚠️ **Breast Cancer Detected (Malignant)**

---

## 📸 Screenshot

![Screenshot (58)](https://github.com/user-attachments/assets/e3281cb8-129c-4629-9fce-e5844259b906)


---

## 📌 Notes

- This app is for **educational/demo purposes only**.
- It is **not a replacement for medical diagnosis**.
- Please consult a doctor for actual health concerns.

---

## ✍️ Author

**CARLOX62**  
[GitHub Profile](https://github.com/CARLOX62)

---
