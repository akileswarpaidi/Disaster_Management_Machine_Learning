import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data for temperature and other features
temperature = np.random.uniform(0, 40, size=10000)  # Example: temperature data in degrees Celsius
humidity = np.random.uniform(0, 100, size=10000)  # Example: humidity data as a percentage
wind_speed = np.random.uniform(0, 30, size=10000)  # Example: wind speed data in km/h
rainfall = np.random.uniform(0, 20, size=10000)  # Example: rainfall data in mm
dryness_index = np.random.uniform(0, 100, size=10000)  # Example: dryness index data

# Define a function to determine wildfire occurrence based on feature values
def determine_wildfire(temperature, humidity, wind_speed, rainfall, dryness_index):
    # Define wildfire conditions based on thresholds
    if temperature > 30 and humidity < 40 and wind_speed > 10 and rainfall < 10 and dryness_index > 50:
        return 1  # Wildfire occurred
    else:
        return 0  # No wildfire

# Apply the function to determine wildfire occurrence for each row
wildfire_occurrence = np.array([determine_wildfire(temp, hum, ws, rain, di) for temp, hum, ws, rain, di in zip(temperature, humidity, wind_speed, rainfall, dryness_index)])

# Create a pandas DataFrame to store the data
data = pd.DataFrame({
    'Temperature': temperature,
    'Humidity': humidity,
    'Wind_Speed': wind_speed,
    'Rainfall': rainfall,
    'Dryness_Index': dryness_index,
    'Wildfire_Occurrence': wildfire_occurrence
})

# Display the first few rows of the generated dataset
print(data.head())

# Save the dataset to a CSV file
data.to_csv('wildfire_dataset.csv', index=False)
