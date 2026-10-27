from sklearn.neighbors import KNeighborsClassifier
import numpy as np

X = np.array([
    [1, 20],
    [2, 21],
    [3, 22],
    [7, 30],
    [8, 31],
    [9, 32]
])

y = np.array(['Low', 'Low', 'Low', 'High', 'High', 'High'])

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

age = float(input("Enter Age: "))
income = float(input("Enter Income: "))

print("Predicted Class:", model.predict([[age, income]])[0])