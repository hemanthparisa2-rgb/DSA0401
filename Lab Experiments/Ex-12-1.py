#line plot of the monthly temperature data.
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("temperature.csv")

months = data["Month"]
temperature = data["Temperature"]

plt.plot(months, temperature, marker="o")

plt.title("Monthly Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.show()

print("Temperature Data:", list(temperature))
print("Line Plot displayed successfully.")
