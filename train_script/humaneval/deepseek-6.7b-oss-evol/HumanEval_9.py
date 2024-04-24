from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    max_num = numbers[0]
    result = [max_num]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        result.append(max_num)
    return result

print(rolling_max([1, 2, 3, 2, 3, 4, 2]))