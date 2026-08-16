import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error, r2_score

# Read dataset
df = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Co4 At2\q7 data.csv")

print(df)

# Features
X = df[["Age", "BP", "Sugar_Level", "BMI", "Previous_Visits"]]

# Target
y = df["Treatment_Cost"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Try different alpha values
for alpha in [0.1, 1.0, 10.0]:

    model = Lasso(alpha=alpha, max_iter=10000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("\nAlpha =", alpha)

    print("MAE =", mean_absolute_error(y_test, y_pred))

    mse = mean_squared_error(y_test, y_pred)
    print("MSE =", mse)

    print("RMSE =", np.sqrt(mse))

    print("R2 =", r2_score(y_test, y_pred))

    print("Coefficients:")
    for feature, coefficient in zip(X.columns, model.coef_):
        print(feature, "=", coefficient)

# New patient using alpha 0.1
model = Lasso(alpha=0.1, max_iter=10000)
model.fit(X_train, y_train)

new_patient = [[48, 145, 160, 30, 4]]

prediction = model.predict(new_patient)

print("\nPredicted Treatment Cost:")
print(prediction[0])
