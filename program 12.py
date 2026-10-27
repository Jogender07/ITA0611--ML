from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

X = iris.data
y = iris.target

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

length = float(input("Enter Sepal Length: "))
width = float(input("Enter Sepal Width: "))
plength = float(input("Enter Petal Length: "))
pwidth = float(input("Enter Petal Width: "))

prediction = model.predict([[length, width, plength, pwidth]])

print("Predicted Flower:", iris.target_names[prediction[0]])