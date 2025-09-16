import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from statsmodels.tsa.arima.model import ARIMA


'''
st.set_page_config(page_title="NTPC Energy Dashboard", layout="wide")

st.title("⚡ NTPC Energy Dashboard")
st.markdown("A showcase project from my internship at NTPC.")


st.sidebar.header("Upload Data")
file = st.sidebar.file_uploader("Upload a CSV file with Date, Plant, Generation (MW), Demand (MW)", type=["csv"])

if file is not None:
    df = pd.read_csv(file, parse_dates=["Date"])
    st.success("Data uploaded successfully!")

    st.subheader("🔎 Data Overview")
    st.dataframe(df.head())

    
    st.subheader("📊 Summary Statistics")
    st.write(df.describe())

   
    st.subheader("⚡ Power Generation vs Demand")
    fig1 = px.line(df, x="Date", y=["Generation (MW)", "Demand (MW)"], color_discrete_sequence=["green", "red"])
    st.plotly_chart(fig1, use_container_width=True)


    st.subheader("🏭 Plant-wise Power Generation")
    fig2 = px.bar(df, x="Plant", y="Generation (MW)", color="Plant", barmode="group")
    st.plotly_chart(fig2, use_container_width=True)


    # Forecasting with ARIMA
    st.subheader("📈 Energy Demand Forecast")
    try:
        demand_series = df.groupby("Date")["Demand (MW)"].sum()
        model = ARIMA(demand_series, order=(2,1,2))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=7)

        forecast_df = pd.DataFrame({"Date": pd.date_range(start=demand_series.index[-1] + pd.Timedelta(days=1), periods=7),
                                    "Forecasted Demand (MW)": forecast})

        fig3 = px.line(forecast_df, x="Date", y="Forecasted Demand (MW)", markers=True)
        st.plotly_chart(fig3, use_container_width=True)
    except Exception as e:
        st.warning(f"Could not generate forecast: {e}")

    
    if "Renewable (MW)" in df.columns:
        st.subheader("🌱 Renewable Energy Contribution")
        total_gen = df["Generation (MW)"].sum()
        total_renew = df["Renewable (MW)"].sum()

        labels = ["Renewable", "Non-Renewable"]
        values = [total_renew, total_gen - total_renew]

        fig4 = px.pie(values=values, names=labels, title="Renewable vs Non-Renewable Share")
        st.plotly_chart(fig4, use_container_width=True)
else:
    st.info("👈 Please upload a dataset to continue.")


# st.markdown("---")
# st.caption("")

'''