def pluck(arr):
    even_values = [val for val in arr if val % 2 == 0]
    if not even_values:
        return []
    min_even_value = min(even_values)
    min_index = arr.index(min_even_value)
    return [min_even_value, min_index]