



import shap
import tensorflow as tf

# Load evaluation data
eval_data = ... # Load your evaluation data

# Load model
model = tf.keras.models.load_model('../models/yolo-v8')

# Create SHAP explainer
explainer = shap.KernelExplainer(model.predict, eval_data)

# Calculate SHAP values
shap_values = explainer.shap_values(eval_data)

# Plot SHAP values
shap.summary_plot(shap_values, eval_data)
