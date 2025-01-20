
import pandas as pd
import numpy as np
import os

import matplotlib.pyplot as plt
from matplotlib import rcParams

data = pd.read_csv(r"./dataset/Loan_data.csv")
data = data.replace('?', np.nan)
data.head()


print("***Number of missing values***\n")
print(data.isna().sum())

data['Gender']=data['Gender'].fillna(data['Gender'].mode()[0])
data['Married']=data['Married'].fillna(data['Married'].mode()[0])
data['Dependents']=data['Dependents'].fillna(data['Dependents'].mode()[0])
data['LoanAmount']=data['LoanAmount'].fillna(int(data['LoanAmount'].mean()))
data['Self_Employed']=data['Self_Employed'].fillna(data['Self_Employed'].mode()[0])
data['Loan_Amount_Term']=data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mode()[0])
data['Credit_History']=data['Credit_History'].fillna(data['Credit_History'].mode()[0])
print("***After Removing missing values***\n")

print(data.isna().sum())

Dataset=data.to_csv(os.path.join(r'./preprocess_dataset/preprocess_Loan.csv'), index=False)

Dataset = pd.read_csv(r'./preprocess_dataset/preprocess_Loan.csv')

Dataset.head()

Dataset.tail()

Dataset.info()

Dataset.describe()


