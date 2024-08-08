# Import packages
import os

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from scipy.stats import boxcox
from statsmodels.tsa.seasonal import seasonal_decompose

# Read in the data
data = pd.read_csv(
    "../../Software Engineering /make-example/AirPassengers.csv", index_col=0
)
data.index = pd.to_datetime(data.index)

# Plot the data
fig = px.line(
    data,
    x=data.index,
    y="#Passengers",
    labels=({"#Passengers": "Passengers", "Month": "Date"}),
)

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

fig.write_image("../images/" + str("passenger.png"))
fig.show()

# Apply boxcox to acquire additive model
data["Additive Decomposition"], lam = boxcox(data["#Passengers"])

# Plot the decomposition for additive series
decomposition_plot_add = seasonal_decompose(
    data["Additive Decomposition"], model="additive"
)
decomposition_plot_add.plot()
plt.show()

# Plot the decomposition for multiplicative series
data.rename(columns={"#Passengers": "Multiplicative Decomposition"}, inplace=True)
decomposition_plot_multi = seasonal_decompose(
    data["Multiplicative Decomposition"], model="multiplicative"
)
decomposition_plot_multi.plot()
plt.show()
