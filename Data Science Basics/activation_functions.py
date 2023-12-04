# Import packages
import numpy as np
import plotly.express as px
import os


# RelU function
def relu(x):
    return np.maximum(0, x)


# x and y
x = np.linspace(-5, 5, 100)
y = relu(x)

# Graph
fig = px.line(x=x, y=y)
fig.update_xaxes(title='x')
fig.update_yaxes(title='ReLU(x)')
fig.update_layout(template="simple_white", font=dict(size=18), title_text='ReLU Plot',
                  width=650, title_x=0.5, height=400)

if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_image("../images/relu.png")

fig.show()


# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# x and y
x = np.linspace(-5, 5, 100)
y = sigmoid(x)

# Plot
fig = px.line(x=x, y=y)
fig.update_xaxes(title='x')
fig.update_yaxes(title='sigmoid(x)')
fig.update_layout(template="simple_white", font=dict(size=18), title_text='Sigmoid Function Plot',
                  width=650, title_x=0.5, height=400)

if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_image("../images/sigmoid.png")

fig.show()


# Tanh function
def tanh(x):
    return np.tanh(x)


# x and y values
x = np.linspace(-5, 5, 100)
y = tanh(x)

# Plot
fig = px.line(x=x, y=y)
fig.update_xaxes(title='x')
fig.update_yaxes(title='tanh(x)')
fig.update_layout(template="simple_white", font=dict(size=18), title_text='Tanh Plot',
                  width=650, title_x=0.5, height=400)

if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_image("../images/tanh.png")

fig.show()


#  Leaky ReLU function
def leaky_relu(x, alpha=0.01):
    return np.where(x >= 0, x, alpha * x)


# x and y values
x = np.linspace(-5, 5, 100)
y = leaky_relu(x)

# Plot
fig = px.line(x=x, y=y)
fig.update_xaxes(title='x')
fig.update_yaxes(title='Leaky ReLU(x)')
fig.update_layout(template="simple_white", font=dict(size=18), title_text='Leaky ReLU Plot',
                  width=650, title_x=0.5, height=400)

if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_image("../images/leaky_relu.png")

fig.show()


#  parabola
def parabola(x):
    return 10 * x ** 2


# x and y values
x = np.linspace(-5, 5, 100)
y = parabola(x)

# Plot
fig = px.line(x=x, y=y)
fig.update_xaxes(title='x')
fig.update_yaxes(title='10x^2')
fig.update_layout(template="simple_white", font=dict(size=18), title_text='Example Parabola',
                  width=650, title_x=0.5, height=400)

if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_image("../images/parabola.png")

fig.show()


def elu(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))


# x and y values
x = np.linspace(-5, 5, 100)
y = elu(x)

# Plot
fig = px.line(x=x, y=y)
fig.update_xaxes(title='x')
fig.update_yaxes(title='ELU(x)')
fig.update_layout(template="simple_white", font=dict(size=18), title_text='ELU Plot',
                  width=650, title_x=0.5, height=400)

if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_image("../images/elu.png")

fig.show()
