def sort_array(arr):
    # Create a list of tuples containing the binary representation of each number and the number itself
    binary_repr = [(bin(num)[2:].count('1'), num) for num in arr]
    # Sort the list of tuples based on the number of ones in the binary representation
    sorted_binary_repr = sorted(binary_repr)
    # Extract the sorted decimal values from the sorted list of tuples
    sorted_arr = [num for _, num in sorted_binary_repr]
    return sorted_arr