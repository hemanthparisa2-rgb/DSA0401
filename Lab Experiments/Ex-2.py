#company sells dataset
import numpy as np
import pandas as pd
sales=pd.read_csv(r"C:\Users\heman\Downloads\FDS\Ex-2 data.csv")
print("sales data:",sales)
avg_score=np.mean(sales)
print("Average scores:",avg_score)
