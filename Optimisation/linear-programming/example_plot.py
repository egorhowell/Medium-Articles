import plotly.graph_objects as go
import numpy as np

# Define the constants
x_limit = 75
y_limit = 100
xy_limit = 140

# Define the lines
xy_line = np.array([0, xy_limit])

# Create the plot
fig = go.Figure()

fig.add_trace(go.Scatter(x=np.linspace(0, xy_limit, 100),
                         y=xy_limit - np.linspace(0, xy_limit, 100),
                         mode='lines', line=dict(color='blue', width=4), name='x + y <= 140'))

fig.add_trace(go.Scatter(x=[0, xy_limit+10], y=[y_limit, y_limit],
                         mode='lines', line=dict(color='green', width=4), name='y <= 100'))

fig.add_trace(go.Scatter(x=[x_limit, x_limit], y=[0, y_limit+10],
                         mode='lines', line=dict(color='red', width=4), name='x <= 75'))

fig.add_trace(go.Scatter(x=np.linspace(0, x_limit-1, 100),
                         y=np.minimum(y_limit-1, xy_limit-1 - np.linspace(0, x_limit, 100)),
                         mode='lines', fill='tozeroy', fillcolor='rgba(211, 211, 211, 0.5)',
                         line=dict(color='lightgrey'), showlegend=False))

fig.add_annotation(
    x=x_limit / 2,
    y=y_limit / 2,
    text="Feasible Region",
    showarrow=False,
    font=dict(size=20, color='black'),
)

fig.update_layout(
    title='Linear Programming Example',
    xaxis=dict(title='x (Smoothies)', range=[0, x_limit+10], tickfont=dict(size=16)),
    yaxis=dict(title='y (Coffees)', range=[0, y_limit+10], tickfont=dict(size=16)),
    showlegend=True,
    legend=dict(font=dict(size=16)),
    template="simple_white",
    height=500,
    width=800,
    title_x=0.5,
    title_font=dict(size=24)
)

fig.show()
