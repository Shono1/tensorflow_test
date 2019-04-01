import tensorflow as tf
from tensorflow import keras

dataset = keras.datasets.mnist

(train_images, train_labels), (test_images, test_labels) = dataset.load_data()

print(test_images.shape)

train_images = train_images / 255.0

test_images = test_images / 255.0

model = keras.Sequential([keras.layers.Flatten(input_shape=(28, 28)),
                         keras.layers.Dense(128, activation=tf.nn.crelu),
                         keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)
