def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if base < 2 or base > 10:
        raise ValueError("Base must be between 2 and 10")
    if x < 0:
        raise ValueError("Input number must be non-negative")
    if x == 0:
        return "0"

    digits = []
    while x > 0:
        digits.append(str(x % base))
        x = x // base

    return ''.join(digits[::-1])

print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'