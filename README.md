# 🧬 Breast Cancer Prediction App

A Streamlit-based web app for predicting breast cancer (Malignant or Benign) using diagnostic features of cell nuclei. This app utilizes a machine learning model trained on the Breast Cancer Wisconsin Diagnostic Dataset.

<p align="center">
  <img src="https://img.shields.io/github/languages/top/CARLOX62/Breast-Cancer-predict" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/CARLOX62/Breast-Cancer-predict" alt="Last Commit">
  <img src="https://img.shields.io/github/repo-size/CARLOX62/Breast-Cancer-predict" alt="Repo Size">
</p>

---

## 📂 Repository Contents

```bash
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

Built with `Python`, `scikit-learn`, and `Streamlit`, it enables real-time predictions from a simple web interface.

---

## 📊 Dataset Details

- **Name**: Breast Cancer Wisconsin (Diagnostic) Dataset
- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))
- **Features**: 30 numeric values including:
  - mean radius, texture, smoothness, concavity, symmetry, etc.
- **Samples**: 569
- **Target classes**:
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

You can install required packages manually:

```bash
pip install streamlit pandas numpy scikit-learn matplotlib seaborn
```

Or generate a `requirements.txt`:

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

### 3️⃣ Run the Web App

```bash
streamlit run app.py
```

---

## 🧪 How It Works

- The model was trained and evaluated inside the `Breast Cancer.ipynb` notebook.
- The final model was saved as `breast_cancer_detector.pickle`.
- The app (`app.py`) loads this model and takes 30 feature inputs from the user.
- Based on the inputs, it displays:
  - ✅ "No Breast Cancer (Benign)"
  - ⚠️ "Breast Cancer Detected (Malignant)"

---

## 📷 Screenshots

![Screenshot (47)](https://github.com/user-attachments/assets/51f2b83f-6f67-4a0f-9ded-fbbd600b5c0d)




---

## 📌 Notes

- This app is for **educational/demo purposes only**.
- It is **not** a replacement for professional medical diagnosis.
- Always consult a healthcare provider for medical advice.

---

## ✍️ Author

**CARLOX62**  
[GitHub Profile](https://github.com/CARLOX62)

---



## 🌐 Live Demo 


```markdown
🔗 Live App: [Click Here](http://localhost:8501/)
```
