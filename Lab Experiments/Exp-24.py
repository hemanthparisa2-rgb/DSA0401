#input the sample size, confidence level, and desired level of precision.
import numpy as np

# Read CSV file
data = np.genfromtxt(r"C:\Users\heman\Downloads\FDS\Exp-24 data.csv", delimiter=",", skip_header=1)

# User input
n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level (%): "))
precision = float(input("Enter desired precision: "))

# Check sample size
if n > len(data):
    print("Sample size is larger than available data.")
    exit()

# Random sample
sample = np.random.choice(data, n, replace=False)

# Point estimate
mean = np.mean(sample)

# Standard deviation
sd = np.std(sample, ddof=1)

# Standard error
se = sd / np.sqrt(n)

# Z value for common confidence levels
if confidence == 90:
    z = 1.645
elif confidence == 95:
    z = 1.96
elif confidence == 99:
    z = 2.576
else:
    print("Use 90, 95, or 99 confidence level.")
    exit()

# Margin of error
margin = z * se

# Confidence interval
lower = mean - margin
upper = mean + margin

print("\nSample:", sample)
print("Point Estimate (Mean):", round(mean, 3))
print("Standard Deviation:", round(sd, 3))
print("Margin of Error:", round(margin, 3))
print("Confidence Interval:", round(lower, 3), "to", round(upper, 3))

# Precision check
if margin <= precision:
    print("Desired precision is achieved.")
else:
    print("Desired precision is NOT achieved.")
    print("Consider increasing the sample size.")
