from fastapi import FastAPI
import pandas as pd
import joblib

model = joblib.load("../Model/customer_churn_model.pkl") 
scaler=joblib.load("../Model/scaler.pkl")
saved_columns=joblib.load("../Model/X_test_columns.pkl")


app = FastAPI()


@app.get("/")
def home():
    return {"Everything works"}

@app.post("/predict")
def predict_churn(data: dict):
    df = pd.DataFrame([data])

    df = pd.get_dummies(df)

    df = df.reindex(columns=saved_columns, fill_value=0)

    numerical_cols =['Zip Code','Tenure Months','Monthly Charges','Total Charges','CLTV']

    df[numerical_cols] = scaler.transform(df[numerical_cols])

    # Make prediction
    prediction = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1] * 100 
    
    return {
        "prediction": "Churn" if prediction == 1 else "No Churn",
        "probability": round(prob, 2)
    }
