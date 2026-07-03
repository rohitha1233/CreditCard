# Data Collection Module

## Introduction
The Data Collection Module represents Epic 1 of the SmartBridge Credit Card Approval Prediction lifecycle. It handles loading the raw applicant and credit files into the memory space and checking core shapes and columns.

## Purpose
To ingest demographic information and credit history files, verifying that the dataset dimensions, attributes, and column headers are loaded correctly for subsequent data analysis and preprocessing phases.

## Objectives
- Import the required Python scientific libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`, `sklearn`, `xgboost`, `joblib`, `os`).
- Load `application_record.csv` and `credit_record.csv` using Pandas.
- Run shape checks, check basic statistics (`info()`, `describe()`), and sample records.
- Assess missing value counts, duplicates, and unique ID mappings.

## Workflow
1. Import all libraries with markdown annotations describing their specific utilities.
2. Construct file system paths pointing to the `03_Dataset/` folder.
3. Read dataset files and verify correct load via `head()` and `tail()`.
4. Perform data quality and size inspections.

## Files Present
- [README.md](file:///c:/Users/laksh/CreditCard/04_Data_Collection/README.md): Documentation of the data collection stage.
- [Data_Collection.ipynb](file:///c:/Users/laksh/CreditCard/04_Data_Collection/Data_Collection.ipynb): Jupyter notebook carrying out collection routines.

## Technologies Used
- Jupyter Notebook
- Pandas (data loading and checking structures)
- OS module (handling local folder pathings)

## Execution Process
Run the notebook cells sequentially. Ensure that `application_record.csv` and `credit_record.csv` are already generated in `03_Dataset/`.

## Expected Outputs
- Loaded applicant records (5,000 samples) and credit record details (approx. 180,000 logs).
- Summary matrices of null value lists and data type properties.

## Screenshots
Check `12_Screenshots` directory for terminal and notebook runtime screens.

## Conclusion
The data was successfully loaded. There are null fields in applicant details (specifically `OCCUPATION_TYPE`), which must be treated during preprocessing.

## Future Improvements
Implement dynamic connection wrappers to ingest data directly from remote data warehouses or SQL databases (PostgreSQL/MySQL) instead of static local CSV structures.
