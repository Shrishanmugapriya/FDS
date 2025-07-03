import numpy as np

# Example 3x3 matrix
# Each row represents a different product
# Each column could represent sales on different weeks or different transactions
sales_data = np.array([
    [120.50, 130.00, 125.75],
    [99.99, 105.25, 110.00],
    [150.00, 145.50, 155.25]
])

# Step: Calculate average price of all products sold
average_price = np.mean(sales_data)

# Output
print("Average price of all products sold in the past month: ₹",average_price)