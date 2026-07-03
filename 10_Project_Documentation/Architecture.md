# Technical Architecture Documentation

This document explains the technical architecture, data model, and component interactions of the Credit Card Approval Prediction System.

## 1. System Topology

The application uses a standard three-tier web application architecture:

```
[Presentation Tier]         [Application Tier]           [Data & Model Tier]
  Web Browser (HTML5)    ──►   Flask Web Server   ──►   best_model.pkl (Scikit-Learn)
  CSS Styles (style.css) ◄──   (app.py & utils.py)◄──   scaler.pkl & encoder.pkl
  JS (validation.js)
```

1. **Presentation Tier:** A responsive web application built with HTML5, CSS3, JavaScript, and Bootstrap 5. It uses client-side validation (`validation.js`) to check inputs and display error warnings before submitting data to the server.
2. **Application Tier:** A Flask web backend (`app.py`) that handles routes, manages application sessions, performs backend data validation, and calls the preprocessing and inference utilities in `utils.py`.
3. **Data & Model Tier:** Preprocessing transformers (`scaler.pkl` and `encoder.pkl`) and the trained machine learning model (`best_model.pkl`) that perform feature transformations and predict the approval status.

---

## 2. Data Model & Entity Relations

The ER diagram defines the structures and relationships of the data tables:

- **APPLICANT:** Stores demographic and financial details. Primary Key: `ID`.
- **CREDIT_RECORD:** Stores monthly payment status histories linked to applicants. Foreign Key: `ID` referencing `APPLICANT.ID`. Relation: `1` to `N` (an applicant can have many months of payment records).
- **PREDICTION:** Stores the outputs of the prediction engine. Linked to `APPLICANT.ID` (1 to 1). Includes the confidence score and approval decision.
- **ML_MODEL:** Tracks the model parameters (accuracy, AUC, and path to the serialized pickle file).

---

## 3. Web Service Routes

The Flask application exposes the following routes:

| Route Path | Method | Description | Rendered Template |
| :--- | :--- | :--- | :--- |
| `/` | `GET` | Main landing page of the bank portal. | `home.html` |
| `/about` | `GET` | Explains the project context and models. | `about.html` |
| `/predict` | `GET` | Displays the credit eligibility form. | `index.html` |
| `/predict` | `POST` | Processes form inputs, validates fields, and runs predictions. | Redirects to `/result` |
| `/result` | `GET` | Displays the final approval or rejection card. | `result.html` |
| `/health` | `GET` | Returns JSON status for container health checks. | JSON response |
| Custom 404 | Any | Handles invalid URL paths. | `error.html` |

---

## 4. Inference Data Pipeline

When an analyst submits an application form, the following pipeline executes:

1. **Ingestion:** Form details are collected into a dictionary.
2. **Backend Validation:** Check for negative values, invalid ages, or illogical employment periods.
3. **Alignment:** Fields are sorted to match the model's training columns.
4. **Encoding:** Categorical variables are converted to numeric codes using `encoder.pkl`.
5. **Scaling:** The features are scaled using the fitted standard scaler (`scaler.pkl`).
6. **Inference:** The scaled feature matrix is passed to `best_model.pkl` to compute the prediction and probability score.
7. **Rendering:** The outcome is saved in the session and displayed on the results dashboard.
