#plot Monthly sales
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("monthly_sales.csv")

months = data["Month"]
sales = data["Sales"]

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)
plt.show()
