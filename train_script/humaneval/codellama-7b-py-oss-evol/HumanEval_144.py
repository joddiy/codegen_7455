def simplify(x, n):
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    # Multiply the numerators and denominators
    product_num = x_num * n_num
    product_den = x_den * n_den

    # Check if the product is a whole number
    return product_num % product_den == 0

print(simplify("1/5", "5/1"))  # True
print(simplify("1/6", "2/1"))  # False
print(simplify("7/10", "10/2"))  # False