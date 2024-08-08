import plotly.graph_objects as go
from scipy.stats import hypergeom

# Define the hypergeometric distribution parameters
N = 52
K = 4
n = 20

# Number of possible successes
k = list(range(0, n + 1))

# The PMF
pmf = hypergeom.pmf(k, N, K, n)

# Plot the PMF
fig = go.Figure(data=[go.Bar(x=k, y=pmf, marker_color="rgba(176, 224, 230)")])
fig.update_layout(
    title="Hypergeometric Distribution Example",
    xaxis_title="Number of Kings",
    yaxis_title="Probability",
    width=650,
    height=400,
    template="plotly_white",
    margin=dict(l=80, r=40, t=60, b=40),
    title_x=0.5,
)
fig.update_xaxes(range=[-0.5, K + 1.5])
fig.show()

# Define the hypergeometric distribution parameters
N = 52
K = 13
n = 30

# Number of possible successes
k = list(range(0, K + 1))

# The PMF
pmf = hypergeom.pmf(k, N, K, n)

# Plot the PMF
fig = go.Figure(data=[go.Bar(x=k, y=pmf, marker_color="rgba(176, 224, 230)")])
fig.update_layout(
    title="Hypergeometric Distribution Example",
    xaxis_title="Number of Spades",
    yaxis_title="Probability",
    width=650,
    height=400,
    template="plotly_white",
    margin=dict(l=80, r=40, t=60, b=40),
    title_x=0.5,
)
fig.update_xaxes(range=[-0.5, K + 0.5])
fig.show()
