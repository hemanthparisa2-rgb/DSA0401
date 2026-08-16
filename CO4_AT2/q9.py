import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error, r2_score

# Read dataset
df = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Co4 At2\q9 data.csv")

print(df)

# Input variables
X = df[["CGPA", "Aptitude_Score",
        "Coding_Score", "Communication_Score"]]

# Output variable
y = df["Package_LPA"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Test prediction
y_pred = model.predict(X_test)

print("\nActual Package:")
print(y_test.values)

print("\nPredicted Package:")
print(y_pred)

# New student
new_student = [[8.1, 82, 85, 78]]

prediction = model.predict(new_student)

print("\nPredicted Package for New Student:")
print(prediction[0], "LPA")

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE =", mae)
print("MSE =", mse)
print("RMSE =", rmse)
print("R2 Score =", r2)
