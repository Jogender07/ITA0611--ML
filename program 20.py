from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([
    [1], [2], [3], [4], [5], [6]
])

y = np.array([
    120, 150, 180, 210, 250, 280
])

model = LinearRegression()
model.fit(X, y)

month = float(input("Enter Future Month Number: "))

print("Predicted Sales:", model.predict([[month]])[0])