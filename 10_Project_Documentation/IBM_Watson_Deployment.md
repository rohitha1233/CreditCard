# IBM Watson Cloud Deployment Guide

This guide details the procedure to deploy the trained machine learning pipeline (XGBoost / Scikit-Learn) into the **IBM Watson Machine Learning (WML)** cloud environment and connect it to your Flask web application.

---

## 1. Prerequisites
* An active [IBM Cloud Account](https://cloud.ibm.com/).
* An instance of the **Watson Machine Learning** service provisioned on your IBM Cloud account.
* IBM Watson Machine Learning Python client installed:
  ```bash
  pip install ibm-watson-machine-learning
  ```

---

## 2. Setting Up the Deployment Space
1. Log in to the [IBM Cloud Console](https://cloud.ibm.com/).
2. Navigate to **Services and software** and open your **Watson Machine Learning** instance.
3. Open the **Watson Studio** interface and go to **Deployments** > **View all spaces**.
4. Click **New deployment space**:
   * Name your space (e.g., `Credit_Card_Approval_Space`).
   * Associate it with your Object Storage and Machine Learning services.
5. Copy the **Deployment Space ID** from the Space settings tab (needed for API calls).

---

## 3. Uploading and Deploying the Model

You can write a short Python script (or use a Jupyter notebook cell) to upload the model.

```python
from ibm_watson_machine_learning import APIClient

# Define credentials
wml_credentials = {
    "url": "https://us-south.ml.cloud.ibm.com", # Change region if different
    "apikey": "YOUR_IBM_CLOUD_API_KEY"
}

# Initialize WML Client
client = APIClient(wml_credentials)
client.set.default_space("YOUR_DEPLOYMENT_SPACE_ID")

# Model Metadata Specifications
model_metadata = {
    client.repository.ModelMetaNames.NAME: "Credit_Card_Approval_XGBoost",
    client.repository.ModelMetaNames.TYPE: "scikit-learn_1.0", # Adjust to match Scikit-Learn version
    client.repository.ModelMetaNames.SOFTWARE_SPEC_UID: client.software_spec.get_id_by_name("runtime-22.1-py3.9")
}

# Store model in space
model_details = client.repository.store_model(
    model="07_Model_Building/best_model.pkl",
    meta_props=model_metadata
)

# Extract Model ID
model_id = client.repository.get_model_id(model_details)
print(f"Model ID: {model_id}")

# Create Online Deployment (REST API Endpoint)
deployment_metadata = {
    client.deployments.ConfigurationMetaNames.NAME: "Credit_Card_Approval_Deployment",
    client.deployments.ConfigurationMetaNames.ONLINE: {}
}

deployment_details = client.deployments.create(
    model_uid=model_id,
    meta_props=deployment_metadata
)

# Extract Deployment Endpoint
scoring_url = client.deployments.get_scoring_href(deployment_details)
print(f"Scoring Endpoints: {scoring_url}")
```

---

## 4. Connecting WML to the Flask Web Application
Once the model is deployed on WML, update your Flask application config to query WML rather than loading the local `.pkl` files.

1. Create a `.env` file in the `08_Web_Application/` directory with your cloud credentials:
   ```env
   WML_API_KEY=YOUR_IBM_CLOUD_API_KEY
   WML_URL=https://us-south.ml.cloud.ibm.com
   WML_SPACE_ID=YOUR_DEPLOYMENT_SPACE_ID
   WML_SCORING_URL=YOUR_DEPLOYMENT_SCORING_URL
   ```
2. Modify `08_Web_Application/utils.py` to route queries through the WML API:
   ```python
   import requests
   
   # Retrieve IAM Access Token
   token_response = requests.post(
       'https://iam.cloud.ibm.com/identity/token',
       data={
           'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
           'apikey': WML_API_KEY
       }
   )
   mltoken = token_response.json()["access_token"]
   
   # Query Scoring endpoint
   headers = {
       'Content-Type': 'application/json',
       'Authorization': 'Bearer ' + mltoken
   }
   payload = {
       "input_data": [{
           "fields": feature_order,
           "values": [scaled_features.tolist()]
       }]
   }
   response = requests.post(WML_SCORING_URL, json=payload, headers=headers)
   prediction = response.json()["predictions"][0]["values"][0][0]
   ```
