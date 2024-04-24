def smallest_change(arr):
    n = len(arr)
    if n % 2 == 1:
        return n // 2
    else:
        return n // 2 - 1