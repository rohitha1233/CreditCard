# Local Deployment Guide

This guide details the steps to deploy the **Credit Card Approval Prediction System** web application locally on your computer.

## Prerequisites

Ensure you have completed the initial project setup steps. If not, refer to the [Installation Guide](file:///c:/Users/laksh/CreditCard/01_Project_Setup/installation_guide.md).

* Python 3.10 or higher installed.
* Conda (recommended) or virtualenv installed.
* Saved model artifacts present in the `07_Model_Building/` directory:
  * `best_model.pkl`
  * `scaler.pkl`
  * `encoder.pkl`

---

## Steps for Local Deployment

### Step 1: Clone the Repository
Open your terminal (PowerShell, Command Prompt, or bash) and navigate to your workspace:
```bash
git clone https://github.com/rohitha1233/CreditCard.git
cd CreditCard
```

### Step 2: Activate the Virtual Environment
Activate your configured virtual environment containing Flask, Scikit-Learn, and XGBoost:

* **Using Conda:**
  ```bash
  conda activate credit_card_approval
  ```

* **Using Pip (Windows):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

* **Using Pip (macOS/Linux):**
  ```bash
  source venv/bin/activate
  ```

### Step 3: Verify Model Artifact Paths
Before starting the server, ensure that the model binaries are in the correct directory. The configuration file `08_Web_Application/config.py` looks for:
* `../07_Model_Building/best_model.pkl`
* `../07_Model_Building/scaler.pkl`
* `../07_Model_Building/encoder.pkl`

### Step 4: Run the Flask Server
Navigate to the web application folder and run the server script:
```bash
cd 08_Web_Application
python app.py
```

### Step 5: Access the Application
Open your web browser of choice and enter the following address:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Verifying the Local Deployment

To ensure that the application is running normally and can make predictions:
1. **Home Page**: Navigate to `/` to view the landing page dashboard.
2. **Prediction Page**: Click the "Predict Approval" button (or go to `/predict`) to load the demographic form.
3. **Form Submissions**: Fill in applicant variables and click **Submit Application**.
4. **Health Check API**: Visit [http://127.0.0.1:5000/health](http://127.0.0.1:5000/health) to confirm the backend configuration and model parameters are successfully loaded (returns `{"model_loaded": true, "status": "healthy"}`).
