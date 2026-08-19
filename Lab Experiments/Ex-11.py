#plot to show sales dataset
import matplotlib.pyplot as plt

# Monthly data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 170, 210, 250]

# Bar Plot
plt.bar(months, sales, color='green')

plt.title("Monthly Sales Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()
