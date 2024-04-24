def maximum(arr, k):
    arr.sort(reverse=True)  # Sort the array in descending order
    return arr[:k]  # Return the first k elements of the sorted array