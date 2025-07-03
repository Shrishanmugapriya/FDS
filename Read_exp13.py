import string
from collections import Counter

# Step 1: Read the file
with open("sample_text.txt", "r") as file:
    text = file.read()

# Step 2: Preprocess the text
text = text.lower()  # convert to lowercase
text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
words = text.split()  # tokenize by whitespace

# Step 3: Count word frequencies
word_freq = Counter(words)

# Step 4: Display the frequency distribution
print("Word Frequency Distribution:\n")
for word, freq in word_freq.most_common():
    print(f"{word}: {freq}")
