import plotly.express as px

# Power generation vs demand
def plot_generation_vs_demand(df):
    fig = px.line(df, x="Date", y=["Generation (MW)", "Demand (MW)"],
                  color_discrete_sequence=["green", "red"],
                  title="Power Generation vs Demand")
    return fig

# Plant-wise generation
def plot_plantwise_generation(df):
    fig = px.bar(df, x="Plant", y="Generation (MW)", color="Plant", barmode="group",
                 title="Plant-wise Power Generation")
    return fig

# Renewable contribution pie chart
def plot_renewable_contribution(df):
    total_gen = df["Generation (MW)"].sum()
    total_renew = df["Renewable (MW)"].sum()
    labels = ["Renewable", "Non-Renewable"]
    values = [total_renew, total_gen - total_renew]
    fig = px.pie(values=values, names=labels, title="Renewable vs Non-Renewable Share")
    return fig

# Coal usage bar chart
def plot_coal_usage(df):
    if "Coal Used (tons)" in df.columns:
        fig = px.bar(df, x="Plant", y="Coal Used (tons)", color="Plant",
                     title="Coal Consumption by Plant")
        return fig
    return None

# Waste generation line chart
def plot_waste_generated(df):
    if "Waste (tons)" in df.columns:
        fig = px.line(df, x="Date", y="Waste (tons)", color="Plant",
                      title="Waste Generation Over Time")
        return fig
    return None

# Efficiency comparison
def plot_efficiency(df):
    if "Coal Used (tons)" in df.columns:
        df_eff = df.copy()
        df_eff["Efficiency (%)"] = (df_eff["Generation (MW)"] / df_eff["Coal Used (tons)"]) * 100
        fig = px.box(df_eff, x="Plant", y="Efficiency (%)", color="Plant",
                     title="Plant Efficiency Comparison")
        return fig
    return None
