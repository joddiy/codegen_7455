def is_sorted(lst):
    if len(lst) <= 1:
        return True
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False
    return True