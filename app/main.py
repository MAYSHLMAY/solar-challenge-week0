import streamlit as st
import pandas as pd
from utils import load_data, downsample, plot_time_series, plot_box, plot_heatmap

st.set_page_config(page_title="Solar EDA Dashboard", layout="wide")

st.title("Solar Farm Data Analysis")

# --- Sidebar ---
st.sidebar.header("Controls")

# Select country
country_files = {
    "Benin": "../data/benin_clean.csv",
    "Sierra Leone": "../data/sierra_leone_clean.csv",
    "Togo": "../data/togo_clean.csv"
}

selected_country = st.sidebar.selectbox("Select Country", list(country_files.keys()))
selected_metric = st.sidebar.selectbox("Select Metric", ["GHI", "DNI", "DHI", "ModA", "ModB", "Tamb", "RH", "WS"])

# --- Load data with caching ---
@st.cache_data
def get_data(file_path):
    df = load_data(file_path)
    return df

df = get_data(country_files[selected_country])
df_plot = downsample(df, step=20)

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["Time Series", "Boxplots", "Correlation Heatmap"])

with tab1:
    st.subheader(f"{selected_metric} over Time")
    st.plotly_chart(plot_time_series(df_plot, selected_metric), use_container_width=True)

with tab2:
    st.subheader(f"{selected_metric} Boxplot")
    st.plotly_chart(plot_box(df_plot, selected_metric), use_container_width=True)

with tab3:
    st.subheader("Correlation Heatmap")
    numeric_cols = df_plot.select_dtypes(include='number').columns.tolist()
    st.plotly_chart(plot_heatmap(df_plot, numeric_cols), use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.write("Data Points:", len(df))
st.sidebar.write("Downsampled for plotting:", len(df_plot))
