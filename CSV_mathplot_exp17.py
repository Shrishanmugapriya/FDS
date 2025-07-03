import pandas as pd
import string
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
import nltk

# Download stopwords (only needed once)
nltk.download('stopwords')

# Set of English stopwords
stop_words = set(stopwords.words('english'))

# Load dataset
df = pd.read_csv("data.csv")  # Ensure 'data.csv' is in the same folder

# Combine all feedback into a single text string
text = ' '.join(df['feedback'].dropna()).lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Split into words
words = text.split()

# Remove stopwords
filtered_words = [word for word in words if word not in stop_words]

# Count word frequencies
word_freq = Counter(filtered_words)

# Ask user for N
N = 5

# Get top N most common words
most_common_words = word_freq.most_common(N)

# Display the top N frequent words
print(f"\nTop {N} most frequent words:\n")
for word, freq in most_common_words:
    print(f"{word}: {freq}")

# Plot the frequencies
words, frequencies = zip(*most_common_words)
plt.figure(figsize=(10, 6))
plt.bar(words, frequencies, color='skyblue')
plt.title(f'Top {N} Most Frequent Words')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
