from sklearn.mixture import GaussianMixture
import numpy as np

X = np.array([
    [1], [2], [3], [8], [9], [10]
])

model = GaussianMixture(n_components=2, random_state=1)
model.fit(X)

value = float(input("Enter a value: "))

print("Predicted Cluster:", model.predict([[value]])[0])