def closest_integer(value):
    # Convert the string to a float
    value = float(value)

    # Check if the value is equidistant from two integers
    if value > 0:
        # Round it away from zero
        if value - int(value) >= 0.5:
            return int(value) + 1
        else:
            return int(value)
    else:
        # Round it away from zero
        if abs(value - int(value)) >= 0.5:
            return int(value) - 1
        else:
            return int(value)

# Test the function
print(closest_integer("10"))  # Output: 10
print(closest_integer("15.3"))  # Output: 15
print(closest_integer("14.5"))  # Output: 15
print(closest_integer("-14.5"))  # Output: -15