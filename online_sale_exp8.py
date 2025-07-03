import pandas as pd

# Sample sales data
data = {
    'product_name': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse', 'Monitor', 'Monitor', 'Mouse', 'Keyboard'],
    'quantity_sold': [5, 10, 3, 4, 8, 6, 7, 2, 5]
}

# Create DataFrame
sales_data = pd.DataFrame(data)

# Group by product and sum the quantity sold
product_sales = sales_data.groupby('product_name')['quantity_sold'].sum()

# Sort products by total quantity sold in descending order
top_5_products = product_sales.sort_values(ascending=False).head(5)

# Output
print("Top 5 best-selling products:")
print(top_5_products)
