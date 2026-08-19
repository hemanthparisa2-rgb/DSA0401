import numpy as np

# Item prices and quantities
prices = np.array([50, 100, 30])
quantities = np.array([2, 1, 4])

# Discount and tax rates (in percentage)
discount_rate = 10
tax_rate = 5

# Calculate subtotal
subtotal = np.sum(prices * quantities)

# Calculate discount
discount = (discount_rate / 100) * subtotal

# Price after discount
amount_after_discount = subtotal - discount

# Calculate tax
tax = (tax_rate / 100) * amount_after_discount

# Final total cost
total_cost = amount_after_discount + tax

# Display results
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Tax:", tax)
print("Total Cost:", total_cost)
