import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# a) Read dataset
df = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Co4 At2\q3.csv")

print("Dataset:")
print(df)

# b) Features and target
X = df[["TV_Ads", "Social_Media_Ads",
        "Newspaper_Ads", "Email_Campaigns"]]

y = df["Sales"]

# c) Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# d & e) Lasso Regression
model = Lasso(alpha=0.1)

model.fit(X_train, y_train)

# f) Predict test data
y_pred = model.predict(X_test)

print("\nActual Sales:")
print(y_test.values)

print("\nPredicted Sales:")
print(y_pred)

# g) Predict new campaign
new_campaign = [[95, 55, 18, 9]]

new_sales = model.predict(new_campaign)

print("\nPredicted Sales for New Campaign:")
print(new_sales[0], "Lakhs")

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

# i) Display coefficients
print("\nLasso Coefficients:")

for feature, coefficient in zip(X.columns, model.coef_):
    print(feature, "=", coefficient)
