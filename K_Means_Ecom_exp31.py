import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv("ecommerce_customers.csv")

# Optional: view column names
print("Columns in dataset:", list(df.columns))

# Select features for clustering
X = df[['age', 'annual_income', 'spending_score', 'visit_frequency']]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Choose number of clusters (k)
k = 4  # You can adjust this based on your needs
model = KMeans(n_clusters=k, random_state=42)
df['Segment'] = model.fit_predict(X_scaled)

# Output the cluster labels
print("\n--- Customer Segments Assigned ---")
print(df[['age', 'annual_income', 'spending_score', 'visit_frequency', 'Segment']].head())

# Visualize using 2D plot (choose any 2 features)
plt.figure(figsize=(8, 5))
plt.scatter(df['annual_income'], df['spending_score'], c=df['Segment'], cmap='viridis')
plt.title("Customer Segmentation (Income vs Spending Score)")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.grid(True)
plt.colorbar(label="Segment")
plt.show()
