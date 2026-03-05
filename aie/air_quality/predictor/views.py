from django.shortcuts import render
import joblib
import os
import requests

# Load the model once
MODEL_PATH = os.path.join('model.pkl')
model = joblib.load(MODEL_PATH)

# Define sensor labels
labels = [
    "Temperature", "Humidity", "CO2", "PM2.5", "PM10",
    "TVOC", "CO", "Light", "Motion", "Occupancy"
]

# ThingSpeak channel info
channel_id = '3017296'
thingspeak_url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?results=1'

def predict_view(request):
    result = None
    thingspeak_data = {}

    try:
        # Fetch real-time data from ThingSpeak
        response = requests.get(thingspeak_url).json()
        feed = response['feeds'][0]
        for i in range(1, 7):
            thingspeak_data[f'field{i}'] = feed.get(f'field{i}', 'N/A')
    except Exception as e:
        thingspeak_data = {"error": f"Failed to fetch ThingSpeak data: {e}"}

    if request.method == "POST":
        try:
            features = [float(request.POST[label.lower()]) for label in labels]
            prediction = model.predict([features])[0]
            result = prediction
        except Exception as e:
            result = f"Error: {e}"

    return render(request, 'index.html', {
        'labels': labels,
        'result': result,
        'thingspeak_data': thingspeak_data
    })
