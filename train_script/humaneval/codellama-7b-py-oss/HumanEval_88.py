def sort_array(array):
    if not array:
        return []

    if sum(array[0]) + sum(array[-1]) % 2 == 0:
        return sorted(array)
    else:
        return sorted(array, reverse=True)