import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from config import Config
from utils import predict_approval, load_artifacts

app = Flask(__name__)
app.config.from_object(Config)

# Try loading ML artifacts at startup to confirm path and file validity
try:
    load_artifacts()
    print("[INFO] Machine Learning artifacts loaded successfully at startup.")
except Exception as e:
    print(f"[WARNING] Machine Learning artifacts could not be pre-loaded: {e}")

@app.route('/')
def home():
    """Render the landing home page."""
    return render_template('home.html')

@app.route('/about')
def about():
    """Render the project description and architecture details."""
    return render_template('about.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Handle prediction form inputs and run classification inferences."""
    if request.method == 'POST':
        # Retrieve form data
        try:
            form_data = {
                'CODE_GENDER': request.form.get('gender'),
                'FLAG_OWN_CAR': request.form.get('own_car'),
                'FLAG_OWN_REALTY': request.form.get('own_realty'),
                'CNT_CHILDREN': int(request.form.get('children', 0)),
                'AMT_INCOME_TOTAL': float(request.form.get('income', 0.0)),
                'NAME_INCOME_TYPE': request.form.get('income_type'),
                'NAME_EDUCATION_TYPE': request.form.get('education_type'),
                'NAME_FAMILY_STATUS': request.form.get('family_status'),
                'NAME_HOUSING_TYPE': request.form.get('housing_type'),
                'FLAG_WORK_PHONE': int(request.form.get('work_phone', 0)),
                'FLAG_PHONE': int(request.form.get('phone', 0)),
                'FLAG_EMAIL': int(request.form.get('email', 0)),
                'OCCUPATION_TYPE': request.form.get('occupation_type'),
                'CNT_FAM_MEMBERS': float(request.form.get('family_members', 1.0)),
                'Age_Years': float(request.form.get('age', 18.0)),
                'Employed_Years': float(request.form.get('employed_years', 0.0))
            }
            
            # Simple backend validation checks
            errors = []
            if form_data['AMT_INCOME_TOTAL'] <= 0:
                errors.append("Annual Income must be a positive number.")
            if form_data['Age_Years'] < 18 or form_data['Age_Years'] > 120:
                errors.append("Age must be between 18 and 120 years.")
            if form_data['Employed_Years'] < 0:
                errors.append("Employment duration cannot be negative.")
            if form_data['Employed_Years'] > form_data['Age_Years'] - 14:
                errors.append("Employment years exceed logical work lifespan.")
            if form_data['CNT_CHILDREN'] < 0 or form_data['CNT_FAM_MEMBERS'] < 1:
                errors.append("Invalid family or children count.")
                
            if errors:
                return render_template('index.html', errors=errors, prev_inputs=request.form)
                
            # Perform prediction
            prediction_res = predict_approval(form_data)
            
            # Put results and inputs in session to follow Post-Redirect-Get pattern
            session['prediction_result'] = prediction_res
            session['applicant_details'] = form_data
            
            return redirect(url_for('result'))
            
        except Exception as e:
            err_msg = f"Error processing prediction input: {str(e)}"
            return render_template('index.html', errors=[err_msg], prev_inputs=request.form)
            
    # GET request shows form
    return render_template('index.html')

@app.route('/result')
def result():
    """Render prediction outcome from session metrics."""
    prediction_result = session.get('prediction_result')
    applicant_details = session.get('applicant_details')
    
    if not prediction_result or not applicant_details:
        return redirect(url_for('predict'))
        
    return render_template('result.html', result=prediction_result, applicant=applicant_details)

@app.route('/health')
def health():
    """API endpoint to monitor container health and load configurations."""
    try:
        load_artifacts()
        return jsonify({"status": "healthy", "model_loaded": True}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500

@app.errorhandler(404)
def page_not_found(e):
    """Render a premium custom 404 page for missing routes."""
    return render_template('error.html'), 404

if __name__ == '__main__':
    # Standard Flask execution
    app.run(host='127.0.0.1', port=5000, debug=False)
