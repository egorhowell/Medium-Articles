# Import packages
import numpy as np
import plotly.express as px
import os


# relu function
def relu(x):
    return np.maximum(0, x)


# Generate data
x = np.linspace(-5, 5, 100)
y = relu(x)

# Graph
fig = px.line(x=x, y=y)
fig.update_layout(
    template="simple_white",
    font=dict(size=18),
    title_text="ReLU",
    width=650,
    title_x=0.5,
    height=400,
)

if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_image("../images/relu.png")

fig.show()
