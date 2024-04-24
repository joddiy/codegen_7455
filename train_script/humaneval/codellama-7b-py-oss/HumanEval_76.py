def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases."""
    if n == 1:
        return x == 1
    if x == n:
        return True
    if x % n != 0:
        return False
    return is_simple_power(x // n, n)