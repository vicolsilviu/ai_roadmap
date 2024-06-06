from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

# Load the iris dataset
iris = load_iris()

# Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# # Create a KNeighborsClassifier object
# knn = KNeighborsClassifier(n_neighbors=3)

# # Train the model using the training sets
# knn.fit(X_train, y_train)

# # Make predictions on the testing set
# y_pred = knn.predict(X_test)

# Print the accuracy of the model
# print(type(iris))
# print(iris.data)
# print(iris.target)
# print(f"Accuracy: {knn.score(X_test, y_test)}")
# print(iris.target_names)
# print(iris.feature_names)

# X=iris.data
# y=iris.target

# # print(X)
# # print(y)


# knn = KNeighborsClassifier(n_neighbors=1)
# knn.fit(X, y)

# print(knn.predict([[3, 5, 4, 2],[5, 4, 3, 2]]))

# logreg = LogisticRegression()
# logreg.fit(X,y)

