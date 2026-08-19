import pandas as pd

# Sample DataFrame
property_data = pd.DataFrame({
    'Property_ID': [101, 102, 103, 104, 105],
    'Location': ['Chennai', 'Mumbai', 'Chennai', 'Delhi', 'Mumbai'],
    'Bedrooms': [3, 5, 4, 6, 2],
    'Area_sqft': [1500, 2500, 1800, 3000, 1200],
    'Listing_Price': [6000000, 12000000, 7500000, 15000000, 5000000]
})

# 1. Average listing price of properties in each location
avg_price = property_data.groupby('Location')['Listing_Price'].mean()
print("Average Listing Price by Location:")
print(avg_price)

# 2. Number of properties with more than four bedrooms
more_than_4_bedrooms = property_data[property_data['Bedrooms'] > 4].shape[0]
print("\nNumber of Properties with More Than 4 Bedrooms:")
print(more_than_4_bedrooms)

# 3. Property with the largest area
largest_property = property_data.loc[property_data['Area_sqft'].idxmax()]
print("\nProperty with the Largest Area:")
print(largest_property)
