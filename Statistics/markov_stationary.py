import numpy as np
import matplotlib.pyplot as plt

# set the one-step transition
transition_matrix =  np.array([[0, 0.4, 0.6],
                               [0.5, 0.3, 0.2],
                               [0.5, 0.3, 0.2]])

# equilibrium for transition matrix
arr = transition_matrix

for _ in range(50):
  
    # multiply matrix
    arr = arr @ transition_matrix
    
print(arr)
   
  
  
# for a given starting distribution
initial_dist = np.array([1,0,0])

for _ in range(100):
    update = initial_dist @ transition_matrix
    initial_dist = update
    
print(initial_dist)
  
  
  
  
# plotting the equilibrium
def plot(steps, x, axes,title):
    axes.plot(steps,x)
    axes.set_title(label=title, fontdict = {'fontsize' : 18})
    axes.set_xlabel('Steps', fontsize=14)
    axes.set_ylabel('Probability', fontsize=14)
    
    for tick in axes.xaxis.get_majorticklabels().: 
        tick.set_fontsize(14) 
        
    for tick in axes.yaxis.get_majorticklabels(): 
        tick.set_fontsize(14) 
        
        
fig, axes = plt.subplots(1,3,figsize=(15,5))
plot(steps,x1,axes[0],'x1')
plot(steps,x2,axes[1],'x2')
plot(steps,x3,axes[2],'x3')
