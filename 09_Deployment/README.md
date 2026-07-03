# Deployment Module

This directory contains the documentation, workflows, and scripts needed to deploy the **Credit Card Approval Prediction System** into target environments.

## Deployment Options

We support two primary modes of deployment:

### 1. [Local Deployment Guide](file:///c:/Users/laksh/CreditCard/09_Deployment/Local_Deployment.md)
* Details how to run the Flask application server on local environments (development, debugging, and demonstration).
* Leverages local file-system serialization of `best_model.pkl`, `scaler.pkl`, and `encoder.pkl`.

### 2. [IBM Watson Cloud Deployment Guide](file:///c:/Users/laksh/CreditCard/09_Deployment/IBM_Watson_Deployment.md)
* Details how to containerize and deploy the machine learning classifier using the **IBM Watson Machine Learning (WML)** Cloud platform.
* Integrates the cloud-hosted scoring endpoint back into the web portal for production use cases.

---

## Deployment Process Flow
```mermaid
graph TD
    A[Train Model in Jupyter] --> B[Export best_model.pkl & Preprocessors]
    B --> C{Choose Target}
    C -->|Local| D[Run Flask app.py locally]
    C -->|Production Cloud| E[Upload artifacts to IBM Cloud WML]
    D --> F[Localhost Portal /predict]
    E --> G[Create Online WML Endpoint]
    G --> H[Query scoring endpoint from Flask]
```

For specific steps, please refer to the corresponding markdown files linked above.
