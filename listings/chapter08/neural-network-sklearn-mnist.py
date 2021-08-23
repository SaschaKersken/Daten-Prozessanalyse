import csv
from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

X_train = []
y_train = []
X_test = []
y_test = []
with open('mnist_train.csv', 'r') as train_file:
    for line in csv.reader(train_file, quoting=csv.QUOTE_NONNUMERIC):
        X_train.append(line[1:])
        y_train.append(line[0])
with open('mnist_test.csv', 'r') as test_file:
    for line in csv.reader(test_file, quoting=csv.QUOTE_NONNUMERIC):
        X_test.append(line[1:])
        y_test.append(line[0])

# KNN erzeugen und mit Trainingsdaten trainieren
ann = MLPClassifier(
    hidden_layer_sizes = (64, 128, 64),
    activation = 'relu',
    max_iter = 1000
)
ann.fit(X_train, y_train)

# Genauigkeit der Vorhersage für die Testdaten testen
accuracy = ann.score(X_test, y_test)
print(f"Genauigkeit: {accuracy}")
