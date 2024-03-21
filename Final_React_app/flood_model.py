""" 
Script to train a Gradient Boosting classifier on flood dataset and make predictions.

Author:
Paidi Akileswar

Packages:
pandas - pip install pandas
scikit-learn - pip install scikit-learn

Usage:
python3 flood_prediction.py
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import warnings

def train_gb_classifier(dataset_path):
    # Load the dataset
    warnings.filterwarnings('ignore')
    data = pd.read_csv(dataset_path)

    # Extract features and target variable
    X = data[['Precipitation', 'River_Discharge', 'River_Stage', 'Weather_Forecast', 'Soil_Moisture']]
    y = data['Flood_Occurrence']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the Gradient Boosting Classifier
    gb_classifier = GradientBoostingClassifier(n_estimators=100, random_state=42)

    # Train the classifier
    gb_classifier.fit(X_train, y_train)

    # Predict on the test set
    y_pred = gb_classifier.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    # print("Accuracy:", accuracy)

    # Return trained classifier
    return gb_classifier

def predict_flood_occurrence(features):
    # Predict for given features
    classifier = train_gb_classifier(r'Final_React_app\datasets\flood_dataset.csv')
    prediction = classifier.predict(features)
    return prediction

# if __name__ == "__main__":
#     warnings.filterwarnings('ignore')
#     example_features = [[55, 310, 6, 32, 75]]  # Example features for prediction
#     prediction = predict_flood_occurrence(example_features)
#     print("Prediction for example:", prediction)
