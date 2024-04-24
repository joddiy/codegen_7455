def unique_digits(x):
    # Initialize an empty list to store the results
    result = []

    # Iterate over each number in the list
    for num in x:
        # Convert the number to a string to check each digit
        num_str = str(num)
        # Check if all digits are odd
        if all(digit % 2 != 0 for digit in map(int, num_str)):
            # If so, add the number to the result list
            result.append(num)

    # Sort the result list in increasing order
    result.sort()

    # Return the sorted list
    return result