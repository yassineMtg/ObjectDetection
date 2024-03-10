# src/features/store_features.py

from feast import FeatureStore

store = FeatureStore(repo_path='./feast_repo')
features = ['feature1', 'feature2', ...]

# Retrieve training features from the feature store
training_data = store.get_historical_features(
    entity_df=entity_dataframe,
    feature_refs=features,
).to_df()
