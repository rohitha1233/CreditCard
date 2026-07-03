# Web Application Module

## Introduction
The Web Application Module represents the final user-facing layer (Epic 5) of the Credit Card Approval Prediction System. It exposes a responsive dashboard letting users submit applicant demographic details and receive instant eligibility assessments.

## Purpose
To deploy the trained machine learning pipeline into a responsive browser interface.

## Objectives
- Load the pre-trained classification models (`best_model.pkl`), StandardScaler scale parameters (`scaler.pkl`), and categorical LabelEncoders (`encoder.pkl`) at startup.
- Implement Flask controller routes and session states.
- Run frontend validations and display prediction scores.

## Files Present
- [app.py](file:///c:/Users/laksh/CreditCard/08_Web_Application/app.py): Flask application controller.
- [config.py](file:///c:/Users/laksh/CreditCard/08_Web_Application/config.py): Core configurations.
- [utils.py](file:///c:/Users/laksh/CreditCard/08_Web_Application/utils.py): Preprocessing and inference executor.
- [requirements.txt](file:///c:/Users/laksh/CreditCard/08_Web_Application/requirements.txt): Local dependencies.
- **[templates/](file:///c:/Users/laksh/CreditCard/08_Web_Application/templates)**:
  - `layout.html`: Base frame containing Font Awesome and Poppins font loads.
  - `home.html`: Land page greeting and feature cards.
  - `about.html`: Detail model specifications.
  - `index.html`: Applicant form inputs.
  - `result.html`: Green/Red visual decisions outcome.
  - `error.html`: Custom 404 page.
- **[static/](file:///c:/Users/laksh/CreditCard/08_Web_Application/static)**:
  - `css/`: Vanilla sheets governing animations, forms, responsive viewports, and primary colors.
  - `js/`: Frontend form listeners and validation functions.
  - `images/`: Logo vectors and graphic assets.

## Execution Process
Run `python app.py` and open `http://127.0.0.1:5000` in a web browser.
