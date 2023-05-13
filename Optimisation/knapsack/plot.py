import plotly.graph_objs as go

# Define the data
fortran_time = [2.343, 1.705, 1.234, 0.417, 0.332, 0.246, 0.125, 0.104, 0.103]
python_time = [138, 63, 28.68, 13.2, 6.5, 3.444, 1.579, 0.707, 0.36597]
num_items = [25, 24, 23, 22, 21, 20, 19, 18, 17]

# Create the plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=num_items, y=fortran_time, name='Fortran', line=dict(color='#3f7f93', width=4)))
fig.add_trace(go.Scatter(x=num_items, y=python_time, name='Python', line=dict(color='#fda085', width=4)))
fig.update_layout(title=dict(text='Execution Time Comparison', font=dict(size=24)),
                  title_x=0.5,
                  xaxis_title=dict(text='Number of Items', font=dict(size=20)),
                  yaxis_title=dict(text='Time (s)', font=dict(size=20)),
                  legend_title=dict(text='Language', font=dict(size=18)),
                  legend=dict(font=dict(size=18)),
                  template="simple_white",
                  width=700,
                  height=450,
                  margin=dict(l=50, r=50, b=50, t=80),
                  hovermode='x',
                  hoverlabel=dict(font=dict(size=18)),
                  )
fig.show()
