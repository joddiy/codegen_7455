def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.

    Args:
    l1 (list): First list of elements.
    l2 (list): Second list of elements.

    Returns:
    list: Sorted unique common elements between l1 and l2.

    """
    s1 = set(l1)
    s2 = set(l2)
    common_elements = list(s1.intersection(s2))
    return sorted(common_elements)