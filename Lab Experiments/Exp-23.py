#an A/B test to evaluate the effectiveness of two different website designs
import pandas as pd
from scipy.stats import ttest_ind

# Read dataset
df = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Exp-23 data.csv")

# Separate the two designs
A = df[df["Design"] == "A"]["Conversion_Rate"]
B = df[df["Design"] == "B"]["Conversion_Rate"]

# Calculate means
mean_A = A.mean()
mean_B = B.mean()

# Perform independent two-sample t-test
t_stat, p_value = ttest_ind(A, B)

print("Mean Conversion Rate - Design A:", round(mean_A, 2))
print("Mean Conversion Rate - Design B:", round(mean_B, 2))

print("T-statistic:", round(t_stat, 3))
print("P-value:", round(p_value, 5))

# Decision
if p_value < 0.05:
    print("There is a statistically significant difference.")
else:
    print("There is no statistically significant difference.")
