from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([
    [500, 1],
    [700, 2],
    [900, 2],
    [1100, 3],
    [1300, 3],
    [1500, 4]
])

y = np.array([2000000, 2800000, 3500000, 4500000, 5200000, 6000000])

model = LinearRegression()
model.fit(X, y)

area = float(input("Enter House Area in sq.ft: "))
rooms = float(input("Enter Number of Rooms: "))

print("Predicted House Price:", model.predict([[area, rooms]])[0])