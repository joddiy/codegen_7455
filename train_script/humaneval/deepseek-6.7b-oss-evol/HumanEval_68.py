def pluck(arr):
    even_values = [(val, idx) for idx, val in enumerate(arr) if val % 2 == 0]
    if not even_values:
        return []
    smallest_even_value = min(even_values, key=lambda x: x[0])
    return [smallest_even_value[0], smallest_even_value[1]]