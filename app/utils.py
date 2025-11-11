import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def load_data(file_path):
    """Load CSV data"""
    df = pd.read_csv(file_path, parse_dates=['Timestamp'])
    return df

def downsample(df, step=10):
    """Take every nth row to reduce plot load"""
    return df.iloc[::step, :]

def plot_time_series(df, column, title="Time Series"):
    """Generate time series plot with Plotly"""
    fig = px.line(df, x='Timestamp', y=column, title=title)
    fig.update_layout(
        autosize=True,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def plot_box(df, column, title="Box Plot", group=None):
    """Generate boxplot for a metric"""
    if group:
        fig = px.box(df, x=group, y=column, title=title, points="all")
    else:
        fig = px.box(df, y=column, title=title, points="all")
    fig.update_layout(
        autosize=True,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def plot_heatmap(df, columns, title="Correlation Heatmap"):
    corr = df[columns].corr()
    fig = px.imshow(corr, text_auto=True, color_continuous_scale='Viridis', title=title)
    fig.update_layout(
        autosize=True,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig
