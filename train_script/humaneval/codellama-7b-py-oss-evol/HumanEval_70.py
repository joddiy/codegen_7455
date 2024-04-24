def strange_sort_list(lst):
    if not lst:
        return []

    result = []
    min_val = min(lst)
    max_val = max(lst)

    while lst:
        result.append(min_val)
        lst.remove(min_val)
        if lst:
            result.append(max_val)
            lst.remove(max_val)
        min_val = min(lst)
        max_val = max(lst)

    return result