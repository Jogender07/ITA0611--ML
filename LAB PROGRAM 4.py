from sklearn.neural_network import MLPClassifier
import numpy as np

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 1, 1, 1])

model = MLPClassifier(hidden_layer_sizes=(5,), max_iter=2000, random_state=1)
model.fit(X, y)

a = int(input("Enter first input (0/1): "))
b = int(input("Enter second input (0/1): "))

print("Predicted Output:", model.predict([[a, b]])[0])