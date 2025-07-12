import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import STL                                                                                                                                                                                             
# Generate synthetic time series data
np.random.seed(42)
time = np.arange(1, 101)
trend = 0.05 * time  # Linear trend
seasonality = 2 * np.sin(2 * np.pi * time / 12)  # Seasonal component (12-period cycle)
noise = np.random.normal(scale=0.5, size=len(time))  # Random noise

series = trend + seasonality + noise  # Combined series

# Apply STL decomposition
stl = STL(series, period=12)  # Assuming a seasonal cycle of 12
result = stl.fit()

# Plot decomposition results
fig, axes = plt.subplots(4, 1, figsize=(8, 6), sharex=True)

axes[0].plot(time, series, label="Original Series", color='black')
axes[0].set_title("Original Time Series")
axes[0].legend()

axes[1].plot(time, result.trend, label="Trend Component", color='blue')
axes[1].set_title("Trend")
axes[1].legend()

axes[2].plot(time, result.seasonal, label="Seasonal Component", color='green')
axes[2].set_title("Seasonality")
axes[2].legend()

axes[3].plot(time, result.resid, label="Residuals", color='red')
axes[3].set_title("Residuals")
axes[3].legend()

plt.tight_layout()
plt.show()