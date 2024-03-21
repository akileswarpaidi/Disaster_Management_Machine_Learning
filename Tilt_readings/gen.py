import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data for each feature
tilt_readings = np.random.uniform(-90, 90, size=10000)  # Example: tilt readings in degrees
water_depth = np.random.uniform(0, 500, size=10000)  # Example: water depth in meters
seismic_activity = np.random.uniform(0, 10, size=10000)  # Example: seismic activity level
coastal_location = np.random.choice([0, 1], size=10000)  # Example: binary coastal location (0 for inland, 1 for coastal)

# Define a function to determine tsunami occurrence based on feature values
def determine_tsunami(tilt_readings, water_depth, seismic_activity, coastal_location):
    # Define tsunami conditions based on thresholds
    if tilt_readings > 45 and water_depth > 100 and seismic_activity > 5 and coastal_location == 1:
        return 1  # Tsunami occurred
    else:
        return 0  # No tsunami

# Apply the function to determine tsunami occurrence for each row
tsunami_occurrence = np.array([determine_tsunami(tr, wd, sa, cl) for tr, wd, sa, cl in zip(tilt_readings, water_depth, seismic_activity, coastal_location)])

# Create a pandas DataFrame to store the data
data = pd.DataFrame({
    'Tilt_Readings': tilt_readings,
    'Water_Depth': water_depth,
    'Seismic_Activity': seismic_activity,
    'Coastal_Location': coastal_location,
    'Tsunami_Occurrence': tsunami_occurrence
})

# Display the first few rows of the generated dataset
print(data.head())

# Save the dataset to a CSV file
data.to_csv('tsunami_dataset.csv', index=False)
