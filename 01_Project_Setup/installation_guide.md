# Installation Guide

Follow these step-by-step instructions to configure and set up the Credit Card Approval Prediction project locally.

## Method 1: Using Anaconda (Recommended)

1. Open **Anaconda Prompt** or terminal.
2. Navigate to the project root directory:
   ```bash
   cd path/to/CreditCardApprovalPrediction
   ```
3. Create the Conda environment using the `environment.yml` file:
   ```bash
   conda env create -f environment.yml
   ```
4. Activate the newly created environment:
   ```bash
   conda activate credit_card_approval
   ```

## Method 2: Using Standard Python & Pip

1. Open your terminal or Command Prompt.
2. Navigate to the project root directory.
3. Create a python virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - **Windows (CMD/PowerShell)**:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Setting up Jupyter Kernel inside VS Code

To execute the Jupyter notebooks under the correct virtual environment, follow these steps:
1. Open the project folder in VS Code.
2. Open any `.ipynb` file in `04_Data_Collection/`, `05_Data_Analysis/`, etc.
3. In the top right corner of the notebook editor, click **Select Kernel**.
4. Choose **Python Environments...** and select the environment corresponding to `credit_card_approval` or the path to your `./venv/Scripts/python.exe`.
