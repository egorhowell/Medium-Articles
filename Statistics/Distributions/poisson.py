import numpy as np
import plotly.graph_objects as go
from scipy.stats import poisson


# Define the arrays
k = np.arange(5, 41)
y = poisson.pmf(k, mu=20)

# Create the plot
fig = go.Figure(data=go.Scatter(x=k, y=y, mode='lines'))

# Set title and axis labels
fig.update_layout(title='Example Poisson PMF',
                  xaxis_title='k: Number of shop visits in an hour',
                  yaxis_title='Probability',
                  font=dict(size=18),
                  width=650,
                  title_x=0.5,
                  height=400,
                  template="simple_white")

# Show the plot
fig.show()

# Define our mean values
mu_values = [10, 20, 30]

# Plot
fig = go.Figure()

# Generate the Poisson PMF for different means
for mu in mu_values:
    y = poisson.pmf(k, mu)
    fig.add_trace(go.Scatter(x=k, y=y, mode='lines', name=f'Mean = {mu}'))

fig.update_layout(title='Example Poisson PMF: Different Means',
                  xaxis_title='k: Number of shop visits in an hour',
                  yaxis_title='Probability',
                  font=dict(size=18),
                  width=700,
                  title_x=0.5,
                  height=400,
                  template="simple_white")
fig.show()





