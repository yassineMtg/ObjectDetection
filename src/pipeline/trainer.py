from tfx.v1.components import Trainer
from tfx.v1.proto import trainer_pb2
from tfx.v1.orchestration.experimental.interactive.interactive_context import InteractiveContext

# Initialize TFX context
context = InteractiveContext()

# Define the trainer component
trainer = Trainer(
    module_file=os.path.abspath('../../models/yolo-v8/trainer_component.py'),
    examples=example_gen.outputs['examples'],
    schema=schema_gen.outputs['schema'],
    train_args=trainer_pb2.TrainArgs(num_steps=2000),
    eval_args=trainer_pb2.EvalArgs(num_steps=1000)
)

# Run the Trainer component
context.run(trainer)
