import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def predict_landslide_occurrence(sample_data):
    # Load the dataset
    data = pd.read_csv('landslide_dataset.csv')

    # Split the data into features (X) and target variable (y)
    X = data.drop('Landslide_Occurrence', axis=1)
    y = data['Landslide_Occurrence']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the Random Forest classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X_train, y_train)

    # Predict the sample data
    sample_prediction = rf_classifier.predict(sample_data)
    
    return sample_prediction

# Example sample data [Soil_Drift, Rainfall, Slope_Angle, Temperature]
# sample_data = np.array([[7.5, 80, 25, 35]])
# prediction = predict_landslide_occurrence(sample_data)
# print("Sample Prediction:", prediction)
