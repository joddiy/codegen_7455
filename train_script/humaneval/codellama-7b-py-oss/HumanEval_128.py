def prod_signs(arr):
    if not arr:
        return None

    signs = [1 if x > 0 else -1 if x < 0 else 0 for x in arr]
    magnitudes = [abs(x) for x in arr]

    total_sum = sum(magnitudes)
    total_prod = 1
    for sign in signs:
        if sign == 0:
            total_prod = 0
            break
        total_prod *= sign

    return total_sum * total_prod