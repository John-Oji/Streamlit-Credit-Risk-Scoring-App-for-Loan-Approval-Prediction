# Streamlit-Credit-Risk-Scoring-App-for-Loan-Approval-Prediction
### Automated Credit Risk Scoring System

## Project Overview
The **Automated Credit Risk Scoring System** is a Machine Learning-powered web application developed using **Streamlit** to predict loan eligibility based on an applicant’s financial profile.

The system evaluates applicant information such as income, credit score, debt-to-income ratio, savings, employment status, and loan details to determine whether a loan application is likely to be **Approved** or **Rejected**.

The goal of this project is to assist financial institutions in making faster, more consistent, and data-driven loan approval decisions.

---

## Problem Statement
Manual loan approval processes can be time-consuming and prone to inconsistencies. This project automates the credit risk assessment process by using a trained machine learning model to evaluate applicant financial metrics and predict loan eligibility.

---

## Project Features
The application includes the following features:

- **Machine Learning Loan Prediction**
  - Predicts whether a loan application should be approved or rejected.

- **Interactive User Interface**
  - Built using Streamlit for easy interaction.

- **Real-Time Prediction**
  - Generates instant underwriting decisions.

- **Applicant Financial Assessment**
  - Evaluates financial and demographic variables.

- **Model Deployment**
  - Integrated trained `.pkl` machine learning model using Joblib.

- **Error Handling**
  - Handles model loading and transformation errors gracefully.

---

## Technologies Used
- **Python**
- **Streamlit**
- **Pandas**
- **Joblib**
- **Machine Learning**

---

## Input Features Used in the Model
The prediction model was trained using **8 numerical features and 1 categorical feature**:

### Numerical Features
1. Applicant Income  
2. Coapplicant Income  
3. Credit Score  
4. Age  
5. Loan Amount  
6. Loan Term  
7. Savings  
8. Debt-to-Income Ratio (DTI)

### Categorical Feature
9. Employment Status

The employment status categories include:

- Salaried  
- Self-employed  
- Contract  
- Unemployed

---

## How the Application Works
Users enter applicant financial information into the application form, including:

- Monthly income
- Credit score
- Savings balance
- Debt-to-income ratio
- Age
- Loan amount
- Loan term
- Employment status

After clicking the **"Run Risk Assessment Metric"** button, the trained machine learning model processes the inputs and returns one of the following decisions:

### Approved
If the applicant meets acceptable credit risk conditions.

### Rejected
If the applicant profile falls outside acceptable risk thresholds.

---
## Application Preview

Below is the interface of the Automated Credit Risk Scoring System built with Streamlit.



<img width="847" height="876" alt="image" src="https://github.com/user-attachments/assets/049f166f-5598-4a64-94f2-625f5cc8a95c" />

<img width="792" height="858" alt="image" src="https://github.com/user-attachments/assets/63b3d791-a4d8-41ca-b01e-9a5d70919355" />


---
