# src/features/build_features.py

import tensorflow_transform as tft
import tensorflow_transform.beam as tft_beam

def preprocessing_fn(inputs):
    # Define preprocessing steps
    return {
        'input_features': tft.scale_to_z_score(inputs['input_features'])
        # Add additional preprocessing here
    }

# Apply the preprocessing function
with tft_beam.Context(temp_dir='temp'):
    transformed_dataset, transform_fn = (
        (train_data, raw_metadata) | tft_beam.AnalyzeAndTransformDataset(preprocessing_fn)
    )
transformed_data, transformed_metadata = transformed_dataset
