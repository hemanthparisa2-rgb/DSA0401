import pandas as pd

data = pd.read_csv(r"C:\Users\heman\Downloads\FDS\stock_data.csv")

# Remove extra spaces from column names
data.columns = data.columns.str.strip()

print("Columns:", data.columns)

mean_price = data["Close"].mean()
max_price = data["Close"].max()
min_price = data["Close"].min()
std_dev = data["Close"].std()

print("\nAverage Closing Price :", mean_price)
print("Maximum Closing Price :", max_price)
print("Minimum Closing Price :", min_price)
print("Standard Deviation    :", round(std_dev, 2))
