from itertools import product
import time

num_items = 22
max_weight = 800

weight = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]
value = [10, 2, 3, 4, 20, 68, 75, 58, 9, 29, 56, 43, 38, 91, 27, 33, 200, 18, 300, 18, 400, 200]

max_value = 0
item_selected = [0] * num_items

start_time = time.time()

for item_combination in product([0, 1], repeat=num_items):
    current_weight = sum(w * i for w, i in zip(weight, item_combination))
    current_value = sum(v * i for v, i in zip(value, item_combination))

    if current_weight <= max_weight and current_value > max_value:
        max_value = current_value
        item_selected = item_combination

end_time = time.time()

print("Items in best solution:")
for i, is_selected in enumerate(item_selected, start=1):
    if is_selected:
        print(f"Item {i}: weight={weight[i-1]}, value={value[i-1]}")

print(f"Total value: {max_value}")
print(f"Time taken: {end_time - start_time} seconds")
