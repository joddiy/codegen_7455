def prod_signs(arr):
    if not arr:
        return None
    else:
        signs = [1 if x > 0 else -1 for x in arr]
        magnitudes = [abs(x) for x in arr]
        return sum(x*y for x, y in zip(signs, magnitudes))