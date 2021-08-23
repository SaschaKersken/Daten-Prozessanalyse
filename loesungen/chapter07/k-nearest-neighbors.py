from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Iris-Datenmenge laden
X, y = load_iris(return_X_y=True)

# In Trainings- und Testdaten unterteilen, dabei mischen
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33
)

# k-nearest-neighbors mit Trainingsdaten trainieren
kn = KNeighborsClassifier().fit(X_train, y_train)

# Genauigkeit der Vorhersage für die Testdaten testen
accuracy = kn.score(X_test, y_test)
print(f"Genauigkeit: {accuracy}")
