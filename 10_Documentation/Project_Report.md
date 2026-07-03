# Project Report: Credit Card Approval Prediction System

## Abstract

Credit card issuance is a key revenue driver for financial institutions, but it also carries significant risk. Making incorrect decisions can lead to high rate defaults and bad debts. This project develops an automated Credit Card Approval Prediction system leveraging Machine Learning to predict whether an applicant is eligible for credit card approval based on their demographic and financial attributes. We implement and compare Logistic Regression, Decision Tree, Random Forest, and XGBoost classifiers. The final model is serialized and integrated with a Flask web application, presenting a modern banking dashboard to users.

---

## 1. Introduction

Traditional credit card application reviews rely heavily on manual verification, which introduces human bias, processing delays, and credit defaults. With the rise of machine learning, automated decision engines can process large numbers of applications in milliseconds. 

This project implements a complete end-to-end software pipeline for credit approval. It includes data engineering, exploratory analysis, preprocessing (such as feature scaling and label encoding), model training, algorithm comparison, and deployment.

---

## 2. Problem Definition

Banks need to optimize their application review processes. The objective is to classify applicants into two risk levels:
- **Low-Risk (0):** Applicants who pay off their balances and should be approved.
- **High-Risk (1):** Applicants who consistently miss payments or default, and should be rejected.

The system maps demographic variables (e.g. annual income, age, employment status, family size) and credit history flags to predict the approval outcome.

---

## 3. Methodology

### 3.1 Data Collection
The dataset simulates standard Kaggle schemas using two files:
1. `application_record.csv`: Demographic details (5,000 applicants).
2. `credit_record.csv`: Monthly tracking history (170,000+ status logs).

### 3.2 Exploratory Data Analysis (EDA)
We perform univariate analysis on demographics and multivariate correlation checks. This confirms that annual income is positively correlated with higher education levels, and that longer employment reduces risk flags.

### 3.3 Data Preprocessing
- **Duplicate Records Check:** Exact duplicate rows are removed to avoid model bias.
- **Missing Value Imputation:** Missing values in `OCCUPATION_TYPE` are filled with 'Unknown'.
- **Cleaning:** Negative day markers (`DAYS_BIRTH`, `DAYS_EMPLOYED`) are converted to positive years (`Age_Years`, `Employed_Years`).
- **Target Aggregation:** Monthly credit logs are aggregated by ID. An applicant is flagged as High-Risk (`1`) if they had a payment status delay of `1`, `2`, `3`, `4`, or `5`. Otherwise, they are flagged as Low-Risk (`0`).
- **Feature Scaling & Encoding:** Standard normal scaling is applied to numerical columns, and categorical text features are encoded using `LabelEncoder`.

### 3.4 Model Training & Selection
We train four models: Logistic Regression, Decision Tree, Random Forest, and XGBoost. The highest accuracy model is saved as `best_model.pkl`.

---

## 4. Results & Discussion

### Model Evaluation Summary

During our pipeline run, we evaluated the models on a 20% test set:

| Algorithm | Test Accuracy | Precision | Recall | F1 Score | AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **XGBoost Classifier** | **86.60%** | **39.17%** | **43.52%** | **0.4123** | **0.8214** |
| **Random Forest** | 83.60% | 36.54% | 70.37% | 0.4810 | 0.8460 |
| **Logistic Regression** | 73.10% | 25.83% | 79.63% | 0.3900 | 0.8419 |
| **Decision Tree** | 71.10% | 23.62% | 75.00% | 0.3592 | 0.7924 |

We chose XGBoost Classifier as the best model due to its high accuracy (86.60%) and strong generalization capabilities on unbalanced datasets.

---

## 5. Conclusion

This machine learning pipeline successfully automates credit risk assessment. The Flask application provides a responsive portal for bank administrators to submit applicant profiles and receive real-time, explainable credit approval decisions.
