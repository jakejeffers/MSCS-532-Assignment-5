import random
import time
import numpy as np

# Deterministic Quicksort
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quicksort(left) + middle + deterministic_quicksort(right)

# Randomized Quicksort
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Function to measure running time
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time

# Testing configurations
input_sizes = [10**3, 10**4, 10**5]
distributions = ['random', 'sorted', 'reverse_sorted']
results = {}

# Run experiments
for size in input_sizes:
    for dist in distributions:
        if dist == 'random':
            arr = np.random.randint(0, 10000, size).tolist()
        elif dist == 'sorted':
            arr = list(range(size))
        elif dist == 'reverse_sorted':
            arr = list(range(size, 0, -1))

        # Measure deterministic Quicksort
        det_time = measure_time(deterministic_quicksort, arr.copy())
        
        # Measure randomized Quicksort
        rand_time = measure_time(randomized_quicksort, arr.copy())

        # Store results
        results[(size, dist)] = (det_time, rand_time)
        print(f"Size: {size}, Distribution: {dist}, Deterministic: {det_time:.5f}s, Randomized: {rand_time:.5f}s")
