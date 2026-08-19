import pandas as pd

# Create DataFrame
data = {
    "Customer": ["A", "B", "C", "D", "E", "F", "G"],
    "Age": [25, 30, 25, 40, 30, 25, 35]
}

df = pd.DataFrame(data)

# Frequency distribution of ages
frequency = df["Age"].value_counts().sort_index()

# Display result
print("Frequency Distribution of Customer Ages:")
print(frequency)
