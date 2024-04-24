def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Initialize the count of numbers starting or ending with 1
    count = 0
    
    # Iterate through all possible n-digit numbers
    for num in range(10 ** (n - 1), 10 ** n):
        # Check if the number starts or ends with 1
        if str(num).startswith('1') or str(num).endswith('1'):
            count += 1
    
    return count