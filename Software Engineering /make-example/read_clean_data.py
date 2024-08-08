import pickle

import pandas as pd
from scipy.stats import boxcox

# Read in the data
data = pd.read_csv("AirPassengers.csv")
data["Month"] = pd.to_datetime(data["Month"])

# Make the variance stationary
data["Passengers_Boxcox"], lam = boxcox(data["#Passengers"])
data.dropna(inplace=True)

# Make the mean stationary
data["Passenger_diff"] = data["Passengers_Boxcox"].diff()
data.dropna(inplace=True)

# Pickle the lam variable
with open("lam.pickle", "wb") as f:
    pickle.dump(lam, f)

# Write data to file
data.to_csv("clean_data.csv", index=False)
