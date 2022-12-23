# Import packages
import plotly.graph_objects as go
import pandas as pd
import os

# Read in the data
data = pd.read_csv('../AirPassengers.csv')
data['Month'] = pd.to_datetime(data['Month'])

# Split train and test
train = data.iloc[:-int(len(data) * 0.2)]
test = data.iloc[-int(len(data) * 0.21):]


def plot_func(forecast, title, save_path):
    """Function to plot the forecasts."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=train['Month'], y=train['#Passengers'], name='Train'))
    fig.add_trace(go.Scatter(x=test['Month'], y=test['#Passengers'], name='Test'))
    fig.add_trace(go.Scatter(x=test['Month'], y=forecast, name='Forecast'))
    fig.update_layout(template="simple_white", font=dict(size=18), title_text=title,
                      width=650, title_x=0.5, height=400, xaxis_title='Date',
                      yaxis_title='Passenger Volume')

    if not os.path.exists("../images"):
        os.mkdir("../images")

    fig.write_image("images/" + str(save_path))
    return fig.show()


# Average forecast
test['mean_forecast'] = train['#Passengers'].mean()
plot_func(test['mean_forecast'], 'Average Forecast', 'average_forecast.png')

# Naive forecast
test['naive_forecast'] = train['#Passengers'].iloc[-1]
plot_func(test['naive_forecast'], 'Naive Forecast', 'naive_forecast.png')

# Seasonal naive forecast
train['month_number'] = pd.DatetimeIndex(train['Month']).month
test['month_number'] = pd.DatetimeIndex(test['Month']).month

snaive_fc = []
for row_idx, row in test.iterrows():
    month = row['month_number']
    forecast = train['#Passengers'] .loc[train['month_number'] == month].iloc[-1]
    snaive_fc.append(forecast)

plot_func(snaive_fc, 'Seasonal Naive Forecast', 'snaive_forecast.png')

# Drift forecast
constant = (train['#Passengers'].iloc[-1] - train['#Passengers'].iloc[0])/(len(train)-1)
test['h'] = range(len(test))
test['drift_forecast'] = train['#Passengers'].iloc[-1] + test['h']*constant

plot_func(test['drift_forecast'], 'Drift Forecast', 'drift_forecast.png')