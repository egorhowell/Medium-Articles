# Import packages
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Load data
data = pd.read_csv('Salary_dataset.csv')

# Build model and get line of best fit
model = sm.OLS(data['Salary'], data['YearsExperience'])
results = model.fit()
predictions = results.get_prediction(data['YearsExperience']).summary_frame(0.05)

# Plot regression line
plt.scatter(data['YearsExperience'], data['Salary'], label='Sample Data', color='black')
plt.fill_between(data['YearsExperience'], predictions['obs_ci_lower'], predictions['obs_ci_upper'],
                 alpha=0.1, label='Prediction interval')
plt.plot(data['YearsExperience'], predictions['mean'], label='Regression Line')
plt.fill_between(data['YearsExperience'], predictions['mean_ci_lower'], predictions['mean_ci_upper'],
                 alpha=0.4, label='Confidence Interval')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary ($)')
plt.legend()
plt.tight_layout()
plt.savefig('confidence.png')
plt.show()
