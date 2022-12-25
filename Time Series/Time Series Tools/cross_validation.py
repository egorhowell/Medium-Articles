# Import packages
import plotly.graph_objects as go
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
import os


# Read in the data
data = pd.read_csv('../AirPassengers.csv')
data['Month'] = pd.to_datetime(data['Month'])

# Split modelling and test
df_model = data.iloc[:-int(len(data) * 0.2)]
df_test = data.iloc[-int(len(data) * 0.2):]

# Cross validation split
tscv = TimeSeriesSplit(n_splits=3)
for train_index, valid_index in tscv.split(df_model):
    print(train_index, valid_index)


