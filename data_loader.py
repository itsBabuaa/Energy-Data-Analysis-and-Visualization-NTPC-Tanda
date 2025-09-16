import pandas as pd
import streamlit as st

def load_data(file):
    try:
        df = pd.read_csv(file, parse_dates=["Date"])
        st.success("✅ Data uploaded successfully!")
        return df
    except Exception as e:
        st.error(f"❌ Error loading file: {e}")
        return None


def show_overview(df):
    # Show data preview and statistics
    st.subheader("🔎 Data Overview")
    st.dataframe(df.head(6))

    st.subheader("📊 Summary Statistics")
    st.write(df.describe())
