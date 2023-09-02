# Import packages
import numpy as np
from scipy.stats import t, norm
import plotly.graph_objects as go

# Generate data
x = np.linspace(-5, 5, 1000)
normal_pdf = norm.pdf(x, 0, 1)

# Create plot
fig = go.Figure()

# Add standard normal distribution to plot
fig.add_trace(go.Scatter(x=x, y=normal_pdf, mode='lines', name='Standard Normal'))

# Add t-distributions to plot for various degrees of freedom
for df in [1, 5, 10, 20]:
    t_pdf = t.pdf(x, df)
    fig.add_trace(go.Scatter(x=x, y=t_pdf, mode='lines', name=f't-distribution (df={df})'))

fig.update_layout(title='Comparison of Normal and t-distributions',
                  xaxis_title='Value',
                  yaxis_title='PDF',
                  legend_title='Distribution',
                  font=dict(size=16),
                  title_x=0.5,
                  width=900,
                  height=500,
                  template="simple_white")
fig.show()
