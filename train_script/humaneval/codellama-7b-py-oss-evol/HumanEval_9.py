from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = float('-inf')
    result = []
    for num in numbers:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)
    return result

print(rolling_max([1, 2, 3, 2, 3, 4, 2]))