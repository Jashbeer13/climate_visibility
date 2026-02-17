import pickle
import numpy as np

with open('random_forest_regressor_scaled_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Test with various scaled inputs to understand the model's expected input range
print("Testing different input patterns:\n")

# Test 1: All zeros (scaled)
test1 = np.array([[0, 0, 0, 0, 0]])
pred1 = model.predict(test1)
print(f"All zeros: {pred1[0]:.4f}")

# Test 2: All ones (scaled)
test2 = np.array([[1, 1, 1, 1, 1]])
pred2 = model.predict(test2)
print(f"All ones: {pred2[0]:.4f}")

# Test 3: All negative ones
test3 = np.array([[-1, -1, -1, -1, -1]])
pred3 = model.predict(test3)
print(f"All -1: {pred3[0]:.4f}")

# Test 4: Mixed scaled values
test4 = np.array([[0.5, -0.5, 1.0, 0, -1.0]])
pred4 = model.predict(test4)
print(f"Mixed: {pred4[0]:.4f}")

# Test 5: Typical scaled weather (assuming StandardScaler was used)
# Good visibility conditions: warm, low humidity, moderate wind
test5 = np.array([[0.5, -1.0, 0.0, 0.0, 0.5]])
pred5 = model.predict(test5)
print(f"Good conditions (scaled): {pred5[0]:.4f}")

# Test 6: Poor visibility conditions: cold, high humidity
test6 = np.array([[-1.0, 1.5, -0.5, 0.0, -0.5]])
pred6 = model.predict(test6)
print(f"Poor conditions (scaled): {pred6[0]:.4f}")
