import pickle

import pandas as pd
from pmdarima import auto_arima
from scipy.special import inv_boxcox

# Read in the data
data = pd.read_csv("clean_data.csv")

# Unpickle the lam variable
with open("lam.pickle", "rb") as f:
    lam = pickle.load(f)

# Split train and test
train = data.iloc[: -int(len(data) * 0.2)]
test = data.iloc[-int(len(data) * 0.2) :]

# Use pmdarima to fit the ARIMA model with automatic differencing
model = auto_arima(
    train["Passengers_Boxcox"], d=None, seasonal=True, m=12, suppress_warnings=True
)

# Forecast using the fitted model
boxcox_forecasts = model.predict(n_periods=len(test))
forecasts = inv_boxcox(boxcox_forecasts, lam)

# Save train, test, and forecasts to CSV files
train.to_csv("train_data.csv", index=False)
test.to_csv("test_data.csv", index=False)
forecasts_df = pd.DataFrame({"Forecasts": forecasts}, index=test.index)
forecasts_df.to_csv("forecasts.csv", index=True)
