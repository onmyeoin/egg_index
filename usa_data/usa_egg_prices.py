import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use Solarize Light 2 style
plt.style.use("Solarize_Light2")

# Load the reformatted CSV
file_path = "egg_price_reformatted.csv"
df = pd.read_csv(file_path)

# Parse dates
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", dayfirst=True)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Clean and sort
df = df.dropna(subset=["Date", "Price"]).sort_values("Date")

# Shared settings
line_color = "green"
line_width = 1.3

# 1️⃣ Full Historical Chart (1980 - Present)
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Price"], color=line_color, linewidth=line_width)
plt.title("US Egg Prices Per Dozen (1980 - Present)", fontsize=14, pad=15)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Price (USD per dozen)", fontsize=12)
plt.xticks(rotation=45)
sns.despine()  # Clean look: remove unnecessary spines
plt.tight_layout()
plt.savefig("egg_prices_1980_present.pdf")
plt.close()

# 2️⃣ Recent Chart (2020 - Present)
df_recent = df[df["Date"] >= "2020-01-01"]
plt.figure(figsize=(10, 5))
plt.plot(df_recent["Date"], df_recent["Price"], color=line_color, linewidth=line_width)
plt.title("US Egg Prices Per Dozen (2020 - Present)", fontsize=14, pad=15)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Price (USD per dozen)", fontsize=12)
plt.xticks(rotation=45)
sns.despine()
plt.tight_layout()
plt.savefig("egg_prices_2020_present.pdf")
plt.close()

print("✅ PDF exports saved using Solarize Light 2 style.")
