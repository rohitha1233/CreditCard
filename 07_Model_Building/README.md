# Machine Learning Model Building Module

## Introduction
The Model Building Module (Epic 4) implements supervised classification models to predict credit card approvals. It fits, evaluates, and compares multiple models before packaging the highest-performing model for real-time web inference.

## Purpose
To build a classification model that identifies applicants likely to default or make late payments, enabling banking administrators to evaluate credit risk.

## Objectives
- Train and tune three supervised classification algorithms: **Logistic Regression**, **Decision Tree Classifier**, and **Random Forest Classifier**.
- Evaluate each model using multiple metrics: **Accuracy**, **Precision**, **Recall**, **F1 Score**, and **ROC-AUC**.
- Generate model comparison charts and statistical reports automatically.
- Select the best model dynamically based on accuracy (and F1 score as fallback) and export it as `model.pkl` to the Flask web application module.

## Files Present
- [README.md](file:///c:/Users/laksh/CreditCard/07_Model_Building/README.md): Model development documentation.
- [logistic_regression.ipynb](file:///c:/Users/laksh/CreditCard/07_Model_Building/logistic_regression.ipynb): Notebook for training Logistic Regression.
- [decision_tree.ipynb](file:///c:/Users/laksh/CreditCard/07_Model_Building/decision_tree.ipynb): Notebook for training Decision Tree.
- [random_forest.ipynb](file:///c:/Users/laksh/CreditCard/07_Model_Building/random_forest.ipynb): Notebook for training Random Forest.
- [model_comparison.ipynb](file:///c:/Users/laksh/CreditCard/07_Model_Building/model_comparison.ipynb): Notebook comparing performance and exporting the best model.
- `best_model.pkl`: Copy of the selected model classifier.
- `scaler.pkl`: Copied from Preprocessing.
- `encoder.pkl`: Copied from Preprocessing.
- **[outputs/](file:///c:/Users/laksh/CreditCard/07_Model_Building/outputs)**:
  - `confusion_matrix_logistic.png`: Logistic Regression confusion matrix.
  - `confusion_matrix_tree.png`: Decision Tree confusion matrix.
  - `confusion_matrix_randomforest.png`: Random Forest confusion matrix.
  - `accuracy_comparison.png`: Performance bar chart comparing model accuracies.
  - `feature_importance.png`: Feature importance of the Random Forest model.
  - `roc_curve.png`: Comparative ROC curves for all models.

## Machine Learning Models Implemented
1. **Logistic Regression**: Linear classifier that establishes baseline performance (`max_iter=1000`, `random_state=42`).
2. **Decision Tree Classifier**: Non-linear classifier splitting features based on Gini impurity (`max_depth=6`, `random_state=42`).
3. **Random Forest Classifier**: Ensemble bagging classifier to reduce overfitting (`n_estimators=100`, `max_depth=10`, `random_state=42`).

## Evaluation Results
The models were trained on the real preprocessed dataset (80/20 train-test stratified split):

| Model Name | Accuracy | Precision | Recall | F1 Score | Training Time | Prediction Time |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | **82.30%** | **82.30%** | **100.00%** | **0.9029** | **0.0085s** | **0.0000s** |
| **Random Forest** | 82.30% | 82.30% | 100.00% | 0.9029 | 0.2910s | 0.0107s |
| **Decision Tree** | 81.50% | 82.22% | 98.91% | 0.8980 | 0.0091s | 0.0000s |

> [!NOTE]
> Logistic Regression was selected as the best performing model for deployment due to its equivalent accuracy/F1 score and significantly faster training and prediction times.

## Conclusion
The baseline Logistic Regression model captures the data relationships exceptionally well and offers ultra-low latency prediction, making it ideal for the live Flask web application. Feature importances from the Random Forest model reveal that years of employment and age are among the strongest predictive factors for credit eligibility.

