import json
from Final_React_app.earthquake_model import predict_earthquake
from Final_React_app.flood_model import predict_flood_occurrence
from Final_React_app.landslide_model import predict_landslide_occurrence
from Final_React_app.tsunami_model import tsunami_prediction
from Final_React_app.wildfire_model import predict_wildfire_occurrence

from Test_API.test_api import get_location_coordinates,get_data
"""
Script to predict natural disasters using pre-trained models.

Author: Paidi Akileswar

Packages:
- earthquake_model: Module containing functions for earthquake prediction.
- flood_model: Module containing functions for flood prediction.
- landslide_model: Module containing functions for landslide prediction.
- tsunami_model: Module containing functions for tsunami prediction.
- wildfire_model: Module containing functions for wildfire prediction.

Usage:
- Make predictions for various natural disasters using data obtained from APIs.
- Store predictions in a JSON file.
import json
from earthquake_model import predict_earthquake
from flood_model import predict_flood_occurrence
from landslide_model import predict_landslide_occurrence
from tsunami_model import tsunami_prediction
from wildfire_model import predict_wildfire_occurrence

"""

def get_predictions(location):
    """
    Function to predict natural disasters using pre-trained models and return predictions.

    Returns:
    predictions (dict): Predictions for various natural disasters in JSON format.
    """
    # Given data from APIs

    latitude, longitude = get_location_coordinates(location)
    # print("Location coordinates:", latitude, longitude)
    
    output = get_data(latitude, longitude , location)
    # print("Weather data:", output)
    
    temperature_celsius = output['temperature_celsius']
    humidity_percent = output['humidity_percent']
    windspeed_kmh = output['windspeed_kmh']
    rainfall_mm = output['rainfall_mm']
    precipitation_mm = output['precipitation_mm']
    magnitude = output['magnitude']
    depth = output['depth']
    coastal = output['coastal']
    population_density = output['population_density']
    distance_to_fault = output['distance_to_fault']
    river_discharge = output['river_discharge']
    soil_moisture = output['soil_moisture']
    soil_drift = output['soil_drift']
    slope_angle = output['slope_angle']
    tilt_readings = output['tilt_readings']
    water_depth = output['water_depth']
    seismic_activity = output['seismic_activity']
    dryness_index = 20
    building_density = 0.3
    river_stage = 5

    earthquake_data = [[magnitude, depth, distance_to_fault, population_density, building_density]]
    rainfall_data = [[precipitation_mm, river_discharge, river_stage, temperature_celsius,soil_moisture]]
    soil_drift_data = [[soil_drift,rainfall_mm, slope_angle,temperature_celsius]]
    tilt_data = [[tilt_readings, water_depth, seismic_activity, coastal]]
    temperature_data = [[temperature_celsius, humidity_percent, windspeed_kmh,rainfall_mm , dryness_index]]
    
    try:
        print("Predicting earthquake...")
        earthquake_prediction = predict_earthquake(earthquake_data)
        print("Earthquake prediction completed.")
    except Exception as e:
        print("Error predicting earthquake:", e)
        earthquake_prediction = "error"
    print("===========> COMPLETED <===============\n\n")

    try:
        print("Predicting flood...")
        flood_prediction = predict_flood_occurrence(rainfall_data)  # Using rainfall data for flood prediction
        print("Flood prediction completed.")
    except Exception as e:
        print("Error predicting flood:", e)
        flood_prediction = "error"
    print("===========> COMPLETED <===============\n\n")

    try:
        print("Predicting landslide...")
        landslide_prediction = predict_landslide_occurrence(soil_drift_data)
        print("Landslide prediction completed.")
    except Exception as e:
        print("Error predicting landslide:", e)
        landslide_prediction = "error"
    print("===========> COMPLETED <===============\n\n")

    try:
        print("Predicting tsunami...")
        tsunami_prediction_result = tsunami_prediction(tilt_data)
        print("Tsunami prediction completed.")
    except Exception as e:
        print("Error predicting tsunami:", e)
        tsunami_prediction_result = "error"
    print("===========> COMPLETED <===============\n\n")

    try:
        print("Predicting wildfire...")
        wildfire_prediction = predict_wildfire_occurrence(temperature_data)
        print("Wildfire prediction completed.")
    except Exception as e:
        print("Error predicting wildfire:", e)
        wildfire_prediction = "error"
    print("===========> COMPLETED <===============\n\n")

    # Convert predictions to JSON format
    predictions = {
        'flood': {'reading': f'{rainfall_data[0][0]} milli meters', 'prediction': 'yes' if flood_prediction == 1 else 'no'},
        'earthquake': {'reading': f'{earthquake_data[0][0]} Ritcher Scale', 'prediction': 'yes' if earthquake_prediction == 1 else 'no'},
        'landslide': {'reading': f'{soil_drift_data[0][2]} Slope Angle', 'prediction': 'yes' if landslide_prediction == 1 else 'no'},
        'tsunami': {'reading': f'{tilt_data[0][2]} Seismic Activity', 'prediction': 'yes' if tsunami_prediction_result == 1 else 'no'},
        'wildfire': {'reading': f'{temperature_data[0][0]} Degree Celsius', 'prediction': 'yes' if wildfire_prediction == 1 else 'no'}
    }

    return predictions

# if __name__ == "__main__":
#     predictions = get_predictions()
#     # Save predictions to a JSON file
#     with open('predictions.json', 'w') as json_file:
#         json.dump(predictions, json_file)
#     print("Predictions saved to predictions.json")
