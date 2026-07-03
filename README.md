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
├── 01_Project_Setup/               # Hardware and software pre-requisites
├── 02_Project_Architecture/        # Architectural diagrams and drawio files
├── 03_Dataset/                     # Raw CSV files
├── 04_Data_Collection/             # Ingestion notebook
├── 05_Data_Analysis/               # EDA notebook
├── 06_Data_Preprocessing/          # Cleaning, target mapping, encoding, and scaling
├── 07_Model_Building/              # Training, model comparisons, and weights
├── 08_Web_Application/             # Flask backend & frontend files
├── 09_Deployment/                  # Local and IBM Watson deployment guides
├── 10_Documentation/               # Project reports and workflow details
├── 11_Outputs/                     # Exported charts and graphs
├── 12_Screenshots/                 # Interface screenshots
└── assets/                         # Graphic and design mockups
```

---

## 4. System Architecture

The technical design includes five architectural diagrams located in the [Project Architecture Module](file:///c:/Users/laksh/CreditCard/02_Project_Architecture/README.md):

1. **Entity Relationship Diagram (ERD):** Maps the relationships between applicant tables, credit balance logs, prediction requests, and model parameters.
2. **Project Flow Diagram:** Outlines the linear execution flow from data collection through model evaluation and web display.
3. **Technical Architecture:** Visualizes the client-server interaction patterns and model integrations.
4. **Use Case Diagram:** Models actor-system actions for applicants and systems.
5. **Workflow Diagram:** Illustrates the project development phases.

---

## 5. Machine Learning Models & Evaluation

We evaluate three classifiers on an 80/20 train-test stratified split:

| Algorithm | Test Accuracy | Precision | Recall | F1 Score | AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | **82.30%** | **82.30%** | **100.00%** | **0.9029** | **0.5688** |
| **Random Forest** | 82.30% | 82.30% | 100.00% | 0.9029 | 0.5127 |
| **Decision Tree** | 81.50% | 82.22% | 98.91% | 0.8980 | 0.5207 |

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

- **Local Deployment:** Covered in [Local Deployment Guide](file:///c:/Users/laksh/CreditCard/09_Deployment/Local_Deployment.md).
- **IBM Watson Cloud Deployment:** Covered in [IBM Watson Deployment Guide](file:///c:/Users/laksh/CreditCard/09_Deployment/IBM_Watson_Deployment.md).

---

## 8. License & Acknowledgements

### License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

### Acknowledgements
- Developed for the **SmartBridge Virtual Internship** program.
- Dataset schemas adapted from the Kaggle Credit Card Approval dataset.
