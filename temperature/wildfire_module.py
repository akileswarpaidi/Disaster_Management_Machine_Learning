import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def train_logistic_regression(dataset_path):
    # Load the dataset
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

def predict_wildfire_occurrence(model, example_data):
    # Predict for given features
    predictions = model.predict(example_data)
    return predictions

# Example usage
if __name__ == "__main__":
    trained_model = train_logistic_regression('wildfire_dataset.csv')
    example_data = [[30, 60, 10, 0.5, 1013]]  # Example data for prediction
    prediction = predict_wildfire_occurrence(trained_model, example_data)
    print("Prediction for example:", prediction)
