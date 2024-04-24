def circular_shift(x, shift):
    x_str = str(x)
    shifted_str = x_str[-shift:] + x_str[:-shift]
    return shifted_str