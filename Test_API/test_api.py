# Get Location 
# http://127.0.0.1:8000/predict?location='hyderabad'
"""
Author: Paidi Akileswar
"""
# Get coordinates
# http://api.openweathermap.org/geo/1.0/direct?q=London&appid=31bcb875021221c07d08498714738001
import requests

from Test_API.earthquake import solve
def get_location_coordinates(location):
    """
    Function to retrieve latitude and longitude coordinates for a given location.


    
    Args:
    location (str): The name of the location (e.g., city).

    Returns:
    tuple: A tuple containing latitude and longitude if location data is found, otherwise None.
    """
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&appid=31bcb875021221c07d08498714738001"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data:
            location_data = data[0]
            latitude = location_data.get('lat')
            longitude = location_data.get('lon')
            return latitude, longitude
        else:
            print("No location data found in the response.")
            return None
    else:
        print(f"Failed to retrieve data from the API. Status code: {response.status_code}")
        return None

def is_location_coastal(location):
    cities = [
    "Mumbai", "Kochi", "Chennai", "Kolkata", "Visakhapatnam", "Goa", "Puducherry", "Mangalore", "Surat", "Bhavnagar",
    "Porbandar", "Veraval", "Dwarka", "Diu", "Vasco da Gama", "Kakinada", "Machilipatnam", "Nellore", "Rajahmundry", 
    "Gopalpur", "Paradeep", "Balasore", "Chandipur", "Puri", "Digha", "Haldia", "Cuddalore", "Nagapattinam", "Karaikal", 
    "Pondicherry", "Kannur", "Kozhikode", "Thiruvananthapuram", "Alappuzha", "Kochi", "Kollam", "Karwar", "Honnavar", 
    "Udupi", "Murudeshwar", "Malvan", "Ratnagiri", "Alibag", "Daman", "Okha", "Somnath", "Mandvi", "Kandla", "Mundra", 
    "Jamnagar", "Mangrol", "Junagadh", "Gopnath", "Vasco da Gama", "Mormugao", "Harihareshwar", "Shrivardhan", "Velas", 
    "Guhagar", "Dapoli", "Revdanda", "Murud", "Vengurla", "Malpe", "Bhatkal", "Kumta", "Gokarna", "Kundapura", 
    "Ganpatipule", "Diveagar", "Harnai", "Anjarle", "Jodiya", "Navsari", "Umargam", "Vapi", "Dumas", "Khambhat", 
    "Kodinar", "Mahuva", "Nargol", "Pipavav", "Sikka", "Suvali", "Kutch", "Nani Daman", "Dharampur", "Ghoghla", 
    "Dunetha", "Maroli", "Udvada", "Mithapur", "Jodia", "Umbergaon", "Upleta", "Dahej", "Hansot", "Salaya", 
    "Srikakulam"]
    
    if location in cities: 
        return 1
    else:
        return 0

def get_pop(location):
    city_populations = {
    "Mumbai": 20694,
    "Kolkata": 24252,
    "Delhi": 11320,
    "Chennai": 26903,
    "Bengaluru": 4381,
    "Hyderabad": 18480,
    "Ahmedabad": 11778,
    "Pune": 6946,
    "Surat": 13233,
    "Jaipur": 5834,
    "Lucknow": 5527,
    "Kanpur": 4416,
    "Nagpur": 4259,
    "Visakhapatnam": 5309,
    "Indore": 25570,
    "Thane": 18634,
    "Bhopal": 11083,
    "Pimpri-Chinchwad": 11470,
    "Patna": 18228,
    "Vadodara": 6293,
    "Agra": 19575,
    "Varanasi": 3168,
    "Ludhiana": 3644,
    "Nashik": 3310,
    "Meerut": 3223,
    "Faridabad": 14065,
    "Howrah": 4096,
    "Patiala": 3310,
    "Ghaziabad": 4547,
    "Rajkot": 2681,
    "Jabalpur": 2464,
    "Thiruvananthapuram": 2331,
    "Chandigarh": 10554,
    "Mysore": 8935,
    "Navi Mumbai": 2030,
    "Amritsar": 4135,
    "Jodhpur": 1512,
    "Gwalior": 2327,
    "Vijayawada": 1040,
    "Guwahati": 1077,
    "Hubli–Dharwad": 943,
    "Coimbatore": 1616,
    "Madurai": 1461,
    "Kota": 1201,
    "Kochi": 2092,
    "Kollam": 1258,
    "Dehradun": 1695,
    "Jamnagar": 1051}
    
    if location in city_populations:
        return city_populations[location]
    else:
        return 800

    
    
def get_data(latitude , longitude , location):
    # https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=31bcb875021221c07d08498714738001
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=31bcb875021221c07d08498714738001"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        # Extracting required weather data
        temperature_celsius = round(data['main']['temp'] - 273.15, 2)  # Convert temperature from Kelvin to Celsius
        humidity = data['main']['humidity']
        windspeed_ms = round(data['wind']['speed'], 2)  # Wind speed in m/s
        windspeed_kmh = round(windspeed_ms * 3.6, 2)   # Convert wind speed from m/s to km/h
        rainfall_mm = data.get('rain', {}).get('1h', 0)  # Rainfall in mm (0 if not available)
        precipitation_mm = data.get('precipitation', {}).get('1h', 0)  # Precipitation in mm (0 if not available)

        magnitude,depth = solve(latitude,longitude)
        coastal = is_location_coastal(location)
        # Creating output dictionary
        output = {
            "temperature_celsius": temperature_celsius,
            "humidity_percent": humidity,
            "windspeed_kmh": windspeed_kmh,
            "rainfall_mm": rainfall_mm,
            "precipitation_mm": precipitation_mm,
            "magnitude": magnitude,
            "depth": depth ,
            "coastal": coastal,
            "population_density": get_pop(location),
            "distance_to_fault" : 15,
            "river_discharge": 100,
            "soil_moisture": 10,
            "soil_drift": 2,
            "slope_angle": 10,
            "tilt_readings": 10,
            "water_depth": 100,
            "seismic_activity": 2.5,
        }
        
        return output
    else:
        print(f"Failed to retrieve data from the API. Status code: {response.status_code}")
        return None

