import tensorflow as tf
import datetime

# Load and prepare the MNIST dataset.
# Convert the samples from integers to floating-point numbers:
mnist = tf.keras.datasets.mnist
(train_data, train_labels), (test_data, test_labels) = mnist.load_data()
train_data, test_data = train_data / 255.0, test_data / 255.0

# Define the model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

# Compile the model
model.compile(optimizer='adam',
              loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Number of epochs to train the model
num_epochs = 5

# Directory where the TensorBoard logs will be written
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# Train the model
model.fit(x=train_data, 
          y=train_labels, 
          epochs=num_epochs, 
          validation_data=(test_data, test_labels), 
          callbacks=[tensorboard_callback])
