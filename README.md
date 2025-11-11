# Solar Data Discovery – Week 0

This repository contains the Week 0 challenge for the Solar Data Discovery project.  
It includes exploratory data analysis (EDA), data cleaning, and cross-country comparisons for solar farm data from Benin, Sierra Leone, and Togo.

---

## Project Structure

solar-challenge-week0/
├── notebooks/ # EDA notebooks per country
│ ├── benin_eda.ipynb
│ ├── sierra_leone_eda.ipynb
│ └── togo_eda.ipynb
├── data/ # Cleaned CSVs (ignored from Git)
│ ├── benin_clean.csv
│ ├── sierra_leone_clean.csv
│ └── togo_clean.csv
├── figures/ # Plots exported from notebooks
├── app/ # (Optional) Bonus interactive dashboard
├── src/ # Helper scripts
├── scripts/ # Utility scripts
├── requirements.txt
└── README.md

---

## How to Explore the Data

1. Open the Jupyter notebooks in `notebooks/`.
2. Run each cell sequentially to see the EDA, visualizations, and cleaned datasets.
3. Cleaned CSVs are saved in `data/` (not tracked by Git).

---

## Optional

- For the interactive dashboard, check the `dashboard-dev` branch:
  - Run `app/main.py` using Streamlit.
  - See visualizations, boxplots, heatmaps, and time series charts.