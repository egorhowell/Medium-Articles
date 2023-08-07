# Import packages
import pandas as pd
from scipy.special import inv_boxcox
from statsmodels.tsa.arima.model import ARIMA

# Read in the data
data = pd.read_csv('clean_data.csv')

# Split train and test
train = data.iloc[:-int(len(data) * 0.2)]
test = data.iloc[-int(len(data) * 0.2):]

# Build ARIMA model
model = ARIMA(train['Passengers_Boxcox'], order=(12, 1, 12)).fit()
boxcox_forecasts = model.forecast(len(test))
forecasts = inv_boxcox(boxcox_forecasts, lam)
