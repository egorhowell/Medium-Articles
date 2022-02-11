import numpy as np

# set the one-step transition
transition_matrix =  np.array([[0, 0.5, 0.5],
                               [0.4, 0.3, 0.3],
                               [0.6, 0.2, 0.2]])

# equilibrium for transition matrix
arr = transition_matrix

for _ in range(50):
  
    # multiply matrix
    arr = arr @ transition_matrix
    
# for a given starting distribution
initial_dist = np.array([[1,0,0]])

for _ in range(100):
    update = initial @ transition_matrix
    initial = update
