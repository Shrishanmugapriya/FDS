import numpy as np

# Example fuel efficiency data in miles per gallon (MPG)
# Each element = efficiency of one car model
fuel_efficiency = np.array([22.5, 25.0, 30.5, 28.0, 35.2])

# Step 1: Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Step 2: Calculate percentage improvement between two models
# Let's compare Model A (index 1) and Model B (index 4)
model_a = fuel_efficiency[1]  # 25.0 MPG
model_b = fuel_efficiency[4]  # 35.2 MPG

# Percentage improvement = ((New - Old) / Old) * 100
percentage_improvement = ((model_b - model_a) / model_a) * 100

# Output
print("Average fuel efficiency of all models: ",average_efficiency,"MPG")
print("Percentage improvement from Model A to Model B: ",percentage_improvement,"%")
