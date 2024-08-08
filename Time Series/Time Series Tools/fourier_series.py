# Import packages
import os

import numpy as np
import plotly.graph_objects as go

# General summation plots
x = np.arange(0, 3 * np.pi, 0.001)
y_sin = np.sin(2 * x)
y_cos = np.cos(3 * x)
y_sum = y_sin + y_cos
fig = go.Figure()
fig.add_trace(
    go.Scatter(x=x, y=y_sin, name="sine(2x)", line=dict(color="blue", width=2))
)
fig.add_trace(
    go.Scatter(x=x, y=y_cos, name="cos(3x)", line=dict(color="green", width=2))
)
fig.add_trace(go.Scatter(x=x, y=y_sum, name="sum", line=dict(color="red", width=2)))
fig.update_layout(
    template="simple_white",
    font=dict(size=20),
    title_text="Example Sum of Sinusoidal Waves",
    title_x=0.5,
    width=850,
    height=450,
    xaxis_title="x",
    yaxis_title="y",
    xaxis=dict(
        tickvals=[
            0,
            np.pi / 2,
            np.pi,
            np.pi * 3 / 2,
            2 * np.pi,
            np.pi * 5 / 2,
            3 * np.pi,
        ],
        ticktext=[
            "0",
            "$\\frac{\pi}{2}$",
            "$\pi$",
            "$\\frac{3\pi}{2}$",
            "$2\pi$",
            "$\\frac{5\pi}{2}$",
            "$3\pi$",
        ],
    ),
)
if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_image("../images/fourier_sum.png")
fig.show()

# Square wave plots
x = np.arange(0, 3 * np.pi + 0.01, 0.00001)
y = np.sin(x)
for i in range(3, 200):
    if i % 2 != 0:
        y += np.sin(i * x) / i
print(y)

fig = go.Figure()
fig.add_trace(
    go.Scatter(x=x, y=y, name="Square Wave", line=dict(color="blue", width=2))
)
fig.update_layout(
    template="simple_white",
    font=dict(size=20),
    title_text="Square Wave",
    title_x=0.5,
    width=850,
    height=450,
    xaxis_title="x",
    yaxis_title="y",
    xaxis=dict(
        tickvals=[
            0,
            np.pi / 2,
            np.pi,
            np.pi * 3 / 2,
            2 * np.pi,
            np.pi * 5 / 2,
            3 * np.pi,
        ],
        ticktext=[
            "0",
            "$\\frac{\pi}{2}$",
            "$\pi$",
            "$\\frac{3\pi}{2}$",
            "$2\pi$",
            "$\\frac{5\pi}{2}$",
            "$3\pi$",
        ],
    ),
)
if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_image("../images/square.png")
fig.show()
