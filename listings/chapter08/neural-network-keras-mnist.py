import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Kategorien, 
categories = 10

# Daten laden
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Feature-Skalierung
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# Daten in die richtige Form bringen
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

# Ausgabedaten konvertieren
y_train = keras.utils.to_categorical(y_train, categories)
y_test = keras.utils.to_categorical(y_test, categories)

model = keras.Sequential(
    [
        keras.Input(shape=(28, 28, 1)),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(categories, activation="softmax"),
    ]
)

model.summary()

batch_size = 128
epochs = 15

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

score = model.evaluate(x_test, y_test, verbose=0)
print("Genauigkeit:", score[1])
