import pandas as pd

# Load dataset
df = pd.read_csv("city_temperatures.csv")  # Format: city,date,temp

# Group by city
grouped = df.groupby('city')['temp']

mean_temp = grouped.mean()
std_temp = grouped.std()
range_temp = grouped.max() - grouped.min()

# Insights
most_variable = range_temp.idxmax()
most_consistent = std_temp.idxmin()

print("Mean Temperature:\n", mean_temp)
print("\nStandard Deviation:\n", std_temp)
print(f"\nCity with highest temperature range: {most_variable}")
print(f"City with most consistent temperature: {most_consistent}")
