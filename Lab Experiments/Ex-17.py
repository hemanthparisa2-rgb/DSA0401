#frequency distribution of the ages of the customers
import pandas as pd

df = pd.read_csv("customer_ages.csv")

frequency = df["Age"].value_counts().sort_index()

print("Frequency Distribution of Customer Ages:")
print(frequency)
