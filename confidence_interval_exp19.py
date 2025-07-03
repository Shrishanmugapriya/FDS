import numpy as np
import scipy.stats as stats

# Simulated reduction data (in mmHg)
np.random.seed(42)  # for reproducibility

# Sample size
n_drug = 25
n_placebo = 25

# Simulated reductions (mean = 12 for drug, 5 for placebo, std = 4)
drug_group = np.random.normal(loc=12, scale=4, size=n_drug)
placebo_group = np.random.normal(loc=5, scale=4, size=n_placebo)

# Function to calculate 95% CI
def confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    sem = stats.sem(data)
    margin = stats.t.ppf((1 + confidence) / 2.0, n-1) * sem
    return mean - margin, mean + margin, mean

# Calculate 95% CI for both groups
drug_ci_lower, drug_ci_upper, drug_mean = confidence_interval(drug_group)
placebo_ci_lower, placebo_ci_upper, placebo_mean = confidence_interval(placebo_group)

# Display results
print("95% Confidence Interval Results:\n")
print(f"New Drug Group: Mean = {drug_mean:.2f} mmHg")
print(f"95% CI = ({drug_ci_lower:.2f}, {drug_ci_upper:.2f}) mmHg\n")

print(f"Placebo Group: Mean = {placebo_mean:.2f} mmHg")
print(f"95% CI = ({placebo_ci_lower:.2f}, {placebo_ci_upper:.2f}) mmHg")
