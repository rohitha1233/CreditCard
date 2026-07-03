import os

class Config:
    """Flask application configuration class."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'banking-security-token-938201'
    
    # Model serialization file paths
    MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'model', 'model.pkl'))
    SCALER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'model', 'scaler.pkl'))
    ENCODER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'model', 'encoder.pkl'))
    
    # Environment configs
    DEBUG = False
    TESTING = False
