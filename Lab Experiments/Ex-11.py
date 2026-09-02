#plot to show sales dataset
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_dataset.csv")

months = data["Month"]
sales = data["Sales"]

plt.bar(months, sales)

plt.title("Monthly Sales Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()
