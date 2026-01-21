import numpy as np
'''
Create a 1D array representing 365 days of random “daily salesˮ.

Compute rolling 7-day mean and rolling 30-day mean using NumPy (no 
pandas).
Detect days where sales are > (rolling_30_mean + 2*rolling_30_std).
'''
# 1. Generate 365 days of random sales
np.random.seed(42)
sales = np.random.uniform(100, 1000, size=365)

# 2. Function to calculate rolling stats manually
def get_rolling_stats(data, window):
    means = []
    stds = []
    # We can only start calculating once we have 'window' number of days
    for i in range(window, len(data) + 1):
        segment = data[i-window:i]
        means.append(np.mean(segment))
        stds.append(np.std(segment))
    return np.array(means), np.array(stds)

# Compute 7-day and 30-day metrics
mean_7d, _ = get_rolling_stats(sales, 7)
mean_30d, std_30d = get_rolling_stats(sales, 30)

# 3. Detect anomalies
# The 30-day rolling window starts providing results at index 29 (the 30th day)
sales_aligned = sales[29:] 
threshold = mean_30d + (2 * std_30d)
anomaly_indices = np.where(sales_aligned > threshold)[0]

# Adjust indices to match the original 365-day array
original_days = anomaly_indices + 29

print(f"Rolling 7-day means: {mean_7d}")
print(f"Detected {len(original_days)} anomaly days: {original_days}")
