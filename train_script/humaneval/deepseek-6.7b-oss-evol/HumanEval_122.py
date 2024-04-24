def add_elements(arr, k):
    return sum(x for x in arr[:k] if 1 <= len(str(x)) <= 2)

# Test the function
print(add_elements([111,21,3,4000,5,6,7,8,9], 4))  # Output: 24