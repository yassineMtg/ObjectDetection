from tfx.v1.components import ExampleValidator
from tfx.v1.orchestration.experimental.interactive.interactive_context import InteractiveContext

# Initialize TFX context
context = InteractiveContext()

# Create ExampleValidator component
example_validator = ExampleValidator(
    statistics=statistics_gen.outputs['statistics'],
    schema=schema_gen.outputs['schema']
)

# Run the ExampleValidator component
context.run(example_validator)
