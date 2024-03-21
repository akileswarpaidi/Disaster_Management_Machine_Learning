""" 
Script to train a logistic regression model for predicting wildfire occurrence.

Author:
Paidi Akileswar

Packages:
pandas - pip install pandas
scikit-learn - pip install scikit-learn

Usage:
python3 wildfire_prediction.py
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import warnings

def train_logistic_regression(dataset_path):
    # Load the dataset
    warnings.filterwarnings('ignore')
    data = pd.read_csv(dataset_path)

    # Extract features and target variable
    X = data.drop('Wildfire_Occurrence', axis=1)
    y = data['Wildfire_Occurrence']
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the logistic regression model
    log_reg_model = LogisticRegression(random_state=42)

    # Train the model
    log_reg_model.fit(X_train, y_train)

    # Return trained model
    return log_reg_model

def predict_wildfire_occurrence(data):
    # Predict for given features
    model = train_logistic_regression('Final_React_app\datasets\wildfire_dataset.csv')
    predictions = model.predict(data)
    return predictions

# Example usage
# if __name__ == "__main__":
#     example_data = [[30, 60, 10, 0.5, 1013]]  # Example data for prediction
#     warnings.filterwarnings('ignore')
#     prediction = predict_wildfire_occurrence(example_data)
#     print("Prediction for example:", prediction)
