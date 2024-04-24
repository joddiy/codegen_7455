def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    convert_string = "0123456789"
    result = ""
    while x > 0:
        remainder = x % base
        result = convert_string[remainder] + result
        x = x // base
    return result