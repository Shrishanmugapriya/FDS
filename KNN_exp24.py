import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("patient_data.csv")

# Split into features (X) and target (y)
X = df.drop('condition', axis=1)
y = df['condition']

# Scale the data (important for KNN)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split (not needed for final prediction, but good practice)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Get input from user
print("\nEnter the symptom features for the new patient (0 or 1 values):")
input_features = []
for column in X.columns:
    value = float(input(f"{column}: "))
    input_features.append(value)

# Convert to scaled format
input_scaled = scaler.transform([input_features])

# Get value of k
k = int(input("Enter the number of neighbors (k): "))

# Train KNN
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Predict for new patient
prediction = knn.predict(input_scaled)[0]

# Output result
print("\n--- Prediction Result ---")
print("Prediction:", "Has the condition" if prediction == 1 else "Does not have the condition")
