# import packages
import numpy as np
import matplotlib.pyplot as plt

# generate data and sort it
x = np.random.randn(10)
y = np.random.randn(10)
x.sort()
y.sort()

# calculate the null, proposed and saturated models
null_coeff = np.polyfit(x, y, 0)
null_model = np.poly1d(null_coeff)
null_x = np.linspace(x[0], x[-1])
null_y = null_model(null_x)

saturated_coeff = np.polyfit(x, y, len(x))
saturated_model = np.poly1d(saturated_coeff)
saturated_x = np.linspace(x[0], x[-1])
saturated_y = saturated_model(saturated_x)

proposed_coeff = np.polyfit(x, y, 3)
proposed_model = np.poly1d(proposed_coeff)
proposed_x = np.linspace(x[0], x[-1])
proposed_y = proposed_model(proposed_x)

# plot the models
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(22,7))
ax1.plot(null_x, null_y, color="blue")
ax1.scatter(x,y,s=70, color="blue")
ax1.set_title('Null Model', fontsize=22)
ax1.axes.xaxis.set_visible(False)
ax1.axes.yaxis.set_visible(False)

ax2.plot(proposed_x, proposed_y, color="red")
ax2.scatter(x,y,s=70, color="red")
ax2.set_title('Proposed Model', fontsize=22)
ax2.axes.xaxis.set_visible(False)
ax2.axes.yaxis.set_visible(False)

ax3.plot(saturated_x, saturated_y, color="green")
ax3.scatter(x,y,s=70, color="green")
ax3.set_title('Saturated Model', fontsize=22)
ax3.axes.xaxis.set_visible(False)
ax3.axes.yaxis.set_visible(False)
