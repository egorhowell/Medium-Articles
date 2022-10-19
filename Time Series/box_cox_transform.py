# Import packages
import plotly.express as px
import pandas as pd
import os
from scipy.stats import boxcox

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
plotting_stock_price(title='Airline Passengers', data=data, save_file_path='passengers.png', x='Month',
                     y='#Passengers', x_label='Date', y_label='Passengers')

# Apply box-cox transform
data['Passengers_box_cox'], lam = boxcox(data['#Passengers'])
print(lam)

plotting(title='Airline Passengers', data=data, save_file_path='passenger_box_cox.png',
         x='Month', y='Passengers_box_cox', x_label='Date', y_label='Passenger<br>Box-Cox Transform')

