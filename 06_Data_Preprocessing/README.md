# Data Preprocessing Module

## Introduction
The Data Preprocessing Module (Epic 3) prepares the raw applicant and credit files for the machine learning algorithms. It cleans the raw data structures, engineers new demographic and credit attributes, resolves missing values, encodes categorical items, scales numerical distributions, and constructs the final target variable.

## Purpose
To transform noisy, raw tabular datasets into a high-quality, normalized feature matrix and target vector suited for model training and local web predictions.

## Objectives
- Drop duplicate rows and identify duplicate profiles.
- Standardize categorical levels and convert negative time periods (`DAYS_BIRTH` and `DAYS_EMPLOYED`) into positive representations (`Age` and `Employment_Years`).
- Group monthly credit logs on ID and extract summary statistics: `Open_Month`, `End_Month`, `Credit_Window`, `Latest_Status`, `Max_Delay`, and `Num_Records`.
- Convert payment history codes into a binary classification target: Approved (`0`) vs. Rejected/Delinquent (`1`).
- Perform label encoding and scale features using `StandardScaler`.
- Save `processed_dataset.csv`, `encoder.pkl`, and `scaler.pkl`.

## Files Present
- [README.md](file:///c:/Users/laksh/CreditCard/06_Data_Preprocessing/README.md): Preprocessing documentation.
- [Data_Preprocessing.ipynb](file:///c:/Users/laksh/CreditCard/06_Data_Preprocessing/Data_Preprocessing.ipynb): Pipeline script.
- `processed_dataset.csv`: Processed outputs (automatically created after run).
- `encoder.pkl`: Extracted LabelEncoder mappings.
- `scaler.pkl`: Extracted StandardScaler scale parameters.

## Preprocessing Pipeline Steps
1. **Duplicate Records Check**: Remove duplicate rows from both files.
2. **Handle Missing Values**: Replace missing occupations with "Unknown".
3. **Data Cleaning**: Map days columns to positive numeric years.
4. **Credit Status Aggregation**: Group records on applicant ID and identify the maximum payment delay status.
5. **Target Mapping**: Label applicants as Rejected (`1`) if they had a payment status delay of `1`, `2`, `3`, `4`, or `5`. Otherwise, Approved (`0`).
6. **Join Operations**: Outer/inner join tables on matching ID fields.
7. **Encoding**: Apply LabelEncoder on all categorical properties.
8. **Scaling**: Fit and transform numeric data via standard normal scaling.
9. **Persistence**: Export preprocessing pipelines.

## Technologies Used
- Pandas, NumPy, Scikit-Learn
- Joblib (saving transformers)

## Expected Outputs
- `processed_dataset.csv`
- `scaler.pkl`
- `encoder.pkl`

## Conclusion
A clean, scaled, and encoded dataset reduces model training bias and ensures that backend inputs map cleanly to the same scale during browser runs.
