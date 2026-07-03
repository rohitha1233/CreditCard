# Workflow & Data Processing Pipeline

This document outlines the detailed stages of the data engineering and machine learning pipeline, from data collection to model training and local deployment.

---

## Stage 1: Data Collection

The pipeline begins by ingesting demographic and credit history datasets:
- `application_record.csv` holds demographic variables for 5,000 applicants.
- `credit_record.csv` contains 170,000+ monthly payment logs.

The datasets are joined using the unique applicant ID.

---

## Stage 2: Exploratory Data Analysis (EDA)

We perform exploratory analysis to identify distributions and correlations:
- **Univariate Analysis:** Evaluates the distributions of income, age, education, and family sizes.
- **Multivariate Analysis:** Explores correlation matrices and pairplots, revealing relationships like income variations across education levels.

---

## Stage 3: Data Preprocessing & Cleaning

Data preprocessing transforms the raw features into clean inputs for machine learning:

1. **Handling Duplicates:** Removes exact duplicate rows to prevent training bias.
2. **Imputation:** Fills missing values in `OCCUPATION_TYPE` with 'Unknown'.
3. **Date Conversions:** Converts negative day markers into positive years:
   - $\text{Age (Years)} = \frac{-\text{DAYS\_BIRTH}}{365.25}$
   - $\text{Employment (Years)} = \frac{-\text{DAYS\_EMPLOYED}}{365.25} \quad (\text{or } 0 \text{ if unemployed})$
4. **Target Variable Creation:** Monthly payment statuses (`STATUS`) in `credit_record.csv` are mapped to numeric risk scores:
   - `C` (Paid Off) $\rightarrow 0$
   - `X` (No Loan) $\rightarrow 0$
   - `0` (1-29 days overdue) $\rightarrow 0$
   - `1` (30-59 days overdue) $\rightarrow 1$
   - `2` (60-89 days overdue) $\rightarrow 2$
   - `3` (90-119 days overdue) $\rightarrow 3$
   - `4` (120-149 days overdue) $\rightarrow 4$
   - `5` (150+ days overdue/write-off) $\rightarrow 5$
   
   An applicant is classified as **High-Risk/Rejected (1)** if their maximum status is $\ge 1$ (at least 30 days overdue). Otherwise, they are classified as **Low-Risk/Approved (0)**.
5. **Feature Transformation:** Categorical variables are encoded using `LabelEncoder`, and all features are scaled using `StandardScaler` to ensure numerical inputs are on the same scale.

---

## Stage 4: Model Building & Comparison

We split the preprocessed data into an 80% training set and a 20% test set, and evaluate four classifiers:

1. **Logistic Regression:** Serves as a baseline model.
2. **Decision Tree:** Provides explainable, non-linear split boundaries.
3. **Random Forest:** Ensemble bagging classifier to prevent overfitting.
4. **XGBoost Classifier:** Boosting ensemble optimized for tabular data performance.

We evaluate the models on the test set using Accuracy, Precision, Recall, F1 Score, and ROC-AUC metrics. The model with the highest test accuracy is serialized as `best_model.pkl` using Joblib.
