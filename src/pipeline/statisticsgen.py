from tfx.v1.components import StatisticsGen
from tfx.v1.orchestration.experimental.interactive.interactive_context import InteractiveContext

# Initialize TFX context
context = InteractiveContext()

# Create StatisticsGen component
statistics_gen = StatisticsGen(
    examples=example_gen.outputs['examples']
)

# Run the StatisticsGen component
context.run(statistics_gen)
