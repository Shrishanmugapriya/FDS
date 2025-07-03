import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("used_car_data.csv")

# Encode categorical columns
label_encoders = {}
for col in ['brand', 'engine_type']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Separate features and target
X = df.drop("price", axis=1)
y = df["price"]

# Train CART model
model = DecisionTreeRegressor(random_state=42)
model.fit(X, y)

# Get user input
print("\nEnter details for the car you want to sell:")
mileage = float(input("Mileage (in km): "))
age = int(input("Age (in years): "))
brand = input("Brand (e.g., Toyota, Hyundai): ")
engine_type = input("Engine Type (e.g., Petrol, Diesel): ")

# Encode user input
brand_encoded = label_encoders['brand'].transform([brand])[0]
engine_encoded = label_encoders['engine_type'].transform([engine_type])[0]

# Prepare input
new_car = [[mileage, age, brand_encoded, engine_encoded]]

# Predict price
predicted_price = model.predict(new_car)[0]

# Output result
print("\n--- Prediction Result ---")
print(f"Estimated Price: ₹{predicted_price:,.2f}")

# Display decision path
print("\n--- Decision Tree Path ---")
feature_names = list(X.columns)
tree_rules = export_text(model, feature_names=feature_names)
print(tree_rules)
