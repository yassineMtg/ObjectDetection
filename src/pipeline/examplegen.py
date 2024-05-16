import os
import urllib
from tfx.v1 import types
from tfx.v1.components import CsvExampleGen
from tfx.v1.orchestration.experimental.interactive.interactive_context import InteractiveContext

# Initialize TFX context
context = InteractiveContext()

# Path to the input CSV file
input_data = '../../data/raw/archive/train/train_data.csv'

# Create ExampleGen component
example_gen = CsvExampleGen(input_base=input_data)

# Run the ExampleGen component
context.run(example_gen)
