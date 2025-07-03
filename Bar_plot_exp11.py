import matplotlib.pyplot as plt

# Sample monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [12000, 13500, 15000, 14000, 16000, 17500]

# 1. Line Plot (to visualize trend)
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='blue')
plt.title('Monthly Sales - Line Plot')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Scatter Plot (to visualize actual data points)
plt.figure(figsize=(8, 5))
plt.scatter(months, sales, color='red')
plt.title('Monthly Sales - Scatter Plot')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# 3. Bar Plot (to compare sales month-wise)
plt.figure(figsize=(8, 5))
plt.bar(months, sales, color='green')
plt.title('Monthly Sales - Bar Plot')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()
