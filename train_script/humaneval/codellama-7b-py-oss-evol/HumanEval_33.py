def sort_third(l: list):
    third_elements = sorted([i for i in l[::3]])
    for i in range(0, len(l), 3):
        l[i] = third_elements.pop(0)
    return l