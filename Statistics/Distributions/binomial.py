import plotly.graph_objects as go
import numpy as np
from scipy.stats import binom

# Set the number of trials and probability
n = 50
p = 0.5

# Number of successes
x = np.arange(0, n+1)

# PMF
pmf = binom.pmf(x, n, p)

# Generate plot®
fig = go.Figure(data=[go.Bar(x=x, y=pmf)])
fig.update_layout(title="Binomial Distribution (n=50, p=0.5)",
                  xaxis_title="Number of Successes",
                  yaxis_title="Probability",
                  font=dict(size=18),
                  width=700,
                  title_x=0.5,
                  height=400,
                  template="simple_white")
fig.show()
