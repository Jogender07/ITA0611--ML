from sklearn.tree import DecisionTreeClassifier
import numpy as np

X = np.array([
    [2, 32],
    [3, 64],
    [4, 128],
    [6, 128],
    [8, 256],
    [12, 256]
])

y = np.array([
    'Low',
    'Low',
    'Medium',
    'Medium',
    'High',
    'High'
])

model = DecisionTreeClassifier()
model.fit(X, y)

ram = float(input("Enter RAM in GB: "))
storage = float(input("Enter Storage in GB: "))

print("Predicted Mobile Price Range:",
      model.predict([[ram, storage]])[0])