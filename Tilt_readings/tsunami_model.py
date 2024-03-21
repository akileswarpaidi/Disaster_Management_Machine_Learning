import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def tsunami_prediction():
    # Load the dataset
    data = pd.read_csv('tsunami_dataset.csv')

    # Split the dataset into features (X) and target variable (y)
    X = data.drop('Tsunami_Occurrence', axis=1)
    y = data['Tsunami_Occurrence']

    # Split the data into training and testing sets (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest Classifier model
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)

    # Make predictions on the testing set
    rf_preds = rf_model.predict(X_test)

    # Calculate accuracy for the model
    accuracy = accuracy_score(y_test, rf_preds)
    print("Random Forest Accuracy:", accuracy)

    # Example data point for prediction
    example_data = [[30, 150, 7, 1]]  # Example values for Tilt_Readings, Water_Depth, Seismic_Activity, Coastal_Location

    # Predict the example data point
    prediction = rf_model.predict(example_data)
    print("Predicted Tsunami Occurrence:", prediction)

    return accuracy, prediction

# Call the function
accuracy, prediction = tsunami_prediction()
print(accuracy, prediction)
