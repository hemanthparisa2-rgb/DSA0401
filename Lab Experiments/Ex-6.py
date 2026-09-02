#Customer purchase
import numpy as np
# Item prices and quantities
import numpy as np

data = np.genfromtxt("customer_purchase.csv", delimiter=",", skip_header=1)

prices = data[:, 1]
quantities = data[:, 2]

discount_rate = 10
tax_rate = 5

subtotal = np.sum(prices * quantities)

discount = (discount_rate / 100) * subtotal

amount_after_discount = subtotal - discount

tax = (tax_rate / 100) * amount_after_discount

total_cost = amount_after_discount + tax

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Tax:", tax)
print("Total Cost:", total_cost)
