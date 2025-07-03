import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    'Name': ['Player A', 'Player B', 'Player C', 'Player D', 'Player E', 'Player F', 'Player G'],
    'Age': [22, 30, 28, 24, 35, 27, 31],
    'Position': ['Forward', 'Midfielder', 'Forward', 'Defender', 'Goalkeeper', 'Midfielder', 'Defender'],
    'Goals': [10, 5, 8, 2, 0, 6, 3],
    'Salary': [100000, 120000, 95000, 80000, 110000, 102000, 85000]
}
df = pd.DataFrame(data)
df.to_csv("soccer_players.csv", index=False)

# Read from CSV
df = pd.read_csv("soccer_players.csv")

# Top scorers & top earners
print("\nTop 5 Goal Scorers:")
print(df.nlargest(5, 'Goals')[['Name', 'Goals']])

print("\nTop 5 Highest Paid Players:")
print(df.nlargest(5, 'Salary')[['Name', 'Salary']])

# Average age and players above average
avg_age = df['Age'].mean()
print(f"\nAverage Age: {avg_age:.1f}")
print("\nPlayers above average age:")
print(df[df['Age'] > avg_age][['Name', 'Age']])

# Bar chart of positions
df['Position'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Distribution of Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.grid(True)
plt.show()
