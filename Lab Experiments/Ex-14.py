import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Study_Time": [1, 2, 3, 4, 5, 6, 7, 8],
    "Exam_Score": [40, 50, 55, 65, 70, 80, 85, 95]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display Data
print("Student Data:")
print(df)

# Calculate Correlation
correlation = df["Study_Time"].corr(df["Exam_Score"])

print("\nCorrelation between Study Time and Exam Score:", round(correlation, 2))

# Line Plot
plt.figure(figsize=(6,4))
plt.plot(df["Study_Time"], df["Exam_Score"], marker='o', color='blue')
plt.title("Study Time vs Exam Score (Line Plot)")
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()

# Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df["Study_Time"], df["Exam_Score"], color='red', s=80)
plt.title("Study Time vs Exam Score (Scatter Plot)")
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()

# Insight
if correlation > 0.7:
    print("\nInsight: Strong positive correlation between study time and exam scores.")
elif correlation > 0.3:
    print("\nInsight: Moderate positive correlation between study time and exam scores.")
else:
    print("\nInsight: Weak or no correlation between study time and exam scores.")
