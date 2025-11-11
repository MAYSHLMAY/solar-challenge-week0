# Solar Data Interactive Dashboard

This dashboard lets users explore solar farm data for Benin, Sierra Leone, and Togo.  
It provides simple, interactive visualizations of solar metrics such as GHI, DNI, DHI, temperature, humidity, and wind speed.

---

## Features

- Interactive dashboard using Streamlit and Plotly
- Tabs for Time Series, Boxplots, and Correlation Heatmap
- Sidebar to choose country and metric
- Downsampling and caching for smoother performance

---

## Project Structure

```

solar-challenge-week0/
├── app/
│   ├── main.py
│   ├── utils.py
├── data/
│   ├── benin_clean.csv
│   ├── sierra_leone_clean.csv
│   ├── togo_clean.csv
├── figures/
│   ├── benin_time_series.png
│   ├── sierra_boxplot.png
│   ├── togo_heatmap.png
│   ├── togo_time_series.png
│   ├── benin_boxplot.png
└── README.md

````

---

## How to Run

```bash
cd app
streamlit run main.py
````

Open in browser at:
[http://localhost:8501](http://localhost:8501)

---

## Preview

Benin – Time Series
![Benin Time Series](./figures/benin_ghi_timeseries_full.png)

Benin – Boxplot
![Benin Boxplot](./figures/benin_ghi_boxplot.png)

Benin – Correlation Heatmap
![Benin Heatmap](./figures/benin_correlation_heatmap.png)

Sierra Leone – RH Boxplot
![Sierra Leone Boxplot](./figures/sierra_leone_rh_boxplot.png)

Togo – DNI Time Series
![Togo Time Series](./figures/togo_dni_timeseries.png)


---

This branch (`dashboard-dev`) contains the bonus interactive dashboard.
No need to merge it with `main`; screenshots show the final working app.

````
