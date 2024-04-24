def simplify(x, n):
    x_numerator, x_denominator = map(int, x.split('/'))
    n_numerator, n_denominator = map(int, n.split('/'))

    result_numerator = x_numerator * n_denominator
    result_denominator = x_denominator * n_numerator

    if result_numerator % result_denominator == 0:
        return True
    else:
        return False