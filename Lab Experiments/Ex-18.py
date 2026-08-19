import pandas as pd

# Input: Number of posts
n = int(input("Enter the number of posts: "))

likes = []

# Input likes for each post
for i in range(n):
    like = int(input(f"Enter likes for post {i+1}: "))
    likes.append(like)

# Create DataFrame
df = pd.DataFrame({"Likes": likes})

# Frequency distribution
frequency = df["Likes"].value_counts().sort_index()

# Display result
print("\nFrequency Distribution of Likes:")
print(frequency)
