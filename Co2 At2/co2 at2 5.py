import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

df = pd.DataFrame({
    "Temperature": [30, 32, 28, 35, 31],
    "Humidity": [70, 65, 80, 60, 75],
    "SoilMoisture": [40, 35, 50, 30, 45],
    "CropHealth": [1, 0, 1, 0, 1]
})

print("Average Temperature:", np.mean(df["Temperature"]))

X = df[["Temperature", "Humidity", "SoilMoisture"]]
y = df["CropHealth"]

model = DecisionTreeClassifier()
model.fit(X, y)

prediction = model.predict([[33, 68, 38]])

print("Predicted Crop Health:", prediction[0])

plt.plot(df["Temperature"], label="Temperature")
plt.plot(df["Humidity"], label="Humidity")
plt.legend()
plt.title("Sensor Data")
plt.show()
