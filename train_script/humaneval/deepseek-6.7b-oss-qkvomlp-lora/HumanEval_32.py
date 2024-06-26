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
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 != 0:
        raise ValueError("xs must have an even number of coefficients")
    if max(xs) == 0:
        raise ValueError("xs must have a non-zero coefficient")

    # Use Newton's method to find the zero of the polynomial
    x0 = len(xs) / 2  # Initial guess
    epsilon = 1e-6  # Convergence tolerance
    while True:
        fx = poly(xs, x0)
        fprimex = sum([i * math.pow(x0, i - 1) for i in range(1, len(xs))])
        x1 = x0 - fx / fprimex
        if abs(x1 - x0) < epsilon:
            return x1
        x0 = x1