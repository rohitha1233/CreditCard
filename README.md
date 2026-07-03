# Credit Card Approval Prediction System

<!-- Project Banner & Badges -->
![Apex Bank Banner](08_Web_Application/static/images/hero_banner.png)

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask Framework](https://img.shields.io/badge/framework-Flask-blue.svg)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/library-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An automated Machine Learning-driven decision support system to evaluate credit card applicant profiles and predict eligibility based on demographic and repayment histories. Developed for the SmartBridge Virtual Internship.

---

## 1. Project Description & Problem Statement

### 1.1 Problem Statement
Traditional credit card screening relies on manual verification. This process is time-consuming, prone to human error, and increases credit risk. Financial institutions require a reliable decision-making system to evaluate applicants and flag high-risk accounts.

### 1.2 Objective
To develop a predictive machine learning model that classifies credit card applicants as either Approved (`0`) or Rejected (`1`) based on demographic and repayment histories. This model is integrated into a Flask web application with a responsive dashboard.

---

## 2. Technology Stack

- **Core Programming:** Python 3.10+
- **Data Engineering:** NumPy, Pandas
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-Learn, XGBoost, Joblib
- **Web Application:** Flask, HTML5, CSS3, JavaScript, Bootstrap 5
- **Deployment:** IBM Watson Machine Learning (Documentation)

---

## 3. Folder Structure

```
CreditCardApprovalPrediction/
├── LICENSE
├── requirements.txt
├── environment.yml
├── .gitignore
├── README.md
├── 01_ER_Diagram/                 # Entity Relationship, Technical Architecture & Use Case
├── 02_Project_Workflow/            # Development Workflow and Project Execution Flow
├── 03_Dataset/                     # Raw CSV data files
├── 04_Prerequisites/               # Software environment prerequisites (requirements.txt)
├── 05_Data_Analysis/               # Jupyter Notebook for EDA and descriptive graphs
├── 06_Data_Preprocessing/          # Preprocessing pipeline, target mapping, and scalers
├── 07_Model_Building/              # Training notebooks, comparison results, and best_model.pkl
├── 08_Web_Application/             # Flask application source files, templates, and static assets
├── 09_Deployment/                  # Local/cloud deployment screenshots
└── 10_Project_Documentation/       # Technical architecture reports and execution guides
```

---

## 4. System Architecture

The technical design includes architectural diagrams located in the diagram directories:

1. **Entity Relationship Diagram (ERD):** Maps applicant demographics, credit balance history logs, and targets. Located in [01_ER_Diagram](01_ER_Diagram/).
2. **Project Flow Diagram:** Outlines the logical linear flow from ingestion to result presentation. Located in [02_Project_Workflow](02_Project_Workflow/).
3. **Technical Architecture:** Visualizes Flask server and model scoring client-server flow. Located in [01_ER_Diagram](01_ER_Diagram/).
4. **Use Case Diagram:** Models user actions on the assessment web form. Located in [01_ER_Diagram](01_ER_Diagram/).
5. **Workflow Diagram:** Displays development milestones and project phases. Located in [02_Project_Workflow](02_Project_Workflow/).

---

## 5. Machine Learning Models & Evaluation

We evaluate three classifiers on an 80/20 train-test stratified split:

| Algorithm | Test Accuracy | Precision | Recall | F1 Score | AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | **82.30%** | **82.30%** | **100.00%** | **0.9029** | **0.5585** |
| **Random Forest** | 82.30% | 82.30% | 100.00% | 0.9029 | 0.5165 |
| **Decision Tree** | 81.60% | 82.24% | 99.03% | 0.8986 | 0.5208 |

We selected **Logistic Regression** as the best model for web application integration and deployment due to its high test accuracy, optimal trade-off of recall/precision on delinquent cases, and significantly lower training and inference times compared to the Random Forest model.

---

## 6. Installation & Execution

### 6.1 Clone & Setup Environment
1. Clone the repository and navigate to the project directory:
   ```bash
    git clone https://github.com/rohitha1233/CreditCard.git
    cd CreditCard
   ```
2. Create and activate the Conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate credit_card_approval
   ```

### 6.2 Run local Flask server
1. Navigate to the web application folder:
   ```bash
   cd 08_Web_Application
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open your web browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 7. Deployment

- **Local Deployment:** Covered in [Local Deployment Guide](10_Project_Documentation/Local_Deployment.md).
- **IBM Watson Cloud Deployment:** Covered in [IBM Watson Deployment Guide](10_Project_Documentation/IBM_Watson_Deployment.md).

---

## 8. License & Acknowledgements

### License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

### Acknowledgements
- Developed for the **SmartBridge Virtual Internship** program.
- Dataset schemas adapted from the Kaggle Credit Card Approval dataset.
