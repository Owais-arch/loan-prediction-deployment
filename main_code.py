

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import filterwarnings
filterwarnings("ignore")

"""Load Dataset"""

df=pd.read_csv("/content/train_u6lujuX_CVtuZ9i.csv")
df.head()

df.shape

"""Check Missing Values"""

df.isnull().sum()[df.isnull().sum()>0]

"""Handle Missing Values"""

df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)

df['Married'].fillna(df['Married'].mode()[0], inplace=True)

df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)

df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)

df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)





"""Drop Unnecessary Column"""

df=df.drop("Loan_ID",axis=1)

"""Encode Target Variable"""

df['Loan_Status']=df['Loan_Status'].replace({'Y':1,'N':0})



"""Encode Categorical Variables"""

df=pd.get_dummies(df,drop_first=True,dtype=int)

"""Train Test Split"""

from sklearn.model_selection import train_test_split

df_train,df_test = train_test_split(df, test_size=0.2, random_state=42)

"""Defining Features and Target"""

df_train_x=df_train.drop("Loan_Status",axis=1)
df_train_y=df_train["Loan_Status"]

df_test_x=df_test.drop("Loan_Status",axis=1)
df_test_y=df_test["Loan_Status"]

"""Train Test Split"""

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

model.fit(df_train_x, df_train_y)

"""Training Model and Model Evaluation"""

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

pred = model.predict(df_test_x)

tab=confusion_matrix(df_test_y,pred)
print(tab)

acc=accuracy_score(df_test_y,pred)
print("Accuracy Score:",acc)

print(classification_report(df_test_y,pred))

"""Save Model"""

import pickle

pickle.dump(model, open("loan_model.pkl","wb"))



"""Creating Deployment App"""





import pickle
pickle.dump(model, open("loan_model.pkl","wb"))

#!streamlit run app.py &>/dev/null &

#ngrok config add-authtoken 3AvdOChYo853xwfMVV7rGzd0cSx_7BgeMCPrWUoiK5dLUH2TH

from pyngrok import ngrok

ngrok.set_auth_token("3AvdOChYo853xwfMVV7rGzd0cSx_7BgeMCPrWUoiK5dLUH2TH")

#!streamlit run app.py &>/dev/null &

from pyngrok import ngrok
public_url = ngrok.connect(8501)
print(public_url)



