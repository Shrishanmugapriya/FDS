import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("housing_data.csv")

# Features and target
X = df.drop("price", axis=1)
y = df["price"]

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Get user input for a new house
print("\nEnter features of the new house:")
new_area = float(input("Area (in sq ft): "))
new_bedrooms = int(input("Number of bedrooms: "))
new_bathrooms = int(input("Number of bathrooms: "))

# Prepare input and predict
new_house = [[new_area, new_bedrooms, new_bathrooms]]
predicted_price = model.predict(new_house)[0]

# Output result
print("\n--- Prediction Result ---")
print(f"Estimated House Price: ₹{predicted_price:,.2f}")
