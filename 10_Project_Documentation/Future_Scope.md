# Future Scope & Technical Enhancements

This document outlines future enhancements and scalability improvements for the Credit Card Approval Prediction System.

## 1. Advanced Machine Learning Pipeline

- **Hyperparameter Grid Search:** Implement automated Grid Search or Randomized Search cross-validation to tune model parameters (e.g., learning rate and depth in XGBoost).
- **SMOTE Class Imbalancing:** Implement Synthetic Minority Over-sampling Technique (SMOTE) to balance the target class distribution if the training set becomes highly imbalanced.
- **Deep Learning Classifiers:** Evaluate Artificial Neural Networks (ANNs) built with TensorFlow/Keras for complex non-linear feature mapping.

## 2. Web Application Enhancements

- **Dynamic Form Auto-completion:** Implement auto-completion for occupations and zip codes using public databases.
- **Explainable AI (XAI):** Integrate SHAP (SHapley Additive exPlanations) or LIME in the Flask app to explain which features contributed most to an applicant's approval or rejection.
- **Multi-Factor Authentication:** Implement secure login routes for bank administrators.

## 3. DevOps & Scale-up

- **Docker Containerization:** Package the application using a `Dockerfile` and `docker-compose.yml` to ensure consistent deployments across macOS, Windows, and Linux.
- **Kubernetes Clustering:** Use Kubernetes to auto-scale the Flask prediction service to handle high-traffic spikes.
- **Database Backend:** Migrate the raw CSV files to a relational database like PostgreSQL or MySQL, using SQLAlchemy for query management.
