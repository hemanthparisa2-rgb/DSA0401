#Fuel Efficiency
import numpy as np

data = np.genfromtxt("fuel_efficiency.csv", delimiter=",", skip_header=1, dtype=None, encoding="utf-8")

fuel_efficiency = data[:, 1].astype(float)

average_efficiency = np.mean(fuel_efficiency)

percentage_improvement = ((fuel_efficiency[-1] - fuel_efficiency[0]) / fuel_efficiency[0]) * 100

print("Fuel Efficiency:", fuel_efficiency)
print("Average Fuel Efficiency:", average_efficiency)
print("Percentage Improvement: {:.2f}%".format(percentage_improvement))
