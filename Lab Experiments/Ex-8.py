#Analyzing sales past month
import pandas as pd

sales_data = pd.read_csv("sales.csv")

top_5_products = (
    sales_data.groupby("Product_Name")["Quantity_Sold"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("Top 5 Products Sold:")
print(top_5_products)
