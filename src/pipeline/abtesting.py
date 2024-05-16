from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow as tf

# Load datasets
data = np.load('../data//data.npy')
labels = np.load('path/to/your/labels.npy')

# Split data into training and test sets
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.2)

# Define two models for A/B testing
model_a = tf.keras.models.load_model('../../models/ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8')
model_b = tf.keras.models.load_model('../../models/yolo-v8')

# Evaluate both models
evaluation_a = model_a.evaluate(test_data, test_labels)
evaluation_b = model_b.evaluate(test_data, test_labels)

# Compare the results
print(f'Model A - Loss: {evaluation_a[0]}, Accuracy: {evaluation_a[1]}')
print(f'Model B - Loss: {evaluation_b[0]}, Accuracy: {evaluation_b[1]}')
