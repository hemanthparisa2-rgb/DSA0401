#plot for sales of product
import matplotlib.pyplot as plt
# Monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 30000, 28000, 35000, 40000, 45000]

# Create line plot
plt.plot(months, sales, marker='o')

# Add title and labels
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales")

# Display grid
plt.grid(True)

# Show plot
plt.show()
