def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True  # A list with 1 or fewer elements is considered monotonic

    increasing = l[0] <= l[1]  # Initialize the direction of monotonicity
    for i in range(1, len(l) - 1):
        if l[i] > l[i + 1] and increasing:
            return False  # If the list is increasing and a value is less than the next, return False
        if l[i] < l[i + 1] and not increasing:
            return False  # If the list is decreasing and a value is greater than the next, return False

    return True  # If the list is monotonic, return True