import pandas as pd
import string
from collections import Counter

# Sample data (if reading from CSV, use pd.read_csv('your_file.csv'))
data = {
    'review': [
        "Great product! Very useful and easy to use.",
        "Not satisfied. Product broke after a week.",
        "Excellent quality and fantastic support.",
        "Product is okay, but shipping was delayed.",
        "Loved it! Would definitely recommend this product."
    ]
}
reviews_df = pd.DataFrame(data)

# Combine all reviews into one text string
all_reviews = ' '.join(reviews_df['review'])

# Convert to lowercase and remove punctuation
all_reviews = all_reviews.lower()
all_reviews = all_reviews.translate(str.maketrans('', '', string.punctuation))

# Split into words
words = all_reviews.split()

# Count word frequency
word_freq = Counter(words)

# Display results
print("Frequency Distribution of Words in Customer Reviews:\n")
for word, freq in word_freq.most_common():
    print(f"{word}: {freq}")
