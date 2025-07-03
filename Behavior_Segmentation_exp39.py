import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("ecommerce_transactions.csv")  # Columns: customer_id, total_spent, items_purchased

# Select features
X = df[['total_spent', 'items_purchased']]
X_scaled = StandardScaler().fit_transform(X)

# Apply KMeans
model = KMeans(n_clusters=3, random_state=0)
df['Segment'] = model.fit_predict(X_scaled)

# Scatter plot
plt.scatter(df['total_spent'], df['items_purchased'], c=df['Segment'], cmap='viridis')
plt.xlabel("Total Spent")
plt.ylabel("Items Purchased")
plt.title("Customer Segmentation")
plt.grid(True)
plt.show()
