# Import packages
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import os
from statsmodels.graphics.tsaplots import plot_acf

# Read in the data
data = pd.read_csv('../AirPassengers.csv')
data['Month'] = pd.to_datetime(data['Month'])


def plot_passenger_volumes(df: pd.DataFrame,
                           y: str,
                           save_file_path: str) -> None:
    """General function to plot the passenger data."""

    fig = px.line(df, x='Month', y=y, labels={'Month': 'Date'})
    fig.update_layout(template="simple_white", font=dict(size=18), title_text='Airline Passengers',
                      width=650, title_x=0.5, height=400)

    if not os.path.exists("../images"):
        os.mkdir("../images")
    fig.write_image("../images/" + str(save_file_path))

    return fig.show()


# Plot the airline passenger data
plot_passenger_volumes(df=data, y='#Passengers', save_file_path='passengers_data.png')

# Plot autocorrelation
plt.rc("figure", figsize=(11,5))
plot_acf(data['#Passengers'])
plt.xlabel('Lags', fontsize=18)
plt.ylabel('Correlation', fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.title('Autocorrelation Plot', fontsize=20)
plt.tight_layout()
plt.show()

# Split train and test
train = data.iloc[:-int(len(data) * 0.2)]
test = data.iloc[-int(len(data) * 0.2):]


# def plot_forecasts(forecasts: list[float], title: str, save_path: str) -> None:
#     """Function to plot the forecasts."""
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=train['Month'], y=train['#Passengers'], name='Train'))
#     fig.add_trace(go.Scatter(x=test['Month'], y=test['#Passengers'], name='Test'))
#     fig.add_trace(go.Scatter(x=test['Month'], y=forecasts, name='Forecast'))
#     fig.update_layout(template="simple_white", font=dict(size=18), title_text=title,
#                       width=650, title_x=0.5, height=400, xaxis_title='Date',
#                       yaxis_title='Passenger Volume')
#
#     if not os.path.exists("../images"):
#         os.mkdir("../images")
#
#     fig.write_image("../images/" + str(save_path))
#     return fig.show()
#
#
# # Plot the forecasts
# plot_forecasts(forecasts, 'Moving Average Model', 'result.png')
