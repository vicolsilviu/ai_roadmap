
# from sklearn.datasets import load_iris
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import cross_val_score
# import matplotlib.pyplot as plt

# # read in the iris data
# iris = load_iris()

# # create X (features) and y (response)
# X = iris.data
# y = iris.target
# # 10-fold cross-validation with K=5 for KNN (the n_neighbors parameter)
# knn = KNeighborsClassifier(n_neighbors=5)
# scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
# # search for an optimal value of K for KNN
# k_range = list(range(1, 31))
# k_scores = []
# for k in k_range:
#     knn = KNeighborsClassifier(n_neighbors=k)
#     scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
#     k_scores.append(scores.mean())
# print(k_scores)
# from sklearn.model_selection import GridSearchCV
# # define the parameter values that should be searched
# k_range = list(range(1, 31))
# # print(k_range)
# # create a parameter grid: map the parameter names to the values that should be searched
# param_grid = dict(n_neighbors=k_range)
# print(param_grid)

# # instantiate the grid
# grid = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy')

# # fit the grid with data
# grid.fit(X, y)
