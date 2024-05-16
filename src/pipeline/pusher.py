from tfx.v1.components import Pusher
from tfx.v1.orchestration.experimental.interactive.interactive_context import InteractiveContext
from tfx.v1.proto import pusher_pb2

# Initialize TFX context
context = InteractiveContext()

# Define the Pusher component
pusher = Pusher(
    model=trainer.outputs['model'],
    push_destination=pusher_pb2.PushDestination(
        filesystem=pusher_pb2.PushDestination.Filesystem(
            base_directory='../../models/yolo-v8'
        )
    )
)

# Run the Pusher component
context.run(pusher)
