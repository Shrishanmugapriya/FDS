import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("retail_transactions.csv")

# Select relevant features for clustering
X = df[['total_spent', 'visit_frequency']]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means Clustering
k = 3  # You can change this or use elbow method to decide
model = KMeans(n_clusters=k, random_state=42)
df['Segment'] = model.fit_predict(X_scaled)

# Display segment info
print("\n--- First 5 Customers with Segments ---")
print(df[['customer_id', 'total_spent', 'visit_frequency', 'Segment']].head())

# Visualize the clusters
plt.figure(figsize=(8, 5))
plt.scatter(df['total_spent'], df['visit_frequency'], c=df['Segment'], cmap='viridis')
plt.title("Customer Segments Based on Spending & Visits")
plt.xlabel("Total Spent")
plt.ylabel("Visit Frequency")
plt.grid(True)
plt.colorbar(label='Segment')
plt.show()
