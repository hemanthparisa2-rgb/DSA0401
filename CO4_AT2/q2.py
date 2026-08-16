import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# a) Read dataset
df = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Co4 At2\q2 data.csv")

print("Dataset:")
print(df)

# b) Input features and target
X = df[["Monthly_Bill", "Complaints", "Data_Usage", "Tenure"]]
y = df["Churn"]

# c) Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# d) Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# e) Predict test customers
y_pred = model.predict(X_test)

print("\nActual Churn:")
print(y_test.values)

print("\nPredicted Churn:")
print(y_pred)

# f) Predict new customer
new_customer = [[800, 2, 14, 10]]

prediction = model.predict(new_customer)

if prediction[0] == 1:
    print("\nNew Customer: WILL CHURN")
else:
    print("\nNew Customer: WILL NOT CHURN")

# g) Evaluation
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("\nModel Evaluation:")
print("Accuracy =", accuracy)
print("Confusion Matrix:")
print(cm)
print("Precision =", precision)
print("Recall =", recall)
print("F1 Score =", f1)
