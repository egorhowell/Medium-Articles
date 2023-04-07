# Import packages
import plotly.graph_objects as go
import numpy as np
from faker import Faker
from brute_force_search import BruteForceSearch
import os

# Generate some random city data
n_cities = 6
x = np.random.randint(0, 10, n_cities)
y = np.random.randint(0, 10, n_cities)

# Generate unique labels for cities using Faker
labels = [Faker().city() for _ in range(n_cities)]

# Combine data into a list of tuples
cities = [(labels[i], x[i], y[i]) for i in range(n_cities)]

# Add the first city to the end to complete the loop
x = np.append(x, x[0])
y = np.append(y, y[0])
labels.append(labels[0])
cities.append(cities[0])

# Create figure
fig = go.Figure()

# Add trace for cities
fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers+text',
                         text=labels, textposition="top center",
                         textfont=dict(color='black'),
                         marker=dict(size=8, color='blue'),
                         line=dict(color='blue', width=1),
                         showlegend=False))

# Add marker for the starting point
fig.add_trace(go.Scatter(x=[x[0]], y=[y[0]], mode='markers',
                         marker=dict(size=15, color='red', symbol='circle'),
                         name='Origin City'))

# Style layout
fig.update_layout(title_text="Simulated Cities: Initial Solution",
                  title_x=0.5, font=dict(size=18),
                  xaxis=dict(title='X-coordinate', titlefont=dict(size=16)),
                  yaxis=dict(title='Y-coordinate', titlefont=dict(size=16)),
                  width=800, height=500, template='simple_white')

fig.update_traces(textposition='top center', textfont=dict(size=14))

if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_image("../images/" + str('initial_solution.png'))

fig.show()

# Run brute-force search
bfs = BruteForceSearch(cities)
best_distance, best_route = bfs.run()

# Plot the results
labels, x, y = [[value[i] for value in best_route] for i in range(3)]

# Create figure
fig = go.Figure()

# Add trace for cities
fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers+text',
                         text=labels, textposition="top center",
                         textfont=dict(color='black'),
                         marker=dict(size=8, color='blue'),
                         line=dict(color='blue', width=1),
                         showlegend=False))

# Add marker for the starting point
fig.add_trace(go.Scatter(x=[x[0]], y=[y[0]], mode='markers',
                         marker=dict(size=15, color='red', symbol='circle'), name='Origin City'))

# Style layout
fig.update_layout(title_text="Simulated Cities: Best Found Solution",
                  title_x=0.5, font=dict(size=18),
                  xaxis=dict(title='X-coordinate', titlefont=dict(size=16)),
                  yaxis=dict(title='Y-coordinate', titlefont=dict(size=16)),
                  width=800, height=500, template='simple_white')

fig.update_traces(textposition='top center', textfont=dict(size=14))

if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_image("../images/" + str('best_solution.png'))

fig.show()
