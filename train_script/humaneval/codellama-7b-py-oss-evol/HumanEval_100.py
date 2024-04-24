def make_a_pile(n):
    result = []
    for i in range(n):
        if n % 2 == 0:
            result.append(n + 2 * i)
        else:
            result.append(n + 2 * i + 1)
    return result

print(make_a_pile(3))  # Output: [3, 5, 7]