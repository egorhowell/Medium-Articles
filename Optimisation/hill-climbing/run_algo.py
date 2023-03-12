# Import packages
import pandas as pd
import plotly.express as px
import numpy as np
from hill_climb_module import HillClimb
import os

# Generate some random city data
x = list(np.random.randint(0, 15, 20))
y = list(np.random.randint(0, 15, 20))

# Generate labels for cities by alphabet
letters_org = [chr(i) for i in range(ord('a'), ord('z') + 1)]
letters = letters_org[:len(y)]

# Construct city dataframe with coordinates
df = pd.DataFrame(list(zip(x, y, letters)), columns=['x', 'y', 'point'])
df = df.append(df.iloc[0]).reset_index()
df['cord'] = df[['x', 'y']].values.tolist()

# Plot the cities
fig = px.line(df, x='x', y='y', text='point', title='Simulated Cities: Initial Solution')
fig.update_layout(template="simple_white", font=dict(size=18), width=800, title_x=0.5, height=500)
fig.update_traces(textposition='top center')
if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_image("../images/" + str('initial_solution.png'))
fig.show()

# Get initial tour and dict for city coordinates
df.index = df['point']
df = df.drop(columns=['index', 'x', 'y'])
cities = df['cord'].to_dict()
initial_tour = df['point'].tolist()

# Run our search
searcher = HillClimb(initial_tour, cities)
best_solution = searcher.run_hill_climb(iterations=100)

# Plot the best found solution
best_df = pd.DataFrame(best_solution, columns=['point'])
best_df['cords'] = best_df['point'].map(cities)
best_df[['x', 'y']] = pd.DataFrame(best_df['cords'].tolist(), index=best_df.index)

fig = px.line(best_df, x='x', y='y', text='point', title='Simulated Cities: Best Found Solution')
fig.update_layout(template="simple_white", font=dict(size=18), width=800, title_x=0.5, height=500)
fig.update_traces(textposition='top center')
fig.write_image("../images/" + str('best_solution.png'))
fig.show()
