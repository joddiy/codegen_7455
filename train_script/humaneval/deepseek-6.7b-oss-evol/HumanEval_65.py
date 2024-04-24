def circular_shift(x, shift):
    x = str(x)
    if shift > len(x):
        return x[::-1]
    else:
        return x[-shift:] + x[:-shift]

print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"