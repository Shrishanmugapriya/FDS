import pandas as pd

# Load stock data
df = pd.read_csv("stock_prices.csv")  # Must have 'Date' and 'Close' columns

# Calculate statistics
mean_price = df['Close'].mean()
std_dev = df['Close'].std()
price_range = df['Close'].max() - df['Close'].min()

# Output
print(f"Average Closing Price: ₹{mean_price:.2f}")
print(f"Standard Deviation: ₹{std_dev:.2f}")
print(f"Price Range: ₹{price_range:.2f}")
