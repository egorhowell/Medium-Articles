# Import packages
import os

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import pmdarima as pm
from scipy.special import inv_boxcox
from scipy.stats import boxcox

# Read in the data
data = pd.read_csv("../../Software Engineering /make-example/AirPassengers.csv")
data["Month"] = pd.to_datetime(data["Month"])
data["month_num"] = data["Month"].dt.month

# Stabilise the variance
data["Passengers_Boxcox"], lam = boxcox(data["#Passengers"])
data.dropna(inplace=True)

# Get fourier features
for order in range(1, 10):
    data[f"fourier_sin_order_{order}"] = np.sin(
        2 * np.pi * order * data["month_num"] / 12
    )
    data[f"fourier_cos_order_{order}"] = np.cos(
        2 * np.pi * order * data["month_num"] / 12
    )

# name of fourier features
fourier_features = [i for i in list(data) if i.startswith("fourier")]

# Split train and test
train = data.iloc[: -int(len(data) * 0.2)]
test = data.iloc[-int(len(data) * 0.2) :]

# Build auto-ARIMA model with fourier features
model = pm.auto_arima(
    train["Passengers_Boxcox"],
    X=train[fourier_features],
    seasonal=False,
    stepwise=True,
    suppress_warnings=True,
    max_order=None,
    information_criterion="aicc",
    error_action="ignore",
)

# Get the forecasts and apply inverse box-cox transform
boxcox_forecasts = model.predict(n_periods=len(test), X=test[fourier_features])
forecasts = inv_boxcox(boxcox_forecasts, lam)


def plot_forecasts(forecasts: list[float], title: str, save_path: str) -> None:
    """Function to plot the forecasts."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=train["Month"], y=train["#Passengers"], name="Train"))
    fig.add_trace(go.Scatter(x=test["Month"], y=test["#Passengers"], name="Test"))
    fig.add_trace(go.Scatter(x=test["Month"], y=forecasts, name="Forecast"))
    fig.update_layout(
        template="simple_white",
        font=dict(size=15),
        title_text=title,
        width=900,
        title_x=0.5,
        height=500,
        xaxis_title="Date",
        yaxis_title="Passenger Volume",
    )

    if not os.path.exists("../images"):
        os.mkdir("../images")

    fig.write_image("../images/" + str(save_path))
    return fig.show()


# Plot the forecasts
plot_forecasts(forecasts, "Harmonic Regression", "harmonic.png")
