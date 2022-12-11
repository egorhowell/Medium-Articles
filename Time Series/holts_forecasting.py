# Import packages
import plotly.graph_objects as go
import pandas as pd
import os
from statsmodels.tsa.holtwinters import SimpleExpSmoothing, Holt

# Read in the data
data = pd.read_csv('AirPassengers.csv')
data['Month'] = pd.to_datetime(data['Month'])

# Split train and test
train = data.iloc[:-int(len(data) * 0.2)]
test = data.iloc[-int(len(data) * 0.2):]


def plot_func(forecast1: list[float],
              forecast2: list[float],
              title: str,
              save_path: str) -> None:
    """Function to plot the forecasts."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=train['Month'], y=train['#Passengers'], name='Train'))
    fig.add_trace(go.Scatter(x=test['Month'], y=test['#Passengers'], name='Train'))
    fig.add_trace(go.Scatter(x=test['Month'], y=forecast1, name='Simple'))
    fig.add_trace(go.Scatter(x=test['Month'], y=forecast2, name='Holt'))
    fig.update_layout(template="simple_white", font=dict(size=18), title_text=title,
                      width=650, title_x=0.5, height=400, xaxis_title='Date',
                      yaxis_title='Passenger Volume')

    if not os.path.exists("images"):
        os.mkdir("images")

    fig.write_image("images/" + str(save_path))
    return fig.show()


# Fit simple model and get forecasts
model_simple = SimpleExpSmoothing(train['#Passengers']).fit(optimized=True)
forecasts_simple = model_simple.forecast(len(test))

# Fit Holt's model and get forecasts
model_holt = Holt(train['#Passengers'], damped_trend=True).fit(optimized=True)
forecasts_holt = model_holt.forecast(len(test))

# Plot the forecasts
plot_func(forecasts_simple, forecasts_holt, "Holt's Exponential Smoothing", 'result.png')