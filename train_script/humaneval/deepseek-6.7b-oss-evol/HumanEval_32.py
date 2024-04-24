import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    if len(xs) % 2 != 0:
        raise ValueError("List of coefficients must have an even number of elements")

    largest_coeff = max(abs(coeff) for coeff in xs)
    if largest_coeff == 0:
        raise ValueError("Largest coefficient must be non-zero")

    # Use Newton's method to find a zero
    x = 0.0
    while True:
        f = poly(xs, x)
        if abs(f) < 1e-6:  # tolerance
            return x
        df = sum([i * math.pow(x, i - 1) for i, coeff in enumerate(xs)])
        dx = f / df
        x -= dx