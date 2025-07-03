import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv("real_estate_data.csv")

# Display available columns
print("\nAvailable features in the dataset:")
print(list(df.columns))

# User selects a feature for prediction
feature = input("\nEnter the feature to use for predicting house price (e.g., house_size): ").strip()

# Extract selected feature and target variable
X = df[[feature]]
y = df['price']

# Bivariate Analysis
print(f"\nCorrelation between {feature} and price: {X[feature].corr(y):.2f}")
plt.scatter(X, y, color='blue')
plt.xlabel(feature)
plt.ylabel("House Price")
plt.title(f"{feature} vs Price")
plt.grid(True)
plt.show()

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Output performance
print("\n--- Model Evaluation ---")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Optional: Plot regression line
plt.scatter(X_test, y_test, color='gray', label="Actual")
plt.plot(X_test, y_pred, color='red', linewidth=2, label="Predicted")
plt.xlabel(feature)
plt.ylabel("House Price")
plt.title(f"Linear Regression: {feature} vs Price")
plt.legend()
plt.grid(True)
plt.show()
