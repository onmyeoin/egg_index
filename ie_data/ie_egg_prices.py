import pandas as pd
import matplotlib.pyplot as plt

file_path = "CPM12.20250802T120846.csv"

# Load the CSV
df = pd.read_csv(file_path)

# Convert the "Month" column to datetime (assumes "Month" is like "2024 June")
df["Date"] = pd.to_datetime(df["Month"], format="%Y %B")

# Convert price to per dozen (values are per half dozen)
df["Price_EUR_Dozen"] = df["VALUE"] * 2

# Sort by date
df = df.sort_values("Date")

# --- Styling setup ---
plt.style.use("Solarize_Light2")
line_color = "#D2691E"  # Rust/Orange colour
line_width = 1.3

# --- Full historical chart ---
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df["Date"], df["Price_EUR_Dozen"], color=line_color, linewidth=line_width)
ax.set_title("Ireland Egg Prices Per Dozen (2012 - Present)", fontsize=16)
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("Price (EUR per dozen)", fontsize=12)
ax.tick_params(axis="both", labelsize=10)
ax.grid(False)  # No gridlines

plt.tight_layout()
plt.savefig("ireland_egg_prices_full.png", dpi=300)
plt.close()

# --- Zoomed chart: 2020 to present ---
df_zoom = df[df["Date"] >= "2020-01-01"]

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df_zoom["Date"], df_zoom["Price_EUR_Dozen"], color=line_color, linewidth=line_width)
ax.set_title("Ireland Egg Prices Per Dozen (2020 - Present)", fontsize=16)
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("Price (EUR per dozen)", fontsize=12)
ax.tick_params(axis="both", labelsize=10)
ax.grid(False)  # No gridlines

plt.tight_layout()
plt.savefig("ireland_egg_prices_2020_present.png", dpi=300)
plt.close()

print("✅ Charts saved: ireland_egg_prices_full.png and ireland_egg_prices_2020_present.png")
