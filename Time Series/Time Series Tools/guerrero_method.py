# Import packages
import plotly.express as px
import pandas as pd
import os
from scipy.stats import boxcox, boxcox_llf
import numpy as np
from sktime.transformations.series.boxcox import BoxCoxTransformer


# Read in the data
data = pd.read_csv('../../Software Engineering /make-example/AirPassengers.csv')


def plotting(title, data, x, y, save_file_path, x_label, y_label, text=False, lam=None):
    """General function to plot the passenger data."""
    fig = px.line(data, x=data[x], y=data[y], labels={x: x_label, y: y_label})

    fig.update_layout(template="simple_white", font=dict(size=18),
                      title_text=title, width=650,
                      title_x=0.5, height=400)

    if text:
        fig.add_annotation(x='1952-12-20', y=2.8, text=f'Lambda = {lam:.3f}',
                           align='left', yanchor='bottom', showarrow=False,
                           font=dict(size=20, color="black", family="Courier New, monospace"),
                           bordercolor='black', borderwidth=2, bgcolor="white")

    if not os.path.exists("../images"):
        os.mkdir("../images")

    fig.write_image("../images/" + str(save_file_path))

    fig.show()
#
#
# # Plot the airline passenger data
# plotting(title='Airline Passengers', data=data, save_file_path='passengers.png',
#          x='Month', y='#Passengers', x_label='Date', y_label='Passengers')
#
#
# # Range of lambda values to consider
# lambda_values = np.linspace(-2, 2, 100)
#
# likelihood_values = []
# for lam in lambda_values:
#     log_likelihood = boxcox_llf(lam, data['#Passengers'])
#     likelihood_values.append(log_likelihood)
#
# # Create a Plotly figure for the likelihood function
# fig = px.line(x=lambda_values, y=likelihood_values, labels={'x': 'Lambda', 'y': 'Log Likelihood'})
# fig.update_layout(template="simple_white", font=dict(size=18), xaxis_title='Lambda',
#                   yaxis_title='Log Likelihood', title_text='Box-Cox Likelihood Function', width=650,
#                   title_x=0.5, height=400)
#
# # Show the Plotly figure
# fig.show()
#
# # Apply box-cox transform and plot it
# data['Passengers_box_cox'], lam = boxcox(data['#Passengers'])
#
# plotting(title='Airline Passengers', data=data, save_file_path='passenger_box_cox.png',
#          x='Month', y='Passengers_box_cox', x_label='Date',
#          y_label='Passengers<br>Box-Cox Transform', text=True, lam=lam)


# Guerrero method
transformer = BoxCoxTransformer(method='guerrero', sp=12)
data['Passengers_guerrero'] = transformer.fit_transform(data['#Passengers'])

plotting(title='Airline Passengers', data=data, save_file_path='passenger_guerrero.png',
         x='Month', y='Passengers_guerrero', x_label='Date',
         y_label='Passengers<br>Guerrero Method', text=True, lam=transformer.lambda_)
