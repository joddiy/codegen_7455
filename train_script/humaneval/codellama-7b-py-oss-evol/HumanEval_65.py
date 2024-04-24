def circular_shift(x, shift):
    # Convert the integer to a string
    x_str = str(x)

    # If shift is greater than the number of digits, return the reversed string
    if shift > len(x_str):
        return x_str[::-1]

    # Otherwise, circular shift the digits
    shift %= len(x_str)
    return x_str[-shift:] + x_str[:-shift]

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"