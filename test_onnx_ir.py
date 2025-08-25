import onnx

# Load the original model
model = onnx.load('yolov4-416.onnx')

# Set the model IR version to 9
model.ir_version = 9

# Save the modified model
onnx.save(model, 'yolov4-416-v9.onnx')