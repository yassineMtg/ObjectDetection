from tfx.v1.components import SchemaGen
from tfx.v1.orchestration.experimental.interactive.interactive_context import InteractiveContext

# Initialize TFX context
context = InteractiveContext()

# Create SchemaGen component
schema_gen = SchemaGen(
    examples=example_gen.outputs['examples']
)

# Run the SchemaGen component
context.run(schema_gen)
