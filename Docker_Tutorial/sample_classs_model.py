from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the iris dataset
iris = load_iris()

X = iris.data

y = iris.target

# Split the dataset

X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Make predictions
y_preds = clf.predict(X_test)

# Evaluate the performance

acc_score = accuracy_score(y_test, y_preds)

# Print the acccuracy score
print(f'Accuracy: {acc_score}:.2f%')

