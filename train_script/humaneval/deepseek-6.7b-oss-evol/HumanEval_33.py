def sort_third(l: list):
    divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    divisible_by_three.sort()
    result = l.copy()
    for i in range(len(result)):
        if i % 3 == 0:
            result[i] = divisible_by_three.pop(0)
    return result