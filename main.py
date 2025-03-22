import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Customer Churn Prediction", layout="centered")
st.title("📊 Customer Churn Prediction App")
st.sidebar.header("Enter Customer Information")

zip_code = st.sidebar.number_input("Zip Code", min_value=10000, max_value=99999, value=90007)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.sidebar.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.sidebar.selectbox("Has Partner?", ["No", "Yes"])
dependents = st.sidebar.selectbox("Has Dependents?", ["No", "Yes"])
tenure_months = st.sidebar.slider("Tenure Months", min_value=0, max_value=100, value=22)
phone_service = st.sidebar.selectbox("Phone Service", ["No", "Yes"])
multiple_lines = st.sidebar.selectbox("Multiple Lines", ["No", "Yes"])
internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.sidebar.selectbox("Online Security", ["No", "Yes"])
online_backup = st.sidebar.selectbox("Online Backup", ["No", "Yes"])
device_protection = st.sidebar.selectbox("Device Protection", ["No", "Yes"])
tech_support = st.sidebar.selectbox("Tech Support", ["No", "Yes"])
streaming_tv = st.sidebar.selectbox("Streaming TV", ["No", "Yes"])
streaming_movies = st.sidebar.selectbox("Streaming Movies", ["No", "Yes"])
contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.sidebar.selectbox("Paperless Billing", ["No", "Yes"])
payment_method = st.sidebar.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
monthly_charges = st.sidebar.number_input("Monthly Charges", value=89.1)
total_charges = st.sidebar.number_input("Total Charges", value=1949.4)
cltv = st.sidebar.number_input("Customer Lifetime Value (CLTV)", value=4459.0)


input_data = pd.DataFrame([{
    'Zip Code': zip_code,
    'Gender': 1 if gender == "Male" else 0,
    'Senior Citizen': 1 if senior_citizen == "Yes" else 0,
    'Partner': 1 if partner == "Yes" else 0,
    'Dependents': 1 if dependents == "Yes" else 0,
    'Tenure Months': tenure_months,
    'Phone Service': 1 if phone_service == "Yes" else 0,
    'Multiple Lines': 1 if multiple_lines == "Yes" else 0,
    'Internet Service': internet_service,
    'Online Security': 1 if online_security == "Yes" else 0,
    'Online Backup': 1 if online_backup == "Yes" else 0,
    'Device Protection': 1 if device_protection == "Yes" else 0,
    'Tech Support': 1 if tech_support == "Yes" else 0,
    'Streaming TV': 1 if streaming_tv == "Yes" else 0,
    'Streaming Movies': 1 if streaming_movies == "Yes" else 0,
    'Contract': contract,
    'Paperless Billing': 1 if paperless_billing == "Yes" else 0,
    'Payment Method': payment_method,
    'Monthly Charges': monthly_charges,
    'Total Charges': total_charges,
    'CLTV': cltv
}])

st.subheader("Customer Information Preview")
st.dataframe(input_data)

# Predict button
if st.button("Predict Churn"):
    response = requests.post("http://localhost:8500/predict", json=input_data.to_dict(orient='records')[0],timeout=20)
    prediction = response.json()['prediction']
    probability = response.json()['probability']

    if prediction == "Churn":
        st.error(f" The customer is **likely to churn** with a probability of **{probability:.2f}%**.")
    else:
        st.success(f"✅ The customer is **not likely to churn**, with a confidence of **{100-probability:.2f}%**.")