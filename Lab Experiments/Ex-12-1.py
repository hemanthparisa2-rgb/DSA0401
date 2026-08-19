import matplotlib.pyplot as plt

# Monthly Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

temperature = [22, 24, 28, 32, 35, 33, 30, 29, 28, 27, 25, 23]

# Line Plot
plt.plot(months, temperature, marker='o', color='blue')
plt.title("Monthly Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.show()

# Program Execution
print("Temperature Data:", temperature)
print("Line Plot displayed successfully.")
