import pandas as pd
import plotly.express as px

# Load the reformatted CSV
file_path = "egg_price_reformatted.csv"
df = pd.read_csv(file_path)

# Explicitly parse Date as dd/mm/yyyy and ensure Price is numeric
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", dayfirst=True)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Drop any rows with invalid data
df = df.dropna(subset=["Date", "Price"])

# Sort by Date to ensure chronological plotting
df = df.sort_values("Date")

# Shared color and styling
line_color = "green"
line_mode = "lines"

# 1️⃣ Full historical chart (1980 - Present)
fig_full = px.line(
    df,
    x="Date",
    y="Price",
    title="US Egg Prices Per Dozen (1980 - Present)",
    labels={"Price": "Price (USD per dozen)", "Date": "Date"},
    template="plotly_white",
    color_discrete_sequence=[line_color]
)

fig_full.update_traces(mode=line_mode)
fig_full.update_layout(
    xaxis=dict(title="Year"),
    yaxis=dict(title="Price (USD per dozen)"),
    hovermode="x unified",
    showlegend=False
)

fig_full.show()

# 2️⃣ Focused chart (2020 - Present) with same color and style
df_recent = df[df["Date"] >= "2020-01-01"]

fig_recent = px.line(
    df_recent,
    x="Date",
    y="Price",
    title="US Egg Prices Per Dozen (2020 - Present)",
    labels={"Price": "Price (USD per dozen)", "Date": "Date"},
    template="plotly_white",
    color_discrete_sequence=[line_color]
)

fig_recent.update_traces(mode=line_mode)
fig_recent.update_layout(
    xaxis=dict(title="Year"),
    yaxis=dict(title="Price (USD per dozen)"),
    hovermode="x unified",
    showlegend=False
)

fig_recent.show()
