import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# a) Read dataset
df = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Co4 At2\q4 data.csv")

print("Dataset:")
print(df)

# b) Independent and dependent variables
X = df[["Appliances", "Usage_Hours", "House_Size", "Occupants"]]

y = df["Consumption"]

# c) Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# d & e) Ridge Regression
model = Ridge(alpha=1.0)

model.fit(X_train, y_train)

# f) Predict test data
y_pred = model.predict(X_test)

print("\nActual Consumption:")
print(y_test.values)

print("\nPredicted Consumption:")
print(y_pred)

# g) Predict new house
new_house = [[8, 6, 1100, 4]]

new_consumption = model.predict(new_house)

print("\nPredicted Consumption for New House:")
print(new_consumption[0], "Units")

# h) Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE =", mae)
print("MSE =", mse)
print("RMSE =", rmse)
print("R2 Score =", r2)

# i) Display Ridge coefficients
print("\nRidge Coefficients:")

for feature, coefficient in zip(X.columns, model.coef_):
    print(feature, "=", coefficient)
