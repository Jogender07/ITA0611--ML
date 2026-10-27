from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

X = np.array([[10], [15], [20], [25], [30], [35]])
y = np.array([20, 35, 55, 80, 120, 170])

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X, y)

# Polynomial Regression
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)

temperature = float(input("Enter Temperature: "))

linear_prediction = linear_model.predict([[temperature]])[0]

poly_prediction = poly_model.predict(
    poly.transform([[temperature]])
)[0]

print("Linear Regression Prediction:", linear_prediction)
print("Polynomial Regression Prediction:", poly_prediction)