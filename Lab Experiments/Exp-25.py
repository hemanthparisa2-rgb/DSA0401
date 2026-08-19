import pandas as pd
from scipy.stats import t

# Read the CSV file
df = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Exp-25 data.csv")

# Get ratings
ratings = df["Rating"]

# Sample size
n = len(ratings)

# Mean rating
mean = ratings.mean()

# Standard deviation
sd = ratings.std()

# Standard error
se = sd / (n ** 0.5)

# 95% confidence interval
t_value = t.ppf(0.975, n - 1)

margin = t_value * se

lower = mean - margin
upper = mean + margin

print("Number of customers:", n)
print("Average Rating:", round(mean, 2))
print("Standard Deviation:", round(sd, 2))
print("95% Confidence Interval:")
print("Lower Limit:", round(lower, 2))
print("Upper Limit:", round(upper, 2))
