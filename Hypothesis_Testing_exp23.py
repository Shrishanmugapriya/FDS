import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load data
df = pd.read_csv("clinical_trial.csv")

# Split data into control and treatment groups
control = df[df['group'] == 'control']['effectiveness']
treatment = df[df['group'] == 'treatment']['effectiveness']

# Hypothesis test (two-sample t-test)
t_stat, p_value = stats.ttest_ind(treatment, control)

# Print test results
print("\n--- Hypothesis Test Result ---")
print(f"Control Mean: {control.mean():.2f}")
print(f"Treatment Mean: {treatment.mean():.2f}")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

# Interpret the p-value
if p_value < 0.05:
    print("Result: Statistically significant difference (p < 0.05)")
else:
    print("Result: No statistically significant difference (p ≥ 0.05)")

# Visualization
plt.figure(figsize=(8, 5))
plt.boxplot([control, treatment], labels=['Control', 'Treatment'])
plt.title(f"Effectiveness Comparison\np-value = {p_value:.4f}")
plt.ylabel("Effectiveness Score")
plt.grid(True)
plt.show()
