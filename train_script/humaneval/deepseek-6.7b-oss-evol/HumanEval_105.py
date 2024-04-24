def by_length(arr):
    # Filter out numbers not in the range 1-9
    arr = [i for i in arr if 1 <= i <= 9]
    # Sort the array
    arr.sort(reverse=True)
    # Map the numbers to their corresponding names
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return [names[i-1] for i in arr]