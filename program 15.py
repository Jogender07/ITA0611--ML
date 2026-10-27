from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

iris = load_iris()

X = iris.data
y = iris.target

model = GaussianNB()
model.fit(X, y)

sl = float(input("Enter Sepal Length: "))
sw = float(input("Enter Sepal Width: "))
pl = float(input("Enter Petal Length: "))
pw = float(input("Enter Petal Width: "))

prediction = model.predict([[sl, sw, pl, pw]])

print("Predicted Flower:", iris.target_names[prediction[0]])