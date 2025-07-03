import matplotlib.pyplot as plt

# Sample Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [22, 24, 28, 32, 35, 38, 37, 36, 33, 29, 25, 23]  # °C
rainfall = [15, 20, 40, 60, 110, 200, 250, 220, 150, 80, 40, 20]  # mm

# 1. Line Plot - Monthly Temperature
plt.figure(figsize=(10, 5))
plt.plot(months, temperature, marker='o', linestyle='-', color='orange')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Scatter Plot - Monthly Rainfall
plt.figure(figsize=(10, 5))
plt.scatter(months, rainfall, color='blue')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.tight_layout()
plt.show()
