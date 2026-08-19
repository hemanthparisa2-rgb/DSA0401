#K-Nearest Neighbors (KNN) Classifier
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Read dataset
df = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Exp-30 data.csv")

# Features and target
X = df[["Fever", "Cough", "Headache", "Fatigue"]]
y = df["Condition"]

# Get user input
fever = int(input("Fever (0=No, 1=Yes): "))
cough = int(input("Cough (0=No, 1=Yes): "))
headache = int(input("Headache (0=No, 1=Yes): "))
fatigue = int(input("Fatigue (0=No, 1=Yes): "))

k = int(input("Enter value of k: "))

# Create KNN model
model = KNeighborsClassifier(n_neighbors=k)

# Train model
model.fit(X, y)

# New patient
new_patient = [[fever, cough, headache, fatigue]]

# Prediction
prediction = model.predict(new_patient)

print("\nPrediction:")

if prediction[0] == 1:
    print("Patient has the medical condition.")
else:
    print("Patient does not have the medical condition.")
