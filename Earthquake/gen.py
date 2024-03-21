import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic earthquake data
# Define features
num_samples = 10000
magnitude = np.random.uniform(2.0, 9.0, num_samples)  # Magnitude of the earthquake
depth = np.random.uniform(1.0, 700.0, num_samples)  # Depth of the earthquake (in kilometers)
distance_to_fault = np.random.uniform(1.0, 100.0, num_samples)  # Distance to the fault line (in kilometers)
population_density = np.random.uniform(10, 10000, num_samples)  # Population density of the area (people per square kilometer)
building_density = np.random.uniform(0.1, 1.0, num_samples)  # Building density of the area (fraction of land covered by buildings)

# Determine earthquake occurrence based on rules
# Define a function to determine earthquake occurrence
def determine_earthquake(magnitude, depth, distance_to_fault, population_density, building_density):
    # Define earthquake conditions based on thresholds
    if magnitude > 5.0 and depth < 100.0 and distance_to_fault < 50.0 and population_density > 1000.0 and building_density > 0.5:
        return 1  # Earthquake occurred
    else:
        return 0  # No earthquake

# Apply the function to determine earthquake occurrence for each row
earthquake_occurrence = np.array([determine_earthquake(m, d, df, pd, bd) for m, d, df, pd, bd in zip(magnitude, depth, distance_to_fault, population_density, building_density)])

# Create a pandas DataFrame to store the data
data = pd.DataFrame({
    'Magnitude': magnitude,
    'Depth': depth,
    'Distance_to_Fault': distance_to_fault,
    'Population_Density': population_density,
    'Building_Density': building_density,
    'Earthquake_Occurrence': earthquake_occurrence
})

# Display the first few rows of the generated dataset
print(data.head())

# Save the dataset to a CSV file
data.to_csv('earthquake_dataset.csv', index=False)
