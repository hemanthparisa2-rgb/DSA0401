import pandas as pd
import matplotlib.pyplot as plt
import string
from collections import Counter

# Input number of feedbacks
n = int(input("Enter the number of customer feedbacks: "))

feedback = []

# Input feedback
for i in range(n):
    text = input(f"Enter feedback {i+1}: ")
    feedback.append(text)

# Create DataFrame
df = pd.DataFrame({"feedback": feedback})

# Number of top frequent words
N = int(input("Enter the value of N: "))

# Combine all feedback
text = " ".join(df["feedback"]).lower()

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Stop words
stop_words = {"the","and","is","in","to","of","a","an","on","for","with","at","by","from","this","that","it","as","are","was","be","or","but","not"}

# Remove stop words
words = [word for word in text.split() if word not in stop_words]

# Frequency distribution
freq = Counter(words)

# Top N words
top_words = freq.most_common(N)

# Display result
print("\nTop", N, "Most Frequent Words:")
for word, count in top_words:
    print(word, ":", count)

# Bar graph
x = [item[0] for item in top_words]
y = [item[1] for item in top_words]

plt.bar(x, y)
plt.title("Top Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()
