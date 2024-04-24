def get_positive(l: list):
    return [i for i in l if i > 0]

print(get_positive([-1, 2, -4, 5, 6]))
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))