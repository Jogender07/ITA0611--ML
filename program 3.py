from sklearn.tree import DecisionTreeClassifier
import numpy as np

X = np.array([
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0],
    [1, 1],
    [0, 0]
])

y = np.array([1, 1, 0, 0, 1, 0])

model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

study = int(input("Enter Study (1/0): "))
attendance = int(input("Enter Attendance (1/0): "))

print("Predicted Result:", model.predict([[study, attendance]])[0])