from flask import Flask, jsonify

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

@app.get('/api/homeworlds')
def getHomeworlds():
    return jsonify(homeworlds)

@app.get('/api/units')
def getUnits():
    return jsonify(units)

