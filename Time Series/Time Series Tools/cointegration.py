import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
from statsmodels.tsa.stattools import adfuller
from scipy.stats import linregress

# Generate time series
t = np.arange(1, 20)
A = [2, 4, 6, 8, 10, 8, 8, 12, 14, 18, 18, 20, 16, 18, 20, 14, 14, 16, 20]
B = [2, 3, 7, 9, 11, 9, 10, 11, 12, 15, 17, 19, 15, 16, 21, 12, 12, 17, 22]

# Calculate regression line
slope, intercept, r_value, p_value, std_err = linregress(B, A)
regression_line = slope * B + intercept
print(linregress(B, A))


def adf_test(series):
    """Using an ADF test to determine if a series is stationary"""
    test_results = adfuller(series)
    print('ADF Statistic: ', test_results[0])
    print('P-Value: ', test_results[1])
    print('Critical Values:')
    for thres, adf_stat in test_results[4].items():
        print('\t%s: %.2f' % (thres, adf_stat))


residuals = np.array(A) - 1.000392464678179 * np.array(B)
adf_test(residuals)

fig = make_subplots(rows=1, cols=1)
fig.add_trace(go.Scatter(x=t, y=A, mode='lines', name='A(t)'), row=1, col=1)
fig.add_trace(go.Scatter(x=t, y=B, mode='lines', name='B(t)'), row=1, col=1)
fig.update_xaxes(title_text='Time', row=1, col=1)
fig.update_yaxes(title_text='Value', row=1, col=1)

fig.add_trace(go.Scatter(x=B, y=A, mode='markers', name='A(t) vs B(t)'), row=1, col=2)
fig.update_xaxes(title_text='Value B(t)', row=1, col=2, tickfont=dict(size=14))
fig.update_yaxes(title_text='Value A(t)', row=1, col=2, tickfont=dict(size=14))

fig.add_trace(go.Scatter(x=B, y=regression_line, mode='lines', name='Regression Line'), row=1, col=2)

fig.update_layout(height=400, width=650, title_text="Cointegrated Test Example",
                  template="simple_white", font=dict(size=14), title_x=0.5)
fig.show()


