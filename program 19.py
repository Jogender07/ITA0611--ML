from sklearn.naive_bayes import GaussianNB
import numpy as np

X = np.array([
    [25, 30000],
    [30, 40000],
    [35, 50000],
    [40, 60000],
    [45, 70000],
    [50, 80000]
])

y = np.array([
    'No',
    'No',
    'Yes',
    'Yes',
    'Yes',
    'Yes'
])

model = GaussianNB()
model.fit(X, y)

age = float(input("Enter Age: "))
income = float(input("Enter Annual Income: "))

print("Loan Prediction:", model.predict([[age, income]])[0])