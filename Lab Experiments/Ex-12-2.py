#scatter plot of the monthly rainfall data.
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("rainfall.csv")

months = data["Month"]
rainfall = data["Rainfall"]

plt.scatter(months, rainfall, s=80)

plt.title("Monthly Rainfall")
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.grid(True)

plt.show()

print("Rainfall Data:", list(rainfall))
print("Scatter Plot displayed successfully.")
