import streamlit as st
from data_loader import load_data, show_overview
from visualizations import (
    plot_generation_vs_demand,
    plot_plantwise_generation,
    plot_renewable_contribution,
    plot_coal_usage,
    plot_waste_generated,
    plot_efficiency
)
from forecasting import forecast_demand

st.set_page_config(page_title="NTPC Energy Dashboard", layout="wide")
st.title("⚡ NTPC Energy Dashboard")
# st.markdown("")

# Sidebar
st.sidebar.header("Upload Data")
file = st.sidebar.file_uploader(
    "Upload CSV (Date, Plant, Generation (MW), Demand (MW), Renewable (MW), Coal Used (tons), Waste (tons))",
    type=["csv"]
)

if file is not None:
    df = load_data(file)
    if df is not None:
        show_overview(df)

        # Charts
        st.plotly_chart(plot_generation_vs_demand(df), use_container_width=True)
        st.plotly_chart(plot_plantwise_generation(df), use_container_width=True)

        # Forecast
        forecast_fig = forecast_demand(df)
        if forecast_fig:
            st.plotly_chart(forecast_fig, use_container_width=True)

        # Renewable Contribution
        if "Renewable (MW)" in df.columns:
            st.plotly_chart(plot_renewable_contribution(df), use_container_width=True)

        # Coal, Waste, Efficiency
        coal_fig = plot_coal_usage(df)
        if coal_fig:
            st.plotly_chart(coal_fig, use_container_width=True)

        waste_fig = plot_waste_generated(df)
        if waste_fig:
            st.plotly_chart(waste_fig, use_container_width=True)

        eff_fig = plot_efficiency(df)
        if eff_fig:
            st.plotly_chart(eff_fig, use_container_width=True)

else:
    st.info("👈 Please upload a dataset to continue.")


# st.markdown("---")
# st.caption("Babuaa Here")
