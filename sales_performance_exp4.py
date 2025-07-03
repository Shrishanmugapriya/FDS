import numpy as np

# Example sales data for 4 quarters
# Each element represents sales in one quarter
sales_data = np.array([150000, 180000, 210000, 250000])

# Step 1: Calculate total sales for the year
total_sales = np.sum(sales_data)

# Step 2: Calculate percentage increase from Q1 to Q4
first_quarter = sales_data[0]
fourth_quarter = sales_data[3]
percentage_increase = ((fourth_quarter - first_quarter) / first_quarter) * 100

# Output
print("Total sales for the year: ₹",total_sales)
print("Percentage increase from Q1 to Q4: ",percentage_increase,"%")
