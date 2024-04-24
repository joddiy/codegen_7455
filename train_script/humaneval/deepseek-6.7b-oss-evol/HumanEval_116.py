def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

print(sort_array([1, 5, 2, 3, 4]))
print(sort_array([-2, -3, -4, -5, -6]))
print(sort_array([1, 0, 2, 3, 4]))