# Coterra Data Analytics

- Last updated: August 23, 2024
- Team: Josh Waters | Marti Dolce
- GitHub: https://github.com/tekmation/TektrolAnalytics
- Project: https://tektrolanalytics.onrender.com/
- Pk: Python, Jupyter Notebook, pandas, openpyxl, matplotlib, dash, plotly
---
## Overview:
This project provides a simple line chart analysis for five data points:

## Manual Rebuild Steps:

- [1] Download the Flow data excel from Scadacore
- [2] Perform a data cleaning on the Excel file (Volume, H20, Line, Summary Worksheets)
- [3] Update the BuildHTML Jupiter Notebook to update the HTML Files for the datasets
- [4] Push {index.html, h20_chart.html, line_chart.html, volume_chart.html} to github
- [5] Allow 5 minutes for CI/CD, then confirm render.com update

---

## Data Sets:

> columns_volume = ['ReportDate', 'Volumetric Flow G Previous Rate (SCFM) * 24', 'Volumetric Flow L Previous Rate (bbl/hr) * 24', 'Volumetric Flow G App Previous Rate (SCFM) * 24']

> columns_line = ['ReportDate', 'Line Pressure (psi)', 'Line Temperature (F)']

> columns_h20 = ['ReportDate', 'D Pppl (InH2O)', 'D Pr (InH2O)', 'D Pt (InH2O)']

---

## PII Challenges

> [ ] Include variables for column names
>
> [ ] Add computational functions for volumetric data conversions
> 
>  [ ] Use variables for data constants

