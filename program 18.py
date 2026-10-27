from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron

iris = load_iris()

X = iris.data[:100, :2]
y = iris.target[:100]

model = Perceptron()
model.fit(X, y)

sl = float(input("Enter Sepal Length: "))
sw = float(input("Enter Sepal Width: "))

prediction = model.predict([[sl, sw]])

print("Predicted Class:", prediction[0])