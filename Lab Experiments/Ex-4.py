#company sells in year
import numpy as np
import pandas as pd
sales_data = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Ex-4 data.csv")
sales = sales_data["sales"].to_numpy()
total_sales = np.sum(sales)
percentage_increase = ((sales[3] - sales[0]) / sales[0]) * 100
print("Quarterly Sales:")
print(sales)
print("Total Sales for the Year:", total_sales)
print("Percentage Increase from Q1 to Q4: {:.2f}%".format(percentage_increase))
