def quicksort(arr):
    # Base case: an array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr
    
    # Step 1: Choose the pivot element (here, we select the middle element)
    pivot = arr[len(arr) // 2]
    
    # Step 2: Partition the array into three parts
    left = [x for x in arr if x < pivot]      # Elements less than the pivot
    middle = [x for x in arr if x == pivot]    # Elements equal to the pivot
    right = [x for x in arr if x > pivot]      # Elements greater than the pivot
    
    # Step 3: Recursively sort the left and right parts, then concatenate them with middle
    return quicksort(left) + middle + quicksort(right)
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)  # Output: [1, 1, 2, 3, 6, 8, 10]
