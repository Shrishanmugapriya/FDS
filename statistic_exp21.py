import pandas as pd
import numpy as np
from scipy import stats

# Load data
df = pd.read_csv("rare_elements.csv")
data = df.iloc[:, 0].dropna()  # Get the first column and drop missing values

# User input
sample_size = int(input("Enter sample size: "))
confidence_level = float(input("Enter confidence level (e.g., 0.95): "))
precision = float(input("Enter desired level of precision (margin of error): "))

# Take random sample
sample = np.random.choice(data, size=sample_size, replace=False)
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)

# Calculate confidence interval
alpha = 1 - confidence_level
t_critical = stats.t.ppf(1 - alpha/2, df=sample_size - 1)
margin_of_error = t_critical * (sample_std / np.sqrt(sample_size))

# Check against desired precision
meets_precision = margin_of_error <= precision

# Output results
print("\n--- Results ---")
print(f"Sample Mean: {sample_mean:.4f}")
print(f"Margin of Error: {margin_of_error:.4f}")
print(f"{int(confidence_level * 100)}% Confidence Interval: ({sample_mean - margin_of_error:.4f}, {sample_mean + margin_of_error:.4f})")
print("Desired Precision Met:" , "✅ Yes" if meets_precision else "❌ No")
