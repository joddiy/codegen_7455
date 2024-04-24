def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # The number of n-digit numbers that start or end with 1 is 2 * 9 * 10^(n-2)
    # This is because there are 2 possibilities for the first digit (1 or not 1),
    # 9 possibilities for the second digit (any digit except 1), and 10^(n-2) possibilities
    # for the remaining n-2 digits.
    return 2 * 9 * 10 ** (n - 2)

# Test the function
print(starts_one_ends(2))  # Output: 18
print(starts_one_ends(3))  # Output: 108