# Import packages
import plotly.express as px
import pandas as pd
import os
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt

# Read in the data
data = pd.read_csv('../AirPassengers.csv')

# Plot the data
fig = px.line(data, x='Month', y='#Passengers',
              labels=({'#Passengers': 'Passengers', 'Month': 'Date'}))

fig.update_layout(template="simple_white", font=dict(size=18), title_text='Airline Passengers',
                  width=650, title_x=0.5, height=400)

if not os.path.exists("../images"):
    os.mkdir("../images")

fig.write_image("images/" + str('passenger.png'))
fig.show()

# Plot autocorrelation
plt.rc("figure", figsize=(11,5))
plot_acf(data['#Passengers'], lags=48)
plt.ylim(0,1)
plt.xlabel('Lags', fontsize=18)
plt.ylabel('Correlation', fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.title('Autocorrelation Plot', fontsize=20)
plt.tight_layout()
plt.show()