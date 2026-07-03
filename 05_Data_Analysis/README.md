# Data Analysis Module

## Introduction
The Data Analysis Module (Epic 2) performs deep Exploratory Data Analysis (EDA) on applicant profile records and credit repayment trends.

## Purpose
To uncover structural distributions, relationships, correlations, and anomalies in features before passing them to the preprocessing and model-building stages.

## Objectives
- Conduct Univariate Analysis (frequencies of gender, income types, education levels, housing types, and numerical distributions of age, employment, and income total).
- Conduct Multivariate Analysis (evaluating correlation structures, pairplots, and grouped trends like Income vs. Education or Age vs. Employment).
- Run Descriptive Analysis (calculating skewness, kurtosis, quartiles, variance, and standard deviations).
- Save high-resolution plots to `11_Outputs/`.

## Files Present
- [README.md](file:///c:/Users/laksh/CreditCard/05_Data_Analysis/README.md): Documentation of the data analysis phase.
- [Data_Analysis.ipynb](file:///c:/Users/laksh/CreditCard/05_Data_Analysis/Data_Analysis.ipynb): Interactive notebook running visualization calculations.

## Technologies Used
- Pandas & NumPy (data grouping and description statistics)
- Matplotlib (basic graph alignments)
- Seaborn (premium styling, countplots, heatmaps, pairplots)

## Execution Process
Run the cells of `Data_Analysis.ipynb` sequentially. Ensure that `application_record.csv` is correctly positioned under `03_Dataset/`.

## Expected Outputs
The notebook will generate and save the following files directly inside `11_Outputs/`:
- `histogram.png`: Total Annual Income distribution layout.
- `boxplot.png`: Income vs. Education level ranges.
- `countplot.png`: Distribution of applicant Occupation Types.
- `pairplot.png`: Numerical columns distribution matrices.
- `correlation_heatmap.png`: Heatmap demonstrating relationships among variables.

## Screenshots
Check `12_Screenshots` directory for notebook and graph runs.

## Conclusion
Demographic factors like higher education and stable occupations correlate positively with larger annual incomes. Long-term employment correlates with lower risk flags.

## Future Improvements
Implement dynamic web dashboards (using Plotly/Dash or Streamlit) to let users filter and explore demographic data trends interactively in a web browser.
