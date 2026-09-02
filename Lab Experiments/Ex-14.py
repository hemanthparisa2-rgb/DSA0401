#correlation between students'
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_scores.csv")

print("Student Data:")
print(df)

correlation = df["Study_Time"].corr(df["Exam_Score"])

print("\nCorrelation between Study Time and Exam Score:", round(correlation, 2))

plt.plot(df["Study_Time"], df["Exam_Score"], marker="o")
plt.title("Study Time vs Exam Score")
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()

plt.scatter(df["Study_Time"], df["Exam_Score"])
plt.title("Study Time vs Exam Score")
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()

if correlation > 0.7:
    print("\nInsight: Strong positive correlation between study time and exam scores.")
elif correlation > 0.3:
    print("\nInsight: Moderate positive correlation between study time and exam scores.")
else:
    print("\nInsight: Weak or no correlation between study time and exam scores.")
elif correlation > 0.3:
    print("\nInsight: Moderate positive correlation between study time and exam scores.")
else:
    print("\nInsight: Weak or no correlation between study time and exam scores.")
