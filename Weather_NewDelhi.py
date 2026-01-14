import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# API REQUEST (Open-Meteo)
# -----------------------------
url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 28.6139,          # New Delhi, India
    "longitude": 77.2090,
    "hourly": "temperature_2m",
    "timezone": "Asia/Kolkata"
}

response = requests.get(url, params=params)
data = response.json()

# -----------------------------
# DATA PROCESSING
# -----------------------------
df = pd.DataFrame({
    "Time": pd.to_datetime(data["hourly"]["time"]),
    "Temperature (°C)": data["hourly"]["temperature_2m"]
})

# Optional: Filter only next 24 hours
df_24 = df.head(24)

# -----------------------------
# MATPLOTLIB VISUALIZATION
# -----------------------------
plt.figure(figsize=(12, 6))
plt.plot(df_24["Time"], df_24["Temperature (°C)"], marker="o", color="blue")
plt.title("Hourly Temperature Change in New Delhi (Next 24 Hours)")
plt.xlabel("Time (Hourly)")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------
# SEABORN VISUALIZATION
# -----------------------------
sns.set(style="whitegrid")

plt.figure(figsize=(12, 6))
sns.lineplot(
    data=df_24,
    x="Time",
    y="Temperature (°C)",
    marker="o",
    color="red"
)
plt.title("Hourly Temperature Change in New Delhi (Next 24 Hours)")
plt.xlabel("Time (Hourly)")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
