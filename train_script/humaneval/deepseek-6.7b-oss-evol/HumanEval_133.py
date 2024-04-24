def sum_squares(lst):
    return sum(int(abs(num) + 0.5) ** 2 for num in lst)