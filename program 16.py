from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = load_breast_cancer()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = [
    LogisticRegression(max_iter=5000),
    DecisionTreeClassifier(),
    KNeighborsClassifier()
]

for model in models:
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)
    print(type(model).__name__, "Accuracy:",
          accuracy_score(y_test, prediction))