#scatter plot of the monthly rainfall data.
import matplotlib.pyplot as plt
# Monthly Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

rainfall = [15, 20, 30, 45, 80, 120, 150, 140, 100, 60, 35, 20]

# Scatter Plot
plt.scatter(months, rainfall, color='red', s=80)
plt.title("Monthly Rainfall")
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.grid(True)

plt.show()

# Program Execution
print("Rainfall Data:", rainfall)
print("Scatter Plot displayed successfully.")
