# Solar Data Discovery – Week 0

This repository contains the Week 0 challenge for the Solar Data Discovery project.  
It includes exploratory data analysis (EDA), data cleaning, and cross-country comparisons for solar farm data from Benin, Sierra Leone, and Togo.

---

## Project Structure


solar-challenge-week0/
├── app/
│   ├── main.py
│   ├── utils.py
├── data/
│   ├── benin_clean.csv
│   ├── sierra_leone_clean.csv
│   ├── togo_clean.csv
├── dashboard_screenshots/
│   ├── benin_time_series.png
│   ├── sierra_boxplot.png
│   ├── togo_heatmap.png
│   ├── togo_time_series.png
│   ├── benin_boxplot.png
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
