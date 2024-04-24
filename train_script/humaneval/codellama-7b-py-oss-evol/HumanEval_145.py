def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # Calculate the sum of digits for each number
    sums = [(i, sum(int(digit) for digit in str(i))) for i in nums]

    # Sort the numbers based on their sum of digits and their original index
    sums.sort(key=lambda x: (x[1], nums.index(x[0])))

    # Return the sorted list of numbers
    return [num for _, num in sums]