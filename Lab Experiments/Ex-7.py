import pandas as pd

# Sample DataFrame
order_data = pd.DataFrame({
    'Customer_ID': [101, 102, 101, 103, 102, 101],
    'Order_Date': ['2024-01-10', '2024-01-15', '2024-02-05',
                   '2024-02-10', '2024-03-01', '2024-03-12'],
    'Product_Name': ['Laptop', 'Mouse', 'Keyboard',
                     'Laptop', 'Mouse', 'Laptop'],
    'Order_Quantity': [1, 2, 1, 3, 4, 2]
})

# Convert Order_Date to datetime format
order_data['Order_Date'] = pd.to_datetime(order_data['Order_Date'])

# 1. Total number of orders made by each customer
orders_per_customer = order_data.groupby('Customer_ID').size()
print("Total Orders by Each Customer:")
print(orders_per_customer)

# 2. Average order quantity for each product
avg_quantity = order_data.groupby('Product_Name')['Order_Quantity'].mean()
print("\nAverage Order Quantity for Each Product:")
print(avg_quantity)

# 3. Earliest and latest order dates
earliest_date = order_data['Order_Date'].min()
latest_date = order_data['Order_Date'].max()

print("\nEarliest Order Date:", earliest_date)
print("Latest Order Date:", latest_date)
