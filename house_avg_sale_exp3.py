import numpy as np

# Example house data: [bedrooms, square footage, sale price]
house_data = np.array([
    [3, 1500, 250000],
    [5, 2200, 400000],
    [4, 1800, 320000],
    [6, 3000, 550000],
    [2, 1200, 200000]
])

# Step 1: Filter houses with more than 4 bedrooms
more_than_4_bedrooms = house_data[house_data[:, 0] > 4]

# Step 2: Get the sale prices of those houses (column 2)
sale_prices = more_than_4_bedrooms[:, 2]

# Step 3: Calculate average sale price
average_price = np.mean(sale_prices)

# Output
print("Average sale price of houses with more than 4 bedrooms: ₹",average_price)
