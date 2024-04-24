def monotonic(l: list):
    if len(l) < 2:
        return True
    if l[0] < l[1]:
        return all(x < y for x, y in zip(l, l[1:]))
    else:
        return all(x > y for x, y in zip(l, l[1:]))

print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True