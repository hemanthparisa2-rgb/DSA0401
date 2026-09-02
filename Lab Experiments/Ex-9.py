#Real estate
import pandas as pd

property_data = pd.read_csv("real_estate.csv")

avg_price = property_data.groupby("Location")["Listing_Price"].mean()
print("Average Listing Price by Location:")
print(avg_price)

more_than_4_bedrooms = property_data[property_data["Bedrooms"] > 4].shape[0]
print("\nNumber of Properties with More Than 4 Bedrooms:")
print(more_than_4_bedrooms)

largest_property = property_data.loc[property_data["Area_sqft"].idxmax()]
print("\nProperty with the Largest Area:")
print(largest_property)
