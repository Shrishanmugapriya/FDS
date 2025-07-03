import matplotlib.pyplot as plt

# Sample monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [25000, 28000, 30000, 22000, 26000, 31000, 
         33000, 34000, 29000, 37000, 36000, 39000]

# 1. Line Plot of Monthly Sales
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='blue')
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales (in ₹)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar Plot of Monthly Sales
plt.figure(figsize=(10, 5))
plt.bar(months, sales, color='green')
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales (in ₹)")
plt.tight_layout()
plt.show()
