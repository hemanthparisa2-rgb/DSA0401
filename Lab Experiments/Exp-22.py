#effectiveness of a new drug
import pandas as pd
from scipy.stats import t

df = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Exp-22 data.csv")

for group in ["Drug", "Placebo"]:
    data = df[df["Group"] == group]["Reduction"]

    n = len(data)
    mean = data.mean()
    sd = data.std()
    se = sd / (n ** 0.5)

    t_value = t.ppf(0.975, n - 1)

    lower = mean - t_value * se
    upper = mean + t_value * se

    print("\nGroup:", group)
    print("Number of patients:", n)
    print("Mean reduction:", round(mean, 2))
    print("Standard deviation:", round(sd, 2))
    print("95% Confidence Interval:")
    print("Lower limit:", round(lower, 2))
    print("Upper limit:", round(upper, 2))
