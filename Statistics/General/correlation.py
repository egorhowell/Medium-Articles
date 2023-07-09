# Import packages
import plotly.graph_objects as go
from scipy.stats import linregress
import numpy as np

# Data
size = [700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
#price = [100000, 110000, 130000, 150000, 165000, 175000, 190000, 200000, 220000]
price = [100000, 110000, 150000, 220000, 350000, 500000, 700000, 1000000, 1500000]

# Linear regression
slope, intercept, r_value, p_value, std_err = linregress(size, price)

# Create regression values
x_values = np.linspace(min(size), max(size), 100)
y_values = slope * x_values + intercept

# Create  plot
fig = go.Figure(data=go.Scatter(x=size, y=price, mode='markers', name='Data'))
fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name='Linear Regression'))
fig.update_layout(template="simple_white", font=dict(size=18), title_text='House Price vs Size (Non-Linear)',
                  width=650, title_x=0.5, height=450,  xaxis_title='Size (sqft)', yaxis_title='Price (£)')

fig.show()

