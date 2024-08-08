import plotly.graph_objects as go
import torch


# Function to perform optimization and track theta
def optimize(optimizer_class, theta_init, lr, iterations, **kwargs):
    theta_values = []
    theta = torch.tensor([theta_init], requires_grad=True)
    optimizer = optimizer_class([theta], lr=lr, **kwargs)
    for _ in range(iterations):
        optimizer.zero_grad()
        loss = theta.pow(2)
        loss.backward()
        optimizer.step()
        theta_values.append(theta.item())
    return theta_values


# Initial values
theta_init = 3.0
learning_rate = 0.01
iterations = 1000

# Optimiser configurations
optim_configs = {
    "Regular GD": {"optimizer_class": torch.optim.SGD, "lr": learning_rate},
    "Momentum": {
        "optimizer_class": torch.optim.SGD,
        "lr": learning_rate,
        "momentum": 0.9,
    },
    "Nesterov": {
        "optimizer_class": torch.optim.SGD,
        "lr": learning_rate,
        "momentum": 0.9,
        "nesterov": True,
    },
    "Adagrad": {"optimizer_class": torch.optim.Adagrad, "lr": learning_rate},
    "Adam": {"optimizer_class": torch.optim.Adam, "lr": learning_rate},
    "RMSprop": {"optimizer_class": torch.optim.RMSprop, "lr": learning_rate},
}

# Run optimization for each optimizer and collect theta values
results = {}
for name, config in optim_configs.items():
    results[name] = optimize(**config, theta_init=theta_init, iterations=iterations)

# Plot the results
fig = go.Figure()

for optimiser, theta_values in results.items():
    fig.add_trace(
        go.Scatter(
            x=list(range(iterations)), y=theta_values, mode="lines", name=optimiser
        )
    )

fig.update_layout(
    title="Optimiser Performance Comparison",
    xaxis_title="Iteration Number",
    yaxis_title="Value of Theta",
    legend_title="Optimisers",
    template="plotly_white",
    width=900,
    height=600,
    font=dict(size=18),
    xaxis=dict(tickfont=dict(size=16)),
    yaxis=dict(tickfont=dict(size=16)),
    title_font_size=24,
)

fig.show()
