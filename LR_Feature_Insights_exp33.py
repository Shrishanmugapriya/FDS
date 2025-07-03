import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("car_data.csv")

# Show available columns
print("\nAvailable features in the dataset:")
print(list(df.columns))

# User selects features to use
features = input("\nEnter features to use (comma-separated, e.g., engine_size,horsepower): ").split(",")
features = [f.strip() for f in features]

# Set input (X) and target (y)
X = df[features]
y = df['price']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Output results
print("\n--- Model Evaluation ---")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Show influential features
coefficients = pd.Series(model.coef_, index=features)
print("\n--- Feature Influence on Price ---")
print(coefficients.sort_values(ascending=False))
