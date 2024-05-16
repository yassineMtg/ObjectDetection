import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model('../../models/yolo-v8')

# Define test data
test_data = '../../data/raw/archive/test'

# Evaluate the model
evaluation = model.evaluate(test_data)

# Print the evaluation results
print(f'Test Loss: {evaluation[0]}, Test Accuracy: {evaluation[1]}')
