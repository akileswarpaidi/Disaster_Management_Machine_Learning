import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data for each feature
soil_drift = np.random.uniform(0, 10, size=10000)  # Example: soil drift readings
rainfall = np.random.uniform(0, 100, size=10000)  # Example: rainfall data in mm
slope_angle = np.random.uniform(0, 30, size=10000)  # Example: slope angle data in degrees
temperature = np.random.uniform(0, 40, size=10000)  # Example: temperature data in degrees Celsius

# Define a function to determine landslide occurrence based on feature values
def determine_landslide(soil_drift, rainfall, slope_angle, temperature):
    # Define landslide conditions based on thresholds
    if soil_drift > 5 and rainfall > 50 and slope_angle > 20 and temperature > 30:
        return 1  # Landslide occurred
    else:
        return 0  # No landslide

# Apply the function to determine landslide occurrence for each row
landslide_occurrence = np.array([determine_landslide(sd, rf, sa, temp) for sd, rf, sa, temp in zip(soil_drift, rainfall, slope_angle, temperature)])

# Create a pandas DataFrame to store the data
data = pd.DataFrame({
    'Soil_Drift': soil_drift,
    'Rainfall': rainfall,
    'Slope_Angle': slope_angle,
    'Temperature': temperature,
    'Landslide_Occurrence': landslide_occurrence
})

# Display the first few rows of the generated dataset
print(data.head())

# Save the dataset to a CSV file
data.to_csv('landslide_dataset.csv', index=False)
