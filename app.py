import streamlit as st
import numpy as np
import pickle

# Load the model
with open("breast_cancer_detector.pickle", "rb") as file:
    model = pickle.load(file)

# Feature names
features = [
    'mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness',
    'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry',
    'mean fractal dimension', 'radius error', 'texture error', 'perimeter error',
    'area error', 'smoothness error', 'compactness error', 'concavity error',
    'concave points error', 'symmetry error', 'fractal dimension error',
    'worst radius', 'worst texture', 'worst perimeter', 'worst area',
    'worst smoothness', 'worst compactness', 'worst concavity',
    'worst concave points', 'worst symmetry', 'worst fractal dimension'
]

# Page Config
st.set_page_config(page_title="Breast Cancer Detector", layout="centered")
st.title("🧬 Breast Cancer Detection App")
st.markdown("Enter the patient data to predict the likelihood of breast cancer.")

# Input form
with st.form("prediction_form"):
    st.subheader("Patient Feature Input")
    input_data = [st.number_input(f"{feature}", min_value=0.0, format="%.2f") for feature in features]
    submitted = st.form_submit_button("Predict")

if submitted:
    prediction = model.predict([np.array(input_data)])
    if prediction[0] == 1:
        st.error("⚠️ The model predicts: Breast Cancer **Detected** (Malignant). Please consult a medical professional.")
    else:
        st.success("✅ The model predicts: No Breast Cancer (Benign).")

st.markdown("---")
st.caption("This is a demo model prediction and should not be used as a substitute for professional diagnosis.")
