# Import packages
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import random
import plotly.graph_objects as go
import os

# Generate random coordinates
x = list(np.random.randint(0, 15, 20))
y = list(np.random.randint(0, 15, 20))

# Label each city from the alphabet
letters_org = [chr(i) for i in range(ord('a'), ord('z') + 1)]
letters = letters_org[:len(y)]

# Make last city the origin city
df = pd.DataFrame(list(zip(x, y, letters)), columns=['x', 'y', 'point'])
df = df.append(df.iloc[0]).reset_index()

# Plot the city map
fig = px.line(df, x='x', y='y', text='point', title='City Map')
fig.update_layout(template="simple_white", width=750, title_x=0.5, font=dict(size=18))
fig.update_traces(textposition='top center')

if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_image("../images/cities.png")

fig.show()


class SA:
    def __init__(self, iterations, temp, df, gamma):
        self.iterations = iterations
        self.temp = temp
        self.df = df
        self.gamma = gamma

    @staticmethod
    def total_distance(df):

        def euclidean_distance(x1, x2, y1, y2):
            return np.sqrt((x1-x2)**2+(y1-y2)**2)

        distance = 0
        for idx in range(0, len(df)):
            if idx + 1 >= len(df):
                break
            distance += euclidean_distance(df['x'].loc[idx], df['x'].loc[idx+1],
                                           df['y'].loc[idx], df['y'].loc[idx+1])
        return distance

    @staticmethod
    def cooling_temp(gamma, temp):
        return gamma*temp

    @staticmethod
    def check_accept(temp, new_solution, current_solution):
        prob = min(1, np.exp(-(new_solution - current_solution) / temp))
        if prob > random.uniform(0, 1):
            return True
        else:
            return False

    @staticmethod
    def swap_elements(df):
        df_new = df.copy()
        swap_list_indx = range(1, len(df) - 1)

        i = random.randint(swap_list_indx[0], swap_list_indx[-1])
        j = random.randint(swap_list_indx[0], swap_list_indx[-1])

        if i == j:
            while i == j:
                j = random.randint(swap_list_indx[0], swap_list_indx[-1])

        df_new.iloc[i], df_new.iloc[j] = df_new.iloc[j].copy(), df_new.iloc[i].copy()

        return df_new

    def run(self):

        temp = self.temp
        gamma = self.gamma
        df = self.df

        scores = []
        best_scores = []
        temps = []

        current = self.total_distance(self.df)
        best = self.total_distance(self.df)

        for _ in range(self.iterations):

            # swap cities
            df_new = self.swap_elements(df)

            # calculate new distance
            new = self.total_distance(df_new)
            scores.append(new)

            # log if this new one is the best and restart temp
            if new < best:
                best_df = df_new.copy()
                best = new.copy()
                temp = self.temp
            best_scores.append(best)

            # stay or transition from state a
            if self.check_accept(temp, new, current):
                df = df_new.copy()
                current = new.copy()

            # update temperature
            temps.append(temp)
            temp = self.cooling_temp(gamma, temp)

        return scores, best_scores, temps, best_df

# Set parameters and run the algorithm
iterations = 5000
temp = 200
gamma = 0.9
sa = SA(iterations, temp, df, gamma)
scores, best_scores, temps, best_df = sa.run()

# Plot the results
fig = go.Figure()
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=list(range(iterations)), y=scores, name='Current Score'))
fig.add_trace(go.Scatter(x=list(range(iterations)), y=best_scores, name='Best Score'))
fig.add_trace(go.Scatter(x=list(range(iterations)), y=temps, name='Temperature'), secondary_y=True)
fig.update_layout(template="simple_white", font=dict(size=15), title_text='Simulated Annealing',
                  width=800, title_x=0.5, height=450, xaxis_title='Iteration',
                  yaxis_title='Distance')
fig.update_yaxes(title_text="Temperature", secondary_y=True, automargin=True)
fig.update_xaxes(automargin=True)

if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_image("../images/solution.png")

fig.show()

# Plot resultant map
fig = px.line(best_df, x='x', y='y', text='point', title='Best City Map')
fig.update_layout(template="simple_white", width=750, title_x=0.5, font=dict(size=18))
fig.update_traces(textposition='top center')

if not os.path.exists("../images"):
    os.mkdir("../images")
fig.write_image("../images/cities_final.png")

fig.show()
