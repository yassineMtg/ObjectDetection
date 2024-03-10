# In src/pipeline.py

import tensorflow_transform as tft
import tensorflow_transform.beam.impl as tft_beam

def preprocessing_fn(inputs):
    ...
    # Your preprocessing logic here
    ...

# Execute the preprocessing pipeline
with tft_beam.Context(temp_dir=temporary_dir):
    transformed_dataset, transform_fn = (
        (raw_data, raw_data_metadata) | tft_beam.AnalyzeAndTransformDataset(preprocessing_fn)
    )
