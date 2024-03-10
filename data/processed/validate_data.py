import tensorflow_data_validation as tfdv

def validate_data(data_path):
    # Generate statistics from the dataset
    stats = tfdv.generate_statistics_from_csv(data_location=data_path)
    # Infer the schema
    schema = tfdv.infer_schema(statistics=stats)
    tfdv.display_schema(schema=schema)
    # Check for anomalies
    anomalies = tfdv.detect_anomalies(statistics=stats, schema=schema)
    tfdv.display_anomalies(anomalies)

if __name__ == "__main__":
    # Replace 'data/raw/train_data.csv' with the path to your dataset
    validate_data('data/raw/train_data.csv')


# import tensorflow_data_validation as tfdv

# def validate_data(data_path):
#     # Generate statistics from the dataset
#     stats = tfdv.generate_statistics_from_csv(data_location=data_path)
#     # Infer the schema
#     schema = tfdv.infer_schema(statistics=stats)
#     tfdv.display_schema(schema=schema)
#     # Check for anomalies
#     anomalies = tfdv.detect_anomalies(statistics=stats, schema=schema)
#     tfdv.display_anomalies(anomalies)

# if __name__ == "__main__":
#     # Replace 'data/raw/train_data.csv' with the path to your dataset
#     validate_data('data/raw/train_data.csv')
