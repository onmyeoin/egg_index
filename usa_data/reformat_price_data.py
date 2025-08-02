import pandas as pd

# Load the original CSV
file_path = "egg_price_per_dozen_usa.csv"
df = pd.read_csv(file_path)

# Melt the dataframe to long format
df_long = df.melt(id_vars=["Year"], var_name="Month", value_name="Price")

# Drop missing price values (e.g., blank future months)
df_long.dropna(subset=["Price"], inplace=True)

# Map month names to numbers
month_map = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}
df_long["Month_Num"] = df_long["Month"].map(month_map)

# Create a proper datetime column
df_long["Date"] = pd.to_datetime(
    dict(year=df_long["Year"], month=df_long["Month_Num"], day=1)
)

# Sort by date chronologically
df_long = df_long.sort_values(by="Date")

# Reformat date to dd/mm/yyyy
df_long["Date"] = df_long["Date"].dt.strftime("%d/%m/%Y")

# Keep only Date and Price columns
df_final = df_long[["Date", "Price"]]

# Save to new CSV
output_file = "egg_price_reformatted.csv"
df_final.to_csv(output_file, index=False)

print(f"Reformatted and chronologically ordered CSV saved to {output_file}")
