def odd_count(lst):
    result = []
    for i in range(len(lst)):
        count = sum(int(digit) % 2 for digit in lst[i])
        result.append(f"the number of odd elements {count}n the str{count}ng {count} of the {count}nput.")
    return result