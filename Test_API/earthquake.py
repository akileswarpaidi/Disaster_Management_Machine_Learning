import requests

def get_earthquake_data(latitude, longitude, radius_km=100):
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&latitude={latitude}&longitude={longitude}&maxradiuskm={radius_km}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        earthquakes = data.get('features', [])
        return earthquakes
    else:
        print(f"Failed to retrieve earthquake data. Status code: {response.status_code}")
        return None

def filter_earthquakes_by_location(earthquakes, target_latitude, target_longitude, max_distance_km=50):
    filtered_earthquakes = []
    for earthquake in earthquakes:
        quake_latitude = earthquake['geometry']['coordinates'][1]
        quake_longitude = earthquake['geometry']['coordinates'][0]
        distance = calculate_distance(target_latitude, target_longitude, quake_latitude, quake_longitude)
        if distance <= max_distance_km:
            filtered_earthquakes.append(earthquake)
    return filtered_earthquakes

def calculate_distance(lat1, lon1, lat2, lon2):
    # This function calculates the distance between two geographical coordinates using Haversine formula
    # You can replace it with a more accurate distance calculation method if needed
    from math import radians, sin, cos, sqrt, atan2
    R = 6371.0  # Radius of the Earth in kilometers
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def solve(latitude,longitude):
    earthquakes = get_earthquake_data(latitude, longitude)
    if earthquakes:
        filtered_earthquakes = filter_earthquakes_by_location(earthquakes, latitude, longitude)
        
        if filtered_earthquakes:
            for earthquake in filtered_earthquakes:
                magnitude = earthquake['properties']['mag']
                depth = earthquake['geometry']['coordinates'][2]
                return magnitude, depth
        else:
            return 0,0
    else:
        return 0,0
