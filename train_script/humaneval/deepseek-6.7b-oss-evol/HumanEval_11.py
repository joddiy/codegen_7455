from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert the strings to lists of integers
    a_list = list(map(int, a))
    b_list = list(map(int, b))

    # Perform XOR operation
    xor_result = [str(x ^ y) for x, y in zip(a_list, b_list)]

    # Join the list of strings into a single string
    return ''.join(xor_result)


# Test the function
print(string_xor('010', '110'))  # Output: '100'