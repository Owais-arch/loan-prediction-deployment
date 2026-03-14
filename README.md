Live Demo

You can access the web application here:
https://tetchily-interpervasive-tosha.ngrok-free.dev


# loan-prediction-deployment
End-to-End ML project for loan approval prediction


# Loan Approval Prediction - End-to-End Machine Learning Project

## Project Overview

This project predicts whether a loan application will be approved or rejected based on applicant information such as income, credit history, education, and property area.

The goal of this project is to demonstrate an **end-to-end machine learning pipeline**, including data preprocessing, model training, evaluation, and deployment using a simple web application.

---

## Problem Statement

Banks receive thousands of loan applications and manually evaluating each one can be time-consuming.
This project builds a machine learning model that automatically predicts whether a loan should be approved based on historical data.

---

## Dataset

The dataset contains information about loan applicants, including:

* Gender
* Marital Status
* Education
* Self Employment
* Applicant Income
* Coapplicant Income
* Loan Amount
* Loan Term
* Credit History
* Property Area

Target variable:

* **Loan_Status**

  * 1 → Loan Approved
  * 0 → Loan Rejected

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit
* Pickle

---

## Machine Learning Model

Model used in this project:

**Random Forest Classifier**

The model was trained using the processed dataset and evaluated using accuracy and classification metrics.

---

## Model Performance

Evaluation metrics used:

* Accuracy Score
* Confusion Matrix
* Classification Report

The model performs well in predicting loan approval based on applicant features.

---

## Project Workflow

1. Import libraries
2. Load dataset
3. Handle missing values
4. Encode cat
   
