""" 
Script to predict tsunami occurrence using a trained Random Forest classifier.

Author:
Paidi Akileswar

Packages:
pandas - pip install pandas
scikit-learn - pip install scikit-learn

Usage:
python3 tsunami_prediction.py
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import warnings

def tsunami_prediction(ex_data):
    # Load the dataset
    warnings.filterwarnings('ignore')
    data = pd.read_csv(r'Final_React_app\datasets\tsunami_dataset.csv')

    # Split the dataset into features (X) and target variable (y)
    X = data.drop('Tsunami_Occurrence', axis=1)
    y = data['Tsunami_Occurrence']
    # print(X,y)
    # Split the data into training and testing sets (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest Classifier model
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)

    # Make predictions on the testing set
    rf_preds = rf_model.predict(X_test)

    # Calculate accuracy for the model
    accuracy = accuracy_score(y_test, rf_preds)
    # print("Random Forest Accuracy:", accuracy)

    # Predict the example data point
    prediction = rf_model.predict(ex_data)
    # print("Predicted Tsunami Occurrence:", prediction)

    return prediction

# if __name__ == "__main__":
#     # Example values for Tilt_Readings, Water_Depth, Seismic_Activity, Coastal_Location
#     warnings.filterwarnings('ignore')
#     example_data = [[30, 150, 7, 1]] 
    
#     # Call the function
#     prediction = tsunami_prediction(example_data)
#     print(prediction)
