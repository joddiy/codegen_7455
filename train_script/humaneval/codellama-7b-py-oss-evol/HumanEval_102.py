def choose_num(x, y):
    # Initialize the maximum even number to -1
    max_even = -1

    # Iterate over the range from x to y
    for num in range(x, y + 1):
        # Check if the number is even and greater than the current max_even
        if num % 2 == 0 and num > max_even:
            # Update the max_even if a greater even number is found
            max_even = num

    # Return the max_even
    return max_even