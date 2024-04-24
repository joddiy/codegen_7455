def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    # Convert the integers to strings to access their unit digits
    str_a = str(a)
    str_b = str(b)
    
    # Extract the unit digits and multiply them
    unit_digit_a = int(str_a[-1])
    unit_digit_b = int(str_b[-1])
    result = unit_digit_a * unit_digit_b
    
    return result