# Machine Learning Model Building Module

## Introduction
The Model Building Module (Epic 4) implements supervised classification models to predict credit card approvals. It fits, evaluates, and compares multiple models before packaging the highest-performing model for real-time web inference.

## Purpose
To build a classification model that identifies applicants likely to default or make late payments, enabling banking administrators to evaluate credit risk.

## Objectives
- Train and tune four supervised classification algorithms: **Logistic Regression**, **Decision Tree**, **Random Forest**, and **XGBoost**.
- Evaluate each model using multiple metrics: **Accuracy**, **Precision**, **Recall**, **F1 Score**, and **ROC-AUC**.
- Generate model comparison charts and statistical reports.
- Select the best model and export it as `best_model.pkl` alongside scaler and encoder artifacts.

## Files Present
- [README.md](file:///c:/Users/laksh/CreditCard/07_Model_Building/README.md): Model development documentation.
- [Model_Building.ipynb](file:///c:/Users/laksh/CreditCard/07_Model_Building/Model_Building.ipynb): Model training script.
- `best_model.pkl`: Serialized model classifier (generated after notebook execution).
- `scaler.pkl`: Copied from Preprocessing (generated after notebook execution).
- `encoder.pkl`: Copied from Preprocessing (generated after notebook execution).

## Machine Learning Models Implemented
1. **Logistic Regression**: Linear classifier that establishes baseline performance.
2. **Decision Tree**: Non-linear classifier that splits features on entropy/gini indices.
3. **Random Forest**: Ensemble bagging classifier that reduces overfitting.
4. **XGBoost**: Extreme Gradient Boosting algorithm designed for high speed and tabular accuracy.

## Evaluation Process
Each model calculates:
- **Confusion Matrix**: Visualizing true/false positives and negatives.
- **ROC Curve**: Charting True Positive Rate vs. False Positive Rate across thresholds.
- **Classification Report**: Tabulating precision, recall, and F1 metrics.
- **Feature Importance**: Graphing the contribution of each demographic feature.

## Expected Outputs
The notebook automatically writes these plots to `11_Outputs/`:
- `confusion_matrix.png`: Layout of predictions.
- `roc_curve.png`: Comparative ROC curves for all models.
- `accuracy_comparison.png`: Performance bar chart.
- `feature_importance.png`: Feature importance coefficients.

## Conclusion
Ensemble methods (Random Forest and XGBoost) generally outperform baseline linear models by capturing non-linear feature interactions (such as income, age, and employment duration).
