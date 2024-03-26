from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from flask import Flask, render_template, request, make_response
from flask import Flask, render_template, request, redirect, url_for, flash
import os

from flask_cors import CORS
from Final_React_app.final_model import get_predictions

app = Flask(__name__)
app.secret_key = 'secret_key'
db_name = 'users.db'
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict():
    location = request.args.get('location')
    if location:
        predictions = get_predictions(location)
        return jsonify(predictions)
    else:
        return jsonify({"error": "Location parameter is missing."})

if __name__ == '__main__':
    app.run()
