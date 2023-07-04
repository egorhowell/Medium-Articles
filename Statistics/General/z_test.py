# Import packages
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Generate data for normal distribution
mu = 0
sigma = 1
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 100)
y = stats.norm.pdf(x, mu, sigma)

# Calculate the 95% confidence interval
conf_interval = stats.norm.interval(0.95, loc=mu, scale=sigma)

# Plot the distribution
plt.plot(x, y, label='Normal Distribution')
plt.fill_between(x, y, where=((x <= conf_interval[0]) | (x >= conf_interval[1])), alpha=0.3, label='95% Confidence Interval')
plt.xlabel('Number of Standard Deviations from the mean')
plt.ylabel('Probability Density')
plt.title('Normal Distribution with 95% Confidence Interval')
plt.legend()
plt.show()
