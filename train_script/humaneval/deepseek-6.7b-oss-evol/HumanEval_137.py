def compare_one(a, b):
    # Check if a and b are of the same type
    if type(a) != type(b):
        return None

    # Convert strings to floats if necessary
    if isinstance(a, str):
        a = float(a.replace(',', '.'))
        b = float(b.replace(',', '.'))

    # Compare the values
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None

# Test cases
print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3"))  # ➞ "2,3"
print(compare_one("5,1", "6"))  # ➞ "6"
print(compare_one("1", 1))  # ➞ None