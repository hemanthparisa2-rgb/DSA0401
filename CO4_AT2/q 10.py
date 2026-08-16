import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# Read dataset
df = pd.read_csv(
    r"C:\Users\heman\Downloads\FDS\Co4 At2\q10 data.csv"
)

print(df)

# Features
X = df[["Experience", "Satisfaction_Score",
        "Overtime_Hours", "Salary_Increment"]]

# Target
y = df["Leave"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Test prediction
y_pred = model.predict(X_test)

print("\nActual Leave:")
print(y_test.values)

print("\nPredicted Leave:")
print(y_pred)

# New employee
new_employee = [[5, 4, 9, 6]]

prediction = model.predict(new_employee)

if prediction[0] == 1:
    print("\nEmployee may LEAVE")
else:
    print("\nEmployee may STAY")

# Evaluation
print("\nModel Evaluation:")

print("Accuracy =",
      accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Precision =",
      precision_score(y_test, y_pred, zero_division=0))

print("Recall =",
      recall_score(y_test, y_pred, zero_division=0))

print("F1 Score =",
      f1_score(y_test, y_pred, zero_division=0))
