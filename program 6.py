from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np

X = np.array([
    [20, 1],
    [25, 1],
    [30, 0],
    [35, 0],
    [40, 0],
    [22, 1]
])

y = np.array([1, 1, 0, 0, 0, 1])

model = GaussianNB()
model.fit(X, y)

age = float(input("Enter Age: "))
student = int(input("Are you a Student? (1/0): "))

prediction = model.predict([[age, student]])

print("Predicted Class:", prediction[0])
print("Accuracy:", accuracy_score(y, model.predict(X)))
print("Confusion Matrix:")
print(confusion_matrix(y, model.predict(X)))