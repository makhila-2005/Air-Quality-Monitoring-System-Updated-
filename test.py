import pandas as pd
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")  # Make sure this matches your save path

# Define feature order (must match training data)
feature_names = [
    "Temperature (?C)", "Humidity (%)", "CO2 (ppm)", "PM2.5 (?g/m?)",
    "PM10 (?g/m?)", "TVOC (ppb)", "CO (ppm)", "Light Intensity (lux)",
    "Motion Detected", "Occupancy Count"
]

# Manual input — you can replace these with input() for user entry
input_values = [float(input(f"Enter {col}: ")) for col in feature_names]
# Convert to DataFrame
X_input = pd.DataFrame([input_values], columns=feature_names)

# Predict
prediction = model.predict(X_input)[0]

print(f"🌀 Predicted Ventilation Status: {prediction}")
