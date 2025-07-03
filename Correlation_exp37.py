import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("study_scores.csv")  # Columns: 'StudyTime', 'Score'

# Correlation
correlation = df['StudyTime'].corr(df['Score'])
print(f"Correlation: {correlation:.2f}")

# Scatter plot + regression
sns.lmplot(x='StudyTime', y='Score', data=df)
plt.title("Study Time vs Exam Score")
plt.grid(True)
plt.show()
