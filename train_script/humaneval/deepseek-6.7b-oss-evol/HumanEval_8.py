from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_num = 0
    product_num = 1
    for num in numbers:
        sum_num += num
        product_num *= num
    return sum_num, product_num


# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)