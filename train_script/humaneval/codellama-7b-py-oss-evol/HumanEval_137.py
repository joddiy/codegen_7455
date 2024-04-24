def compare_one(a, b):
    try:
        a = float(a.replace(',', '.'))
    except ValueError:
        a = float(a)

    try:
        b = float(b.replace(',', '.'))
    except ValueError:
        b = float(b)

    if a == b:
        return None
    elif a > b:
        return a
    else:
        return b