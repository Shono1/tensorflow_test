import tensorflow as tf
from tensorflow import keras

dataset = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = dataset.load_data()
