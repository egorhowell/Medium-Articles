from math import comb

import plotly.graph_objects as go

# Parameters
r = 2
p = 1 / 6


# PMF
def neg_binomial_pmf(x, r, p):
    if x < r:
        return 0
    q = 1 - p
    return comb(x - 1, r - 1) * (p**r) * (q ** (x - r))


# Values
x = list(range(1, 30))
probs = [neg_binomial_pmf(k, r, p) for k in x]

# Plot
fig = go.Figure(data=[go.Bar(x=x, y=probs, marker_color="rgba(176, 224, 230)")])
fig.update_layout(
    title="Negative Binomial Distribution",
    xaxis_title="x (number of trials to get second 4)",
    yaxis_title="Probability",
    template="simple_white",
    font=dict(size=16),
    title_x=0.5,
    width=700,
    height=500,
)
fig.show()
