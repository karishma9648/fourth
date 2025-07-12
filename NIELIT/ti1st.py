import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.linear_model import LinearRegression

# Generate synthetic time series data
np.random.seed(42)
time = np.arange(100)
trend = time * 0.5  # Linear trend
seasonality = 10 * np.sin(2 * np.pi * time / 12)  # Seasonal component
noise = np.random.normal(0, 2, size=100)  # Random noise
data = trend + seasonality + noise

# Create DataFrame
df = pd.DataFrame({"Time": time, "Value": data})
df.set_index("Time", inplace=True)

# Function to check stationarity using ADF test
def check_stationarity(timeseries, title=""):
    result = adfuller(timeseries)
    print(f"ADF Test for {title}")
    print("Test Statistic:", result[0])
    print("P-Value:", result[1])
    print("Critical Values:", result[4])
    print("Stationary" if result[1] < 0.05 else "Not Stationary", "\n")

# 1. Original Data - Check Stationarity
check_stationarity(df["Value"], "Original Data")
plt.figure(figsize=(12, 6))
plt.plot(df["Value"], label="Original Data")
plt.legend()
plt.title("Original Time Series")
plt.show()

# 2. Differencing
df["Differenced"] = df["Value"].diff().dropna()
check_stationarity(df["Differenced"].dropna(), "Differenced Data")

plt.figure(figsize=(12, 6))
plt.plot(df["Differenced"], label="Differenced Data", color='orange')
plt.legend()
plt.title("Differenced Time Series")
plt.show()

# 3. Detrending using Linear Regression
X = time.reshape(-1, 1)
y = df["Value"].values.reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)
trend_estimate = model.predict(X).flatten()
df["Detrended"] = df["Value"] - trend_estimate

check_stationarity(df["Detrended"], "Detrended Data")

plt.figure(figsize=(12, 6))
plt.plot(df["Detrended"], label="Detrended Data", color='green')
plt.legend()
plt.title("Detrended Time Series")
plt.show()

# 4. Deseasonalizing using Seasonal Decomposition
decomposition = seasonal_decompose(df["Value"], period=12, model="additive")
df["Deseasonalized"] = df["Value"] - decomposition.seasonal

check_stationarity(df["Deseasonalized"], "Deseasonalized Data")

plt.figure(figsize=(12, 6))
plt.plot(df["Deseasonalized"], label="Deseasonalized Data", color='red')
plt.legend()
plt.title("Deseasonalized Time Series")
plt.show()