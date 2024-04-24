from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ""
    for i in range(max(len(a), len(b))):
        bit_a = int(a[i]) if i < len(a) else 0
        bit_b = int(b[i]) if i < len(b) else 0
        result += str(bit_a ^ bit_b)
    return result