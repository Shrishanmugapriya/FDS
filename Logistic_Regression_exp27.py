import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("customer_data.csv")

# Features and target
X = df.drop("churn", axis=1)
y = df["churn"]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split (optional but good for model evaluation)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Get user input for new customer
print("\nEnter features for the new customer:")
input_features = []
for col in X.columns:
    val = float(input(f"{col}: "))
    input_features.append(val)

# Scale and reshape input
input_scaled = scaler.transform([input_features])

# Predict
prediction = model.predict(input_scaled)[0]
probability = model.predict_proba(input_scaled)[0][1]  # Probability of churn (class 1)

# Output
print("\n--- Prediction Result ---")
print("Prediction:", "Customer likely to churn" if prediction == 1 else "Customer likely to stay")
print(f"Probability of churn: {probability:.2%}")
