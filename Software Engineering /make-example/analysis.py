# Import packages
import plotly.graph_objects as go
import pandas as pd
import os

# Read in the data
data = pd.read_csv('AirPassengers.csv')


def plot_forecasts(forecasts: list[float], title: str, save_path: str) -> None:
    """Function to plot the forecasts."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=train['Month'], y=train['#Passengers'], name='Train'))
    fig.add_trace(go.Scatter(x=test['Month'], y=test['#Passengers'], name='Test'))
    fig.add_trace(go.Scatter(x=test['Month'], y=forecasts, name='Forecast'))
    fig.update_layout(template="simple_white", font=dict(size=18), title_text=title,
                      width=650, title_x=0.5, height=400, xaxis_title='Date',
                      yaxis_title='Passenger Volume')

    if not os.path.exists("../images"):
        os.mkdir("../images")

    fig.write_image("../images/" + str(save_path))
    return fig.show()


# Plot the forecasts
plot_forecasts(forecasts, 'ARIMA', 'result.png')
