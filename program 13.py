from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([
    [2, 50000],
    [3, 45000],
    [4, 40000],
    [5, 35000],
    [6, 30000],
    [7, 25000]
])

y = np.array([800000, 700000, 600000, 500000, 400000, 300000])

model = LinearRegression()
model.fit(X, y)

age = float(input("Enter Car Age: "))
km = float(input("Enter Kilometers Driven: "))

print("Predicted Car Price:", model.predict([[age, km]])[0])