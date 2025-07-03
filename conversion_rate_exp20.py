import numpy as np
from scipy import stats

# Simulated conversion rate data (in %)
# Example: 1 = converted, 0 = not converted

# Group A (e.g., 100 users, 30 converted)
group_a = np.random.binomial(1, 0.30, 100)

# Group B (e.g., 100 users, 38 converted)
group_b = np.random.binomial(1, 0.38, 100)

# Calculate means
mean_a = group_a.mean()
mean_b = group_b.mean()

# Perform independent t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)

# Display results
print("A/B Test Results:")
print(f"Mean Conversion Rate - Design A: {mean_a:.2%}")
print(f"Mean Conversion Rate - Design B: {mean_b:.2%}")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Interpret result
alpha = 0.05
if p_value < alpha:
    print("Result: Statistically significant difference in conversion rates (p < 0.05).")
else:
    print("Result: No statistically significant difference (p ≥ 0.05).")
