# In data/make_dataset.py

import tensorflow_data_validation as tfdv

# Generate statistics from the dataset
stats = tfdv.generate_statistics_from_csv(data_location='data/raw/your_data.csv')

# Infer the schema
schema = tfdv.infer_schema(statistics=stats)
tfdv.display_schema(schema=schema)

# Check for anomalies
anomalies = tfdv.detect_anomalies(statistics=stats, schema=schema)
tfdv.display_anomalies(anomalies)
