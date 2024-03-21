""" 
Script to train a Random Forest classifier on earthquake dataset and make predictions.

Author:
Paidi Akileswar

Packages:
pandas - pip install pandas
scikit-learn - pip install scikit-learn

Usage:
python3 earthquake_prediction.py
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import warnings

def train_random_forest_model(dataset_path):
    # Load the dataset
    warnings.filterwarnings('ignore')
    data = pd.read_csv(dataset_path)

    # Split data into features and target variable
    X = data.drop('Earthquake_Occurrence', axis=1)
    y = data['Earthquake_Occurrence']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize Random Forest Classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train the model
    rf_classifier.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = rf_classifier.predict(X_test)

    # Evaluate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    # print("Accuracy of Random Forest Classifier:", accuracy)

    # Return trained model
    return rf_classifier

def predict_earthquake(example_features):
    # Make prediction for example features
    model = train_random_forest_model('Final_React_app\datasets\earthquake_dataset.csv')
    prediction = model.predict(example_features)
    # print("Prediction for example:", prediction)
    return prediction

# if __name__ == "__main__":
#     # Example usage
#     warnings.filterwarnings('ignore')
#     example_features = [[55, 310, 6, 32, 75]]  # Example features for prediction
#     prediction = predict_earthquake(example_features)
#     print("Prediction for example:", prediction)
