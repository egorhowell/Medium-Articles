import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.stats import gaussian_kde

# Sample data
n_points = 1000000

# Adjusted mean and standard deviation for the underlying normal distribution
mu, sigma = 0, 0.5

# This is the log(X) that is normally distributed with adjusted parameters
logX_samples = mu + sigma * np.random.randn(n_points)
# This is the X that is log-normally distributed
X_samples = np.exp(logX_samples)

# Kernel Density Estimation
kde_logX = gaussian_kde(logX_samples)
kde_X = gaussian_kde(X_samples)

# Spaced data points for smooth curves
x_logX = np.linspace(min(logX_samples), max(logX_samples), 1000)
x_X = np.linspace(min(X_samples), max(X_samples), 1000)

# Create subplot figure
fig = make_subplots(rows=1, cols=2,
                    subplot_titles=("X - Log-normally Distributed", "ln(X) - Normally Distributed"))

# X trace
fig.add_trace(go.Scatter(x=x_X,
                         y=kde_X(x_X),
                         mode='lines',
                         name='X'),
              row=1, col=1)

# Log(X) trace
fig.add_trace(go.Scatter(x=x_logX,
                         y=kde_logX(x_logX),
                         mode='lines',
                         name='ln(X)'),
              row=1, col=2)

# Update layout
fig.update_layout(title_text="Comparison of X and ln(X) Distributions",
                  template="plotly_white",
                  title_x=0.5,
                  font=dict(size=14),
                  height=550,
                  width=800)
fig.update_yaxes(title_text="PDF", row=1, col=1)
fig.update_yaxes(title_text="PDF", row=1, col=2)
fig.update_xaxes(title_text="Value", row=1, col=1)
fig.update_xaxes(title_text="Value", row=1, col=2)

fig.show()
