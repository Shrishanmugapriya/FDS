import pandas as pd

# Sample property data
data = {
    'property_id': [101, 102, 103, 104, 105],
    'location': ['City A', 'City B', 'City A', 'City C', 'City B'],
    'bedrooms': [3, 5, 4, 2, 6],
    'area_sqft': [1200, 2500, 1800, 900, 3000],
    'listing_price': [350000, 550000, 420000, 280000, 600000]
}

# Create DataFrame
property_data = pd.DataFrame(data)

# 1. Average listing price of properties in each location
avg_price_by_location = property_data.groupby('location')['listing_price'].mean()

# 2. Number of properties with more than 4 bedrooms
more_than_4_bedrooms = property_data[property_data['bedrooms'] > 4].shape[0]

# 3. Property with the largest area
largest_area_property = property_data.loc[property_data['area_sqft'].idxmax()]

# Output
print("1. Average listing price by location:")
print(avg_price_by_location)

print(f"\n2. Number of properties with more than 4 bedrooms: {more_than_4_bedrooms}")

print("\n3. Property with the largest area:")
print(largest_area_property)
