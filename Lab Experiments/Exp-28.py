import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.preprocessing import LabelEncoder

# Read dataset
df = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Exp-28 data.csv")

# Convert text columns into numbers
brand_encoder = LabelEncoder()
engine_encoder = LabelEncoder()

df["Brand"] = brand_encoder.fit_transform(df["Brand"])
df["Engine"] = engine_encoder.fit_transform(df["Engine"])

# Features and target
X = df[["Brand", "Age", "Mileage", "Engine"]]
y = df["Price"]

# Create CART model
model = DecisionTreeRegressor(max_depth=4, random_state=42)

# Train model
model.fit(X, y)

# Get user input
brand = input("Enter car brand (Toyota/Honda/Hyundai/Ford/BMW): ")
age = int(input("Enter car age: "))
mileage = int(input("Enter mileage: "))
engine = input("Enter engine type (Petrol/Diesel): ")

# Convert user input
brand_code = brand_encoder.transform([brand])[0]
engine_code = engine_encoder.transform([engine])[0]

# Create new car data
new_car = [[brand_code, age, mileage, engine_code]]

# Predict price
prediction = model.predict(new_car)[0]

print("\nPredicted Car Price: ₹", round(prediction, 2))

# Display decision path
tree_rules = export_text(
    model,
    feature_names=["Brand", "Age", "Mileage", "Engine"]
)

print("\nDecision Tree:")
print(tree_rules)
