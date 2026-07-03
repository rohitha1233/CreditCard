# Project Application Screenshots

This folder hosts screenshots of the running application, Jupyter notebooks, local servers, and cloud configurations. 

## Screenshots Present

1. **[home_page.png](file:///c:/Users/laksh/CreditCard/12_Screenshots/home_page.png):** Displays the landing home page of the Apex Bank Credit Portal.
2. **[prediction_page.png](file:///c:/Users/laksh/CreditCard/12_Screenshots/prediction_page.png):** Displays the credit eligibility form with validation triggers.
3. **[result_page.png](file:///c:/Users/laksh/CreditCard/12_Screenshots/result_page.png):** Renders the approved or rejected card output with decision indicators.
4. **[notebook_execution.png](file:///c:/Users/laksh/CreditCard/12_Screenshots/notebook_execution.png):** Shows the cell logs and outputs of the Jupyter notebooks.
5. **[flask_running.png](file:///c:/Users/laksh/CreditCard/12_Screenshots/flask_running.png):** Shows the local Flask server running in the terminal.
6. **[github_repository.png](file:///c:/Users/laksh/CreditCard/12_Screenshots/github_repository.png):** Shows the Git directory structure of the repository.
7. **[deployment.png](file:///c:/Users/laksh/CreditCard/12_Screenshots/deployment.png):** Shows the endpoint status on IBM Watson Machine Learning.

## How to Capture Live Screenshots

1. Launch the local Flask server:
   ```bash
   cd 08_Web_Application
   python app.py
   ```
2. Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) and open the Home page. Press `PrtScn` or `Windows + Shift + S` to capture the screen, and save it as `home_page.png` in this directory.
3. Open the prediction form at `/predict`. Enter test values to capture the screen, and save it as `prediction_page.png`.
4. Submit the form to view the results. Capture the result card and save it as `result_page.png`.
5. Capture your terminal window showing the running server, and save it as `flask_running.png`.
