def common(l1: list, l2: list):
    # Convert the lists to sets to get the unique elements
    set1 = set(l1)
    set2 = set(l2)

    # Use the intersection method of sets to get the common elements
    common_elements = set1.intersection(set2)

    # Convert the set back to a list and sort it
    sorted_common_elements = sorted(list(common_elements))

    return sorted_common_elements