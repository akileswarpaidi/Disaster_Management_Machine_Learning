import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_random_forest_model(dataset_path):
    # Load the dataset
    data = pd.read_csv(dataset_path)

    # Split data into features and target variable
    X = data.drop('Earthquake_Occurrence', axis=1)
    y = data['Earthquake_Occurrence']

    feature_names = X.columns.tolist()
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
    print("Accuracy of Random Forest Classifier:", accuracy)

    # Return trained model
    return rf_classifier

def predict_example(model, example_features):
    # Make prediction for example features
    prediction = model.predict(example_features)
    print("Prediction for example:", prediction)
    return prediction

# Example usage
# trained_model = train_random_forest_model('earthquake_dataset.csv')
# example_features = [[55, 310, 6, 32, 75]]  # Example features for prediction
# prediction = predict_example(trained_model, example_features)
