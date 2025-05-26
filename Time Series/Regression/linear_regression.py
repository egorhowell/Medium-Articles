import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Load the AirPassengers dataset
# This version is monthly totals of international airline passengers from 1949 to 1960
url = (
    "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
)
df = pd.read_csv(url, parse_dates=["Month"])
df.columns = ["Date", "Passengers"]
df["Time"] = np.arange(len(df))  # Add a time index

# 2. Prepare the data
X = df[["Time"]]
y = df["Passengers"]

# 3. Fit a linear regression model
model = LinearRegression()
model.fit(X, y)
df["Predicted"] = model.predict(X)

# 4. Plot the actual vs predicted values
plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Passengers"], label="Actual Passengers", marker="o")
plt.plot(df["Date"], df["Predicted"], label="Linear Trend (Regression)", color="red")
plt.title("Time Series Linear Regression: Air Passengers")
plt.xlabel("Date")
plt.ylabel("Number of Passengers")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
