import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data for each feature
precipitation = np.random.uniform(0, 100, size=10000)  # Example: precipitation data in mm
river_discharge = np.random.uniform(0, 500, size=10000)  # Example: river discharge data in cubic meters per second
river_stage = np.random.uniform(0, 10, size=10000)  # Example: river stage data in meters
weather_forecast = np.random.uniform(0, 40, size=10000)  # Example: weather forecast data in degrees Celsius
soil_moisture = np.random.uniform(0, 100, size=10000)  # Example: soil moisture data as a percentage

# Define a function to determine flood occurrence based on feature values
def determine_flood(precipitation, river_discharge, river_stage, weather_forecast, soil_moisture):
    # Define flood conditions based on thresholds
    if precipitation > 50 and river_discharge > 300 and river_stage > 5 and weather_forecast > 30 and soil_moisture > 70:
        return 1  # Flood occurred
    else:
        return 0  # No flood

# Apply the function to determine flood occurrence for each row
flood_occurrence = np.array([determine_flood(p, rd, rs, wf, sm) for p, rd, rs, wf, sm in zip(precipitation, river_discharge, river_stage, weather_forecast, soil_moisture)])

# Create a pandas DataFrame to store the data
data = pd.DataFrame({
    'Precipitation': precipitation,
    'River_Discharge': river_discharge,
    'River_Stage': river_stage,
    'Weather_Forecast': weather_forecast,
    'Soil_Moisture': soil_moisture,
    'Flood_Occurrence': flood_occurrence
})

# Display the first few rows of the generated dataset
print(data.head())

# Save the dataset to a CSV file
data.to_csv('flood_dataset.csv', index=False)
