# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score

# # Încărcarea datelor
# data = datasets.load_iris()
# X = data.data
# y = data.target

# # Împărțirea datelor
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Standardizarea caracteristicilor
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# # Antrenarea modelului
# model = LogisticRegression()
# model.fit(X_train, y_train)

# # Prezicerea și evaluarea
# y_pred = model.predict(X_test)
# print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error

# # Încărcarea datelor
# data = datasets.load_boston()
# X = data.data
# y = data.target

# # Împărțirea datelor
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Standardizarea caracteristicilor
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# # Antrenarea modelului
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Prezicerea și evaluarea
# y_pred = model.predict(X_test)
# print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
