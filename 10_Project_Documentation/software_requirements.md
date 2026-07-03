# Software Requirements

The Credit Card Approval Prediction System requires the following software environment settings to execute successfully:

## Core Environment
- **Python**: Version 3.10.x (Recommended: 3.10.12)
- **Pip**: Version 22.0+

## Scientific Data Libraries
- **NumPy** (`>=1.22.0`): Multi-dimensional array operations.
- **Pandas** (`>=1.4.0`): Data manipulations, CSV loading, data aggregation, and status groupings.
- **Scikit-Learn** (`>=1.0.0`): Standard ML algorithms (Logistic Regression, Decision Tree, Random Forest), Label Encoders, Standard Scalers, and metric calculations.
- **XGBoost** (`>=1.5.0`): Boosting model training.
- **Joblib** (`>=1.1.0`): Persistence utility to dump and load `.pkl` pipelines.

## Visualization Libraries
- **Matplotlib** (`>=3.5.0`): Basic plotting utilities.
- **Seaborn** (`>=0.11.0`): Premium statistical graphs (heatmaps, countplots, pairplots).

## Web Application Backend
- **Flask** (`>=2.0.0`): Application routing, REST API endpoints, request lifecycle, custom error templates.
- **Gunicorn** (`>=20.1.0`): WSGI production HTTP Server for Unix environments (helpful for staging deployment).
- **Jinja2** (`>=3.0.0`): Template engines for mapping backend variables to HTML files.
