#Fuel Efficiency
import numpy as np

# Fuel efficiency of different car models (in miles per gallon)
fuel_efficiency = np.array([20, 25, 30, 35])

# Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Calculate percentage improvement from Model 1 to Model 4
percentage_improvement = ((fuel_efficiency[3] - fuel_efficiency[0]) / fuel_efficiency[0]) * 100

# Display results
print("Fuel Efficiency:", fuel_efficiency)
print("Average Fuel Efficiency:", average_efficiency)
print("Percentage Improvement: {:.2f}%".format(percentage_improvement))
