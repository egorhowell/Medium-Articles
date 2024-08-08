# Import packages
import os

import pandas as pd
import plotly.graph_objects as go
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

# Read in the data
data = pd.read_csv("../../Software Engineering /make-example/AirPassengers.csv")
data["Month"] = pd.to_datetime(data["Month"])

# Split train and test
train = data.iloc[: -int(len(data) * 0.2)]
test = data.iloc[-int(len(data) * 0.2) :]


def plot_func(forecast: list[float], title: str, save_path: str) -> None:
    """Function to plot the forecasts."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=train["Month"], y=train["#Passengers"], name="Train"))
    fig.add_trace(go.Scatter(x=test["Month"], y=test["#Passengers"], name="Test"))
    fig.add_trace(go.Scatter(x=test["Month"], y=forecast, name="Forecast"))
    fig.update_layout(
        template="simple_white",
        font=dict(size=18),
        title_text=title,
        width=650,
        title_x=0.5,
        height=400,
        xaxis_title="Date",
        yaxis_title="Passenger Volume",
    )

    if not os.path.exists("../images"):
        os.mkdir("../images")

    fig.write_image("../images/" + str(save_path))
    return fig.show()


# Fit model and get forecasts
model = SimpleExpSmoothing(train["#Passengers"]).fit(optimized=True)
forecasts = model.forecast(len(test))

# Plot the forecasts
plot_func(forecasts, "Simple Exponential Smoothing", "result.png")
