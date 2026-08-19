#correlation between students
import pandas as pd
# Read dataset from CSV file
data = pd.read_csv(r"C:\Users\heman\Downloads\FDS\temperature_data.csv")

# Display dataset
print("Temperature Dataset:")
print(data)

# Remove extra spaces in column names
data.columns = data.columns.str.strip()

# Group data by City
group = data.groupby("City")["Temperature"]

# Calculate Mean Temperature
mean_temp = group.mean()

# Calculate Standard Deviation
std_temp = group.std()

# Calculate Temperature Range
temp_range = group.max() - group.min()

# Display Results
print("\nMean Temperature for Each City")
print(mean_temp)

print("\nStandard Deviation for Each City")
print(std_temp)

print("\nTemperature Range for Each City")
print(temp_range)

# Find city with highest temperature range
highest_range_city = temp_range.idxmax()
highest_range = temp_range.max()

print("\nCity with Highest Temperature Range")
print("City :", highest_range_city)
print("Temperature Range :", highest_range)
