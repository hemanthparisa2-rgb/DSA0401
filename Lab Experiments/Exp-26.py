import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Read dataset
df = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Exp-26 data.csv")

# Separate groups
control = df[df["Group"] == "Control"]["Improvement"]
treatment = df[df["Group"] == "Treatment"]["Improvement"]

# Calculate means
control_mean = control.mean()
treatment_mean = treatment.mean()

# Perform independent t-test
t_stat, p_value = ttest_ind(treatment, control)

# Display results
print("Control Mean:", round(control_mean, 2))
print("Treatment Mean:", round(treatment_mean, 2))
print("T-statistic:", round(t_stat, 3))
print("P-value:", round(p_value, 5))

# Hypothesis testing
if p_value < 0.05:
    print("There is a statistically significant effect.")
else:
    print("There is no statistically significant effect.")

# Visualization
plt.boxplot([control, treatment], tick_labels=["Control", "Treatment"])
plt.ylabel("Improvement")
plt.title("Control vs Treatment")

# Display p-value on graph
plt.text(1.05, max(treatment) - 1,
         "p-value = " + str(round(p_value, 5)))

plt.show()
