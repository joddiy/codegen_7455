def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))