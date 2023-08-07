import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import CubicSpline

# Hypothetical income distribution data
income_percentile = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
cumulative_income = np.array([0, 1, 2, 8, 14, 22, 32, 42, 50, 65, 100])

# Add points (0, 0) and (100, 100) to close the curve
income_percentile = np.insert(income_percentile, 0, 0)
cumulative_income = np.insert(cumulative_income, 0, 0)
income_percentile = np.append(income_percentile, 100)
cumulative_income = np.append(cumulative_income, 100)

# Remove duplicate entries from the income_percentile array
unique_indices = np.unique(income_percentile, return_index=True)[1]
income_percentile = income_percentile[unique_indices]
cumulative_income = cumulative_income[unique_indices]

# Define a finer range of income_percentile values for smoother interpolation
fine_income_percentile = np.linspace(0, 100, 1000)

# Cubic spline interpolation to create a smoother curve
cs = CubicSpline(income_percentile, cumulative_income)

# Calculate the cumulative share of income for perfect equality (diagonal line)
perfect_equality = fine_income_percentile

# Calculate the y values for Lorenz curve and perfect equality line
lorenz_curve_y = cs(fine_income_percentile)
perfect_equality_y = perfect_equality

# Plot the Lorenz curve using Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=fine_income_percentile, y=lorenz_curve_y, mode='lines', name='Lorenz Curve'))
fig.add_trace(go.Scatter(x=fine_income_percentile, y=perfect_equality_y, mode='lines', name='Perfect Equality', line=dict(dash='dash')))

# Add annotations 'A' and 'B'
fig.add_annotation(
    x=60, y=cs(72),
    text='A',
    showarrow=False,
    font=dict(size=26, color="black"),
)
fig.add_annotation(
    x=75, y=cs(50),
    text='B',
    showarrow=False,
    font=dict(size=26, color="black"),
)

fig.update_layout(
    title='Lorenz Curve',
    xaxis_title='Cumulative Population (%)',
    yaxis_title='Cumulative Income (%)',
    template="simple_white",
    font=dict(size=16),
    title_x=0.5,
    width=800,
    height=500,
)

fig.show()
