def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    if isinstance(a, str) or isinstance(b, str):
        a = a.replace(',', '.')
        b = b.replace(',', '.')
    if isinstance(a, int) and isinstance(b, int):
        return a if a > b else b if b > a else None
    elif isinstance(a, float) and isinstance(b, float):
        return a if a > b else b if b > a else None
    elif isinstance(a, str) and isinstance(b, str):
        return a if float(a) > float(b) else b if float(b) > float(a) else None
    else:
        raise ValueError("Invalid input types")