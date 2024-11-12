import random

def randomized_quicksort(arr):
    # Base case: an array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr
    
    # Step 1: Randomly choose a pivot
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    
    # Step 2: Partition the array around the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Step 3: Recursively sort left and right, and concatenate with middle
    return randomized_quicksort(left) + middle + randomized_quicksort(right)
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = randomized_quicksort(arr)
print(sorted_arr)  # Output: [1, 1, 2, 3, 6, 8, 10]