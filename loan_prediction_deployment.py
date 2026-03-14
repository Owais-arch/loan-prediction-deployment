import streamlit as st
import pickle
import numpy as np


model = pickle.load(open("loan_model.pkl","rb"))

st.title("Loan Approval Prediction")

ApplicantIncome = st.number_input("Applicant Income")
CoapplicantIncome = st.number_input("Coapplicant Income")
LoanAmount = st.number_input("Loan Amount")
Loan_Amount_Term = st.number_input("Loan Amount Term")
Credit_History = st.selectbox("Credit History",[0,1])

Gender = st.selectbox("Gender",["Male","Female"])
Married = st.selectbox("Married",["Yes","No"])
Education = st.selectbox("Education",["Graduate","Not Graduate"])
Self_Employed = st.selectbox("Self Employed",["Yes","No"])
Property_Area = st.selectbox("Property Area",["Urban","Semiurban","Rural"])

if st.button("Predict"):

    Gender_Male = 1 if Gender=="Male" else 0
    Married_Yes = 1 if Married=="Yes" else 0
    Education_Not_Graduate = 1 if Education=="Not Graduate" else 0
    Self_Employed_Yes = 1 if Self_Employed=="Yes" else 0
    Property_Area_Semiurban = 1 if Property_Area=="Semiurban" else 0
    Property_Area_Urban = 1 if Property_Area=="Urban" else 0

    input_data = np.array([[ApplicantIncome,
                            CoapplicantIncome,
                            LoanAmount,
                            Loan_Amount_Term,
                            Credit_History,
                            Gender_Male,
                            Married_Yes,
                            0,0,0,
                            Education_Not_Graduate,
                            Self_Employed_Yes,
                            Property_Area_Semiurban,
                            Property_Area_Urban]])

    prediction = model.predict(input_data)

    if prediction[0]==1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")





