import pandas as pd

# Sample dataset (you can replace this with your actual DataFrame)
interaction_data = pd.DataFrame({
    'post_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'likes': [12, 5, 10, 5, 12, 7, 5, 10]
})

# Calculate frequency distribution of likes
likes_distribution = interaction_data['likes'].value_counts().sort_index()

# Display the result
print("Frequency distribution of likes among posts:\n")
print(likes_distribution)
