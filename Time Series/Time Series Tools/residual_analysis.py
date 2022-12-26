# Import packages
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import acorr_ljungbox


# Read in the data
data = pd.read_csv('../AirPassengers.csv')
data['Month'] = pd.to_datetime(data['Month'])

# Split train and test
train = data.iloc[:-int(len(data) * 0.2)]
test = data.iloc[-int(len(data) * 0.2):]


def plot_func(forecast: list[float],
              title: str,
              save_path: str) -> None:
    """Function to plot the forecasts."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=train['Month'], y=train['#Passengers'], name='Train'))
    fig.add_trace(go.Scatter(x=test['Month'], y=test['#Passengers'], name='Test'))
    fig.add_trace(go.Scatter(x=test['Month'], y=forecast, name='Forecast'))
    fig.update_layout(template="simple_white", font=dict(size=18), title_text=title,
                      width=700, title_x=0.5, height=400, xaxis_title='Date',
                      yaxis_title='Passenger Volume')

    if not os.path.exists("../images"):
        os.mkdir("../images")

    fig.write_image("../images/" + str(save_path))
    return fig.show()


# Fit Holt Winters model and get forecasts
model = ExponentialSmoothing(train['#Passengers'], trend='mul', seasonal='mul', seasonal_periods=12) \
    .fit(optimized=True)
forecasts = model.forecast(len(test))

# Plot the forecasts
plot_func(forecasts,  "Holt Winters Forecast", 'result.png')

# Residual analysis
train['fittedvalues'] = model.fittedvalues
train['residuals'] = model.resid
print(train)

# Plot ACF and PACF
fig, ax = plt.subplots(1,2,figsize=(8,3))
plot_acf(train['residuals'], lags=30, ax=ax[0])
ax[0].set_xlabel('Lags')
plot_pacf(train['residuals'], lags=30, ax=ax[1])
ax[1].set_xlabel('Lags')
plt.tight_layout()
plt.savefig('residual_acf.png')
plt.show()

# Carry out Ljung-Box test
print(acorr_ljungbox(train['residuals'], return_df=True))

# Plot histogram of the residuals
fig = px.histogram(train, x="residuals")
fig.update_layout(template="simple_white", font=dict(size=18), title_text='Distribution of Residuals',
                  width=700, title_x=0.5, height=400, xaxis_title='Residuals', yaxis_title='Count')
fig.write_image("images/" + "histogram.png")
fig.show()

# Mean of residuals
print(train['residuals'].mean())
