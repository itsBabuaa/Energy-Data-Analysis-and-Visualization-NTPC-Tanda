from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import plotly.express as px
import streamlit as st

def forecast_demand(df, steps=7):
    try:
        demand_series = df.groupby("Date")["Demand (MW)"].sum()
        model = ARIMA(demand_series, order=(2,1,2))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=steps)

        forecast_df = pd.DataFrame({
            "Date": pd.date_range(start=demand_series.index[-1] + pd.Timedelta(days=1), periods=steps),
            "Forecasted Demand (MW)": forecast
        })

        fig = px.line(forecast_df, x="Date", y="Forecasted Demand (MW)", markers=True,
                      title=f"{steps}-Day Energy Demand Forecast")
        return fig
    except Exception as e:
        st.warning(f"⚠ Could not generate forecast: {e}")
        return None
