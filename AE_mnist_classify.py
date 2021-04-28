import tensorflow as tf
import numpy as np

from tensorflow import keras
from tensorflow.keras import Sequential, layers, Model, losses
from tensorflow.keras.datasets import fashion_mnist

# load fashion mnist data
(x_data, y_data), (x_test, y_test) = fashion_mnist.load_data()

# hyperparameter
epochs = 400
hidden = 200
n_encoding = 20
n_input = 784
n_classes = 10
batch_size = 256

# data normalize
x_data = x_data / 255
x_test = y_data / 255

# reconstruction model (encoder, decoder)
reconstructor = Sequential([
    layers.Flatten(),
    layers.Dense(hidden, activation='relu'),
    layers.Dense(hidden, activation='relu'),
    layers.Dense(784, activation='sigmoid'),
    layers.Reshape((28, 28)),
])
reconstructor._name="reconstruction"

# classifier model
classifier = Sequential([
  layers.Flatten(),
  layers.Dense(n_classes, activation='softmax')
])
classifier._name="classification"

inputs = layers.Input(shape=(28,28), name="example")
reconstruct_x = reconstructor(inputs)
y_hat = classifier(reconstruct_x)

# model training
model = Model(
    inputs=inputs,
    outputs=[reconstruct_x, y_hat],
    name="autoencoder_classifier"
)

model.compile(
    optimizer='adam',
    loss={
      "reconstruction" : losses.MSE,
      "classification" : losses.sparse_categorical_crossentropy,
    },
    metrics=['accuracy']
)

model.fit(
    x_data,
    {"reconstruction" : x_data, "classification" : y_data},
    epochs=40,
    batch_size=32,
)


