# Take text input from the user
text = input("Enter the text: ").lower()

# Remove punctuation
for ch in ".,!?;:\"'()[]{}":
    text = text.replace(ch, "")

# Split into words
words = text.split()

# Count word frequencies
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Display frequency distribution
print("\nWord Frequency Distribution:")
for word, count in freq.items():
    print(word, ":", count)
