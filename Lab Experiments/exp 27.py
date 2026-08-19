import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\heman\Downloads\FDS\27 data.csv")
print("Top 5 players who scored more goals\n")
print(df.sort_values("Goals", ascending=False).head(5))
print("Top 5 players with highest salary\n")
print(df.sort_values("Weekly_Salary",ascending=False).head(5))
avg_age=df["Age"].mean()
print(avg_age)
print(df[df["Age"] > avg_age][["Name", "Age"]])
position = df["Position"].value_counts()
print("\nPlayers by Position:")
print(position)
position.plot(kind="bar")
plt.title("Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.show()

