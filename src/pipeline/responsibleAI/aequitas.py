


import pandas as pd
from aequitas.group import Group
from aequitas.preprocessing import preprocess_input_df

# Load evaluation data
eval_data = pd.read_csv('../data/processed/_annotations.csv')

# Add predictions to the data
eval_data['predictions'] = model.predict(eval_data[feature_columns])

# Preprocess data for Aequitas
input_data = preprocess_input_df(eval_data)

# Perform bias audit
g = Group()
xtab, _ = g.get_crosstabs(input_data)
bias_report = g.get_disparity_predefined_groups(
    xtab, original_df=input_data
)

# Save bias report
bias_report.to_csv('bias_report.csv')


