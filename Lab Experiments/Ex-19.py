import pandas as pd

# Input number of reviews
n = int(input("Enter the number of customer reviews: "))

reviews = []

# Input reviews
for i in range(n):
    review = input(f"Enter review {i+1}: ")
    reviews.append(review)

# Create DataFrame
df = pd.DataFrame({"Review": reviews})

# Combine all reviews into one string
text = " ".join(df["Review"]).lower()

# Remove punctuation
for ch in ".,!?;:\"'()[]{}":
    text = text.replace(ch, "")

# Split into words
words = text.split()

# Calculate frequency distribution
frequency = pd.Series(words).value_counts()

# Display result
print("\nFrequency Distribution of Words:")
print(frequency)
