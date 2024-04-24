import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Check if the list has an even number of coefficients and the largest non-zero coefficient
    if len(xs) % 2 == 0 and max([coeff for coeff in xs if coeff != 0]) != xs[-1]:
        raise ValueError("The polynomial must have an even number of coefficients and the largest non-zero coefficient must be the last one.")

    # Calculate the derivative of the polynomial
    derivative = [xs[i] * (i + 1) for i in range(len(xs) - 1)]

    # Find the root of the derivative
    root = -xs[-1] / derivative[-1]

    # Check if the root is a real number
    if not math.isclose(poly(derivative, root), 0, abs_tol=1e-9):
        raise ValueError("The polynomial does not have a real root.")

    return root

# Test the function
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3