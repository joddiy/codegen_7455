def double_the_difference(lst):
    if not lst:
        return 0
    else:
        sum = 0
        for num in lst:
            if isinstance(num, int) and num > 0 and num % 2 != 0:
                sum += num ** 2
        return sum