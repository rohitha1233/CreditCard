# Credit Card Approval Dataset Module

## Introduction
This module hosts the datasets required for predicting credit card approval status. The raw data consists of applicant demographic/financial profiles and their historical credit repayment behavior.

## Dataset Structure
We utilize two primary files for model development:
1. `application_record.csv`: Demographic details, income, family size, education, and housing types of credit card applicants.
2. `credit_record.csv`: Monthly credit card repayment history, recording delays, write-offs, or active payment records for every applicant ID.

## Feature Descriptions

### 1. Application Record (`application_record.csv`)
| Feature Name | Data Type | Description |
| :--- | :--- | :--- |
| `ID` | Integer (Unique) | Unique applicant identification key. |
| `CODE_GENDER` | Categorical (`M`/`F`) | Gender of the applicant. |
| `FLAG_OWN_CAR` | Categorical (`Y`/`N`) | Status of personal vehicle ownership. |
| `FLAG_OWN_REALTY` | Categorical (`Y`/`N`) | Status of real estate property ownership. |
| `CNT_CHILDREN` | Integer | Total number of children. |
| `AMT_INCOME_TOTAL` | Float | Annual income (currency units). |
| `NAME_INCOME_TYPE` | Categorical | Income class (e.g., Working, Pensioner, Commercial associate). |
| `NAME_EDUCATION_TYPE`| Categorical | Education level (e.g., Higher education, Secondary special). |
| `NAME_FAMILY_STATUS` | Categorical | Marital status (e.g., Married, Single, Separated). |
| `NAME_HOUSING_TYPE` | Categorical | Type of dwelling (e.g., Rented apartment, With parents, House). |
| `DAYS_BIRTH` | Integer (Negative)| Number of days from birth date (negative value, divide by -365 for age). |
| `DAYS_EMPLOYED` | Integer (Negative)| Duration of employment in days (negative; positive means unemployed). |
| `FLAG_MOBIL` | Binary (`0`/`1`) | Mobile phone availability indicator. |
| `FLAG_WORK_PHONE` | Binary (`0`/`1`) | Work phone availability indicator. |
| `FLAG_PHONE` | Binary (`0`/`1`) | Home landline phone availability indicator. |
| `FLAG_EMAIL` | Binary (`0`/`1`) | Email availability indicator. |
| `OCCUPATION_TYPE` | Categorical | Job profile (e.g., Laborers, Core staff). Contains nulls. |
| `CNT_FAM_MEMBERS` | Float | Total family members. |

### 2. Credit Record (`credit_record.csv`)
| Feature Name | Data Type | Description |
| :--- | :--- | :--- |
| `ID` | Integer | Foreign key linking to application record. |
| `MONTHS_BALANCE` | Integer (Negative)| Monthly balance offset. `0` represents current month, `-1` represents last month, etc. |
| `STATUS` | Categorical | Repayment status: `C`: paid off; `X`: no loan; `0`: 1-29 days overdue; `1`: 30-59 days overdue; `2`: 60-89 days overdue; `3`: 90-119 days overdue; `4`: 120-149 days overdue; `5`: 150+ days overdue/write-off. |

## Target Variable
The target variable is derived by analyzing payment statuses in `credit_record.csv`. Individuals with a maximum delay of 30+ days (status codes `1`, `2`, `3`, `4`, `5`) are flagged as **High-Risk/Rejected (`1`)**, while timely payers (status codes `0`, `C`, `X`) are flagged as **Low-Risk/Approved (`0`)**.

## Execution Steps
Run the dataset generation script to programmatically output both CSV files before starting exploratory notebook runs.
