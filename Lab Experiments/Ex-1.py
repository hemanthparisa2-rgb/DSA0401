import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Ex-1 data.csv")
student_scores = df.to_numpy()
subjects = df.columns.tolist()
average_scores = np.mean(student_scores, axis=0)
highest_index = np.argmax(average_scores)
highest_subject = subjects[highest_index]
print("Average Scores:")
for subject, avg in zip(subjects, average_scores):
    print(f"{subject}: {avg:.2f}")
print("\nSubject with Highest Average Score:", highest_subject)
print("Highest Average Score:", average_scores[highest_index])
