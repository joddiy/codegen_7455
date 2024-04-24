def generate_integers(a, b):
    if a > b:
        a, b = b, a
    return [i for i in range(a, b+1) if i % 2 == 0]

print(generate_integers(2, 8))  # [2, 4, 6, 8]
print(generate_integers(8, 2))  # [2, 4, 6, 8]
print(generate_integers(10, 14))  # []