# Import packages
import plotly.express as px
import pandas as pd
import os
from statsmodels.tsa.stattools import adfuller
import numpy as np

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
plotting(title='Airline Passengers', data=data, save_file_path='passengers.png', x='Month',
         y='#Passengers', x_label='Date', y_label='Passengers')


# Take the difference and plot it
data["Passenger_Diff"] = data["#Passengers"].diff()

plotting(title='Airline Passengers', data=data,
         save_file_path='passengers_one_difference.png', x='Month', y='Passenger_Diff',
         x_label='Date', y_label='Passengers<br>Difference Transform')


# Take the log and plot it
data["Passenger_Log"] = np.log(data["#Passengers"])

plotting(title='Airline Passengers', data=data,
         save_file_path='passenger_log.png', x='Month',
         y='Passenger_Log', x_label='Date', y_label='Passenger<br>Log Transform')


# Take the difference and log and plot it
data["Passenger_Diff_Log"] = data["Passenger_Log"].diff()

plotting(title='Airline Passengers', data=data,
         save_file_path='passenger_difference_and_log.png', x='Month',
         y='Passenger_Diff_Log', x_label='Date', y_label='Passenger<br>Log and Difference')


# ADF test
def adf_test(series):
    """Using an ADF test to determine if a series is stationary"""
    test_results = adfuller(series)
    print('ADF Statistic: ', test_results[0])
    print('P-Value: ', test_results[1])
    print('Critical Values:')
    for thres, adf_stat in test_results[4].items():
        print('\t%s: %.2f' % (thres, adf_stat))


adf_test(data["Passenger_Diff_Log"][1:])
