import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Sample dataset (Age and %Fat for 18 adults)
data = {
    'Age': [23, 45, 34, 50, 29, 31, 40, 38, 49, 35, 28, 60, 55, 36, 42, 30, 33, 41],
    '%Fat': [14.2, 25.4, 18.9, 28.5, 17.3, 16.8, 22.1, 21.5, 26.7, 19.4, 15.7, 30.1, 29.4, 20.6, 23.8, 16.2, 18.3, 22.9]
}

# Create DataFrame
df = pd.DataFrame(data)

# 1. Mean, Median, Std Deviation
print("Summary Statistics:\n")
print("Age:")
print(f"Mean: {df['Age'].mean():.2f}")
print(f"Median: {df['Age'].median():.2f}")
print(f"Standard Deviation: {df['Age'].std():.2f}\n")

print("%Fat:")
print(f"Mean: {df['%Fat'].mean():.2f}")
print(f"Median: {df['%Fat'].median():.2f}")
print(f"Standard Deviation: {df['%Fat'].std():.2f}")

# 2. Boxplots
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['Age'], color='skyblue')
plt.title('Boxplot of Age')

plt.subplot(1, 2, 2)
sns.boxplot(y=df['%Fat'], color='lightgreen')
plt.title('Boxplot of %Fat')
plt.tight_layout()
plt.show()

# 3. Scatter Plot
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Age', y='%Fat', data=df)
plt.title('Scatter Plot: Age vs %Fat')
plt.xlabel('Age')
plt.ylabel('%Fat')
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Q-Q Plot
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title("Q-Q Plot for Age")

plt.subplot(1, 2, 2)
stats.probplot(df['%Fat'], dist="norm", plot=plt)
plt.title("Q-Q Plot for %Fat")

plt.tight_layout()
plt.show()
 