import pandas as pd
from collections import Counter

# Sample sales_data for demonstration (remove this if you already have your own DataFrame)
sales_data = pd.DataFrame({
    'customer_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'age': [25, 30, 22, 30, 28, 25, 22, 30],
    'purchase_date': [
        '2025-06-03', '2025-06-15', '2025-06-20', '2025-06-10',
        '2025-06-12', '2025-06-30', '2025-05-28', '2025-06-08'
    ]
})

# Convert purchase_date to datetime
sales_data['purchase_date'] = pd.to_datetime(sales_data['purchase_date'])

# Filter for purchases made in the past month
last_month = pd.Timestamp.today() - pd.DateOffset(months=1)
recent_sales = sales_data[sales_data['purchase_date'] >= last_month]

# Frequency distribution of customer ages
age_distribution = recent_sales['age'].value_counts().sort_index()

# Display the result
print("Frequency distribution of customer ages (past month):\n")
print(age_distribution)