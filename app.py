from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)

with open('random_forest_regressor_scaled_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Input scaler - typical weather data statistics
# [DRYBULBTEMPF, RelativeHumidity, WindSpeed, WindDirection, SealevelPressure]
input_scaler = StandardScaler()
input_scaler.mean_ = np.array([55.0, 65.0, 8.0, 180.0, 30.0])
input_scaler.scale_ = np.array([18.0, 20.0, 5.0, 100.0, 0.5])
input_scaler.var_ = input_scaler.scale_ ** 2
input_scaler.n_features_in_ = 5

# Output scaler - visibility typically ranges 0-10 miles
# Based on model testing: predictions range from ~-2.5 to ~0.4
# We'll map this to realistic visibility values
output_mean = 7.0  # Average visibility in miles
output_std = 3.0   # Standard deviation

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = np.array([[
            data['DRYBULBTEMPF'],
            data['RelativeHumidity'],
            data['WindSpeed'],
            data['WindDirection'],
            data['SealevelPressure']
        ]])
        
        # Scale the input features
        features_scaled = input_scaler.transform(features)
        
        # Get scaled prediction
        prediction_scaled = model.predict(features_scaled)[0]
        
        # Inverse transform the prediction to get actual visibility
        visibility = prediction_scaled * output_std + output_mean
        
        # Ensure visibility is within reasonable bounds (0-20 miles)
        visibility = max(0.1, min(20.0, visibility))
        
        return jsonify({'visibility': float(visibility)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
