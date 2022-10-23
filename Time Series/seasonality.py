# Import packages
import plotly.express as px
import pandas as pd
import os
from statsmodels.tsa.stattools import adfuller

# Read in the data
data = pd.read_csv('AirPassengers.csv')


def plotting(title, data, x, y, save_file_path, x_label, y_label):
    """General function to plot the passenger data."""
    fig = px.line(data, x=data[x], y=data[y], labels={x: x_label, y: y_label})

    fig.update_layout(template="simple_white", font=dict(size=18),
                      title_text=title, width=650,
                      title_x=0.5, height=400)

    if not os.path.exists("images"):
        os.mkdir("images")

    fig.write_image("images/" + str(save_file_path))

    fig.show()


# Plot the airline passenger data
plotting(title='Airline Passengers', data=data, save_file_path='passengers.png',
         x='Month', y='#Passengers', x_label='Date', y_label='Passengers')

# Take the seasonal difference and plot it
data["Passenger_Season_Diff"] = data["#Passengers"].diff(periods=12)

plotting(title='Airline Passengers', data=data,
         save_file_path='passenger_seasonal_difference.png', x='Month',
         y='Passenger_Season_Diff', x_label='Date', y_label='Passenger<br>Seasonal Difference')


# ADF test
def adf_test(series):
    """Using an ADF test to determine if a series is stationary"""
    test_results = adfuller(series)
    print('ADF Statistic: ', test_results[0])
    print('P-Value: ', test_results[1])
    print('Critical Values:')
    for thres, adf_stat in test_results[4].items():
        print('\t%s: %.2f' % (thres, adf_stat))


adf_test(data["Passenger_Season_Diff"][12:])