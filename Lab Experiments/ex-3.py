#Houses more than four bedrooms
import pandas as pd
import numpy as np
house_data = pd.read_csv(r"C:\Users\heman\Downloads\FDS\Exp-3 data.csv").to_numpy()
filtered = house_data[house_data[:, 0] > 4]
average_price = np.mean(filtered[:, 2])
print("Average Sale Price:", average_price)
