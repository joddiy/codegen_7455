def compare_one(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    elif isinstance(a, str) and isinstance(b, str):
        if a.replace(",", ".") > b.replace(",", "."):
            return a
        elif b.replace(",", ".") > a.replace(",", "."):
            return b
        else:
            return None
    else:
        raise TypeError("Input values must be integers, floats, or strings representing real numbers")