def by_length(arr):
    # Filter the array to only include numbers between 1 and 9
    arr = [i for i in arr if 1 <= i <= 9]

    # Sort the array in descending order
    arr.sort(reverse=True)

    # Replace each number with its corresponding name
    arr = [str(i) for i in arr]
    arr = [{"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}[i] for i in arr]

    return arr