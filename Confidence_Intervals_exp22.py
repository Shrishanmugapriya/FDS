import pandas as pd
import numpy as np
from scipy import stats

# Load the data
df = pd.read_csv("customer_reviews.csv")

# Ensure we only take the 'rating' column and remove missing values
ratings = df['rating'].dropna()

# Sample statistics
sample_size = len(ratings)
sample_mean = np.mean(ratings)
sample_std = np.std(ratings, ddof=1)

# Confidence level
confidence_level = 0.95
alpha = 1 - confidence_level

# t-critical value for the confidence interval
t_critical = stats.t.ppf(1 - alpha/2, df=sample_size - 1)

# Margin of error
margin_of_error = t_critical * (sample_std / np.sqrt(sample_size))

# Confidence interval
lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

# Output
print("\n--- Customer Review Analysis ---")
print(f"Sample Size: {sample_size}")
print(f"Average Rating: {sample_mean:.2f}")
print(f"{int(confidence_level*100)}% Confidence Interval: ({lower_bound:.2f}, {upper_bound:.2f})")
