def multiply(a, b):
    """
    Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    """
    # Convert the numbers to strings to easily access their unit digits
    str_a = str(a)
    str_b = str(b)
    
    # Get the last digit of each number
    last_digit_a = int(str_a[-1])
    last_digit_b = int(str_b[-1])
    
    # Return the product of the last digits
    return last_digit_a * last_digit_b