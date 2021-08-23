import csv
from neural_network import NeuralNetwork
from random import shuffle

with open('digits.csv', 'r') as digits_file:
    reader = csv.reader(digits_file, quoting=csv.QUOTE_NONNUMERIC)
    digits = list(reader)
shuffle(digits)
network = NeuralNetwork(64, 256, 10, learning_rate = 0.005)
x_test, y_test, x_train, y_train = network.prepare(
    digits, test_ratio = 0.1
)
for i in range(300):
    network.train(x_train, y_train)
correct, percent = network.predict(x_test, targets = y_test)
print(f"{correct} korrekte Vorhersagen ({percent}%).")
