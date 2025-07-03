import pandas as pd

# Sample data
data = {
    'customer_id': [101, 102, 101, 103, 102, 101],
    'order_date': ['2023-01-05', '2023-01-10', '2023-02-15', '2023-03-01', '2023-03-12', '2023-04-01'],
    'product_name': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse', 'Monitor'],
    'order_quantity': [1, 2, 1, 1, 3, 2]
}

# Create DataFrame
order_data = pd.DataFrame(data)

# Convert 'order_date' to datetime format
order_data['order_date'] = pd.to_datetime(order_data['order_date'])

# 1. Total number of orders made by each customer
orders_per_customer = order_data['customer_id'].value_counts()

# 2. Average order quantity for each product
avg_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()

# 3. Earliest and latest order dates
earliest_date = order_data['order_date'].min()
latest_date = order_data['order_date'].max()

# Output
print("1. Total number of orders by each customer:")
print(orders_per_customer)

print("\n2. Average order quantity for each product:")
print(avg_quantity_per_product)

print("\n3. Earliest order date:", earliest_date.date())
print("   Latest order date:", latest_date.date())
