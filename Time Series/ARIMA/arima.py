# Import packages
import os

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy.special import inv_boxcox
from scipy.stats import boxcox
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA

# Read in the data
data = pd.read_csv("../../Software Engineering /make-example/AirPassengers.csv")
data["Month"] = pd.to_datetime(data["Month"])


def plot_passenger_volumes(df: pd.DataFrame, y: str, save_file_path: str) -> None:
    """General function to plot the passenger data."""

    fig = px.line(df, x="Month", y=y, labels={"Month": "Date"})
    fig.update_layout(
        template="simple_white",
        font=dict(size=18),
        title_text="Airline Passengers",
        width=650,
        title_x=0.5,
        height=400,
    )

    if not os.path.exists("../images"):
        os.mkdir("../images")
    fig.write_image("../images/" + str(save_file_path))

    return fig.show()


# Plot the airline passenger data
plot_passenger_volumes(df=data, y="#Passengers", save_file_path="passengers_data.png")

# Make the data stationary
data["Passengers_Boxcox"], lam = boxcox(data["#Passengers"])
data.dropna(inplace=True)

# Plot the stationary passenger data
plot_passenger_volumes(
    df=data, y="Passengers_Boxcox", save_file_path="passengers_boxcox.png"
)

# Make the mean stationary
data["Passenger_diff"] = data["Passengers_Boxcox"].diff()
data.dropna(inplace=True)

# Plot acf and pacf
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5), dpi=80)
plot_acf(data["Passenger_diff"])
plot_pacf(data["Passenger_diff"], method="ywm")
ax1.tick_params(axis="both", labelsize=12)
ax2.tick_params(axis="both", labelsize=12)
plt.savefig("acf_pacf.png")
plt.show()

# Split train and test
train = data.iloc[: -int(len(data) * 0.2)]
test = data.iloc[-int(len(data) * 0.2) :]

# Build ARIMA model
model = ARIMA(train["Passengers_Boxcox"], order=(12, 1, 12)).fit()
boxcox_forecasts = model.forecast(len(test))
forecasts = inv_boxcox(boxcox_forecasts, lam)


def plot_forecasts(forecasts: list[float], title: str, save_path: str) -> None:
    """Function to plot the forecasts."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=train["Month"], y=train["#Passengers"], name="Train"))
    fig.add_trace(go.Scatter(x=test["Month"], y=test["#Passengers"], name="Test"))
    fig.add_trace(go.Scatter(x=test["Month"], y=forecasts, name="Forecast"))
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


# Plot the forecasts
plot_forecasts(forecasts, "ARIMA", "result.png")
