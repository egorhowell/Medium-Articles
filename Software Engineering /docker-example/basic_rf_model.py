# Import Packages
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
x = iris.data
y = iris.target

# Split into train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

# Train our model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Generate predictions
preds = model.predict(x_test)

# Get accuracy
print(f'Accuracy: {accuracy_score(y_test, preds)}')
