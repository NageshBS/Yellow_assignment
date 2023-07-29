from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GOOGLE_PLACES_API_KEY = 'AIzaSyD4mBGQhGV_tiV13CXb1HbSnJaG5asgD4I'
# Temporary storage for past 10 locations
past_locations = []

@app.route('/restaurants', methods=['POST'])
def get_restaurants():
    data = request.get_json()
    lat = 37.7749
    lon = 122.4194
    # To Store the current location in past_locations
    past_locations.append({'latitude': lat, 'longitude': lon})
    if len(past_locations) > 10:
        past_locations.pop(0)

    # Get the closest restaurants using the Google Places API
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lon}&radius=5000&type=restaurant&key={AIzaSyD4mBGQhGV_tiV13CXb1HbSnJaG5asgD4I}'
    response = requests.get(url)
    restaurants_data = response.json()
    restaurants = restaurants_data.get('results', [])

    return jsonify({'restaurants': restaurants, 'past_locations': past_locations})

if __name__ == '__main__':
    app.run(debug=True)
