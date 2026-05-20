import streamlit as st
import pandas as pd
import joblib

# 1. App Configuration & Setup
st.set_page_config(page_title="Credit Risk Analyzer", layout="centered")
st.title("Automated Credit Risk Scoring System")
st.write("### Enter Applicant Financial Metrics")

# Load model safely with caching
@st.cache_resource
def load_model():
    try:
        return joblib.load('loan_status_predictor.pkl')
    except Exception as e:
        st.error(f"Error loading model template file: {e}")
        return None

model = load_model()

# 2. Layout Inputs inside a Form
with st.form("streamlined_loan_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        applicant_income = st.number_input("Applicant Monthly Income ($)", min_value=0, value=6500, step=100)
        coapplicant_income = st.number_input("Coapplicant Monthly Income ($)", min_value=0, value=0, step=100)
        savings = st.number_input("Total Savings Balance ($)", min_value=0, value=12000, step=500)
        dti_ratio = st.slider("Debt-to-Income (DTI) Ratio", 0.0, 1.0, 0.32, step=0.01)
        
    with col2:
        credit_score = st.slider("Credit Score Matrix", 300, 850, 680)
        age = st.number_input("Applicant Age (Years)", min_value=18, max_value=100, value=35, step=1)
        loan_amount = st.number_input("Requested Loan Principal ($)", min_value=0, value=25000, step=100)
        loan_term = st.selectbox("Amortization Term (Months)", [12, 24, 36, 60, 72, 84])
        
    employment_status = st.selectbox("Employment Verification Classification", ["Salaried", "Self-employed", "Contract", "Unemployed"])
    submit_btn = st.form_submit_button("Run Risk Assessment Metric")

# 3. Model Inference Execution
if submit_btn and model:
    # Build dataframe directly and coerce types inline to skip manual casting lists
    input_df = pd.DataFrame([{
        'Applicant_Income': float(applicant_income), 'Coapplicant_Income': float(coapplicant_income),
        'Credit_Score': float(credit_score), 'Age': float(age),
        'Loan_Amount': float(loan_amount), 'Loan_Term': float(loan_term),
        'Savings': float(savings), 'DTI_Ratio': float(dti_ratio),
        'Employment_Status': str(employment_status)
    }])
    
    try:
        prediction = model.predict(input_df)
        st.write("### Underwriting Decision")
        
        if prediction[0] in [1, 'Yes']:
            st.success("✅ **LOAN ELIGIBILITY STATUS: APPROVED**")
            st.balloons()
        else:
            st.error("❌ **LOAN ELIGIBILITY STATUS: REJECTED**")
            st.warning("Application details present a profile outside acceptable volatility limits.")
    except Exception as err:
        st.error(f"Data transformation error: {err}")