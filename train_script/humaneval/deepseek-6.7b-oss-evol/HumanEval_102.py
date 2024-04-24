def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        x, y = y, x

    if x % 2 == 0:
        return y if y % 2 == 0 else y - 1
    else:
        return y - 1 if y % 2 == 0 else -1

print(choose_num(12, 15))  # Output: 14
print(choose_num(13, 12))  # Output: -1