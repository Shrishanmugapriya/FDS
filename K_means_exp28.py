import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("customer_data.csv")

# Features only (no labels needed for clustering)
X = df

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train KMeans model
k = 3  # Number of clusters (you can adjust this)
model = KMeans(n_clusters=k, random_state=42)
model.fit(X_scaled)

# User input for new customer
print("\nEnter shopping-related features for the new customer:")
input_features = []
for col in df.columns:
    val = float(input(f"{col}: "))
    input_features.append(val)

# Scale and predict cluster for the new customer
input_scaled = scaler.transform([input_features])
cluster = model.predict(input_scaled)[0]

# Output
print("\n--- Customer Segmentation Result ---")
print(f"The new customer belongs to Segment (Cluster): {cluster}")
