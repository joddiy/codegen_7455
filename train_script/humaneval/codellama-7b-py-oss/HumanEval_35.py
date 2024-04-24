def max_element(l: list):
    """Return maximum element in the list."""
    if not l:
        return None  # Return None for empty list
    max_val = l[0]  # Initialize max_val with the first element of the list
    for i in range(1, len(l)):
        if l[i] > max_val:
            max_val = l[i]  # Update max_val if a larger element is found
    return max_val  # Return the maximum element found in the list