from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    deviations = [abs(num - mean) for num in numbers]
    mad = sum(deviations) / len(deviations)
    return mad


print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))