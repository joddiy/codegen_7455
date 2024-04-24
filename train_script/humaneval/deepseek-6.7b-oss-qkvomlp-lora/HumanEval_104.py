def unique_digits(x):
    unique_list = []
    for num in x:
        if all(digit % 2 != 0 for digit in map(int, str(num))):
            unique_list.append(num)
    return sorted(unique_list)