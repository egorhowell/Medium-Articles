# Import packages
import time
from itertools import product

import numpy as np

# Declare our variables
num_items = 22
max_weight = 800
best_value = 0
best_combination = np.zeros(num_items)
weight = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
    110,
    120,
    130,
    140,
    150,
    160,
    170,
    180,
    190,
    200,
    210,
    220,
]
value = [
    10,
    2,
    3,
    4,
    20,
    68,
    75,
    58,
    9,
    29,
    56,
    43,
    38,
    91,
    27,
    33,
    200,
    18,
    300,
    18,
    400,
    200,
]

start_time = time.time()

# Brute force search
for new_combination in product([0, 1], repeat=num_items):
    new_weight = sum(w * i for w, i in zip(weight, new_combination))
    new_value = sum(v * i for v, i in zip(value, new_combination))

    if new_weight <= max_weight and new_value > best_value:
        best_value = new_value
        best_combination = new_combination

end_time = time.time()

print("Items in best combination:")
for item, in_knapsack in enumerate(best_combination, start=1):
    if in_knapsack:
        print(f"Item {item}: weight={weight[item-1]}, value={value[item-1]}")

print(f"Best value: {best_value}")
print(f"Time taken: {end_time - start_time} seconds")
