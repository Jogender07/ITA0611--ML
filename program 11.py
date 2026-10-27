from sklearn.tree import DecisionTreeClassifier
import numpy as np

X = np.array([
    [20, 30000],
    [25, 40000],
    [30, 50000],
    [35, 60000],
    [40, 70000],
    [45, 80000]
])

y = np.array(['Poor', 'Poor', 'Average', 'Average', 'Good', 'Good'])

model = DecisionTreeClassifier()
model.fit(X, y)

age = float(input("Enter Age: "))
income = float(input("Enter Annual Income: "))

print("Credit Score:", model.predict([[age, income]])[0])