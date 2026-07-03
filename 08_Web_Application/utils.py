import os
import joblib
import pandas as pd
import numpy as np
from config import Config

# Global variables for caching model artifacts
_MODEL = None
_SCALER = None
_ENCODER_DICT = None

def load_artifacts():
    """Load model, scaler, and encoder files from storage if not already cached."""
    global _MODEL, _SCALER, _ENCODER_DICT
    
    if _MODEL is None:
        if not os.path.exists(Config.MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at: {Config.MODEL_PATH}")
        _MODEL = joblib.load(Config.MODEL_PATH)
        
    if _SCALER is None:
        if not os.path.exists(Config.SCALER_PATH):
            raise FileNotFoundError(f"Scaler file not found at: {Config.SCALER_PATH}")
        _SCALER = joblib.load(Config.SCALER_PATH)
        
    if _ENCODER_DICT is None:
        if not os.path.exists(Config.ENCODER_PATH):
            raise FileNotFoundError(f"Encoder file not found at: {Config.ENCODER_PATH}")
        _ENCODER_DICT = joblib.load(Config.ENCODER_PATH)

def predict_approval(data):
    """
    Perform preprocessing and prediction on the input dictionary.
    
    Parameters:
        data (dict): Dictionary containing the input feature keys.
            
    Returns:
        dict: Containing 'decision' ('Approved' or 'Rejected'),
              'confidence' (float), and 'status' (0 or 1)
    """
    load_artifacts()
    
    # Define exact feature alignment order expected by scaler
    feature_order = [
        'CODE_GENDER', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY', 'CNT_CHILDREN',
        'AMT_INCOME_TOTAL', 'NAME_INCOME_TYPE', 'NAME_EDUCATION_TYPE',
        'NAME_FAMILY_STATUS', 'NAME_HOUSING_TYPE', 'FLAG_WORK_PHONE',
        'FLAG_PHONE', 'FLAG_EMAIL', 'OCCUPATION_TYPE', 'CNT_FAM_MEMBERS',
        'Age_Years', 'Employed_Years'
    ]
    
    # Standardize/format raw input values
    processed_row = {}
    for col in feature_order:
        val = data.get(col)
        # Default numeric fallback
        if col in ['CNT_CHILDREN', 'FLAG_WORK_PHONE', 'FLAG_PHONE', 'FLAG_EMAIL']:
            processed_row[col] = int(val) if val is not None else 0
        elif col in ['AMT_INCOME_TOTAL', 'CNT_FAM_MEMBERS', 'Age_Years', 'Employed_Years']:
            processed_row[col] = float(val) if val is not None else 0.0
        else:
            # Categorical string
            processed_row[col] = str(val) if val is not None else 'Unknown'
            
    # Apply Label Encoding
    for col, le in _ENCODER_DICT.items():
        val = processed_row[col]
        if val not in le.classes_:
            if 'Unknown' in le.classes_:
                processed_row[col] = 'Unknown'
            else:
                processed_row[col] = le.classes_[0]
        processed_row[col] = le.transform([processed_row[col]])[0]
        
    # Convert row dictionary to aligned DataFrame
    row_df = pd.DataFrame([processed_row])[feature_order]
    
    # Scale using pre-fitted StandardScaler
    scaled_features = _SCALER.transform(row_df)
    
    # Run model prediction
    prediction = int(_MODEL.predict(scaled_features)[0])
    
    # Calculate confidence/probability if supported by model
    if hasattr(_MODEL, "predict_proba"):
        probabilities = _MODEL.predict_proba(scaled_features)[0]
        confidence = float(probabilities[prediction])
    else:
        confidence = 1.0
        
    # Translate model target code (0 = Approved, 1 = Rejected)
    decision = "Approved" if prediction == 0 else "Rejected"
    
    return {
        "decision": decision,
        "confidence": round(confidence * 100, 2),
        "status": prediction
    }
