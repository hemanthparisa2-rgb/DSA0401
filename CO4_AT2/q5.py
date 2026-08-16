import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# a) Read dataset
df = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Co4 At2\q5 data.csv")

print("Dataset:")
print(df)

# b) Input and output variables
X = df[["Distance", "Traffic_Level", "Packages", "Weather_Score"]]

y = df["Time"]

# c) Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# d) Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# e) Predict test records
y_pred = model.predict(X_test)

print("\nActual Delivery Time:")
print(y_test.values)

print("\nPredicted Delivery Time:")
print(y_pred)

# f) Predict new delivery
new_delivery = [[28, 6, 38, 6]]

new_time = model.predict(new_delivery)

print("\nPredicted Delivery Time for New Delivery:")
print(new_time[0], "Hours")

# g) Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE =", mae)
print("MSE =", mse)
print("RMSE =", rmse)
print("R2 Score =", r2)
