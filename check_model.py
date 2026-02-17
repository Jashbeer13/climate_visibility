import pickle
import numpy as np

# Load and inspect the model
with open('random_forest_regressor_scaled_model.pkl', 'rb') as f:
    model_data = pickle.load(f)

print("Model type:", type(model_data))
print("\nModel structure:")

# Check if it's a pipeline or just a model
if hasattr(model_data, 'named_steps'):
    print("This is a Pipeline with steps:")
    for name, step in model_data.named_steps.items():
        print(f"  - {name}: {type(step)}")
elif hasattr(model_data, '__dict__'):
    print("Model attributes:", list(model_data.__dict__.keys())[:10])

# Try a test prediction
test_input = np.array([[70, 50, 10, 180, 30]])
print("\nTest input:", test_input)
try:
    prediction = model_data.predict(test_input)
    print("Test prediction:", prediction)
except Exception as e:
    print("Error:", e)
