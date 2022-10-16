# Import packages
import plotly.express as px
import yfinance as yf
import os
from statsmodels.tsa.stattools import adfuller
import numpy as np

# Read in the data
msft = yf.Ticker("MSFT")
data = msft.history(period='10Y')
data.reset_index(inplace=True)


def plotting_stock_price(title, data, x, y, save_file_path, x_label, y_label):
    """General function to plot the stock data."""
    fig = px.line(data, x=data[x], y=data[y], labels={x: x_label, y: y_label})

    fig.update_layout(template="simple_white", font=dict(size=18),
                      title_text=title, width=650,
                      title_x=0.5, height=400)

    if not os.path.exists("images"):
        os.mkdir("images")

    fig.write_image("images/" + str(save_file_path))

    fig.show()


# Plot the stock data
plotting_stock_price(title='Microsoft Stock Price', data=data, save_file_path='stock_price.png', x='Date',
                     y='Open', x_label='Date', y_label='Open Price ($)')

# Take the difference and plot it
data["Open_Diff"] = data["Open"].diff()

plotting_stock_price(title='Microsoft Stock Price', data=data,
                     save_file_path='stock_price_one_difference.png', x='Date', y='Open_Diff', x_label='Date',
                     y_label='Open Price<br>Difference Transform<br>($)')

# Take the log and plot it
data["Open_Log"] = np.log(data["Open"])

plotting_stock_price(title='Microsoft Stock Price', data=data, save_file_path='stock_price_log.png',
                     x='Date', y='Open_Log', x_label='Date', y_label='Open Price<br>Log Transform<br>($)')

# Take the difference and log and plot it
data["Open_Diff_Log"] = data["Open_Log"].diff()

plotting_stock_price(title='Microsoft Stock Price', data=data,
                     save_file_path='stock_price_one_difference_and_log.png', x='Date', y='Open_Diff_Log',
                     x_label='Date', y_label='Open Price<br>Log and Difference<br>Transform($)')


# ADF test
def adf_test(series):
    """Using an ADF test to determine if a series is stationary"""
    test_results = adfuller(series)
    print('ADF Statistic: ', test_results[0])
    print('P-Value: ', test_results[1])
    print('Critical Values:')
    for thres, adf_stat in test_results[4].items():
        print('\t%s: %.2f' % (thres, adf_stat))


adf_test(data["Open_Diff_Log"][1:])
