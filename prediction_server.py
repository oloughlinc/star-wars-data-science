from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
from fastparquet import ParquetFile
from fastparquet import write
import pyarrow as pa

print('loading model...')
with open("trained_model.pkl", 'rb') as f:
    model = pickle.load(f)
print('model loaded!')
    
print('loading data...')
df = pd.read_parquet('clean_data.parquet', engine='fastparquet')
print('data loaded')

print('building homeworlds and units')
homeworlds = df['homeworld'].unique().tolist()
units = df['unit_type'].unique().tolist()
print('complete!')

# def retrieveHomeworldList():
#     return df['homeworld'].tolist()

# def retrieveUnitList():
#     return df['unit_type'].tolist()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.get('/api/homeworlds')
def getHomeworlds():
    return jsonify(homeworlds)

@app.get('/api/units')
def getUnits():
    return jsonify(units)

# thanks chatgpt
def preprocess_data(planet, unit):
    # One-hot encode 'planet' and 'unit'
    planet_encoded = np.zeros(len(homeworlds))
    print(planet_encoded)
    print(homeworlds)
    print(planet)
    planet_encoded[homeworlds.index(planet)] = 1

    unit_encoded = np.zeros(len(units))
    unit_encoded[units.index(unit)] = 1

    # Concatenate encoded features
    features = np.concatenate([planet_encoded, unit_encoded])

    return features.reshape(1, -1)  # Reshape to (1, n_features) to match model input shape


@app.post('/api/predict')
def makePrediction():
    data = request.get_json()
    print(data)
    # pred_df = pd.DataFrame(data)
    # print(pred_df)
    # X = pred_df[['homeworld', 'unit_type']]
    # encoded = pd.get_dummies(X)
    # print(encoded)
    y_pred = model.predict(preprocess_data(data['homeworld'][0], data['unit_type'][0]))
    print(y_pred.tolist())
    return jsonify(['Resistance' if y_pred[0] else 'Empire'])

# makePrediction({
# 'homeworld': ['Rodia'], 
# 'unit_type': ['x-wing']
# })
