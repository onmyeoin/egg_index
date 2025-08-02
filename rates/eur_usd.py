import pandas as pd
import requests

# Frankfurter API endpoint: fetch from 1999 to today
url = "https://api.frankfurter.app/1999-01-01..?to=USD&from=EUR"
response = requests.get(url)
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data["rates"]).T  # Transpose dates as rows
df.index = pd.to_datetime(df.index)
df.columns = ["EUR_USD"]

# Convert to monthly average
df_monthly = df.resample("M").mean()

# Save to CSV
df_monthly.to_csv("eur_usd.csv")
print(df_monthly.head())
