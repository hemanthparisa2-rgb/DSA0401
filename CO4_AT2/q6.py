import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score

# Read dataset
df = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Co4 At2\q6 data.csv")

print(df)

# Independent variables
X = df[["Income", "Credit_Score", "Existing_Loan",
        "Employment_Years"]]

# Dependent variable
y = df["Approved"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Test prediction
y_pred = model.predict(X_test)

print("\nActual:", y_test.values)
print("Predicted:", y_pred)

# New applicant
new_applicant = [[50000, 700, 100000, 4]]

prediction = model.predict(new_applicant)

if prediction[0] == 1:
    print("\nLoan Approved")
else:
    print("\nLoan Rejected")

# Evaluation
print("\nAccuracy =", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Precision =", precision_score(y_test, y_pred, zero_division=0))
print("Recall =", recall_score(y_test, y_pred, zero_division=0))
print("F1 Score =", f1_score(y_test, y_pred, zero_division=0))
