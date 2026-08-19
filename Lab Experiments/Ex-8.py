import pandas as pd

# Sample DataFrame
sales_data = pd.DataFrame({
    'Product_Name': ['Laptop', 'Mouse', 'Laptop', 'Keyboard',
                     'Mouse', 'Laptop', 'Keyboard', 'Monitor'],
    'Quantity_Sold': [5, 10, 3, 7, 8, 6, 2, 9]
})

# Find the top 5 products sold the most
top_5_products = (
    sales_data.groupby('Product_Name')['Quantity_Sold']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("Top 5 Products Sold:")
print(top_5_products)
