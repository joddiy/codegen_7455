def is_simple_power(x, n):
    """
    This function returns True if a number x is a simple power of n and False in other cases.
    x is a simple power of n if n**int=x
    """
    if n == 1:
        return x == 1
    else:
        return x == n ** round(pow(x / n, 1 / 2))

# Test cases
print(is_simple_power(1, 4))  # True
print(is_simple_power(2, 2))  # True
print(is_simple_power(8, 2))  # True
print(is_simple_power(3, 2))  # False
print(is_simple_power(3, 1))  # False
print(is_simple_power(5, 3))  # False