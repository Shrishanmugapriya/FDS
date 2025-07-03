from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
species = iris.target_names

# Train the Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X, y)

# Get user input
print("\nEnter measurements for the new Iris flower:")
sepal_length = float(input("Sepal length (cm): "))
sepal_width = float(input("Sepal width (cm): "))
petal_length = float(input("Petal length (cm): "))
petal_width = float(input("Petal width (cm): "))

# Create input array for prediction
new_flower = [[sepal_length, sepal_width, petal_length, petal_width]]

# Predict species
prediction = model.predict(new_flower)[0]
predicted_species = species[prediction]

# Output
print(f"\n--- Prediction Result ---")
print(f"The predicted species is: 🌼 **{predicted_species.capitalize()}**")
