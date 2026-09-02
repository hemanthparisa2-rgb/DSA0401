#E-Commerce
import pandas as pd

order_data = pd.read_csv("ecommerce.csv")

order_data['Order_Date'] = pd.to_datetime(order_data['Order_Date'])

orders_per_customer = order_data.groupby('Customer_ID').size()
print("Total Orders by Each Customer:")
print(orders_per_customer)

avg_quantity = order_data.groupby('Product_Name')['Order_Quantity'].mean()
print("\nAverage Order Quantity for Each Product:")
print(avg_quantity)

earliest_date = order_data['Order_Date'].min()
latest_date = order_data['Order_Date'].max()

print("\nEarliest Order Date:", earliest_date)
print("Latest Order Date:", latest_date)
