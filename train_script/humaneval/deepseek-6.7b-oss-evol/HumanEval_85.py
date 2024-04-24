def add(lst):
    return sum(lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0)

print(add([4, 2, 6, 7]))  # Output: 2